import os, time
import numpy as np
import librosa
import sounddevice as sd
import serial
import serial.tools.list_ports
import requests
from colorama import init, Fore, Style
init(autoreset=True)

SR                 = 22050
EMOTIONS           = ['anger', 'fear', 'happy', 'neutral', 'sad']
TARGET             = {'anger': 'A', 'happy': 'H'}   # only these two
SERVER             = 'http://localhost:5000/predict'
STATE_URL          = 'http://localhost:5000/state'
SILENCE_THRESHOLD  = 0.012   # RMS below this = nobody speaking, skip window
CONFIDENCE_MIN     = 0.60    # must be above 60% to report
STREAK_NEEDED      = 2       # same emotion in N consecutive windows before sending

def load_model():
    if os.path.exists('inference_model.onnx'):
        import onnxruntime as ort
        sess = ort.InferenceSession('inference_model.onnx')
        name = sess.get_inputs()[0].name
        print(Fore.GREEN + "  Model loaded (ONNX)")
        return lambda f: sess.run(None, {name: f})[0][0]
    print(Fore.RED + "  No model file. Put inference_model.onnx here.")
    exit(1)

def find_esp32():
    for p in serial.tools.list_ports.comports():
        desc = (p.description or '').lower()
        if any(k in desc for k in ['cp210', 'ch340', 'ch341', 'esp']):
            return p.device
    return None

def extract(audio):
    zcr  = librosa.feature.zero_crossing_rate(audio)
    rms  = librosa.feature.rms(y=audio)
    mfcc = librosa.feature.mfcc(y=audio, sr=SR, n_mfcc=40)
    feat = np.vstack([zcr, rms, mfcc])
    feat = feat[:, :130] if feat.shape[1] >= 130 \
           else np.pad(feat, ((0,0),(0, 130 - feat.shape[1])))
    feat = (feat - feat.mean()) / (feat.std() + 1e-8)
    return feat[np.newaxis, ...].astype(np.float32)

def send_to_server(emotion, confidence):
    try:
        requests.post(SERVER,
                      json={'emotion': emotion, 'confidence': float(confidence)},
                      timeout=0.5)
    except:
        pass

def is_paused():
    try:
        r = requests.get(STATE_URL, timeout=0.3)
        return not r.json().get('recording', True)
    except:
        return False   # if server unreachable, keep going

def send_serial(ser, code):
    if ser:
        try: ser.write(code.encode())
        except: pass

def main():
    os.system('cls')
    print(Fore.CYAN + Style.BRIGHT + '\n  HEARD — Emotion Detection\n')

    run = load_model()

    ser, port = None, find_esp32()
    if port:
        try:
            ser = serial.Serial(port, 115200, timeout=1)
            time.sleep(2)
            print(Fore.GREEN + f"  ESP32 on {port}")
        except:
            print(Fore.YELLOW + "  ESP32 found but could not connect")
    else:
        print(Fore.YELLOW + "  No ESP32 — WiFi only")

    print(Fore.WHITE + Style.DIM + '\n  Listening. Ctrl+C to stop.\n')
    print(f"  {'STATUS':<14} {'EMOTION':<12} {'CONF':>5}  NOTE")
    print('  ' + '─' * 52)

    streak      = 0
    last_emo    = None

    try:
        while True:
            # Check if dashboard has paused recording
            if is_paused():
                print(Fore.WHITE + Style.DIM + '  [paused]')
                time.sleep(1)
                continue

            # Record 2-second window
            audio = sd.rec(int(2 * SR), samplerate=SR, channels=1, dtype='float32')
            sd.wait()
            audio = audio.flatten()

            # Energy check — skip silence and background noise
            rms_energy = float(np.sqrt(np.mean(audio ** 2)))
            if rms_energy < SILENCE_THRESHOLD:
                print(Fore.WHITE + Style.DIM +
                      f'  {"silence":<14} {"—":<12} {"—":>5}  rms={rms_energy:.4f}')
                continue

            # Predict
            probs = run(extract(audio))
            idx   = int(np.argmax(probs))
            emo   = EMOTIONS[idx]
            conf  = float(probs[idx])

            # Debounce — only send after STREAK_NEEDED consecutive same-emotion windows
            if emo == last_emo:
                streak += 1
            else:
                last_emo = emo
                streak   = 1

            if emo in TARGET and conf >= CONFIDENCE_MIN and streak >= STREAK_NEEDED:
                code  = TARGET[emo]
                color = Fore.YELLOW if emo == 'happy' else Fore.RED
                note  = f'streak={streak}'
                send_to_server(emo, conf)
                send_serial(ser, code)
            else:
                code  = 'N'
                color = Fore.WHITE + Style.DIM
                note  = 'waiting' if streak < STREAK_NEEDED else 'low conf'
                # still log to server so dashboard stays live
                send_to_server(emo, conf)
                send_serial(ser, 'N')

            bar = '█' * int(conf * 25)
            print(f'  {color + Style.BRIGHT}{"voice":<14}{emo:<12}'
                  f'{conf:.0%}  {note}  rms={rms_energy:.3f}')

    except KeyboardInterrupt:
        send_serial(ser, 'N')
        if ser: ser.close()
        print(Fore.WHITE + Style.DIM + '\n  Stopped.\n')

if __name__ == '__main__':
    main()