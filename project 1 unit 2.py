print("********************************************************")
print("Welcome to Binary Oracle 🤓")
print("I am going to read your MIND 🧠")
print("********************************************************")

def get_yes_no(question):
    while True:
        answer = input(question + " (yes/no): ").strip().lower()
        if answer in ["yes", "no"]:
            return answer
        else:
            print("⚠ Please answer only with 'yes' or 'no'.")

while True:
    start = input("Do you want to start? (yes/no): ").strip().lower()
    
    if start == "no":
        print("Okay, maybe next time! 👋")
        break
    elif start != "yes":
        print("⚠ Please type 'yes' or 'no'.")
        continue

    print("\nThink of a number between 1 and 10.")
    print("Answer only with yes or no ⚠.")
    print("--------------------------------------------------")

    low = 1
    high = 10
    questions = 0

    while low < high:
        mid = (low + high) // 2
        questions += 1

        answer = get_yes_no(f"Is your number greater than {mid}?")

        if answer == "yes":
            low = mid + 1
        else:
            high = mid

    print("\n🎉 I found your number! It is", low)
    print(f"It took me {questions} questions to read your mind 😎")

    replay = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if replay != "yes":
        print("Thanks for playing! 👋")
        break
