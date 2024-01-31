import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("PASSWORD GENERATOR")
    print("-------------------")

    # User Input
    try:
        length = int(input("Enter the desired length of the password: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    # Generate Password
    password = generate_password(length)

    # Display the Password
    print("\nGenerated Password: ")
    print(password)

if __name__ == "__main__":
    main()
