import google.generativeai as generativeai

GOOGLE_API_KEY = 'votre-cle-api-google'
generativeai.configure(api_key=GOOGLE_API_KEY)
model = generativeai.GenerativeModel('gemini-1.0-pro-latest')

#response = generativeai.GenerativeModel('gemini-1.0-pro-latest').generate_content(input('Enter a prompt: '))
#
#print(response.text)

convo = model.start_chat()

while True:
    user_input = input('==> You: ')
    convo.send_message(user_input)
    print('    Gemini AI:', convo.last.text)
    