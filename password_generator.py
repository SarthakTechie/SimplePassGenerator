import random
import string

def generate_password(length=24):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print("🔐 Your new secure password is:")
    print(generate_password())
