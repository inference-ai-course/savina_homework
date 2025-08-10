from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse,JSONResponse
import uvicorn
import whisper
from transformers import pipeline
import pyttsx3


# Define Global Variables
app = FastAPI(title="Voice Search LLM Agent", description="API for voice agent functionalities")
#llm = pipeline("text-generation", model="meta-llama/Llama-3-8B")
llm=pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v0.6")
asr_model = whisper.load_model("small")
conversation_history = []

def transcribe_audio(audio_bytes):

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
    outputs = llm(prompt, max_new_tokens=100)
    bot_response = outputs[0]["generated_text"]
    conversation_history.append({"role": "assistant", "text": bot_response})
    #print(f"conversation_history:{conversation_history}")

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
async def chat_endpoint(file: UploadFile = File(...)):
    audio_bytes = await file.read()
    
    # ASR → LLM → TTS

    user_text = transcribe_audio(audio_bytes)
    bot_text = generate_response(user_text)
    audio_path = synthesize_speech(bot_text)    

    return FileResponse(path=audio_path, media_type="audio/wav", filename=audio_path)

@app.get("/chathist/")
def get_chat_history():
    return JSONResponse(content=conversation_history)



if __name__ == "__main__":

    print("Starting Voice Agent API...")

    print("API will be available at: http://localhost:8002")

    print("Interactive docs at: http://localhost:8002/docs")

    uvicorn.run(app, host="localhost", port=8002)

