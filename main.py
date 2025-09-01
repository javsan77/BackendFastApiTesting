from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todos los orígenes
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

# Modelo para recibir mensajes
class ChatMessage(BaseModel):
    message: str

# Modelo para respuesta
class ChatResponse(BaseModel):
    response: str

@app.post("/chat")
async def chat_endpoint(message: ChatMessage):
    # Aquí va tu lógica del chatbot
    bot_response = f"Recibí tu mensaje: {message.message}"
    
    return ChatResponse(response=bot_response)

# Para probar
@app.get("/")
async def root():
    return {"message": "API funcionando correctamente"}