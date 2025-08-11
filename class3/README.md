# Voice Search Agent 

<img width="933" height="453" alt="UI" src="https://github.com/user-attachments/assets/16d77704-ac25-4dee-82b0-2f49e0ae8c96" />


This application contains frontend and backend API for your voice chat wiht LLM:

## 🎯 Features

- **Voice Recording**: Record audio in WAV format using your microphone
- **AI Integration**: Send recorded audio to your backend `/chat` API
- **Audio Playback**: Play the AI response directly in the browser
- **Download Response**: Download the AI voice response as a WAV file
- **Chat History**: View recent conversation history
- **Modern UI**: Beautiful, responsive interface with real-time status updates

## ✨ LLM Model

- TinyLlama/TinyLlama-1.1B-Chat-v0.6

## 📁 File Structure

```
frontend/
├── voice_chat_app.py          # Gradio frontend (Python)
├── voice_chat_web.html        # HTML frontend (Web)
├── requirements.txt           # Python dependencies
├── README.md                  # Readme
└── gradio_basic.py            # Original basic implementation

backend/
├── main.py                     # Major backend runner (Python)
├── test_backend.py             # Tests for the APIs
├── requirements.txt            # Python dependencies
└── README.md                   # Readme

```

---

**Happy Voice Chatting! 🎤✨**
