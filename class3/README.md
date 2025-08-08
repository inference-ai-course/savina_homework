
# Voice Search Agent in real time

It listens, understands and responds with voice.


## Features

- Speech Recognition (ASR)
- Dialogue Generation with LLMs:
  Feed transcribed user input into LLM and generated nature language responses
- Text-to-Speach(TTS): 
  TTS engine to convert generated responses into spoken audio
- FastAPI for API Serving: 
  Web server with FastAPI to handle audio file uploads and return voice responses
- Conversation State Management: 
  Track conversation history to enable multi-turn interaction
- Low-Latency Real-time Processing: 
  Use asynchronous function to reduce inference time and improve response experience
  


## Tech Stack

**Client:** React, Redux, TailwindCSS

**Server:** Node, Express


## Deployment

To deploy this project run

```bash
  npm run deploy
```

