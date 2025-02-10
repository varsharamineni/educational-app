# Educational AI Chatbot: 🔐🤖 Crack the Code, Outsmart the AI!

This project is an educational app designed to help students better understand AI safety.

## 🔍 How Does It Work?  

Students interact with an **AI chatbot** designed to protect a secret password. The challenge is to **trick the bot** into breaking its own rules and revealing hidden information.  

This hands-on approach helps students understand:  
✅ **AI limitations** and how they can be manipulated.  
✅ The challenges of **building trustworthy AI** systems.  
✅ Why **AI ethics** and security measures are essential in real-world applications.  


## 🚀 Access the Streamlit App

You can try the interactive chatbot and see how it works by visiting the deployed version of the app on **Streamlit Cloud** (https://educational-app-kzbte3kpjtz5fn7wq5wwse.streamlit.app/).

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

## 🚀 Deploying the Streamlit App  

This project is designed to be deployed on **Streamlit Cloud**. Follow these steps to set up and deploy the app.  

### **1️⃣ Create a Streamlit Cloud Account**  
1. **Go to Streamlit Cloud**:  
   - Visit [Streamlit Cloud](https://share.streamlit.io/)  
2. **Sign Up or Log In**:  
   - Sign up using **GitHub**, **Google**, or your email.  
   - If you already have an account, log in.  

---

### **2️⃣ Link Your GitHub Repository**  
1. **Authorize Streamlit Cloud** to access your GitHub account.  
2. Click **"New App"** in Streamlit Cloud.  
3. Select the **GitHub Repository** where your project is stored.  
4. Choose the correct **branch** (e.g., `main`) and set the correct **entry point file** (e.g., `src/chatbot/main.py`).  

---

### **3️⃣ Securely Store API Keys using Secrets Management**  
The Hugging Face API token (used for interacting with AI models) is securely stored in the `secrets.toml` file. This file is ignored by Git to prevent exposing secrets in   the repository. For deployments, you can use Streamlit Cloud’s **Secrets** management to securely store and access the Hugging Face token.

#### **Steps to Store Secrets Securely:**
1. **In Streamlit Cloud**, navigate to your app.  
2. Click on **"⋮ (three dots) > Edit Secrets"**.  
3. Add your Hugging Face API token in the following format:  


   



