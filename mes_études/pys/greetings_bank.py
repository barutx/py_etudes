def main():
    print(greetings())

def greetings(x='hello'):
    
    if x[0:5] == 'hello':
        return "$0"
    elif x[0] =='h' and not x[0:5] == 'hello':
        return '$20'
    else:
        return '$100'

if __name__ == '__main__':
    main()
