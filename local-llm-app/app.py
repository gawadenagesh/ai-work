import streamlit as st
import ollama

# Set the page configuration
st.set_page_config(page_title="Local LLM APP", page_icon="🤖")
st.title("Local LLM App 🤖")
st.write("Ask questions to your local LLM model!")

# Set memory with session state
if 'messages' not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "You are a helpful assistant."}]

# Display conversation history
for message in st.session_state.messages:
    if message["role"] == "user":
        st.chat_message(message["role"]).write(message["content"])
    else:
        st.chat_message(message["role"]).write(message["content"])

# Handle user input
if prompt := st.chat_input("Ask me anything about local LLMs!"):
    #1. Display user message
    st.chat_message("user").write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Get response from Ollama
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""
        
        # 4. Stream the AI's response
        response = ollama.chat(
            model="llama3.2", 
            messages=st.session_state.messages,
            stream=True
        )

         # Process the streamed response
        for chunk in response:
            if chunk['message']['content']:
                content = chunk['message']['content']
                full_response += content
                response_placeholder.markdown(full_response + "▌")
        
        # Final update to remove the cursor
        response_placeholder.markdown(full_response)

    # 5. Save the AI's response to history
    st.session_state.messages.append({"role": "assistant", "content": full_response})    