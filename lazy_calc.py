import random
import time

def lazy_thinking_message():
    thoughts = [
        "Thinking...",
        "Still thinking...",
        "Math is hard...",
        "Or is it?",
        "Wait... what was I doing again?",
    ]
    for t in thoughts:
        print(t)
        time.sleep(0.5)

def lazy_add(a, b):
    lazy_thinking_message()
    if random.random() < 0.5:
        print("Okay, I *think* this is the right answer:🤔")
        return a + b
    else:
        print("I'm just guessing at this point:")
        lower = min(a, b)
        upper = max(a, b) + 42
        return random.randint(lower, upper)

def intro():
    print("=" * 34)
    print("  Welcoming you to lazy calculator.. I'm lazy just like youuu🥱")
    print("=" * 34)
    time.sleep(1)

def lazy_calculator():
    intro()
    name = input("What's your name, math adventurer? ")
    print(f"Hi {name}! Let's break some math rules!🚀\n")

    while True:
        try:
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: "))
        except ValueError:
            print("Invalid input! Try entering numbers only.\n")
            continue

        print("\nCrunching the numbers lazily...")
        time.sleep(1)
        result = lazy_add(a, b)
        print(f"\nHere is your very *suspicious* result: {result}\n 😱")

        again = input("Want to try again? (y/n): ").lower()
        if again != 'y':
            print(f"\nBye! {name} Thanks foryour precious time. Now I'm feeling lazy again like you🤐.\n")
            print("Don't tell your math teacher about me!!☠️")
            break

# Run it
lazy_calculator()
