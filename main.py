from morse_codes import morse_codes


def encrypt(message):
    code = ''
    for letter in message:

        if letter != ' ':
            code += morse_codes[letter] + " "
        else:
            code += "/" + " "
    return f'Morse Code is : {code}'


def decrypt(message):
    global sp
    decode = ''
    citext = ''

    for code in message:

        if code != ' ' and code != '/':
            sp = 0
            decode += code

        elif code == ' ':
            sp += 1
            if sp == 2:
                citext += " "
            else:
                citext += (list(morse_codes.keys()))[list(morse_codes.values()).index(decode)]
                decode = ''
        else:
            pass
    citext += (list(morse_codes.keys()))[list(morse_codes.values()).index(decode)]
    return citext







is_app = True
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

