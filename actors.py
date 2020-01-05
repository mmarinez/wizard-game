import random


class Wizard:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def attack_damage(self, creature):
        my_roll = random.randint(1, 12) * self.level
        creature_roll = random.randint(1, 12) * creature.level

        print("{} the wizard has an attack damage of {}".format(self.name, my_roll))
        print("the {} has an attack damage of {}".format(creature.name, creature_roll))

        return my_roll >= creature_roll

    def attack(self, active_creature):
        print("{} the wizard attacks the creature".format(self.name))
        return self.attack_damage(active_creature)

    def training(self, life_count):
        training_results = random.randint(1, 100)
        if training_results <= 50:
            print('\nThe wizard has taken his training slow and with caution has achive more power\n')
            self.level = self.level + 5
        elif training_results > 50 and training_results < 70:
            print("\n{} becomes unbalanced with his power and is hurt during his training\n".format(self.name))
            life_count = life_count - 1
        elif training_results > 70:
            print('\nThe wizard is now in complete balance with his power and all around him, he is now a lot more powerful than before\n')
            self.level = self.level + 100

        print("The wizard is now level {} and has {} life points".format(self.level, life_count))
        return life_count


class Creatures:
    def __init__(self, creature_name, creature_level):
        self.name = creature_name
        self.level = creature_level