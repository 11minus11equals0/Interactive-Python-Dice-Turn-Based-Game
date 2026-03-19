from logic import Player, Dice, Main
from passives import *
from abilities import *
from ui import EN
from config import setLanguage
from effects import *
from items import *

if __name__ == "__main__":
    setLanguage(EN)

    playerA = Player("A", [Punch(), Stun()], [Juggernaut()], Dice(6), Dice(6), Dice(6))
    playerB = Player("B", [Poison(), Stun()], [Critical()], Dice(6), Dice(6), Dice(6))
    print("\n\n\n")

    playerA.effects.append(PoisonEffect(playerA))
    playerA.effects.append(StunEffect(playerA))

    playerA.inventory.append(StrengthPotion())

    Main(playerA, playerB)
