import random
import string
def generate_captcha(length=5):
    """
    Function to generate a CAPTCHA of a given length.
    Default length is 5 characters.
    """
    characters = string.ascii_letters + string.digits  # A-Z, a-z, 0-9
    captcha = ''.join(random.choice(characters) for _ in range(length))
    return captcha
def test_captcha_generator(count=5, length=5):
    """
    Test the CAPTCHA generator by generating multiple CAPTCHAs.
    Logs each CAPTCHA to a list.
    """
    captchas = []
    for i in range(count):
        captcha = generate_captcha(length)
        captchas.append(captcha)
        print(f"CAPTCHA {i + 1}: {captcha}")
    return captchas
def save_captchas_to_file(captchas, filename="captchas.txt"):
    """
    Save a list of CAPTCHAs to a text file.
    """
    with open(filename, "w") as file:
        for captcha in captchas:
            file.write(captcha + "\n")
    print(f"CAPTCHAs saved to {filename}")
def main():
    print("Welcome to the Enhanced CAPTCHA Generator!")
    # User inputs
    try:
        length = int(input("Enter the desired CAPTCHA length (default is 5): ") or 5)
        count = int(input("Enter the number of CAPTCHAs to generate (default is 5): ") or 5)
        save_option = input("Do you want to save the CAPTCHAs to a file? (yes/no): ").strip().lower()
    except ValueError:
        print("Invalid input. Please enter valid numbers for length and count.")
        return
    # Generate and test CAPTCHAs
    captchas = test_captcha_generator(count, length)
    # Save CAPTCHAs if needed
    if save_option in ['yes', 'y']:
        save_captchas_to_file(captchas)
if __name__ == "__main__":
    main()
