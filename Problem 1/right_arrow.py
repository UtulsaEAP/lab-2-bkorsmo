
#Brady Korsmo Thursday @2


def right_arrow():

    base_char = input()
    head_char = input()

    row1 = '      ' + head_char
    ''' Type your code here. '''
    row2 = base_char*6 +head_char*2
    row3 = base_char*6 +head_char*3


    print(row1)
    print(row2)
    print(row3)
    print(row2)
    print(row1)

if __name__ == "__main__":
    right_arrow()