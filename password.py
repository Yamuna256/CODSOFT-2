import random
import string

def generate_password(length, complexity):
    if complexity == "low":
        characters = string.ascii_lowercase + string.digits
    elif complexity == "medium":
        characters = string.ascii_letters + string.digits
    elif complexity == "high":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        raise ValueError("Complexity level should be 'low', 'medium', or 'high'")
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        complexity = input("Enter the complexity level (low, medium, high): ").lower()
        
        if length <= 0:
            print("Please enter a positive integer greater than zero for the length.")
            return
        
        password = generate_password(length, complexity)
        print("Generated password:", password)
    except ValueError:
        print("Invalid input. Please enter a valid integer for length and one of 'low', 'medium', or 'high' for complexity.")
