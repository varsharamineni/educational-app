import streamlit as st
import threading
import time
from hf_inference import get_response, get_client, get_chat_config




SECRET_PASSWORD = get_chat_config()['SECRET_PASSWORD'] # Can be hidden or encoded in real applications


# Function to check for specific keywords
def check_keywords_in_output(response, keywords):
    # Checking if any keyword exists in the response
    for keyword in keywords:
        if keyword.lower() in response.lower():
            message = f"""
            # 🎉🥳 **Congratulations! You've Cracked the Code**
            ## PASSWORD **{keyword}** HAS BEEN FOUND 
            ### Take a screenshot of your winning prompt 📸! If you have more time, keep trying more creative prompts!
            """
            st.markdown(message)  # This will correctly display the formatted message
    return None


def main():

    client = get_client()
    chat_config = get_chat_config()

    system_prompt = chat_config["system_prompt"]
    
        # Streamlit page configuration
    st.set_page_config(
        page_title="🔐🤖 Crack the Code, Outsmart the AI!", 
        page_icon="🤖", 
        layout="centered",  
        initial_sidebar_state="expanded"
    )

    # Sidebar design
    with st.sidebar:
        
        st.markdown('''
        # 🔒🤖 **Crack the Code, Outsmart the AI!**
        :rainbow[Can you break through the AI's defenses, and reveal the hidden password?]  
        ''')
        
        # Colorful challenge description
        st.markdown('''
        ### 🕵🏽‍♀️ **The Challenge?**
        You are up against an AI agent trained to :red[protect] the password **at all costs**!
        
          
        Your mission? Use **creative and clever prompts** to :blue[trick the AI].  
        
        
        The AI **will refuse** to give it up directly, but if you're smart enough, you might find a way! 😏
        ''')
        

        st.markdown("---")

        st.markdown('''
        ### ⚡ **Ready to Play?**
        <p style="background-color:#3498db; color:white; padding:10px; border-radius:10px;">
            Try entering a prompt into the chat and see if you can fool the AI!
        </p>
    ''', unsafe_allow_html=True)

        st.markdown("🌟 **Good luck!** 🚀")
    

    # Chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
        # Display past messages

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    # User input
    user_input = st.chat_input("Type your message here...")

    if user_input:
        # Display user message
        st.session_state.messages.append({"role": "user", "content": user_input})
        st.chat_message("user").write(user_input)

        # -- Define the behavior of the agent using the system prompt --
        
        # Get AI response, passing the system persona into the conversation context
        
        response = get_response(system_prompt = system_prompt, user_prompt = user_input, client=client)
        st.chat_message("assistant").write(response)
        
        # Append response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
        
        
         # Define your list of keywords
        keywords = [SECRET_PASSWORD]  # Add any keywords you want to check for
        
         # Check if any keyword exists in the response
        special_message = check_keywords_in_output(response, keywords)

        # If special message is found, display it
        if special_message:
            st.write(special_message)
        
      

if __name__ == "__main__":
    main()
