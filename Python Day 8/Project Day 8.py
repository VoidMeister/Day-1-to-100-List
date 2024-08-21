alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
run_code = True



def decrypt(original_text, shift_amount):
    # If it's a letter use the for letter, else just append character to list
    for letter in original_text:
        if letter.isalpha():
            decoded_word.append(alphabet[((alphabet.index(letter) - shift_amount) % len(alphabet))])
        else:
            decoded_word.append(letter)

def encrypt(original_text, shift_amount):

    for letter in original_text:
        #append the letter matching the index in alphabet/ of index of letter in original_text + shift_amount
        # #the brackets in alphabet has to be an integer
        if letter.isalpha():
            coded_word.append(alphabet[((alphabet.index(letter)+ shift_amount) % len(alphabet))])
        else:
            coded_word.append(letter)



def caesar(direction_i, text_i, shift_i):
    if direction_i == "encode":
        encrypt(text_i, shift_i)
        print("".join(coded_word))
    else:
        decrypt(text_i,shift_i)
        print("".join(decoded_word))

while run_code:
    coded_word = []
    decoded_word = []
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(direction, text, shift)
    rerun = input(f"Would you like to rerun the code? Type yes or no")
    if rerun == "yes":
        continue
    else:
        run_code = False



