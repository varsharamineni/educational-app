# Educational AI Chatbot: 🔐🤖 Crack the Code, Outsmart the AI!

This project is an educational app designed to help students learn how to interact with an AI system while testing its ability to safeguard sensitive information. The main objective is to create a fun environment where students try to extract a secret password from the AI chatbot.

- **Interactive Chatbot**: The AI chatbot provides an engaging way to learn how AI can be used to protect sensitive information.
- **AI Security Challenge**: Students are tasked with outsmarting the chatbot to obtain a secret password.

## How It Works

1. The chatbot is designed to protect a **secret password** from unauthorized access.
2. Students' goal is to **outsmart the chatbot** and attempt to obtain the secret password.
3. The chatbot will refuse to provide the password, no matter how students try to trick it.

## Access Challenge Through The App

You can try the interactive chatbot and see how it works by visiting the deployed version of the app on **Streamlit Cloud** (https://educational-app-kzbte3kpjtz5fn7wq5wwse.streamlit.app/).

## Instructions to Run App Locally / Edit for your own use

Follow these steps to get the app running on your local machine.

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-username/educational-app.git
    cd educational-app
    ```

2. **Set up a virtual environment** (Optional, but recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use venv\Scripts\activate
    ```

3. **Install required dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Create `.streamlit/secrets.toml` file**:

    In the root directory of the project, create a `.streamlit/secrets.toml` file with your Hugging Face API token. 

    Example:

    ```toml
    [huggingface]
    HF_TOKEN = "your_huggingface_api_token_here"
    ```

    This file **will not be tracked by Git** due to `.gitignore`.

5. **Run the app locally**:

    ```bash
    streamlit run src/chatbot/main.py
    ```

6. Open your browser and go to `http://localhost:8501` to interact with the chatbot.
   
8.  Deploying using streamlit

   The Hugging Face API token (used for interacting with AI models) is securely stored in the `secrets.toml` file. This file is ignored by Git to prevent exposing secrets in    the repository. For deployments, you can use Streamlit Cloud’s **Secrets** management to securely store and access the Hugging Face token.



