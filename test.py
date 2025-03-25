from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_ollama import OllamaLLM
import asyncio

# Initialize FastAPI app
app = FastAPI()

# Middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust as needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files (CSS/JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Templates directory for HTML files
templates = Jinja2Templates(directory="templates")

# Initialize LLaMA model
llm_model = OllamaLLM(model="llama3", temperature=0.7, max_tokens=512)

# Pydantic model for input validation
class LLMInput(BaseModel):
    input_text: str

# System prompt for professional, clear responses without special characters
SYSTEM_PROMPT = (
    "You are a professional and friendly assistant. Always provide clear, concise, and precise answers. "
    "Organize your responses in plain text without using special characters like asterisks (**), dashes (-), or similar. "
    "Focus on delivering straightforward, easy-to-read information in well-structured sentences and paragraphs."
)

def format_response(response: str) -> str:
    """
    Format the response to ensure consistency and better readability.
    """
    response = response.strip()
    if not response.endswith("."):
        response += "."
    return response.capitalize()

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """
    Serve the HTML page for the chat interface.
    """
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/process-with-llm/")
async def process_with_llm(data: LLMInput):
    """
    Process input text and return a structured response from the LLaMA model.
    """
    try:
        # Log user input in the terminal
        print(f"User Input: {data.input_text}")
        
        # Add system prompt to input
        input_with_prompt = f"{SYSTEM_PROMPT}\nUser: {data.input_text}\nAssistant:"
        raw_response = await asyncio.to_thread(llm_model.invoke, input_with_prompt)

        formatted_response = format_response(raw_response)
        
        # Log bot output in the terminal
        print(f"Bot Response: {formatted_response}")
        
        if formatted_response:
            return {"input": data.input_text, "response": formatted_response}
        else:
            return {"input": data.input_text, "response": "I couldn't process that. Could you please rephrase?"}
    except Exception as e:
        # Log the error in the terminal
        print(f"Error processing text: {e}")
        raise HTTPException(status_code=500, detail=f"Error processing text: {e}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
