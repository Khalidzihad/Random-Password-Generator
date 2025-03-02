import random
import string

def generate_password(length=12):
    """
    Generates a random password.

    Args:
        length (int): Length of the password (default: 12).

    Returns:
        str: Randomly generated password.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    return password

def save_password_to_file(password, filename="passwords.txt"):
    """
    Saves a password to a file.

    Args:
        password (str): The password to save.
        filename (str): The file to save the password in (default: passwords.txt).
    """
    with open(filename, "a") as file:
        file.write(password + "\n")

def main():
    print("Random Password Generator")
    while True:
        try:
            length = int(input("Enter the length of the password (default 12): ") or 12)
            if length < 4:
                print("Password length should be at least 4 characters. Try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        password = generate_password(length)
        print(f"Generated Password: {password}")

        save_password_to_file(password)
        print("Password saved to passwords.txt")

        another = input("Do you want to generate another password? (y/n): ").lower()
        if another != 'y':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
