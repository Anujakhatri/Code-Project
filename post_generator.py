def generate_response(user_input):
    user_input = user_input.lower()

    # Basic rules
    if "hello" in user_input or "hi" in user_input:
        return "Hi there! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm functioning well! 😊"
    elif "your name" in user_input:
        return "I'm a simple chatbot built with Python!"
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I don't understand that yet. Can you ask something else?"

# Main loop
def chatbot():
    print("🤖 Chatbot: Hello! Type 'bye' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("🤖 Chatbot: Bye! 👋")
            break
        response = generate_response(user_input)
        print(f"🤖 Chatbot: {response}")

if __name__ == "__main__":
    chatbot()
