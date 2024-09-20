from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

import google.generativeai as generativeai

GOOGLE_API_KEY = 'votre-cle-api-google'
generativeai.configure(api_key=GOOGLE_API_KEY)
model = generativeai.GenerativeModel('gemini-1.0-pro-latest')
convo = model.start_chat()


class ChatApp(App):
    chat_history = ""

    def send_message(self, instance):
        user_input = self.message_input.text
        if user_input:
            convo.send_message(user_input)
            response = convo.last.text
            self.chat_history += f"You: {user_input}\nGemini AI: {response}\n"
            self.chat_history_label.text = self.chat_history
            self.message_input.text = ""

    def build(self):
        layout = BoxLayout(orientation="vertical")

        chat_title = Label(text="Chat with Gemini AI", font_size=24, halign="center")
        chat_history_scroll = ScrollView(height=200)
        self.chat_history_label = Label(text=self.chat_history, text_size=chat_history_scroll.size)
        chat_history_scroll.add_widget(self.chat_history_label)

        message_input = TextInput(hint_text="Type your message")
        send_button = Button(text="Send", on_press=self.send_message)

        layout.add_widget(chat_title)
        layout.add_widget(chat_history_scroll)
        layout.add_widget(message_input)
        layout.add_widget(send_button)

        return layout


if __name__ == "__main__":
    ChatApp().run()
