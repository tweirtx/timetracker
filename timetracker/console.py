from timetracker.signer import sign


def start():
    while True:
        try:
            print(sign(input("Please enter the user ID to sign in: ")))
        except KeyboardInterrupt:
            exit(0)
