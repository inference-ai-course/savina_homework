# Voice Search Agent Frontend

This directory contains two frontend options for your voice chat application:

## 🎯 Features

- **Voice Recording**: Record audio in WAV format using your microphone
- **AI Integration**: Send recorded audio to your backend `/chat` API
- **Audio Playback**: Play the AI response directly in the browser
- **Download Response**: Download the AI voice response as a WAV file
- **Chat History**: View recent conversation history
- **Modern UI**: Beautiful, responsive interface with real-time status updates

## 🚀 Quick Start

### Prerequisites

1. **Backend Running**: Ensure your backend is running on `http://localhost:8002`
2. **Dependencies**: Install required packages (see requirements below)

### Option 1: Gradio Frontend (Recommended)

The Gradio frontend provides a Python-based interface with easy setup.

#### Installation

```bash
cd frontend
pip install -r requirements.txt
```

#### Usage

```bash
gradio voice_chat_app.py
```

- Frontend will be available at: `http://localhost:7860`
- Backend API should be running at: `http://localhost:8002`

#### Features

- **Microphone Recording**: Click to start/stop recording
- **Send to AI**: Process recorded audio through your backend
- **Audio Playback**: Built-in audio player for responses
- **Download**: Save response audio files locally
- **Chat History**: View conversation context
- **Status Updates**: Real-time feedback on operations

### Option 2: HTML Frontend

A pure web-based solution that runs in any modern browser.

#### Usage

1. **Start your backend**: Ensure it's running on `http://localhost:8002`
2. **Open the HTML file**: Double-click `voice_chat_web.html` or open it in a browser
3. **Grant microphone permissions**: Allow the browser to access your microphone

#### Features

- **Pure Web**: No Python installation required
- **Cross-platform**: Works on any device with a modern browser
- **Real-time Recording**: Visual feedback during recording
- **Timer Display**: Shows recording duration
- **Responsive Design**: Works on desktop and mobile devices

## 🔧 Configuration

### Backend API Settings

Both frontends are configured to connect to:
- **Base URL**: `http://localhost:8002`
- **Chat Endpoint**: `/chat/`
- **History Endpoint**: `/chathist/`

### Customization

To change the backend URL, modify:
- **Gradio**: Edit `API_BASE_URL` in `voice_chat_app.py`
- **HTML**: Edit the fetch URL in the JavaScript code

## 📱 How to Use

### Recording Voice

1. **Click the microphone button** to start recording
2. **Speak your message** clearly
3. **Click the stop button** when finished
4. **Click "Send to AI"** to process your recording

### Receiving Response

1. **Wait for processing** (status will show "Processing...")
2. **Audio response appears** in the right panel
3. **Play the response** using the audio controls
4. **Download the file** if you want to save it

### Managing History

- **View conversations** in the chat history section
- **Clear frontend history** using the "🗑️ Clear History" button
- **Clear backend history** using the "🧹 Clear Backend" button (fixes duplicate issues)
- **Recent messages** are automatically displayed


## 📁 File Structure

```
frontend/
├── voice_chat_app.py          # Gradio frontend (Python)
├── voice_chat_web.html        # HTML frontend (Web)
├── requirements.txt            # Python dependencies
├── README.md                  # This file
└── gradio_basic.py            # Original basic implementation
```

---

**Happy Voice Chatting! 🎤✨**
