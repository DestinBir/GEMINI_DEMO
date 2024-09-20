Here is the English version of the `README.md`:

# Google Generative AI Chatbot

This project is a chatbot based on the **Google Generative AI** API, using the **Gemini-1.5-pro-latest** model to generate responses from real-time conversations. It integrates customizable generation settings as well as safety filters to ensure a safe and controlled use of the generative model.

## Features

- Uses the Google Generative AI API for generating text-based responses.
- Adjustable generation settings (temperature, `top_p`, etc.).
- Built-in safety features to filter harmful content (hate speech, harassment, etc.).
- Maintains conversation history for smoother and more coherent interactions.

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/DestinBir/GEMINI_DEMO.git
cd GEMINI_DEMO
```

2. **Install the necessary dependencies:**

Ensure you have Python 3.x installed, then run the following command to install the `google-generativeai` library:

```bash
pip install google-generativeai
pip install streamlit
pip install kivy
```

3. **Configure the API key:**

Obtain a valid API key from your Google Cloud console and replace the value of the `GOOGLE_API_KEY` variable in the Python script:

```python
GOOGLE_API_KEY = 'your-google-api-key'
```

## Usage

Start the chatbot by running the Python script after configuring the API:

```bash
python chatbot-text.py
```

The chatbot will begin interacting with you in the command line. It will wait for user input and automatically respond via the **Gemini-1.5-pro-latest** model.

### Example Interaction:

```
====> You: Hello, how are you?
      Gemini AI: Hello! I am doing well, thank you. How can I assist you today?
```

### Using the Web Interface:

Launch the chatbot interface by running the following Python command after configuring the API:

```bash
python interface.py
```

### Using the Graphical Interface:

Launch the graphical interface by running the following Python command:

```bash
python new.py
```

## Generation Settings

The model's behavior can be adjusted by modifying the following generation configuration:

```python
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}
```

- **temperature**: Controls the creativity of the responses (1 = more creative, 0 = more predictable).
- **top_p**: Limits token selection to those with cumulative probability (0.95 = more diverse).
- **top_k**: Selects the top `k` most likely tokens (0 = disabled).
- **max_output_tokens**: Defines the maximum length of the response in tokens.

## Safety

To ensure the chatbot does not generate harmful content, several safety rules are in place. These rules filter responses that may include potentially harmful or inappropriate content:

```python
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]
```

These parameters can be adjusted based on your needs by modifying the `threshold` for each category.

## Example Code

Here is the main chatbot code that uses the Google Generative AI API to engage in a conversation:

```python
import google.generativeai as generativeai

GOOGLE_API_KEY = 'your-google-api-key'
generativeai.configure(api_key=GOOGLE_API_KEY)

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = generativeai.GenerativeModel(model_name="gemini-1.5-pro-latest", generation_config=generation_config, safety_settings=safety_settings)

convo = model.start_chat(history=[])

while True:
    user_input = input("====> You: ")
    convo.send_message(user_input)
    print('      Gemini AI:', convo.last.text)
```

## Contributions

Contributions are welcome! Feel free to open issues or submit pull requests if you wish to improve the project.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more details.
```

### What this `README_en.md` does:
- It introduces the project and its main features.
- It provides step-by-step installation, usage instructions, and configuration for the chatbot.
- It explains how to adjust the text generation parameters and safety settings.
- It includes an example code ready to use for starting a conversation with the chatbot.
- It provides instructions on how to contribute and includes licensing information.

Feel free to adjust or expand this version based on your project needs!