'''

'''


def main():
    prompt = '''
    1. add
    2. del
    3. list
    4. quit
    
    Enteer number:
    '''

    number = 0

    while number != 4:
        print(prompt)
        number = int(input())


main()
