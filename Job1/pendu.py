# Écrivez un programme pendu.py, qui permet à l’utilisateur de faire une partie du célèbre
# jeu le pendu dans le terminal.
# Le programme devra dans un premier temps demander au joueur le niveau avec lequel il
# souhaite jouer. Il aura un nombre de vies en fonction du niveau choisi (exemple
# débutant 10, intermédiaire 7, expert 4). Vous êtes libres de choisir le nombre de vies par
# niveau.
# Le programme devra donc choisir aléatoirement un mot dans le dictionnaire disponible
# ici, et afficher :
# - Le nombre de vies restantes au joueur
# - Les lettres déjà proposées par le joueur (dans le mode débutant et intermédiaire.
# En expert, la liste n’apparaîtra pas)
# - Des “_” pour remplacer les lettres non trouvées
# - Les lettres proposées qui se trouvent dans le mot
# La partie prend fin lorsque le joueur a trouvé le mot, ou qu’il n’a plus de vie.

import random


def myUpperASCII(myString:str):
    string_list = list(myString)
    to_up_ascii = {
        "a" : "A",
        "b" : "B",
        "c" : "C",
        "d" : "D",
        "e" : "E",
        "f" : "F",
        "g" : "G",
        "h" : "H",
        "i" : "I",
        "j" : "J",
        "k" : "K",
        "l" : "L",
        "m" : "M",
        "n" : "N",
        "o" : "O",
        "p" : "P",
        "q" : "Q",
        "r" : "R",
        "s" : "S",
        "t" : "T",
        "u" : "U",
        "v" : "V",
        "w" : "W",
        "x" : "X",
        "y" : "Y",
        "z" : "Z",
        "à" : "A",
        "â" : "A",
        "é" : "E",
        "è" : "E",
        "ê" : "E",
        "ë" : "E",
        "î" : "I",
        "ï" : "I",
        "ô" : "O",
        "ö" : "O",
        "ù" : "U",
        "û" : "U",
        "ü" : "U",        
        "À" : "A",
        "Â" : "A",
        "É" : "E",
        "È" : "E",
        "Ê" : "E",
        "Ë" : "E",
        "î" : "I",
        "Ï" : "I",
        "ô" : "O",
        "Ö" : "O",
        "Ù" : "U",
        "û" : "U",
        "Ü" : "U",
    }

    # x used for string_list handling by index
    x = 0
    for char in string_list:
        # if char is in the keys of to_up_ascii, replace the current character by the value of the key of the dictionnary
        if char in to_up_ascii:
            string_list[x] = to_up_ascii[char]
        x += 1
            
    upper_string = ""
    for char in string_list:
        upper_string += char

    return upper_string


with open("dico_france.txt") as data:
    dictionary = data.readlines()
# print(dictionary)

word = myUpperASCII(random.choice(dictionary))
# print(word)

# remove last character from word which is a line break \n
word = word[:-1]

# use lists to manipulate their value by index
word_list = []
user_word_list = []

proposed_characters = ""

for char in word:
    word_list.append(char)
    user_word_list.append('_')

lives = 2

difficulty = input("Bonjour, à quel niveau souhaites-tu jouer ? (Débutant, Intermédiaire, Expert) ")

match difficulty:
    case "Débutant":
        lives = 10
    case "Intermédiaire":
        lives = 7
    case "Expert":
        lives = 4

while True:
    print("Vies restantes : {}".format(lives))

    # game over conditions
    if lives <= 0:
        print("Perdu !")
        break
    elif user_word_list == word_list:
        print("C'est gagné !")
        break

    # print(word_list)
    user_input = myUpperASCII(input("Quelle lettre proposes-tu ? "))

    # x will be used to send the user character to the corresponding index, if matching with the word character
    x = 0
    # nb_matches will be used to handle lives variable
    nb_matches = 0

    # add the corresponding character to the list if user guess is correct
    for char in word:
        if user_input == char:
            user_word_list[x] = char
            nb_matches += 1
        x += 1

    if nb_matches == 0:
        lives -= 1

    proposed_characters += user_input + " "

    # add the variable to display the user_word with values found by user
    user_word = ""
    for user_char in user_word_list:
        user_word += user_char + " "

    if difficulty != "Expert":
        print("Lettres proposées : {}".format(proposed_characters))
    
    print(user_word)
    