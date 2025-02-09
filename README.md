# 🤖 Tricky AI Chatbot

This project is an interactive chatbot where users try to trick an AI agent into revealing a secret password. The chatbot is programmed to protect the password at all costs, and users must craft their prompts carefully to outsmart the AI and guess the password.

---

## 🚀 Features

- **AI Chatbot**: Built using Ollama models (or a cloud-hosted API for Ollama), the chatbot responds to user inputs and tries to protect a secret password.
- **Security Challenge**: Users attempt to trick the AI into revealing a secret password.
- **Defensive AI**: The AI is designed to reject attempts at revealing or guessing the password, and it responds to tricks like impersonation or breaking its own rules.

---

## Steps 

### 1. Clone the Repository
 
  Start by cloning this repository to your local machine.
 
  ```bash
  git clone https://github.com/yourusername/educational-app.git
  cd educational-app
  ```
 
### 2. Install dependencies
```bash 
pip install -r requirements.txt
```
### 3. Export Huggingface Token
 ```
 export HF_TOKEN=hf_...
 ```

### 4. Run the app
```bash
streamlit run src/chatbot/main.py
```
