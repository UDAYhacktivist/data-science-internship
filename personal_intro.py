# Week 1: Personal Introduction Program

def main():
    # Welcome banner
    print("========================================")
    print(" Welcome to the Personal Bio Generator! ")
    print("========================================\n")
    
    # 1. Ask at least 3 user questions using input()
    name = input("What is your name? ")
    age = input("How old are you? ")
    hobby = input("What is your favorite hobby? ")
    
    # 2. Display friendly output using formatted strings (f-strings)
    print("\n" + "="*40)
    print(f"🎉 Welcome {name}! 🎉")
    print(f"You are {age} years old and love {hobby}.")
    print("="*40)

if __name__ == "__main__":
    main()