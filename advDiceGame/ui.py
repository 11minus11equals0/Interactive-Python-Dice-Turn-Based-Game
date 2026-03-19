EN = {
    "combat": {
        "punchHit": "{player.name} punches {target.name} for {punch.damage} damage!",
        "poisonHit": "{player.name} infects {target.name} with poison, penetrating the skin for 1 damage!",
        "poisonTick": "{player.name} takes {eff.value} {eff.name} damage",
        "strengthBuff": "{player.name}'s {ability.name} is empowered by {eff.name}! ({ability.baseDamage} -> {ability.damage})",
        "stunned": "{player.name} is stunned this turn!",
        "stunHit": "{player.name} stuns {target.name} for next two turns, dealing {ability.damage} damage!",
        "stunMiss": "{player.name} deals {ability.damage} damage to {target.name}, but fails to stun!",
        "heal": "{player.name} heals for 4 health",
        "victory": "{winner.name} defeated {loser.name} with {winner.health}HP remaining!",

        "remaining": "{player.name} has {player.health}HP remaining!",
        "dodge": "{player.name} dodged",
    },

    "names": {
        "player": "player",
        "name": "name",
        "health": "health",
        "mana": "mana",

        "dices": "dices",
        "manaDice": "mana dice",
        "atkDice": "attacker dice",
        "defDice": "defender dice",

        "passives": "passives",
        "default": "default",
        "juggernaut": "juggernaut",
        "lifesteal": "lifesteal",
        "critical": "critical",
        "counterstrike": "counterstrike",
        "dodger": "dodger",

        "abilities": "abilities",
        "punch": "punch",
        "heal": "heal",
        "stun": "stun",

        "effects": "effects",
        "poison": "poison",
        "stunEffect": "stun",
        "strength": "strength",

        "bandaid": "bandaid",
        "strengthPotion": "strength potion",
    },

    "descriptions": {
        "defaultEffect": "{eff.name} for {eff.turns} turns",
        "poisonEffect": "{eff.name} {eff.value} damage for {eff.turns} turns",

        "defaultPassive": "No changes.",
        "juggernaut": "starts with +50% of max health",
        "lifesteal": "heals 50% from damage dealt",
        "critical": "has a 50% chance to deal a critical hit",
        "counterstrike": "deals 3 damage on dodge",
        "dodger": "starts with 7D defence dice instead of 6D",

        "punch": "punches a target for 2 damage",
        "poison": "poisons the target for 1 damage for 3 turns",
        "heal": "heals itself for 4 health",
        "stun": "50% chance to stun the enemy",
        "strength": "increases damage by 50% for 2 turns",

        "bandaid": "heals 2HP on use",
        "strengthPotion": "increases attack damage by 50% for 2 turns on use",
    },

    "logic": {
        "manaLack": "You don't have enough mana!",
        "manaRoll": "{player.name} rolled {mana} mana",
        "roll": "{player.name} rolled {player.roll}",
        "actionErr": "Please enter a valid action!",
        "abilityErr": "Please enter a valid ability!",
        "itemErr": "Please enter a valid item!",
        "actions": "{player.name}, What do you want to do? R-roll / A-abilities / S-stats / I-inventory\n->",
        "abilityChoice": "Choose your ability (/ to go back):",
        "itemChoice": "What item do you want to use? (/ to go back):",
        "fullHeal": "{player.name} fully healed to {player.maxHealth}"
    },

    "scenes": {
        "round": "================= Round {roundNo} =================",
        "victory": "=============== {winner.name}'s Victory! ===============",
        "attack": "--------- Attack ----------",
        "heal": "--------- Heal ----------",
        "hit": "--------- Hit ----------",
        "dodge": "--------- Dodge ----------",
        "stats": "--------- Stats ----------",

        "juggernaut": "{psv.user.name} feels his body getting harder as he gains {hpBuff} Health Points!",
        "lifesteal": "{player.name} replenishes {heal}HP from {target.name}'s blood",
        "critical": "{player.name} lands a critical hit! ({ability.baseDamage} -> {ability.damage})",
        "counterstrike": "{player.name} counter-attacks {target.name} dealing 4 damage!",
        "dodger": "{player.name} feels a speed surge!",

        "bandaid": "{player.name} heals with a bandaid for 2HP",
        "strengthPotion": "{player.name} drinks a strength potion, empowering their attacks!",
    }
}
