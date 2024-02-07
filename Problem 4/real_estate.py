
#Brady Korsmo Thursday @2

def real_estate():
    

    print('Enter current price: ')
    current_price = int(input())
    print('Enter last months price: ')
    last_month_price = int(input())
    # Your code goes here

    change=str(current_price-last_month_price)
    mortgage=((current_price*0.051)/12)
    current_price=str(current_price)
    last_month_price=str(last_month_price)
    

    mortgage=f'{mortgage:.2f}'

    print('This house is $' +current_price +'. The change is $'+  change + ' since last month.')
    print('The estimated monthly mortgage is $'+mortgage+'.')




if __name__ == "__main__":
    real_estate()