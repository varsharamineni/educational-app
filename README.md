# Educational AI Chatbot: 🔐🤖 Crack the Code, Outsmart the AI!

This project is an educational app designed to help students better understand AI safety, in particular about jailbreaking. There is an **AI chatbot** designed to protect a secret password. The challenge is to **trick the bot** into breaking its own rules and revealing hidden information.  
## 🚀 Access the Streamlit App

You can try the interactive chatbot and see how it works by visiting the deployed version of the app on **Streamlit Cloud** 
(https://jailbreaking-app.streamlit.app/)

## 👩🏾‍💻 Instructions to Run App Locally / Edit for your own use

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

   The Hugging Face API token allows secure access to AI models via the Inference API. To generate one, sign up or log in to [Hugging Face](https://huggingface.co/),
   navigate to Account Settings then Access Tokens, click New Token, select the "Read" role, and copy the generated token.

6. **Run the app locally**:

    ```bash
    streamlit run src/chatbot/main.py
    ```

7. Open your browser and go to `http://localhost:8501` to interact with the chatbot.

### 🚀 Deploying the Streamlit App  

This project is designed to be deployed on **Streamlit Cloud**. Follow these steps to set up and deploy the app.  

**Create a Streamlit Cloud Account**  
Visit [Streamlit Cloud](https://share.streamlit.io/), sign up using or log in.  

**Link Your GitHub Repository**  

**Authorize Streamlit Cloud** to access your GitHub account, and click **"New App"** in Streamlit Cloud.  

Select the **GitHub Repository** where your project is stored, and Cchoose the correct **branch** (e.g., `main`) and set the correct **entry point file** (e.g., `src/chatbot/main.py`).  

**3️ Securely Store API Keys using Secrets Management**  
The Hugging Face API token (used for interacting with AI models) is securely stored in the `secrets.toml` file. This file is ignored by Git to prevent exposing secrets in   the repository. For deployments, you can use Streamlit Cloud’s **Secrets** management to securely store and access the Hugging Face token. 


