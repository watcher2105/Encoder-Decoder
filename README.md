# Encoder-Decoder

## Introduction
This program provides both encoding (encryption) and decoding (decryption) options. The user can choose the number of positions (shift) for the cipher between 0 and 25.

## How It Works
1. **Encoding**: The program shifts each letter in the input message by a specified number of positions to produce an encoded message. Non-alphabetical characters remain unchanged.
2. **Decoding**: The program shifts each letter in the encoded message backward by the same number of positions to recover the original message.
3. **Shift Validation**: The shift value entered by the user is validated to be between 0 and 25.
4. **Menu-Driven**: The user is presented with a menu to either encode, decode, or exit the program.

## Functions

### 1. `encode(m, s)`
   **Purpose**: This function encodes the input message `m` by shifting its letters by `s` positions in the alphabet.

   **Logic**:
   - The function iterates over each character in the message.
   - If the character is an uppercase letter (A-Z), it calculates the new letter by shifting forward by `s` positions. If the shift goes past 'Z', it wraps around to the beginning of the alphabet ('A').
   - If the character is a lowercase letter (a-z), it does the same, wrapping around from 'z' to 'a' if needed.
   - Non-alphabetical characters (such as spaces, punctuation) remain unchanged.

### 2. `decode(m, s)`
   **Purpose**: This function decodes the encoded message `m` by shifting its letters back by `s` positions in the alphabet to retrieve the original message.
   
   **Logic**:
   - Similar to `encode`, this function iterates over each character in the message.
   - If the character is uppercase, it shifts backward by `s` positions. If the shift goes past 'A', it wraps around to 'Z'.
   - For lowercase letters, it shifts backward and wraps around from 'a' to 'z' if needed.
   - Non-alphabetical characters remain unchanged.

### 3. `shift()`
   **Purpose**: This function ensures that the user inputs a valid integer for the shift (between 0 and 25). It keeps prompting the user until a valid value is entered.

   **Logic**:
   - It uses a `while` loop to repeatedly ask for input.
   - The input is stripped of extra spaces and converted to an integer.
   - If the input is a valid integer and falls within the range of 0 to 25, it is returned. Otherwise, it prints an error message and asks for input again.

### 4. Main Program (Menu-Driven)
   **Logic**:
   - The program presents the user with a menu offering three options: encoding a message, decoding a message, or exiting the program.
   - Based on the user's selection:
     - If they choose to encode, they are asked to input a message and a shift value. The encoded message is displayed.
     - If they choose to decode, they are similarly asked for an encoded message and a shift value, and the decoded message is displayed.
     - If they choose to exit, the program ends with a "Thank you" message.
     - If an invalid option is selected, an error message is displayed, and the menu is shown again.


## Program Flow:
1. Display menu.
2. Get user's choice (encode, decode, exit).
3. If encoding or decoding, prompt for the message and shift value.
4. Use the appropriate function (`encode` or `decode`) to process the message.
5. Display the result.
6. Repeat the process unless the user chooses to exit.

## Requirements:
- Python 3.x
