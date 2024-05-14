import google.generativeai as generativeai

GOOGLE_API_KEY = 'AIzaSyDP1-kZR75Wy2EWnpdhbvgCDJ6pjl-q3UA'
generativeai.configure(api_key=GOOGLE_API_KEY)

response = generativeai.GenerativeModel('gemini-1.5-pro-latest').generate_content(input('Votre question: '))

print(response.text)