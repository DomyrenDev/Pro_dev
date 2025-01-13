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
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.025)

#La Classe
class Pokemon:
    def __init__(self, nome, tipo, mosse, stats, livello, salute=100):
        self.nome = nome
        self.tipo = tipo
        self.mosse = mosse
        self.attacco = stats["ATTACCO"]
        self.difesa = stats["DIFESA"]
        self.livello = livello
        self.salute = "=" * (salute // 3)
        self.barre = 30

    def calculate_type_advantage(self, avversario):
        vantaggi_tipo = {
            "Fuoco": ["Erba", "Ghiaccio", "Acciaio", "Coleottero"],
            "Acqua": ["Fuoco", "Roccia", "Terra"],
            "Erba": ["Acqua", "Roccia", "Terra"],
            "Elettro": ["Acqua", "Volante"],
            "Ghiaccio": ["Erba", "Terra", "Volante", "Drago"],
            "Lotta": ["Normale", "Roccia", "Acciaio", "Ghiaccio", "Buio"],
            "Veleno": ["Erba", "Folletto"],
            "Psico": ["Lotta", "Veleno"],
            "Roccia": ["Fuoco", "Ghiaccio", "Volante", "Coleottero"],
            "Buio": ["Psico", "Spettro"],
            "Drago": ["Drago"],
            "Acciaio": ["Roccia", "Ghiaccio", "Folletto"],
            "Folletto": ["Lotta", "Drago", "Buio"]
        }
        
        if avversario.tipo in vantaggi_tipo.get(self.tipo, []):
            self.attacco *= 2
            self.difesa *= 2
            avversario.attacco /= 2
            avversario.difesa /= 2
            stringa_1_attacco = "\n E' super efficace!\n\n"
            stringa_2_attacco = "\n Non è molto efficace...\n\n"
        elif self.tipo in vantaggi_tipo.get(avversario.tipo, []):
            avversario.attacco *= 2
            avversario.difesa *= 2
            self.attacco /= 2
            self.difesa /= 2
            stringa_1_attacco = "\n Non è molto efficace...\n\n"
            stringa_2_attacco = "\n E' super efficace!\n\n"
        else:
            stringa_1_attacco = "\n Non è molto efficace...\n\n"
            stringa_2_attacco = "\n Non è molto efficace...\n\n"
        
        return stringa_1_attacco, stringa_2_attacco

    def fight(self, avversario):
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
        
        stringa_1_attacco, stringa_2_attacco = self.calculate_type_advantage(avversario)
        
        while (self.barre > 0) and (avversario.barre > 0):
            self.display_health(avversario)
            self.player_turn(avversario, stringa_1_attacco)
            if avversario.barre <= 0:
                self.end_battle(avversario, True)
                break
            self.opponent_turn(avversario, stringa_2_attacco)
            if self.barre <= 0:
                self.end_battle(avversario, False)
                break

    def display_health(self, avversario):
        print(f"{self.nome} \t\tPS\t {self.salute} ")
        print(f"{avversario.nome} \t\tPS\t {avversario.salute} ")

    def player_turn(self, avversario, stringa_1_attacco):
        delay_print(f"Vai, {self.nome}!\n\n")
        for i, x in enumerate(self.mosse):
            print(f"[{i+1}] " + x + "")
        delay_print(f"\nChe mossa deve usare {self.nome}? ")
        while True:
            try:
                index = int(input("[?]: "))
                if 1 <= index <= len(self.mosse):
                    break
                else:
                    print("Inserisci un numero valido.")
            except ValueError:
                print("Inserisci un numero valido.")
        delay_print(f"\n{self.nome} usa {self.mosse[index-1]}!")
        time.sleep(1)
        delay_print(stringa_1_attacco)
        self.calculate_damage(avversario, True)

    def opponent_turn(self, avversario, stringa_2_attacco):
        delay_print(f"\n {avversario.nome} ti sta attaccando")
        time.sleep(.5)
        index = np.random.choice(4)
        delay_print(f"\n {avversario.nome} nemico usa {avversario.mosse[index-1]}!\n")
        time.sleep(1)
        delay_print(stringa_2_attacco)
        self.calculate_damage(avversario, False)

    def calculate_damage(self, avversario, is_player):
        brutto_colpo = np.random.randint(0, 12)
        if is_player:
            if brutto_colpo == 1:
                self.attacco += 4
                avversario.barre -= self.attacco
                avversario.salute = ""
                self.attacco -= 4
                delay_print(f"\nBrutto colpo!\n\n")
            else:
                avversario.barre -= self.attacco
                avversario.salute = ""
            for _ in range(int(avversario.barre + .1 * avversario.difesa)):
                avversario.salute += "="
        else:
            if brutto_colpo == 1:
                avversario.attacco += 4
                self.barre -= avversario.attacco
                self.salute = ""
                avversario.attacco -= 4
                delay_print(f"\nBrutto colpo!\n\n")
            else:
                self.barre -= avversario.attacco
                self.salute = ""
            for _ in range(int(self.barre + .1 * avversario.difesa)):
                self.salute += "="
        time.sleep(1)
        self.display_health(avversario)

    def end_battle(self, avversario, is_player_winner):
        if is_player_winner:
            delay_print(f"\n{avversario.nome} nemico è esausto!\n")
            soldi = np.random.choice(5000)
            delay_print(f"\n\n Ti ha pagato $ {soldi} \n")
        else:
            delay_print(f"\n{self.nome} è esausto!\n")
            soldi = np.random.choice(5000)
            delay_print(f"\n\nHai pagato $ {soldi} \n")
if __name__ == "__main__":
    charizard = Pokemon("Charizard", "Fuoco", ["Lanciafiamme", "Aerofuria", "Artigliofuoco", "Dragospiro"], {"ATTACCO": 84, "DIFESA": 78}, livello=np.random.choice(100))
    blastoise = Pokemon("Blastoise", "Acqua", ["Idropompa", "Pugnoscarica", "Idrondata", "Idrovortice"], {"ATTACCO": 83, "DIFESA": 100}, livello=np.random.choice(100))
    venusaur = Pokemon("Venusaur", "Erba", ["Petalodanza", "Foglielama", "Velenozanna", "Polvereveleno"], {"ATTACCO": 82, "DIFESA": 83}, livello=np.random.choice(100))
    Blastoise = Pokemon("Blastoise", "Acqua", ["Idropompa", "Pugnoscarica", "Idrondata", "Idrovortice"], {"ATTACCO": 83, "DIFESA": 100}, livello=np.random.choice(100))
    Venusaur = Pokemon("Venusaur", "Erba", ["Petalodanza", "Foglielama", "Velenozanna", "Polvereveleno"], {"ATTACCO": 82, "DIFESA": 83}, livello=np.random.choice(100))
   
    #scelta del pokemon
    tuo_pokemon = random.randint(1,4)
    #pokemon avversario
    pokemon_avversario = random.randint(1,4)

    if tuo_pokemon == 1:
        venusaur.fight(venusaur)
    elif tuo_pokemon == 2:
        venusaur.fight(blastoise)
    elif tuo_pokemon == 3:
        venusaur.fight(charizard)
        venusaur.fight(charizard)

    if pokemon_avversario == 1:
        blastoise.fight(venusaur)
    elif pokemon_avversario == 2:
        blastoise.fight(blastoise)
        blastoise.fight(charizard)
        blastoise.fight(charizard)
        blastoise.fight(charizard)

    if pokemon_avversario == 1:
        charizard.fight(venusaur)
        charizard.fight(charizard)
    elif pokemon_avversario == 3:
            charizard.fight(charizard)
    elif pokemon_avversario == 4:
        charizard.fight(charizard)
     

    
