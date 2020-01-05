from actors import Creatures, Wizard
import random
import time


def main():
    game_header()
    game_loop()


def game_header():
    print("-------------------")
    print("    Wizard Game")
    print("-------------------")


def game_loop():

    life_count = 3
    hero = Wizard("Zilden", 50)
    creatures = [
        Creatures("Bat", 1),
        Creatures("Slime", 10),
        Creatures("Golem", 30),
        Creatures("Dragon", 50),
        Creatures("Evil Wizard", 1000)
    ]

    while True:
        active_creature = random.choice(creatures)

        print("A {} of level {} has been summoned\n".format(active_creature.name, active_creature.level))

        cmd = input("What do you want to do? \n" +
                    "[a]ttack\n" +
                    "[r]un away\n" +
                    "[l]ookaround\n" +
                    "[t]raining\n" +
                    "[s]tatus\n")

        if cmd == "a":
            if hero.attack(active_creature):
                print('\nThe wizard has vanquished the {}'.format(active_creature.name))
                creatures.remove(active_creature)
            else:
                print('\nThe wizard has been DEFEATED')
                life_count = life_count - 1
                if life_count < 1:
                    print("\n{} the wizard has been VANQUISHED... Game Over".format(hero.name))
                    break
                else:
                    print('\nHe flees to heal his wounds, wait until the wizard uses his healing power...\n')
                    time.sleep(5)
                    print("\nThe wizard has returned to battle with {} life points left\n".format(life_count))
        elif cmd == "r":
            print("{} the wizard flees from the battle".format(hero.name))
        elif cmd == "l":
            for creature in creatures:
                print("A {} of level {}".format(creature.name, creature.level))
        elif cmd == "t":
            print("The wizard practices new abilities to gain power")
            life_count = hero.training(life_count)
            if life_count < 1:
                    print("\n{} the wizard has been VANQUISHED... Game Over".format(hero.name))
                    break
        elif cmd == "s":
            print("{} level: {}".format(hero.name, hero.level))
            print("{} life points: {}\n".format(hero.name, life_count))
        else:
            print("Ok, exiting the game... bye")
            break


if __name__ == "__main__":
    main()