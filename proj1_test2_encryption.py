#!/usr/bin/python3
# GeekTechStuff

import random

""" 
To find out more about the Vigenère Cipher please visit: https://geektechstuff.com/2019/12/25/vigenere-cipher/
"""


def vigenere_enc():
    alphabet = " abcdefghijklmnopqrstuvwxyz"
    input_string = ""
    enc_key = ""
    enc_string = ""

    # Takes encrpytion key from user
    enc_key = input("Please enter encryption key: ")
    enc_key = enc_key.lower()

    # Takes string from user
    input_string = input("Please enter a string of text: ")
    input_string = input_string.lower()

    # Lengths of input_string
    string_length = len(input_string)

    # Expands the encryption key to make it longer than the inputted string
    expanded_key = enc_key
    expanded_key_length = len(expanded_key)

    while expanded_key_length < string_length:
        # Adds another repetition of the encryption key
        expanded_key = expanded_key + enc_key
        expanded_key_length = len(expanded_key)

    key_position = 0
    input_string_position = 0

    # random number counter
    num_rand_character = 0

    #    for letter in input_string:
    while input_string_position < string_length:
        letter = input_string[input_string_position]
        if letter in alphabet:
            # cycles through each letter to find it's numeric position in the alphabet
            position = alphabet.find(letter)
            # scheduling algorithm j (random)
            i = input_string_position
            t = len(enc_key)
            L = len(input_string)
            j = (L * i) % t
            # get the corresponding shift or random character
            if j > 0 and j < t:
                # print ("j = ",j, "between 1 and t")
                key_character = enc_key[j]
                # print ("Key Character is :", key_character)
                key_character_position = alphabet.find(key_character)
                new_position = position + key_character_position
                if new_position > 26:
                    new_position = new_position - 27
                new_character = alphabet[new_position]
                # print ("Current position: ", position, " .Shifting ", key_character_position, " to right. New position: ",new_position)
                # print ("letter: ", letter, " new character: ", new_character)
                print(
                    "j =",
                    j,
                    "between 1 and t, Key Character is :",
                    key_character,
                    ".Current position:",
                    position,
                    ".Shifting",
                    key_character_position,
                    "to right. New position:",
                    new_position,
                )
                print("letter:", letter, " new character:", new_character)
            # if j < 1 or > t, insert a random character, and push the rest of the string 1 slot backward
            else:
                print("j =", j, ", so random character will be inserted")
                new_character = alphabet[random.randint(0, 26)]
                num_rand_character = num_rand_character + 1
                string_length = string_length + 1
                print("Random Character is :", new_character)
                print("Number of random characters is :", num_rand_character)
                input_string = input_string[:i] + new_character + input_string[i:]
            # moves along key and finds the characters value
            # key_character = expanded_key[key_position]
            # key_character_position = alphabet.find(key_character)
            # key_position = key_position + 1
            # changes the original of the input string character
            enc_string = enc_string + new_character
        else:
            enc_string = enc_string + letter
        input_string_position = input_string_position + 1
    print("Total Number of Random Characters: ", num_rand_character)
    return enc_string


def vigenere_dec():
    alphabet = " abcdefghijklmnopqrstuvwxyz"
    input_string = ""
    dec_key = ""
    dec_string = ""

    # Takes encrpytion key from user
    dec_key = input("Please enter encryption key: ")
    dec_key = dec_key.lower()

    # Takes string from user
    input_string = input("Please enter a string of ciphertext: ")
    input_string = input_string.lower()

    # Lengths of input_string
    string_length = len(input_string)

    # Expands the encryption key to make it longer than the inputted string
    expanded_key = dec_key
    expanded_key_length = len(expanded_key)

    while expanded_key_length < string_length:
        # Adds another repetition of the encryption key
        expanded_key = expanded_key + dec_key
        expanded_key_length = len(expanded_key)

    key_position = 0

    for letter in input_string:
        if letter in alphabet:
            # cycles through each letter to find it's numeric position in the alphabet
            position = alphabet.find(letter)
            # moves along key and finds the characters value
            key_character = expanded_key[key_position]
            key_character_position = alphabet.find(key_character)
            key_position = key_position + 1
            # changes the original of the input string character
            new_position = position - key_character_position
            if new_position < 0:
                new_position = new_position + 27
            new_character = alphabet[new_position]
            dec_string = dec_string + new_character
            print(
                "Current position: ",
                position,
                " .Shifting ",
                key_character_position,
                " to left. New position: ",
                new_position,
            )
            print("letter: ", letter, " new character: ", new_character)
        else:
            dec_string = dec_string + letter
    return dec_string


# Testing
print("Ciphertext: ", vigenere_enc())
# print("Original message: ", vigenere_dec())
