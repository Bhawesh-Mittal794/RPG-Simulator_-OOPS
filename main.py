from game import Game


def main():
    try:
        game = Game()
        game.start()

    except KeyboardInterrupt:
        print("\n\nGame exited by user.")

    except Exception as error:
        print("\nAn unexpected error occurred.")
        print(error)


if __name__ == "__main__":
    main()