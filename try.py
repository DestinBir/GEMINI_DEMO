import google.generativeai as generativeai

GOOGLE_API_KEY = 'votre-cle-api-google'
generativeai.configure(api_key=GOOGLE_API_KEY)

response = generativeai.GenerativeModel('gemini-1.5-pro-latest').generate_content(input('Votre question: '))

print(response.text)