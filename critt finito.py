from pycipher import Vigenere, SimpleSubstitution
from time import sleep

print("Cosa vuoi fare?", "\n 1) Criptare", "\n 2) Decriptare")
scel1 = input("Scegli un'opzione: ")
while True:
    if scel1 == "1":
        print("Cosa vuoi criptare?", "\n 1) Cifrario a sostituzione monoalfabetica", "\n 2) Cifrario di Vigenère")
        scel2 = input("Scegli un'opzione: ")
        while True:
            if scel2 == "1":
                key = input("Inserisci la chiave crittografica: ")
                while True:
                    sure = input("Sei sicuro di aver scritto correttamente? (y/n)")
                    if sure == "y":
                        break
                    elif sure == "n":
                        key = input("Inserisci la chiave crittografica: ")
                    else:
                        continue
                phrase = input("Inserisci la frase da cifrare: ")
                while True:
                    sure = input("Sei sicuro di aver scritto correttamente? (y/n)")
                    if sure == "y":
                        break
                    elif sure == "n":
                        phrase = input("Inserisci la frase da cifrare: ")
                    else:
                        continue
                ss = SimpleSubstitution(key)
                print("La frase criptata è " + ss.encipher(phrase))
                sleep(10)
                exit()
            if scel2 == "2":
                key = input("Inserisci la chiave crittografica: ")
                while True:
                    sure = input("Sei sicuro di aver scritto correttamente? (y/n)")
                    if sure == "y":
                        break
                    elif sure == "n":
                        key = input("Inserisci la chiave crittografica: ")
                    else:
                        continue
                phrase = input("Inserisci la frase da cifrare: ")
                while True:
                    sure = input("Sei sicuro di aver scritto correttamente? (y/n)")
                    if sure == "y":
                        break
                    elif sure == "n":
                        phrase = input("Inserisci la frase da cifrare: ")
                    else:
                        continue
                print("La frase criptata è " + Vigenere(key).encipher(phrase))
                sleep(10)
                exit()
    elif scel1 == "2":
        print("Cosa vuoi decriptare?", "\n 1) Cifrario a sostituzione monoalfabetica", "\n 2) Cifrario di Vigenère")
        scel2 = input("Scegli un'opzione: ")
        while True:
            if scel2 == "1":
                key = input("Inserisci la chiave crittografica: ")
                while True:
                    sure = input("Sei sicuro di aver scritto correttamente? (y/n)")
                    if sure == "y":
                        break
                    elif sure == "n":
                        key = input("Inserisci la chiave crittografica: ")
                    else:
                        continue
                phrase = input("Inserisci la frase da decifrare: ")
                while True:
                    sure = input("Sei sicuro di aver scritto correttamente? (y/n)")
                    if sure == "y":
                        break
                    elif sure == "n":
                        continue
                    else:
                        continue
                ss = SimpleSubstitution(key)
                print("La frase decriptata è " + ss.decipher(phrase))
                sleep(10)
                exit()
            if scel2 == "2":
                key = input("Inserisci la chiave crittografica: ")
                while True:
                    sure = input("Sei sicuro di aver scritto correttamente? (y/n)")
                    if sure == "y":
                        break
                    elif sure == "n":
                        key = input("Inserisci la chiave crittografica: ")
                    else:
                        continue
                phrase = input("Inserisci la frase da decifrare: ")
                while True:
                    sure = input("Sei sicuro di aver scritto correttamente? (y/n)")
                    if sure == "y":
                        break
                    elif sure == "n":
                        phrase = input("Inserisci la frase da decifrare: ")
                    else:
                        continue
                print("La frase decriptata è " + Vigenere(key).decipher(phrase))
                sleep(10)
                exit()
    else:
        continue
