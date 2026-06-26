<div align="center">

# 🎧 Heard

### An AI-powered wearable that translates emotions from sound into something humans can understand.

<img src="https://img.shields.io/badge/AI-Emotion%20Recognition-purple?style=for-the-badge">
<img src="https://img.shields.io/badge/Deep%20Learning-CNN--GRU-blue?style=for-the-badge">
<img src="https://img.shields.io/badge/Hardware-Arduino%20%2B%20LED-green?style=for-the-badge">
<img src="https://img.shields.io/badge/Built%20for-AI%20for%20Good-red?style=for-the-badge">

<br><br>

**A wearable bridge between an inner emotional world and the people trying to understand it.**

</div>


---

# 🌍 The Story Behind Heard

> "The biggest communication problem is we do not listen to understand. We listen to reply."

The project was I spired by watching my younger brother fear playing/interacting with our neighbors autistic child. And that came from the common misconception and stigma surrounding autism.

We want to give caregivers and most especially parents a clearer signal when words and faces are hard to read.
---

# 🧠 What is Heard?

Heard is an experimental AI wearable system that listens to vocal patterns and predicts emotional states.

It does not analyze words.

It listens to the hidden signals inside sound:

- 🎵 Pitch
- ⚡ Energy
- 🌊 Rhythm
- 📈 Voice patterns over time

The AI converts these signals into an emotion prediction.

Then...

A tiny wearable display communicates the result.

A caregiver does not need to ask:

> "What are you feeling?"

The device helps answer:

> "This might be what is happening."

---

# ✨ The Vision

```
Human Emotion
       |
       v
 🎤 Microphone
       |
       v
 AI Emotion Model
       |
       v
 Arduino Controller
       |
       v
 8x8 LED Emotion Display
```

A wearable translator.

From:

**Invisible feelings**

to

**Visible signals**

---

# 🏗️ Architecture

Heard uses a two-stage cross-modal learning approach.

```
                 TRAINING ONLY

      Autism Face Dataset
              |
              v
        MobileNetV2
              |
              |
              v
        Emotion Features
              |
              |
Audio Dataset ---> CNN-GRU ---> Emotion Prediction


              |
              v

        Auxiliary Loss Training

              |
              v

        Better Audio Understanding


                 INFERENCE

          🎤 Audio Only

              |
              v

          CNN-GRU Model

              |
              v

        Emotion Animation
```

The face model is a teacher.

The microphone is the final student.

During deployment:

📌 No camera  
📌 No face recognition  
📌 Only audio

---

# 🎧 Audio Intelligence

The audio pipeline extracts:

## MFCC

A mathematical representation of the sound spectrum.

It captures:

- Voice texture
- Frequency patterns
- Speech characteristics


## Zero Crossing Rate

Measures how often the signal changes direction.

Useful for:

- Harsh sounds
- Excited sounds
- Noisy emotional states


## RMS Energy

Measures intensity.

Useful for:

- Loudness
- Emotional strength


Together:

```
Audio =
MFCC
+
ZCR
+
RMS
```

---

# 🧬 Deep Learning Model

The final audio model:

```
Audio Features

      |
      v

1D CNN

      |
      v

Feature Extraction

      |
      v

GRU

      |
      v

Temporal Understanding

      |
      v

Emotion Classifier
```

Why CNN + GRU?

CNN learns:

> "What patterns exist?"

GRU learns:

> "How do these patterns change through time?"

Emotion is not a single moment.

Emotion is a sequence.

---

# 📊 Results

Final evaluation:

| Emotion | F1 Score |
|-|-|
| 😡 Anger | 91% |
| 😨 Fear | 74% |
| 😊 Happy | 81% |
| 😐 Neutral | 80% |
| 😢 Sad | 77% |

Overall:

## 🚀 81% Test Accuracy

Speaker-independent evaluation.

---

# 🔥 The Hardest Problem

The biggest challenge:

There is almost no public dataset of autistic children's emotional audio.

Most emotion datasets contain:

- Actors
- Controlled recordings
- Artificial emotions


But autistic expression can be different.

A sound that means happiness for one person may not sound like traditional happiness.

This project does not hide that.

AI should not pretend certainty.

AI should communicate uncertainty.

---

# 🤔 The Honest AI Principle

Heard does NOT say:

> "This child is definitely scared."

It says:

> "I think this may be fear. Confidence: 61%."

The human remains the decision maker.

The AI is a signal.

Not a replacement.

---

# 🖥️ Hardware Prototype

The physical system:

```
Lapel Microphone

       |
       v

Laptop / Edge Device

       |
       v

ONNX AI Model

       |
       v

Arduino UNO

       |
       v

MAX7219 8x8 LED Matrix
```

Emotion animations:

😊 Happy

```
   *
  ***
 *****
  ***
   *
```

😢 Sad

```
   *
   *
   *
  ***
 *****
```

😡 Anger

```
*     *
 ** **
  ***
 ** **
*     *
```

😨 Fear

```
* * *
 * *
* * *
```

---

# 🧪 What We Learned

The biggest lesson:

## Better AI is not always more confident AI.

A system that admits:

> "I am uncertain"

can be more useful than a system that confidently gives the wrong answer.

---

# 🚀 Future Versions

Heard v2:

### Personal AI Adaptation

Every person expresses emotion differently.

Future versions could learn:

"How does THIS child sound when happy?"

"How does THIS child sound when stressed?"

---

### Multimodal Understanding

Future sensors:

🎤 Audio  
⌚ Movement  
❤️ Physiological signals  

Because sometimes the strongest emotional signal is not in the voice.

---

# 🏆 Built For

USAII Global AI Hackathon 2026

Theme:

> AI for Good in Your World

Community Challenge:

> Make Support Obvious

---

# 👥 Team

## AI/ML Empire

**Muhammad Mujahid Haruna**

AI Architecture  
Machine Learning  
Hardware Integration


**Cora Zeng**

Research  
Responsible AI  
Personalization Strategy


---

# ⚠️ Disclaimer

Heard is a research prototype.

It is:

✅ An assistive signal  
✅ A communication helper  
✅ A conversation starter  


It is NOT:

❌ A medical diagnosis tool  
❌ A replacement for caregivers  
❌ A perfect emotion detector

---

<div align="center">

# ❤️ Heard

### Because every person deserves to be understood.

Built with curiosity, AI, and the belief that technology should reduce the distance between people.

</div>
