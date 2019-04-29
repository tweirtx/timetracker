from .signer import sign


def start():
    while True:
        print(sign(input("Please enter the user ID to sign in: ")))
