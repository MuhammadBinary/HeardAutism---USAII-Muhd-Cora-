# 🧠🎧 HeardAutism
### AI that helps machines understand emotions beyond words.

<p align="center">
  <img src="https://img.shields.io/badge/AI-Emotion%20Recognition-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Deep%20Learning-CNN%20%2B%20GRU-purple?style=for-the-badge">
  <img src="https://img.shields.io/badge/Computer%20Vision-MobileNetV2-green?style=for-the-badge">
</p>


## 🌍 The Problem

Imagine a child who feels something deeply...

Happy?
Sad?
Scared?
Overwhelmed?

But the people around them cannot understand what emotion they are expressing.

For many autistic individuals, communicating emotions can be difficult — not because emotions are absent, but because traditional ways of understanding emotions may not work.

**HeardAutism explores how AI can become a bridge between human emotion and human understanding. ❤️**


---

# 🚀 What is HeardAutism?

HeardAutism is an experimental AI system designed to recognize emotions using:

🎧 **Voice / Audio signals**

🙂 **Facial expressions**

🧠 **Deep learning feature understanding**

The goal is creating technology that can help interpret emotional states in a more accessible way.


---

# 🏗️ Architecture

```

```
             Human Emotion
                   |
    ┌──────────────┴──────────────┐
    |                             |
  🎧 Audio                      🙂 Face
    |                             |
```

CNN + GRU Model              MobileNetV2
|                             |
└──────────────┬──────────────┘
|
Emotion Understanding
|
┌─────────────────────────┐
│ Happy                    │
│ Sad                      │
│ Fear                     │
│ Anger                    │
│ Neutral                  │
└─────────────────────────┘

```


---

# 🧠 AI Models Used


## 🎧 Audio Emotion Recognition

The audio branch uses:

- CNN layers → learn audio patterns
- GRU layers → understand temporal information
- Mel-spectrogram based features

Pipeline:

```

Audio
↓
Feature Extraction
↓
CNN
↓
GRU
↓
Emotion Prediction

```


---

## 🙂 Facial Emotion Recognition

The vision branch uses:

**MobileNetV2**

Why?

Because it is lightweight and suitable for future edge/mobile deployment.

Pipeline:

```

Face Image
↓
MobileNetV2
↓
Feature Extraction
↓
Emotion Classification

```


---

# 🔥 Multi-Modal Learning Idea

One interesting part of HeardAutism is combining different emotional signals.

The model learns:

> "What does a person look like when producing a certain emotion?"
>
> "What does a person sound like when expressing that emotion?"


During training:

```

Audio + Face
|
|
Deep Feature Learning
|
↓
Better Emotion Representation

```


During deployment:

```

🎧 Audio Only
|
↓
Lightweight Emotion Detection

```


---

# 🛠️ Technologies

| Technology | Purpose |
|-|-|
| Python | Core development |
| TensorFlow / Keras | Deep learning |
| CNN | Pattern recognition |
| GRU | Sequence understanding |
| MobileNetV2 | Face recognition |
| NumPy | Data processing |
| Librosa | Audio processing |


---

# 📂 Project Structure

```

HeardAutism/

│
├── HeardAutism.ipynb     # Main experiment notebook
│
├── models/
│   ├── audio_model
│   └── face_model
│
├── datasets/
│
└── README.md

```


---

# ⚙️ How It Works

1. Audio is converted into machine-readable features 🎧

2. Facial images are processed through a vision network 🙂

3. Neural networks extract hidden emotional patterns 🧠

4. The system predicts an emotional category


---

# 📊 Emotion Classes

Currently:

```

😡 Anger
😨 Fear
😊 Happy
😐 Neutral
😢 Sad

```


---

# 🌱 Future Vision

HeardAutism is a step toward more empathetic AI.

Possible future improvements:

- 📱 Real-time mobile application
- ⌚ Wearable emotion assistant
- 🌍 Support for different cultures and expressions
- 🗣️ Real-time communication assistance
- 🤖 Human-centered AI companions


---

# ⚠️ Important Note

This project is a research exploration.

Emotion recognition from AI is complex and should not replace professional evaluation.

The goal is assistance, understanding, and accessibility.


---

# ⭐ Motivation

Technology should not only become smarter.

It should become more understanding.

**HeardAutism is an attempt to make AI listen, see, and understand human emotions better. ❤️**

```

This will make the repo look like a serious AI research project instead of "just a notebook uploaded".
