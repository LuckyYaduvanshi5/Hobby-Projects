from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
import streamlit as st

# Streamlit title for the web interface
st.title("LangChain-DeepSeek-R1 Web Interface")

# Initialize session state for storing chat history (if not already present)
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Define your prompt template
template = """Question: {question}

Answer: Let's think step by step."""

# Create a chat prompt template with your defined template
prompt = ChatPromptTemplate.from_template(template)

# Initialize the LLM model for DeepSeek R1 (or Ollama)
model = OllamaLLM(model="deepseek-r1:1.5b")  # Use "deepseek-r1" for DeepSeek, or "llama3.1" for Llama

# Set up LangChain chain (combining prompt and model)
chain = prompt | model

# Display previous chat history
for chat in st.session_state.chat_history:
    st.write(f"**Q:** {chat['question']}")
    st.write(f"**A:** {chat['answer']}")

# Streamlit UI for entering a question
question = st.chat_input("Enter your question here:")

# Handling connection errors and maintaining chat history
if question:
    try:
        # Combine current chat history with the new question
        combined_history = "\n".join([f"Q: {chat['question']}\nA: {chat['answer']}" for chat in st.session_state.chat_history])
        updated_prompt = template.format(question=question) + "\n" + combined_history
        response = chain.invoke({"question": updated_prompt})
        
        # Display response
        st.write(f"**A:** {response['answer']}")

        # Append the new question and answer to the chat history
        st.session_state.chat_history.append({"question": question, "answer": response['answer']})
        
    except Exception as e:
        st.error(f"Error occurred: {str(e)}")
