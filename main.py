from morse_codes import morse_codes

code = ''
is_app = True

while is_app:
    choice = input("Type '1' to Start Program, type 'Q' for Quit: ").upper()
    if choice == "1":
        user_input = input(" Enter text to Morse-code: ").upper()

        for letter in user_input:
            if code == '':
               code = morse_codes[letter]
            elif letter == " ":
                code += " " + "/" + " "
            elif letter not in morse_codes:     #if letter is not Numberic or Alphabatic, It will print '#'
                code += " " + "#"
            else:
                code += " " + morse_codes[letter]
        print(f'Morse Code : {code}')

    elif choice == 'Q':
        is_app = False
        print("Thank you for using App, See you soon :)")

    else:
        choice = input("Type '1' to Start Program, type 'Q' for Quit: ").upper()

