import os
import streamlit as st
import google.generativeai as genai

# Set your Gemini API key (ensure you set your API key in the environment variables)
API_KEY = 'AIzaSyBTSCyEE-McpYa29KmpP5w5cZXKQC7E_Rg'
genai.configure(api_key=API_KEY)

# Create the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

# CSS for styling
st.markdown(
    """
    <style>
    /* General Body Styling */
    body {
        background-color: #E0F7FA; /* Background color */
        font-family: 'Arial', sans-serif;
    }

    /* Custom Title Style */
    h1 {
        color: #4B86B4;
        text-align: center;
        font-weight: bold;
        margin-bottom: 1em;
        font-size: 2.5em;
    }

    /* Style for Input Box */
    input[type="text"] {
        border: 2px solid #4B86B4;
        border-radius: 5px;
        padding: 0.75em;
        width: calc(100% - 1.5em); /* Adjust width for padding */
        font-size: 1.2em;
        box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.1);
        transition: border-color 0.3s ease;
    }

    input[type="text"]:focus {
        border-color: #1E2A78; /* Darker color on focus */
        outline: none;
    }

    /* Button Styling */
    button {
        background-color: #FF5722; /* Custom button color */
        color: white;
        border: none;
        padding: 12px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 1.2em;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s ease, transform 0.3s ease;
        margin-top: 1em;
    }

    button:hover {
        background-color: #E64A19; /* Darker color on hover */
        transform: scale(1.05); /* Slightly enlarge button on hover */
    }

    button:active {
        background-color: #BF360C; /* Even darker color on click */
        transform: scale(1); /* Return to normal size on click */
    }

    /* Content Display Box */
    .stText {
        background-color: #E8F0FE;
        border: 1px solid #4B86B4;
        padding: 1em;
        border-radius: 10px;
        font-family: 'Courier New', Courier, monospace;
        color: #1E2A78; /* Dark blue text color */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        margin-top: 1em;
        transition: transform 0.3s ease;
    }

    .stText:hover {
        transform: scale(1.02); /* Slightly enlarge content box on hover */
    }

    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit app setup
st.title("Content Creator using Gemini LLM")

# User input for content topic
content_topic = st.text_input("Enter a Content Topic:")

# Generate content button
if st.button("Generate Content"):
    if content_topic:
        # Initiate a chat session
        chat_session = model.start_chat(
            history=[
                {
                    "role": "user",
                    "parts": [
                        f"generate content based on the topic: {content_topic}",
                    ],
                }
            ]
        )

        # Send the user's message and get a response
        response = chat_session.send_message(content_topic)

        # Display the generated content with custom styling
        st.markdown(f'<div class="stText">{response.text}</div>', unsafe_allow_html=True)
    else:
        st.error("Please enter a content topic.")
