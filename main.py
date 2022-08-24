from morse_codes import morse_codes

is_app = True


def encrypt(message):
    code = ''
    for letter in message:

        if letter != ' ':                  #if letter is not space
            code += morse_codes[letter] + " "   #add morse code from dictionary plus a space
        else:
            code += "/" + " " #if word completes it will add / plus space as per morse-code rule
    return f'Morse Code is : {code}'


def decrypt(message):
    global sp  #space counter to find out complete word
    decode = ''
    citext = ''

    for code in message:

        if code != ' ' and code != '/':
            sp = 0
            decode += code   #it will store every single character until a space

        elif code == ' ': #if space found
            sp += 1
            if sp == 2:  # executes when two consicutive spaces found(' / ')
                citext += " "  #space between words
            else:
                citext += (list(morse_codes.keys()))[list(morse_codes.values()).index(decode)]  #convert morse-code into one character
                decode = ''  #decode goes to 0 so we can store another character
        else:
            pass
    citext += (list(morse_codes.keys()))[list(morse_codes.values()).index(decode)] #convert last character into morse-code

    return citext

while is_app:
    choice = input("Type 'E' to Encrypt,Type D to Decrypt, type 'Q' for Quit: ").upper()
    if choice == "E":
        string_input = input(" Enter text to Morse-code: ").upper()
        print(encrypt(string_input))

    elif choice == "D":
        morse_input = input("Enter Morse-code to decrypt: ")
        print(decrypt(morse_input))

    elif choice == 'Q':
        is_app = False
        print("Thank you for using App, See you soon :)")

    elif choice != ["D", "E", "Q"]:
        print("Please enter from the available options.")

