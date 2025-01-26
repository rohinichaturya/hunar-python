import random
import string
import os
def generate_captcha(length=5, use_upper=True, use_lower=True, use_digits=True):
    """
    Generate a CAPTCHA based on user-specified parameters.
    """
    character_pool = ""
    if use_upper:
        character_pool += string.ascii_uppercase
    if use_lower:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    
    if not character_pool:
        raise ValueError("At least one character set must be selected.")  
    return ''.join(random.choice(character_pool) for _ in range(length))

def save_captchas_to_file(captchas, filename="captchas.txt"):
    """
    Save a list of CAPTCHAs to a file.
    """
    with open(filename, "w") as file:
        for captcha in captchas:
            file.write(captcha + "\n")
    print(f"\nCAPTCHAs saved to {filename}")
def load_captchas_from_file(filename="captchas.txt"):
    """
    Load CAPTCHAs from a file if it exists.
    """
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return file.read().splitlines()
    return []
def verify_captcha(captcha):
    """
    Verify the CAPTCHA by asking the user to re-enter it.
    """
    user_input = input(f"Enter the CAPTCHA displayed ({captcha}): ").strip()
    if user_input == captcha:
        print("Verification successful!")
        return True
    else:
        print("Incorrect CAPTCHA. Please try again.")
        return False
def main():
    print("\n=== Welcome to the Advanced CAPTCHA Generator ===")
    # User inputs
    try:
        length = int(input("Enter the CAPTCHA length (default is 5): ") or 5)
        count = int(input("Enter the number of CAPTCHAs to generate (default is 5): ") or 5)
        use_upper = input("Include uppercase letters? (yes/no, default is yes): ").strip().lower() in ['yes', 'y', '']
        use_lower = input("Include lowercase letters? (yes/no, default is yes): ").strip().lower() in ['yes', 'y', '']
        use_digits = input("Include digits? (yes/no, default is yes): ").strip().lower() in ['yes', 'y', '']
        save_option = input("Do you want to save the CAPTCHAs to a file? (yes/no): ").strip().lower()
        verify_option = input("Do you want to verify the CAPTCHAs? (yes/no): ").strip().lower()
    except ValueError:
        print("Invalid input. Please restart and enter valid values.")
        return
    # Generate CAPTCHAs
    captchas = []
    try:
        for _ in range(count):
            captchas.append(generate_captcha(length, use_upper, use_lower, use_digits))
    except ValueError as e:
        print(f"Error: {e}")
        return
    # Display CAPTCHAs
    print("\nGenerated CAPTCHAs:")
    for i, captcha in enumerate(captchas, start=1):
        print(f"CAPTCHA {i}: {captcha}")
    # Save CAPTCHAs to a file
    if save_option in ['yes', 'y']:
        save_captchas_to_file(captchas)
    # Verify CAPTCHAs
    if verify_option in ['yes', 'y']:
        print("\n=== CAPTCHA Verification ===")
        for captcha in captchas:
            while not verify_captcha(captcha):
                pass
    print("\nThank you for using the Advanced CAPTCHA Generator!")
if __name__ == "__main__":
    main()
