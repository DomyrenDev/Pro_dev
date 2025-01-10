import time
import sys
from pygame import mixer
import random
import numpy as np

#Riproduci la canzone background
mixer.init()
mixer.music.load('Ost/Ninja Toad.mp3')
mixer.music.play()

#Delayprint
def delay_print(s):
    for c in s:
        sys.stout.write(c)
        sys.stoud.flush()
        time.sleep(0.025)

#La Classe
class Pokemon:
    def __init__(self, nome, tipo, mosse, stats, salute= "=============================="):
        self.nome = nome
        self.tipo = tipo
        self.mosse = mosse
        self.mosses = mosse
        self.attacco = stats["ATTACCO"]
        self.difesa = stats["DIFESA"]
        self.salute = salute
        self.barre = 30

    def fight(self,avversario):
        #scriviamo le info della lotta
        delay_print(f"\n----------COMINCIA LA LOTTA ----------")
        print(f"{self.nome} ")
        print(f"TIPO: {self.tipo}")
        print("ATTACCO: " + str(self.attacco))
        print("DIFESA: " + str(self.difesa))
        print("LIVELLO: " + str(self.livello))
        time.sleep(.5)
        delay_print(f"\nVS")
        print(f"\n{avversario.nome} ")
        print(f"TIPO: {avversario.tipo}")
        print("ATTACCO: " + str(avversario.attacco))
        print("DIFESA: " + str(avversario.difesa))
        print("LIVELLO: " + str(avversario.livello))
        time.sleep(2)
        #Vantaggi di tipo
        lista_tipi = ["Fuoco", "Acqua", "Elettro", "Erba", "Ghiaccio", "Lotta", "Veleno", "Psico", "Roccia", "Buio", "Drago", "Acciaio", "Folletto"]
        for i, k in enumerate(lista_tipi):
            if self.tipo == k:
                #sono entrambi dello stesso tipo
                if avversario.tipo == k:
                    stringa_1_attacco = "\n Non è molto efficace...\n\n"
                    stringa_2_attacco = "\n Non è molto efficace...\n\n"
                #l'avversario ha vantaggio di tipo
                if avversario.tipo == lista_tipi[(i+1)%3]:
                    avversario.attacco *= 2
                    avversario.difesa *= 2
                    self.attacco /= 2
                    self.difesa /= 2
                    stringa_1_attacco = "\n Non è molto efficace...\n\n"
                    stringa_2_attacco = "\n E' super efficace!\n\n"
                #l'avversario ha svantaggio di tipo
                if avversario.tipo == lista_tipi[(i+2)%3]:
                    self.attacco *= 2
                    self.difesa *= 2
                    avversario.attacco /= 2
                    avversario.difesa /= 2
                    stringa_1_attacco = "\n E' super efficace!\n\n"
                    stringa_2_attacco = "\n Non è molto efficace...\n\n"
        #proseguire la lotta finchè uno dei due non è esausto
        while (self.barre > 0) and (avversario.barre > 0):
            print(f"{self.nome} \t\tPS\t {self.salute} ")
            print(f"{avversario.nome} \t\tPS\t {avversario.salute} ")
            #comincia la lotta
            delay_print (f"Vai, {self.nome}!\n\n")
            for i,x in enumerate(self.mosse):
                print(f"[{i+1}] " +x+"")
            delay_print(f"\nChe mossa deve usare {self.nome}? ")
            index = int(input("[?]: "))
            delay_print(f"\n{self.nome} usa {self.mosse[index-1]}!")
            time.sleep(1)
            delay_print(stringa_1_attacco)
        
            #Determina il danno
            brutto_colpo = np.random.randint(0, 12)
            if brutto_colpo == 1:
                self.attacco += 4
                avversario.barre -= self.attacco 
                avversario.salute = ""
                self.attacco -= 4
                delay_print(f"\nBrutto colpo!\n\n")
            else:
                avversario.barre -= self.attacco
                avversario.salute = ""
            for j in range(int(avversario.barre+.1*avversario.difesa)):
                avversario.salute += "="
        
            time.sleep(1)
            print(f"{self.nome} \t\tPS\t {self.salute} ")
            print(f"{avversario.nome} \t\tPS\t {avversario.salute} ")
            
            #controllare se l'avversario è esausto 
            if avversario.barre <= 0:
                delay_print(f"\n{avversario.nome} nemico è esausto!\n")
                break
                soldi = np.random.choice(5000)
                delay_print(f"\n\n Ti ha pagato $ {soldi} \n")
            
            #controlla se è il turno dell'avversario
            delay_print(f"\n {avversario.nome} ti sta attaccando")
            time.sleep(.5)
            index = np.random.choice(4)
            delay_print(f"\n {avversario.nome} nemico usa {avversario.mosse[index-1]}!\n")
            time.sleep(1)
            delay_print(stringa_2_attacco)

              #Determina il danno
            brutto_colpo = np.random.randint(0, 12)
            if brutto_colpo == 1:
                avversario.attacco += 4
                self.barre -= avversario.attacco 
                self.salute = ""
                avversario.attacco -= 4
                delay_print(f"\nBrutto colpo!\n\n")
            else:
                self.barre -= avversario.attacco
                self.salute = ""
            for j in range(int(self.barre+.1*avversario.difesa)):
                self.salute += "="
        
            time.sleep(1)
            print(f"{avversario.nome} \t\tPS\t {avversario.salute} ")
            print(f"{self.nome} \t\tPS\t {self.salute} ")
            
            #controllare se il tuo pokemon è esausto 
            if self.barre <= 0:
                delay_print(f"\n{self.nome} è esausto!\n")
                break
                soldi = np.random.choice(5000)
                delay_print(f"\n\nHai pagato $ {soldi} \n")
if __name__ == "_main_":
    #creare due pokemon
    Charizard = Pokemon("Charizard", "Fuoco", ["Lanciafiamme", "Aerofuria", "Artigliofuoco", "Dragospiro"], {"ATTACCO": 84, "DIFESA": 78}, np.random.choise(100))
    Blastoise = Pokemon("Blastoise", "Acqua", ["Idropompa", "Pugnoscarica", "Idrondata", "Idrovortice"], {"ATTACCO": 83, "DIFESA": 100}, np.random.choice(100))
    Venusaur = Pokemon("Venusaur", "Erba", ["Petalodanza", "Foglielama", "Velenozanna", "Polvereveleno"], {"ATTACCO": 82, "DIFESA": 83}, np.random.choice(100))
    

    #scelta del pokemon
    tuo_pokemon = random.randint(1,4)
    #pokemon avversario
    pokemon_avversario = random.randint(1,4)

    if tuo_pokemon == 3:
        if pokemon_avversario == 3:
            Venusaur.fight(Venusaur)
        if pokemon_avversario == 2:
            Venusaur.fight(Blastoise)
        if pokemon_avversario == 1:
            Venusaur.fight(Charizard)
    if tuo_pokemon == 2:
        if pokemon_avversario == 3:
            Blastoise.fight(Venusaur)
        if pokemon_avversario == 2:
            Blastoise.fight(Blastoise)
        if pokemon_avversario == 1:
            Blastoise.fight(Charizard)
    if tuo_pokemon == 1:
        if pokemon_avversario == 3:
            Charizard.fight(Venusaur)
        if pokemon_avversario == 2:
            Charizard.fight(Blastoise)
        if pokemon_avversario == 1:
            Charizard.fight(Charizard)

            

    
