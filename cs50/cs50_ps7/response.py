from validator_collection import validators, checkers, errors

def main():
    print(is_valid(input("Enter your e-mail: ")))


def is_valid(s):

    if valid := checkers.is_email(s):
        return "Valid"
    elif not valid:
        return "Invalid"
    
if __name__ == '__main__':
    main()

    