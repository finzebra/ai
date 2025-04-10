import streamlit as st
from google import genai
from google.genai import types
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import os
from dotenv import load_dotenv
import base64

# Load environment variables
load_dotenv()

# Set up the Streamlit app
st.title("🎭 AI Meme Generator")
st.write("Create custom memes with AI-generated images using Gemini 2.0!")

# Configure Google Gemini API
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    st.error("Please set the GOOGLE_API_KEY environment variable.")
    st.stop()

# Create the Gemini client with API key
client = genai.Client(api_key=GOOGLE_API_KEY)

# Function to generate image using Gemini 2.0
def generate_image(prompt):
    try:
        # Enhance the prompt for better meme-suitable images
        enhanced_prompt = f"Create a funny meme-worthy image of {prompt}. Make it visually clear, colorful, and suitable for adding text captions."
        
        response = client.models.generate_content(
            model="gemini-2.0-flash-exp-image-generation",
            contents=enhanced_prompt,
            config=types.GenerateContentConfig(
                response_modalities=['Text', 'Image']
            )
        )
        
        # Extract the image from the response
        image_text = None
        image_data = None
        
        for part in response.candidates[0].content.parts:
            if part.text is not None:
                image_text = part.text
            elif part.inline_data is not None:
                image_data = part.inline_data.data
                
        if image_data:
            image = Image.open(BytesIO(image_data))
            return image, image_text or "Image generated successfully"
        
        return None, "No image was generated."
    
    except Exception as e:
        st.error(f"Error generating image: {e}")
        return None, str(e)

# Function to add text to image
def add_text_to_image(image, top_text, bottom_text):
    # Create a copy of the image to avoid modifying the original
    img = image.copy()
    draw = ImageDraw.Draw(img)
    width, height = img.size
    
    # Try to use a standard font, or fall back to default
    try:
        # Calculate font size based on image width
        font_size = width // 8
        # Use default font since we can't guarantee specific fonts are installed
        font = ImageFont.load_default()
    except Exception:
        font = ImageFont.load_default()
    
    # Function to draw text with outline for better visibility
    def draw_text_with_outline(text, y_position):
        # Calculate text size to center it
        try:
            text_width = draw.textlength(text, font=font)
        except AttributeError:
            # For older PIL versions
            text_width, _ = draw.textsize(text, font=font)
            
        position = ((width - text_width) / 2, y_position)
        
        # Draw black outline by offsetting the text in multiple directions
        outline_width = 2
        for dx, dy in [(j, i) for i in range(-outline_width, outline_width+1) 
                             for j in range(-outline_width, outline_width+1)]:
            draw.text((position[0]+dx, position[1]+dy), text, font=font, fill="black")
        
        # Draw white text
        draw.text(position, text, font=font, fill="white")
    
    # Add top text
    top_text = top_text.upper()  # Traditional meme format uses uppercase
    draw_text_with_outline(top_text, height * 0.05)
    
    # Add bottom text
    bottom_text = bottom_text.upper()  # Traditional meme format uses uppercase
    draw_text_with_outline(bottom_text, height * 0.85)
    
    return img

# User inputs
st.subheader("Create Your Meme")
image_description = st.text_input("Describe the image you want for your meme:", "cat sitting at computer")
top_text = st.text_input("Top text:", "When you're trying to code")
bottom_text = st.text_input("Bottom text:", "But have no idea what you're doing")

# Template selection
template_option = st.selectbox(
    "Or choose a template idea:",
    ["Custom (use description above)", "Confused Animal", "Thinking Character", "Success Moment", "Funny Fail"]
)

# Handle template selection
if template_option != "Custom (use description above)":
    template_map = {
        "Confused Animal": "a confused cat looking at a computer",
        "Thinking Character": "a person thinking hard with a puzzled expression",
        "Success Moment": "a child celebrating a small victory with a fist pump",
        "Funny Fail": "someone falling or failing at a simple task in a funny way"
    }
    image_description = template_map.get(template_option, image_description)

# Generate button
if st.button("Generate Meme"):
    with st.spinner("Generating an AI image for your meme..."):
        try:
            # Generate image
            img, description = generate_image(image_description)
            
            if img:
                # Add text to the image
                meme = add_text_to_image(img, top_text, bottom_text)
                
                # Display the meme
                st.image(meme, caption="Your Generated Meme", use_column_width=True)
                
                # Convert image to bytes for download
                buf = BytesIO()
                meme.save(buf, format="PNG")
                byte_im = buf.getvalue()
                
                # Add download button
                st.download_button(
                    label="Download Meme",
                    data=byte_im,
                    file_name="ai_meme.png",
                    mime="image/png"
                )
                
                # Show the AI's description
                with st.expander("AI's thoughts about this image"):
                    st.write(description)
                
        except Exception as e:
            st.error(f"Error generating meme: {e}")

# Instructions
with st.expander("How to use this app"):
    st.markdown("""
    1. Enter a description of the image you want or choose a template
    2. Add text for the top and bottom of your meme
    3. Click 'Generate Meme'
    4. Download your creation!
    
    **Note:** This app requires a Google API key with access to the Gemini 2.0 image generation model.
    """)

# Setup instructions
with st.expander("Setup Instructions"):
    st.markdown("""
    ### Setting up your environment:
    
    1. Install required packages:
       ```
       pip install google-generativeai streamlit pillow python-dotenv
       ```
    
    2. Get a Google API key from [Google AI Studio](https://aistudio.google.com/)
    
    3. Create a `.env` file in your project directory with:
       ```
       GOOGLE_API_KEY=your_api_key_here
       ```
    
    4. Run the app with:
       ```
       streamlit run app.py
       ```
    """)

# About GenAI concepts
with st.expander("GenAI Concepts for Beginners"):
    st.markdown("""
    This application demonstrates several key concepts in Generative AI:
    
    - **Text-to-Image Generation**: Converting text descriptions into visual content
    - **Prompt Engineering**: Crafting effective text prompts to get desired outputs
    - **Image Manipulation**: Adding text overlays to generated images
    - **User Interface Design**: Creating interactive interfaces for AI applications
    - **API Integration**: Connecting to external AI services
    
    As you experiment with different prompts, you'll gain insights into how the AI interprets your descriptions and generates corresponding images.
    """)