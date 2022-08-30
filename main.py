from morse_codes import morse_codes, alpha_nums
from art import logo

print(logo)

def encrypt(message):
    code = ''
    for letter in message:

        if letter != ' ':                  #if letter is not space
            code += morse_codes[letter] + " "   #add morse code from dictionary plus a space
        else:
            code += "/" + " " #if word completes it will add / plus space as per morse-code rule
    return f'Morse Code of {message} is : {code}\n'


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
            pass  #if it will find '/' it will skip that character
    citext += (list(morse_codes.keys()))[list(morse_codes.values()).index(decode)] #convert last character into morse-code

    return f'Descryption of {message} is : {citext}\n '

is_app = True
while is_app:
    try:
        choice = input("\n--->> Type 'E' to Encrypt,Type D to Decrypt, type 'Q' for Quit :: ")
        if choice == "E" or choice == 'e':
            string_input = input("\n ==> Enter text to Morse-code: ").upper()
            for letter in string_input:
                if letter in alpha_nums:
                    if letter is string_input[-1]:
                        print(encrypt(string_input))
                else:
                    raise ValueError

        elif choice == "D" or choice == 'd':
            morse_input = input("\n==> Enter Morse-code to decrypt: ").upper()

            if morse_input not in alpha_nums:
                print(decrypt(morse_input))
            else:
                raise RuntimeError

        elif choice == 'Q' or choice == 'q':
            is_app = False
            print("Thank you for using App, See you soon :)")

        elif choice != ["D", "E", "Q", 'd', 'e', 'q']:
            print("Please enter from the available options.")

    except ValueError:
        print("Please Enter String letters and Numbers only.")
    except RuntimeError:
        print("Please Enter valid Morse-code with proper spacing")