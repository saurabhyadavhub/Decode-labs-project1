"""
DecodeLabs Project 1: Rule-Based AI Chatbot
A beginner-friendly command-line chatbot using explicit if/elif/else rules.
Run with: python chatbot.py
"""

def get_response(user_input: str) -> str:
    """Return a response for a predefined input, using rule-based logic."""
    message = user_input.strip().lower()

    if not message:
        return "I didn't catch that. Please type something."
    elif message in {"hi", "hello", "hey", "hii", "good morning", "good afternoon", "good evening"}:
        return "Hello! I'm your DecodeLabs rule-based chatbot. How can I help you?"
    elif message in {"how are you", "how are you?", "how are you doing"}:
        return "I'm doing well, thanks for asking! How can I assist you?"
    elif message in {"what is your name", "what's your name", "who are you"}:
        return "I'm D-Code, a simple chatbot created for DecodeLabs Project 1."
    elif message in {"what can you do", "help", "help me"}:
        return ("I can respond to greetings, tell you my name, answer a few simple "
                "questions, and end our conversation. Try asking about AI or Python.")
    elif "artificial intelligence" in message or message == "what is ai":
        return ("Artificial intelligence (AI) is the field of creating computer "
                "systems that perform tasks associated with human intelligence.")
    elif "python" in message:
        return "Python is a beginner-friendly programming language often used in AI."
    elif message in {"thank you", "thanks", "thank you!", "thanks!"}:
        return "You're welcome! Happy to help."
    elif message in {"bye", "goodbye", "exit", "quit", "stop"}:
        return "Goodbye! Thanks for chatting. Have a great day!"
    else:
        return "I'm not sure how to respond to that yet. Try typing 'help' or ask a supported question."


def main() -> None:
    """Run the chatbot continuously until the user enters an exit command."""
    print("=" * 58)
    print("D-CODE: DECODELABS RULE-BASED AI CHATBOT")
    print("Type 'help' to see what I can do, or 'bye' to exit.")
    print("=" * 58)

    while True:
        try:
            user_input = input("You: ")
        except (EOFError, KeyboardInterrupt):
            print("\nBot: Goodbye! Thanks for chatting.")
            break

        response = get_response(user_input)
        print(f"Bot: {response}")

        if user_input.strip().lower() in {"bye", "goodbye", "exit", "quit", "stop"}:
            break


if __name__ == "__main__":
    main()
