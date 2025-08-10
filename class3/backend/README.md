
# Voice Search Agent

It understands your voice and responds with voice


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

<img width="536" height="141" alt="1-StartupServer" src="https://github.com/user-attachments/assets/62439ffd-ebfd-4f7a-8a84-1b8b17bc8a36" />

2. Access http://localhost:8002/docs

<img width="1180" height="541" alt="2-endpoint-docs" src="https://github.com/user-attachments/assets/e5e37058-744f-4a9b-b0fa-ef3570e3e81f" />

3. Tryout POST /chat and send user's voice

<img width="1159" height="405" alt="3-endpoint-chat-uploadfile" src="https://github.com/user-attachments/assets/989ede5d-2bfd-4252-a9b9-9a7bfae62cf6" />

4. Get the voice of agent

<img width="1122" height="440" alt="4-endpoint-chat-download-response" src="https://github.com/user-attachments/assets/e363dabc-97e5-46a4-84a6-82074186e628" />

5. Retrive the chatting history

<img width="1168" height="691" alt="5-endpoint-chathist" src="https://github.com/user-attachments/assets/72cdd916-d894-4af4-ab5c-c893dcdf412c" />

6. Ctrl + c Stop the server

<img width="433" height="102" alt="6-shutdown" src="https://github.com/user-attachments/assets/4ead108d-f054-4e7a-b72b-0450fdf27491" />



