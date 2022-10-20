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

# import re

lives = 3

word = "bonjour"
# use list to manipulate their value by index
word_list = []
user_word_list = []
proposed_characters = ""

for char in word:
    word_list.append(char)
    user_word_list.append('_')


while True:
    print("Vies restantes : {}".format(lives))

    if lives <= 0:
        print("Perdu !")
        break
    elif user_word_list == word_list:
        print("C'est gagné !")
        break

    user_input = input("Quelle lettre proposes-tu ? ")

    # x will be used to send the user character to the corresponding index, if matching with the word character
    x = 0
    nb_matches = 0

    for char in word:
        if user_input == char:
            user_word_list[x] = char
            nb_matches += 1
        x += 1

    if nb_matches == 0:
        lives -= 1

    proposed_characters += user_input + " "

    user_word = ""
    for user_char in user_word_list:
        user_word += user_char + " "

    print("Lettres proposées : {}".format(proposed_characters))
    print(user_word)
    