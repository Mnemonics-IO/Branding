def eat_rice():
    print("Welcome to the never-ending rice plate")
    print("You can eat as much as you want, the plate will always be full.\n")
    servings_eaten = 0 
    while True:
        action = input("Press Enter to take a bite of rice (or type 'quit' to stop): ").lower()
        if action == 'quit':
            print("You've had your fill for now! The rice plate awaits your return.\n")
            break
        servings_eaten += 1
        print(f"Mmm, delicious rice! You've eaten {servings_eaten} servings. The plate is still full.\n")

if __name__ == "__main__":
    eat_rice()