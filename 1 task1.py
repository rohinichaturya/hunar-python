import random
def generate_captcha():
    # Characters to use in CAPTCHA
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    captcha = ""
    # Generate 5-character CAPTCHA
    for _ in range(5):
        captcha += random.choice(characters)
    return captcha
# Testing the generator
for i in range(5):  # Generate 5 CAPTCHAs for testing
    print(f"CAPTCHA {i+1}: {generate_captcha()}")
