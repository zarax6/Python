import random, time, os

class Hangman:
    def __init__(self, words_param):
        self.words = words_param
        self.attempts = 12
        self.selected_word = random.choice(self.words)
        self.guessed_string = "_" * len(self.selected_word)

    def mainloop(self):
        is_running = True

        while is_running == True:
            while self.attempts != 0:
                print("Осталось попыток: ", self.attempts)
                print(self.guessed_string)
                letter = input("Введите букву: ")

                if self.selected_word.count(letter):
                    for ch in range(len(self.selected_word)):
                        self.guessed_string += letter

                        self.guessed_string += "_"
                    
                pass

    def test(self):
        os.system("cls")
        print(self.words)
        print(self.attempts)
        print(self.selected_word)
        print(self.guessed_string)


word_list = ["Glasses", "River", "Skyscraper"]
s = Hangman(word_list)
s.test()