import time
import random

print("brute force attack simulator")

common_passwords = ["absdfiashdui", "ajhsdbfiaush", "aebf23478ry293rhfi" , "asfaiyr73e278yw387", "password123", "admin", "letmein", "qwerty", "12345678"]

target_password = "nipellampuklamodda"

attempts = 0
found= False

for guess in common_passwords:
    print(f"Attempting password: {guess}")
    time.sleep(1)  # Simulate time taken for each attempt
    attempts += 1
    
    if guess == target_password:
        found = True
        print(f"✅ Password found: {guess} in {attempts} attempts!")
        break


if not found:
    print("❌ Password not found in the list of common passwords.lets start random guessing...")


    for i in range(15):

        attempts += 1
        random_guess=" "
        length = random.randint(8, 16)

        for j in range(length):
            char = random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()")
            random_guess += char
            time.sleep(0.4)

    if random_guess == target_password:
        print(f"✅ Password found: {random_guess} in {attempts} attempts!")

    else:
        print(f"❌ Password not found after {attempts} attempts. Keep trying!")










