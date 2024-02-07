#Brady Korsmo Thursday @2


def caffeine():



    print('Enter mg of Caffeine: ')
    caffeine_mg = float(input())
    

    onehalf= caffeine_mg/2
    twohalf=caffeine_mg/2**2
    threehalf=caffeine_mg/2**4

    print(f'After 6 hours: {onehalf:.2f} mg')
    print(f'After 12 hours: {twohalf:.2f} mg')
    print(f'After 24 hours: {threehalf:.2f} mg')
    
if __name__ == "__main__":
    caffeine()