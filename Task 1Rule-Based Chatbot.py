import datetime
import random

print("=" * 50)
print("🤖 Welcome to Rule-Based Chatbot")
print("Type 'help' to see available commands.")
print("Type 'exit' to quit.")
print("=" * 50)

jokes = [
    "Why don't programmers like nature? Because it has too many bugs!",
    "Why did the computer go to the doctor? Because it caught a virus!",
    "Python is my favorite snake!"
]

while True:
    user = input("\nYou: ").lower().strip()

    # Exit
    if user == "exit":
        print("Bot: Goodbye! Have a great day 😊")
        break

    # Greetings
    elif user in ["hi", "hello", "hey"]:
        print("Bot: Hello! How can I help you?")

    # Asking name
    elif "your name" in user:
        print("Bot: My name is RuleBot.")

    # Asking about chatbot
    elif "who are you" in user:
        print("Bot: I am a Rule-Based Chatbot created using Python.")

    # Time
    elif "time" in user:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        print("Bot: Current time is", current_time)

    # Date
    elif "date" in user:
        today = datetime.date.today()
        print("Bot: Today's date is", today)

    # How are you
    elif "how are you" in user:
        print("Bot: I'm doing great! Thanks for asking.")

    # Joke
    elif "joke" in user:
        print("Bot:", random.choice(jokes))

    # Calculator
    elif user.startswith("calculate"):
        try:
            expression = user.replace("calculate", "").strip()
            result = eval(expression)
            print("Bot: Answer =", result)
        except:
            print("Bot: Invalid expression!")

    # Help
    elif user == "help":
        print("\nAvailable Commands:")
        print("• hi")
        print("• hello")
        print("• your name")
        print("• who are you")
        print("• how are you")
        print("• time")
        print("• date")
        print("• joke")
        print("• calculate 10+20")
        print("• exit")

    # Default response
    else:
        print("Bot: Sorry, I didn't understand that.")
        print("Bot: Type 'help' to see available commands.")