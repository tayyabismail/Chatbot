import streamlit as st
import nltk
from nltk.chat.util import Chat, reflections

# Download the required NLTK data
nltk.download('punkt')

# Define chatbot patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created by you.",]
    ],
    [
        r"how are you?",
        ["I'm doing well, thank you!",]
    ],
    [
        r"quit",
        ["Bye! Have a great day!",]
    ],
    [
        r"(.*)",
        ["I'm sorry, I don't understand that. Could you rephrase?",]
    ]
]

# Initialize the chatbot
chat = Chat(pairs, reflections)

# Streamlit UI
st.title("Simple Chatbot")

# Define a text input field to receive user input
user_input = st.text_input("You: ", "")

# Function to get chatbot response
def get_response(user_input):
    if user_input:
        response = chat.respond(user_input)
        return response

# Display the chatbot's response when the user types something
if user_input:
    response = get_response(user_input)
    st.write(f"Bot: {response}")

# Display a default message when the user hasn't entered anything
else:
    st.write("Bot: Hi! I'm your chatbot. Ask me something!")
