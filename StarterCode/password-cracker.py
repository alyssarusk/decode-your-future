import time
import itertools
import string

# Get password from user
password = input("Give me a password (letters a-z) to guess: ")

# Start timer 
start_time = time.time()

# Define the characters to use (a-z)
characters = string.ascii_lowercase

# Iterate through every combination, increasing size of password guess until the correct password is reached
found = False
password_length = 1
while not found:
    for guess in itertools.product(characters, repeat=password_length):
        guess = ''.join(guess)
        
        # Check if the current guess matches the actual password
        if guess == password:
            found = True
            break
    password_length += 1  # Increase the password length for the next round

# End timer
end_time = time.time()

# Output password
print(f"Password guessed: {guess}")

# Output time
elapsed_time = end_time - start_time
print(f"Time taken: {elapsed_time:.4f} seconds")