import streamlit as st
import google.generativeai as generativeai

GOOGLE_API_KEY = 'votre-cle-api-google'
generativeai.configure(api_key=GOOGLE_API_KEY)
model = generativeai.GenerativeModel('gemini-1.5-pro-latest')
convo = model.start_chat()

st.title("Chat with Gemini AI")

chat_history = []

user_input = st.text_input(label="Type your message: ")

if user_input:
  convo.send_message(user_input)
  response = convo.last.text

  
  chat_history.append(f"You: {user_input}")
  chat_history.append("\n")
  chat_history.append(f"Model: {response}")

  
  chat_history_text = "\n".join(chat_history)

  
  st.write(chat_history_text)

