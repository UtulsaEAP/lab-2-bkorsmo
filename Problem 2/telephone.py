#Brady Korsmo Thursday @2


def telephone():
    
    ''' Type your code here. '''

    print('Enter number')
    phone_number = int(input())

    area_code=str(phone_number//10000000)

    middle=str((phone_number//10000)%1000)

    end=str((phone_number%10000))
    
    print('('+(area_code)+') '+ (middle)+ '-'+(end))

    





if __name__ == "__main__":
    telephone()