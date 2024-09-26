import random
import string

def generate_password(length: int = 10):
    alpha = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(alpha) for i in range(length))
    return password

password = generate_password()
print(f"Generated Password: {password}")


