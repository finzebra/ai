import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key from .env file or environment variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Configure Gemini API (or show error and stop)
if not api_key:
    st.error("🔴 GOOGLE_API_KEY not found. Please set it via .env or environment variable.")
    st.stop()
try:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash-latest')
except Exception as e:
    st.error(f"🔴 Failed to initialize Gemini: {e}")
    st.stop()

# Initialize session state to store poem and topic
st.session_state.setdefault('poem_text', '')
st.session_state.setdefault('poem_topic', '')

# --- App Interface ---
st.title("✍️ AI Poetry Generator")

topic = st.text_input("Enter poem topic:", placeholder="e.g., A lonely robot")

if st.button("Generate Poem ✨"):
    if topic:
        prompt = f"Write a short, creative poem about: {topic}."
        try:
            with st.spinner("Generating..."):
                response = model.generate_content(prompt)
                st.session_state.poem_text = response.text
                st.session_state.poem_topic = topic # Remember the topic
        except Exception as e:
            st.error(f"🔴 Error generating poem: {e}")
            st.session_state.poem_text = "" # Clear on error
            st.session_state.poem_topic = ""
    else:
        st.warning("⚠️ Please enter a topic.")
        st.session_state.poem_text = "" # Clear if no topic entered
        st.session_state.poem_topic = ""


# --- Display Poem and Actions ---
if st.session_state.poem_text:
    st.divider()
    st.subheader(f"📜 Poem about '{st.session_state.poem_topic}'")

    # Display poem in a text area for easy copying ("Share")
    st.text_area(
        "Generated Poem:",
        value=st.session_state.poem_text,
        height=200,
        key="poem_display"
    )

    # Simple filename cleaning (replace non-alphanumeric with '_')
    safe_filename = "".join(c if c.isalnum() else "_" for c in st.session_state.poem_topic)
    safe_filename = f"{safe_filename.lower().strip('_') or 'poem'}.txt" # Ensure name exists

    # Download Button
    st.download_button(
        label="📥 Download (.txt)",
        data=st.session_state.poem_text.encode('utf-8'),
        file_name=safe_filename,
        mime='text/plain'
    )