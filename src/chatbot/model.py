import os
import openai
import ollama

# Load OpenAI API key from environment variable (for GPT-3.5)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def get_response(user_input: str, model: str = "ollama"):
    """
    Generates a chatbot response using either OpenAI or Ollama.
    """
    if model == "openai":
        if not OPENAI_API_KEY:
            return "⚠️ OpenAI API key is missing!"
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "You're a tricky chatbot."},
                      {"role": "user", "content": user_input}]
        )
        return response["choices"][0]["message"]["content"]

    elif model == "ollama":
        response = ollama.chat(model="mistral", messages=[{"role": "user", "content": user_input}])
        return response["message"]["content"]

    return "⚠️ Invalid model selection."