def chatbot():
    print("Chatbot is running! Type 'bye' to exit.")
    
    responses = {
        "hello": "Hi!",
        "how are you": "I'm fine, thanks!",
        "bye": "Goodbye!"
    }
    
    while True:
        user_input = input("You: ").strip().lower()
        
        if user_input in responses:
            print(f"Bot: {responses[user_input]}")
            if user_input == "bye":
                break
        else:
            print("Bot: I don't understand that. Try: hello, how are you, bye")

chatbot()