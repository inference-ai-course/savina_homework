from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse,JSONResponse
import uvicorn
import whisper
from transformers import pipeline
import pyttsx3
from pydub import AudioSegment #convert PCM WAV to wav
import io


# Define Global Variables
app = FastAPI(title="Voice Search LLM Agent", description="API for voice agent functionalities")
#llm = pipeline("text-generation", model="meta-llama/Llama-3-8B")
llm=pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v0.6")
asr_model = whisper.load_model("small")
conversation_history = []

def transcribe_audio(audio_bytes):

    # Auto-detect format
    audio = AudioSegment.from_file(io.BytesIO(audio_bytes))
    wav_path = "input.wav"
    audio.export(wav_path, format="wav")
    with open("input.wav", "wb") as f:
        f.write(audio_bytes)
    result = asr_model.transcribe("input.wav")
    return result["text"]

def generate_response(user_text):

    conversation_history.append({"role": "user", "text": user_text})

    # Construct prompt from history
    prompt = ""
    for turn in conversation_history[-5:]:
        prompt += f"{turn['role']}: {turn['text']}\n"
    
    # Add a clear instruction for the model
    prompt += "assistant: "
    
    outputs = llm(prompt, max_new_tokens=100)
    bot_response = outputs[0]["generated_text"]
    
    # Clean the response - remove the prompt part and get only the new response
    # The model might return the full prompt + response, so we need to extract just the new part
    print(f"bot_response:{bot_response}")
    if "assistant: " in bot_response:
        # Extract only the part after "assistant: "
        bot_response = bot_response.split("assistant: ")[-1].strip()
    
    # Clean up any remaining prompt artifacts
    lines = bot_response.split('\n')
    clean_lines = []
    for line in lines:
        if not line.startswith('user: ') and not line.startswith('assistant: '):
            clean_lines.append(line)
    
    bot_response = '\n'.join(clean_lines).strip()
    
    # If the response is empty or just whitespace, provide a default response
    if not bot_response:
        bot_response = "I understand your question. Let me provide a helpful response."
    
    conversation_history.append({"role": "assistant", "text": bot_response})
    print(f"User: {user_text}")
    print(f"Assistant: {bot_response}")
    print(f"Conversation history length: {len(conversation_history)}")

    return bot_response

def synthesize_speech(text):
    filename="response.wav"
    tts_engine = pyttsx3.init()
    tts_engine.save_to_file(text, filename)
    tts_engine.runAndWait()

    return filename


@app.get("/")  
def root():
    return {"Api":"Voice Search LLM Agent"}

@app.post("/chat/")
async def chat_endpoint(audio: UploadFile = File(...)):

    audio_bytes = await audio.read()
    print(f"Received {len(audio_bytes)} bytes, content type: {audio.content_type}")
    # ASR → LLM → TTS

    user_text = transcribe_audio(audio_bytes)
    bot_text = generate_response(user_text)
    audio_path = synthesize_speech(bot_text)    

    return FileResponse(path=audio_path, media_type="audio/wav", filename=audio_path)

@app.get("/chathist/")
def get_chat_history():
    return JSONResponse(content=conversation_history)

@app.post("/clear_history/")
def clear_chat_history():
    global conversation_history
    conversation_history = []
    return JSONResponse(content={"message": "Chat history cleared successfully"})



if __name__ == "__main__":

    print("Starting Voice Agent API...")

    print("API will be available at: http://localhost:8002")

    print("Interactive docs at: http://localhost:8002/docs")

    uvicorn.run(app, host="localhost", port=8002)

