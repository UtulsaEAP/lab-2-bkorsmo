
def caffeine():



    print('Enter mg of Caffeine: ')
    caffeine_mg = float(input())
    

    onehalf= caffeine_mg/2
    twohalf=caffeine_mg/2/2
    threehalf=caffeine_mg/2/2/2/2

    print(f'{onehalf:.2f}')
    print(f'{twohalf:.2f}')
    print(f'{threehalf:.2f}')
    
if __name__ == "__main__":
    caffeine()