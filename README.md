# Telegram Chatbot with OpenAI Integration

This repository contains a Python-based Telegram chatbot that uses OpenAI API for generating responses. The chatbot engages in conversations with users and provides meaningful responses based on both predefined answers and context from previous interactions.

## Requirements

Before running the chatbot, make sure you have the following installed:

1. Python 3.x
2. `telebot` library: `pip install pyTelegramBotAPI`
3. `openai` library: `pip install openai`

## Setup

1. Clone this repository to your local machine.
2. Obtain an OpenAI API key. If you don't have one, sign up for an account at https://beta.openai.com/signup/.
3. Replace the `openai.api_key` value with your API key in the `bot.py` file:

```python
openai.api_key = "YOUR_OPENAI_API_KEY"
```

## How It Works

The chatbot uses OpenAI's `text-davinci-003` engine for generating responses. It maintains a chat history for each user to provide context during conversations. The chat history is limited to the last 50 user inputs.

### Predefined Answers

The chatbot has predefined answers for certain question patterns, such as name, age, location, occupation, relationship status, and dislikes. If a user input matches any of these patterns, the chatbot responds with the corresponding predefined answer.

### Generating Responses

If the user input does not match any predefined patterns, the chatbot generates a response using the OpenAI API. It combines the user input with the chat history to provide context. The generated response is limited to 100 tokens and has a temperature of 0.2 for controlled randomness.

### Telegram Bot Interaction

The chatbot interacts with users through a Telegram bot. When the user sends a message, the bot processes it, generates a response, and sends it back to the user. The bot also shows a typing indicator for a short duration to simulate a natural delay in response.

## Usage

1. Run the `bot.py` script to start the Telegram bot.
2. Interact with the bot by sending messages to it.
3. The bot will respond based on predefined answers or generate responses using OpenAI.

## Important Note

Remember to handle your API keys securely, especially if you plan to share the code or deploy the bot in a production environment. Avoid hardcoding sensitive information like API keys in the code itself. Instead, use environment variables or configuration files to store such data securely.

## Contributions

Contributions to this project are welcome! If you find any issues or have ideas to improve the chatbot, feel free to open an issue or submit a pull request.

## Disclaimer

This chatbot is for educational and demonstrative purposes only. The generated responses are based on the data available up to the knowledge cutoff date (September 2021) and might not reflect the most up-to-date information or follow the intended behavior. Use it responsibly and avoid using it for any malicious or harmful purposes.

Happy chatting! 😄
