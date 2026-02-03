# MR 1st Morse Code Translator

# One tuple for the letters in English
alphabet = ("A","B","C","D","E","F","G","H","I","J","K","L","M",
            "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," ")

# One tuple for the Morse code letters
morse_code = (".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
              "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",
              "..-","...-",".--","-..-","-.--","--..","/")

# 3 functions
# function for translating Enlgish to Morse code
# Another function translating morse code into english
# Main loop that is a function that lets users choose what to do
# Morse code to English or exit
# be able to check for invalid inputs


# function: translate English text to morse code
def english_to_morse(text):

    # change to upper so it match tuple
    text = text.upper()

    result = ""

    # go letter by letter
    for ch in text:

        if ch in alphabet:
            index = alphabet.index(ch)
            result = result + morse_code[index] + " "
        else:
            # this char dont exist in morse list
            print("Skipping bad character:", ch)

    return result.strip()


# function: translate morse code to English
def morse_to_english(code):

    result = ""

    # split symbols by space
    parts = code.split(" ")

    for symbol in parts:

        if symbol in morse_code:
            index = morse_code.index(symbol)
            result = result + alphabet[index]
        else:
            # user maybe typed it wrong here
            print("Not valid morse part:", symbol)

    return result.lower()


# function that shows intro and menu and gets choice
def show_menu():

    # intro so user know what program does
    print("\nWelcome to the Morse Code Translator")
    print("This program translate English and Morse Code")
    print("Pick one option below\n")

    print("MAIN MENU:")
    print("1. Translate from Morse Code to English")
    print("2. Translate from English to Morse Code")
    print("3. Exit")

    choice = input("\nEnter choice (1-3): ")
    return choice


# main function runs the loop and controls program
def main():

    running = True

    # program loop keep going until exit
    while running == True:

        choice = show_menu()

        if choice == "1":
            print("\nMORSE CODE TO ENGLISH:")
            code = input("What is the code you need translated:\n")

            answer = morse_to_english(code)

            print("\nYour message says:")
            print(answer)

        elif choice == "2":
            print("\nENGLISH TO MORSE CODE:")
            text = input("What is the message you need translated:\n")

            answer = english_to_morse(text)

            print("\nYour message says:")
            print(answer)

        elif choice == "3":
            print("Program now stopping, bye")
            running = False

        else:
            print("That choice not right, try again")


# start the program
main()
