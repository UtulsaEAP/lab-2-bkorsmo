def telephone():
    
    ''' Type your code here. '''

    print('Enter number')
    phone_number = int(input())

    area_code=phone_number//10000000

    middle=(phone_number//10000)%10000

    end=(phone_number%10000)

    print('('+str(area_code)+') '+ str(middle)+ '-'+str(end))

    





if __name__ == "__main__":
    telephone()