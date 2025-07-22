#Password Strength checker using Python 
#Evaluates password strength by checking for essential security criteria, including length, uppercase and lowercase letters, digits, and special characters. 
#It provides information on missing elements and continuously prompts the user until a "Very Strong" password is created.

import re

def check_password_strength(password):
    strength = 0
    missing_criteria = []
    
    criteria = [
        (r"[a-z]", "Lowercase letter"),
        (r"[A-Z]", "Uppercase letter"),
        (r"\d", "Digit"),
        (r"[@$!%*?&#]", "Special character")
    ]
    
    for pattern, desc in criteria:
        if re.search(pattern, password):
            strength += 1
        else:
            missing_criteria.append(desc)
    
    if len(password) >= 8:
        strength += 1
    else:
        missing_criteria.append("Minimum 8 characters")
    
    if strength == 5:
        return "Very Strong"
    return f"{['Very Weak', 'Weak', 'Moderate', 'Strong'][strength-1]} \nTry adding: " + ", ".join(missing_criteria)

if __name__ == "__main__":
    while True:
        password = input("Enter your password: ")
        strength = check_password_strength(password)
        print(f"Password Strength: {strength}")
        if strength == "Very Strong":
            break
