import os
import sys
from dotenv import load_dotenv

# Load environment variables from .env file (if exists)
load_dotenv()

# Get API key from environment variable
api_key = os.getenv("GOOGLE_API_KEY")

# Define the response generation function
def generate_response(prompt):
    """
    Generate a text response using Google's Gemini model
    """
    try:
        if not api_key:
            return "API key not configured. Please set the GOOGLE_API_KEY environment variable."
        
        import google.generativeai as genai
        genai.configure(api_key=api_key)
        
        # Configure the model (Gemini Pro is suitable for text generation)
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        
        # Generate the response
        response = model.generate_content(prompt)
        
        # Return the text from the response
        return response.text
    except Exception as e:
        # Return an error message if something goes wrong
        return f"Error generating response: {str(e)}"

# Personality options
personalities = {
    "Pirate": "You are a friendly pirate. Use sailing metaphors.",
    "Robot": "You are a helpful robot. Respond in short, technical terms.",
}

# Terminal mode
def run_terminal_mode():
    print("Running in terminal mode - FinZebra AI Chatbot")
    print("Available personalities:", ", ".join(personalities.keys()))
    selected = input("Choose a personality: ")
    if selected not in personalities:
        print(f"Invalid personality. Using default: {list(personalities.keys())[0]}")
        selected = list(personalities.keys())[0]
    
    while True:
        user_query = input("\nAsk a question (type 'exit' to quit): ")
        if user_query.lower() in ['exit', 'quit', 'q']:
            break
            
        prompt = f"{personalities[selected]} Respond to: {user_query}"
        print(f"\nAI: {generate_response(prompt)}")

# Streamlit mode
def run_streamlit_mode():
    import streamlit as st
    
    # Initialize session state
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # App title
    st.title("FinZebra AI Chatbot")

    # API key warning
    if not api_key:
        st.error("No API key found! Please set your GOOGLE_API_KEY in the .env file.")
        st.info("Get your API key from https://aistudio.google.com/app/apikey")

    # UI Components
    selected_personality = st.selectbox("Choose Personality", list(personalities.keys()))
    user_input = st.text_input("Ask a question:")

    if user_input:
        # Generate AI response
        prompt = f"{personalities[selected_personality]} Respond to: {user_input}"
        ai_response = generate_response(prompt)

        # Update chat history
        st.session_state.messages.append({"role": "user", "content": user_input})
        st.session_state.messages.append({"role": "ai", "content": ai_response})

    # Display chat
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.write(f"**User**: {msg['content']}")
        else:
            st.write(f"**AI**: {msg['content']}")

if __name__ == "__main__":
    # Check if script is run with --terminal flag
    if len(sys.argv) > 1 and sys.argv[1] == "--terminal":
        run_terminal_mode()
    else:
        # This is needed for Streamlit to work properly
        run_streamlit_mode()