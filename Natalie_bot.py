import telebot
import openai
import re
import time

# Set up the OpenAI API
openai.api_key = "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"

# Set up the chat settings
model_engine = "text-davinci-003"
prompt = "You are my friend. You say:"

# Create a Telegram bot
bot = telebot.TeleBot("5921432792:AAHQ5tIQ-9VKmiD6lWkl2w5sjQCuQFQ4Tc4")

# Define the chat history
chat_history = {}

# Define a function to generate a response
def generate_response(prompt, user_input, chat_history):
    chat_history.append(user_input)
    chat_text = "\n".join(chat_history[-50:])  # Consider the last 50 user inputs for context
    prompt_with_history = f"{prompt}\n{chat_text}"

    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt_with_history,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.2,
    )
    message = response.choices[0].text.strip()

    return message

# Define predefined answers based on question patterns
def get_predefined_answer(user_input):
    if re.search(r"\bfather\b.*\bname\b", user_input):
        return "My father's name is John."
    elif re.search(r"\bmother\b.*\bname\b", user_input):
        return "My mother's name is Jane."
    elif re.search(r"\bage\b", user_input):
        return "Age is just a number, my friend!"
    elif re.search(r"\bname\b", user_input):
        return "My name is Natalie."
    elif re.search(r"\blocation\b", user_input):
        return "I am located in Paris, France."
    elif re.search(r"\boccupation\b", user_input):
        return "I am studying art history at Stanford University."
    elif re.search(r"\bdislikes\b", user_input):
        return "I dislike BTS."
    elif re.search(r"\brelationship\b.*\bstatus\b", user_input):
        return "I am happily single."
    elif re.search(r"\bname\b", user_input):
        return "My name is Natalie."
    elif re.search(r"\bage\b", user_input):
        return "I'm forever young, just like our friendship!"
    else:
        return None

# Define a handler for the "/start" command
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Hi! I'm Natalie. How can I make your day better?")

# Define a handler for all other messages
@bot.message_handler(content_types=["text"])
def handle_message(message):
    user_input = message.text.lower().rstrip('. ') + '.'  # Add a full stop at the end of the input
    user_id = message.from_user.id

    if user_id in chat_history:
        chat = chat_history[user_id]
        chat.append(user_input)
    else:
        chat_history[user_id] = [user_input]

    # Check if the user's input contains any predefined keywords
    predefined_answer = get_predefined_answer(user_input)
    if predefined_answer:
        bot.send_message(message.chat.id, predefined_answer)
        return

    # Show typing indicator
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(1)  # Simulate bot typing delay

    # Generate response based on conversation context
    response = generate_response(prompt, user_input, chat_history[user_id])

    if response:
        response_lines = response.split("\n")
        if len(response_lines) > 2:
            response = "\n".join(response_lines[:2])  # Limit the response to two lines
        bot.send_message(message.chat.id, response)
        chat_history[user_id].append(response)
    else:
        bot.send_message(message.chat.id, "I'm here for you, but it seems like I'm having trouble generating a response right now.")

# Start the bot
bot.polling()
