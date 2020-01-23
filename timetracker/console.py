from timetracker.signer import sign


def start():
    while True:
        try:
            print(sign(input("Please enter the user ID to sign in: ")))
        except KeyboardInterrupt:
            print("You must be superuser to do that!")
        except EOFError:
            print("You must be superuser to do that!")
