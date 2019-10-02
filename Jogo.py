# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>> Jogo da Forca <<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

    # Método Construtor
    def __init__(self, word):
        self.word = word
        self.list_wrong = []
        self.list_right = []

    # Método para adivinhar a letra
    def guess(self, letter):
        if letter in self.word and letter not in self.list_right:
            self.list_right.append(letter)
        elif letter not in self.word and letter not in self.list_wrong:
            self.list_wrong.append(letter)
        else:
            return False
        return True

    # Método para verificar se o jogo terminou
    def hangman_over(self):
        return self.hangman_won() or (len(self.list_wrong) == 6)

    # Método para verificar se o jogador venceu
    def hangman_won(self):
        if "_ " not in self.hide_word():
            return True
        return False

    # Método para não mostrar a letra no board
    def hide_word(self):
        a = ""
        for letter in self.word:
            if letter not in self.list_right:
                a += "_ "
            else:
                a += letter
        return a

    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):

        print(board[len(self.list_wrong)])
        print("\nPalavra:", self.hide_word())
        print("\nLetras Erradas:", self.list_wrong)
        print("\nLetras Certas:", self.list_right, "\n")

        # print(board[num], "\nPalavra: ",word,"\nLetras Erradas:",wrong,"\nLetras Certas:",right

# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
        with open("palavras.txt", "rt") as file:
                word = file.readlines()
        return word[random.randint(0, len(word))].strip()


# Função Main - Execução do Programa
def main():
    # Objeto
    game = Hangman(rand_word())

    # Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
    while not game.hangman_over():
        game.print_game_status()
        let = input("\nDigite a letra:")
        game.guess(let)

    # Verifica o status do jogo
    game.print_game_status()

    # De acordo com o status, imprime mensagem na tela para o usuário
    if game.hangman_won():
        print('\nParabéns! Venceste!!')
    else:
        print('\nGame over! Perdeste.')
        print('A palavra era ' + game.word)

    print('\nFoi bom jogar contigo! Agora vai estudar!\n')

# Executa o programa		
if __name__ == "__main__":
    main()
