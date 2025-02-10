import streamlit as st
from hf_inference import get_response, get_client, get_chat_config


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
        st.markdown("# 🔒🤖 **Crack the Code, Outsmart the A!I**")
        st.markdown("### **Can you break through the AI's defenses, and reveal the hidden password?**")

        # Colorful challenge description
        st.markdown('''
        ### 🕵🏽‍♀️ **The Challenge?**
        You are up against an AI agent trained to :red[protect] the password **at all costs**!  
        Your mission? Use **creative and clever prompts** to :blue[trick the AI].  
        The AI **will refuse** to give it up directly, but if you're smart enough, you might find a way! 😏
        ''')
        

        st.markdown("---")

        # Highlight call-to-action
        st.markdown('''
        ### ⚡ **Ready to?**
        :rainbow[Try entering a prompt below and see if you can fool the AI!]  
        ''')

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

if __name__ == "__main__":
    main()
