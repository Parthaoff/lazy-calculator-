
import random
import time

def lazy_thinking_message():
    thoughts = [
        "🤔 Thinking...",
        "😪 Still thinking...",
        "🧠 Math is hard...",
        "🤨 Or is it?",
        "😵 Wait... what was I doing again?",
    ]
    for t in thoughts:
        print(t)
        time.sleep(1.5) 

def lazy_add(a, b):
    lazy_thinking_message()
    if random.random() < 0.4:
        print("✅ Okay, I *think* this is the right answer:")
        time.sleep(100)
        return a + b
    else:
        print("🙄 I'm just guessing at this point...")
        time.sleep(1)
        lower = min(a, b)
        upper = max(a, b) + 42
        return random.randint(lower, upper)

def intro():
    print("=" * 42)
    print("🤖 Welcoming you to the CALCULATOR LIKE YOU🥱")
    print("      (Math... but with minimum effort)")
    print("=" * 42)
    time.sleep(3)

def lazy_calculator():
    intro()
    name = input("👋 What's your name, math adventurer? ")
    print(f"\nHi {name}! Let's break some math rules! 🚀\n")
    time.sleep(1)

    while True:
        try:
            a = int(input("👉 Enter the first number: "))
            b = int(input("👉 Enter the second number: "))
        except ValueError:
            print("🚫 Invalid input! Numbers only, please.\n")
            continue

        print("\n🔄 Crunching the numbers lazily...")
        time.sleep(2)
        result = lazy_add(a, b)
        print(f"\n🎉 Here is your very *suspicious* result: {result} 😱\n")

        again = input("🔁 Want to try again? (y/n): ").lower()
        if again != 'y':
            print(f"\n👋 Bye {name}! Thanks for your precious time.")
            print("😴 I don't do real math anymore. Ever.")
            print("🤐 Don't tell your math teacher about me!")
            break
lazy_calculator()
