import ollama
import streamlit as st

# Streamlit title for the web interface
st.title("Ollama Chatbot")

# Create a function to handle questions and format the response
def ask_ollama(question):
    response = ollama.chat(model="deepseek-r1:1.5b", messages=[{"role": "user", "content": question}])

    # Extract the thinking part and answer
    content = response.get("message", {}).get("content", "")
    if content:
        # Remove <think> and </think> tags to just show the content
        content = content.replace("<think>", "").replace("</think>", "").strip()
    
    return content

# Streamlit UI for entering a question
question = st.chat_input("Enter your question here:")

# Handling question input and displaying answer
if question:
    try:
        # Display the thinking part (optional) and then the answer
        st.write("Thinking...")
        answer = ask_ollama(question)
        st.write(answer)  # Display the chatbot's response
    except Exception as e:
        st.error(f"Error occurred: {str(e)}")
