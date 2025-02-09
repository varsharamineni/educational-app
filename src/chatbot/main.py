import streamlit as st
from hf_inference import get_response, get_client, get_chat_config


def main():

    client = get_client()
    chat_config = get_chat_config()

    system_prompt = chat_config["system_prompt"]

    # Streamlit page config
    st.set_page_config(page_title="Tricky AI Chatbot", page_icon="🤖")

    st.title("🤖 Tricky AI Chatbot")
    st.write("You are trying to get the password from an AI Agent that is trying to protect it! Can you outsmart the agent?")

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
