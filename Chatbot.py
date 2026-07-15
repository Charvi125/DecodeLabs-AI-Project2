print(" Welcome to Rule-Based AI Chatbot")
print("Type 'exit' anytime to end the conversation.\n")

while True:
    user = input("You: ").lower()

    if user == "hello" or user == "hi":
        print("Bot: Hello! Nice to meet you.")

    elif user == "how are you":
        print("Bot: I am fine. Thank you!")

    elif user == "what is your name":
        print("Bot: I am RuleBot.")

    elif user == "what is ai":
        print("Bot: AI stands for Artificial Intelligence.")

    elif user == "who created you":
        print("Bot: I was created using Python.")

    elif user == "what can you do":
        print("Bot: I can answer simple predefined questions.")

    elif user == "bye":
        print("Bot: Goodbye! Have a wonderful day.")
        break

    elif user == "exit":
        print("Bot: Chat ended.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")
