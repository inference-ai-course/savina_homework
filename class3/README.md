
# Voice Search Agent

It understands your voice and responds with voice.


## Features

- Speech Recognition (ASR)
- Dialogue Generation with LLMs:
  Feed transcribed user vovo into LLM and generated nature language responses
- Text-to-Speach(TTS): 
  TTS engine to convert generated responses into spoken audio
- API Serving: 
  Web server with API to handle audio file uploads and return voice responses
- Conversation State Management: 
  Track conversation history to enable multi-turn interaction
- Low-Latency Real-time Processing: 
  Use asynchronous function to reduce inference time and improve response experience
  


## Deployment

To deploy this project run

```bash
  pip install -r requirements.txt
```


## API Reference

#### POST user's voice file in .mp3 or .wav format

```http
  POST /chat
```

|  Description                |
|  :------------------------- |
| Post the user voice file as data |

#### Get the conversation history between user and the search agent

```http
  GET /chathist
```

|  Description                       |
|  :-------------------------------- |
|  It fetches the conversation history |



## Demo

1. Startup server：python main.py 
screenshots\1-StartupServer.png

2. Access http://localhost:8002/docs
screenshots\2-endpoint-docs.png

3. Tryout POST /chat and send user's voice
screenshots\3-endpoint-chat-uploadfile.png

4. Get the voice of agent
screenshots\4-endpoint-chat-download-response.png

5. Retrive the chatting history
screenshots\5-endpoint-chathist.png

6. Ctrl + c Stop the server
screenshots\6-shutdown.png



