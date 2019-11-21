def main():
    game_header()
    game_loop()


def game_header():
    print("-------------------")
    print("    Wizard Game")
    print("-------------------")


def game_loop():
    while True:
        cmd = input("What do you want to do? \n[a]ttack\n[r]un away\n[l]ookaround\n")

        if cmd == "a":
            print("attack")
        elif cmd == "r":
            print("runaway")
        elif cmd == "l":
            print("lookaround")
        else:
            print("Ok, exiting the game... bye")
            break


if __name__ == "__main__":
    main()