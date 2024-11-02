# Importing the logo from art.pyfrom art import logo
from art import logo
print(logo)

# List of alphabet characters to be used for shifting in the Caesar Cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Function to encode or decode the message
def caesar(original_text, shift_amount, encode_or_decode):
    output_text = "" 

    # Reverse the shift for decoding
    if encode_or_decode == "decode":
                shift_amount *= -1

    for letter in original_text:
        # Keep non-alphabet characters unchanged
        if letter not in alphabet:
            output_text += letter
        else:
            # Calculate the shifted position
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)  # Wrap around the alphabet
            output_text += alphabet[shifted_position]
        
    print(f"Here is the {encode_or_decode}d result: {output_text}")

# Main loop to run the program
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    # Ask if the user wants to run the program again
    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("GoodBye")
