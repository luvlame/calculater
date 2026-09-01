import random
import time
import math

def troll_calculator():
    print("=" * 40)
    print("   WELCOME TO THE CALCULATOR")
    print("   (It definitely works perfectly)")
    print("=" * 40)
    print()
    
    troll_messages = [
        "Calculating... just kidding, I was napping 😴",
        "Error 404: Brain not found 🤖",
        "I'm sorry, I'm too lazy to compute that 🦥",
        "Processing... and processing... and processing... (still processing) ⏳",
        "Answer: Wait, what was the question again? 🤔",
        "Invalid answer. The correct answer is 'potato' 🥔",
        "Your math is so bad, I'm embarrassed for you",
        "Actually, the answer is the number of cookies I ate today 🍪",
        "I would calculate that, but I have better things to do 😎",
        "Congratulations! You've been trolled! 🎉"
    ]
    
    while True:
        try:
            print("\nEnter calculation (or 'quit' to exit):")
            user_input = input(">> ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("Leaving so soon? I'm heartbroken 💔")
                time.sleep(1)
                print("Just kidding! Get trolled! Bye! 👋")
                break
            
            # Random chance to troll with a timer
            if random.random() < 0.3:
                print("Let me think about that for a moment...")
                for i in range(3, 0, -1):
                    print(f"   {i}...")
                    time.sleep(0.5)
                print("   SYKE! That was a waste of time!")
                continue
            
            # Random chance to give a completely wrong answer
            if random.random() < 0.2:
                wrong_answers = [
                    random.randint(-999, 999),
                    "Probably a bird? 🐦",
                    "42 (the answer to everything)",
                    f"{random.randint(1,10)} and a half",
                    "Error: Too much math for my brain",
                    "I see dead pixels 👻"
                ]
                print(f"Answer: {random.choice(wrong_answers)}")
                continue
            
            # Random chance to add extra junk to the calculation
            if random.random() < 0.15 and user_input in ['1+1', '2+2', '3+3']:
                print("OH! That's an EASY one!")
                time.sleep(1)
                print("Wait... let me double-check...")
                time.sleep(1)
                print("...")
                time.sleep(0.5)
                print(f"Answer: {random.choice(['2', '3', '5', '11', 'I don't know'])}")
                continue
            
            # Actually do the math (with a twist sometimes)
            try:
                # Safe eval - only allow math operations
                result = eval(user_input, {"__builtins__": {}}, 
                             {"sin": math.sin, "cos": math.cos, 
                              "sqrt": math.sqrt, "pi": math.pi})
                
                # Add a random troll occasionally even when it works
                if random.random() < 0.15:
                    print(f"I compute: {result}")
                    time.sleep(0.5)
                    print("But my cat says it's: 🐱")
                    time.sleep(0.3)
                    print(f"Cat's answer: {result + random.randint(0,5)}")
                else:
                    # Sometimes just do it right (to keep them off guard)
                    print(f"Answer: {result}")
                    
            except Exception:
                print(f"ERROR: {random.choice(troll_messages)}")
                
        except KeyboardInterrupt:
            print("\n\nOh no! You broke me! (Not really, I'm fine 😎)")
            break
        except Exception:
            print(f"💥 BOOM! {random.choice(troll_messages)}")

# Add some fun ASCII art at the start
print("""
    ╔═══════════════════════════════════════╗
    ║        TROLL CALCULATOR 3000         ║
    ║    (Now with 100% more trolling)     ║
    ╚═══════════════════════════════════════╝
""")

troll_calculator()
