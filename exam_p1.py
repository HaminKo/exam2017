trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si', '5':'wu', 
         '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi', '100': 'bai'}



def speak_Chinese(number):
    '''
    number: an integer, 0<=number<=999

    Returns: a string that is the number in Chinese
    '''
    string_num = str(number)
    
    if number <= 10:
        return trans[str(number)]
    elif number <= 19:
        return trans[str(10)] + ' ' + trans[str(number - 10)]
    elif number <= 99:
        if number%10 == 0:
            return trans[str(number//10)] + ' ' + trans[str(10)]
        else:
            return trans[str(number//10)] + ' ' + trans[str(10)] + ' ' + trans[str(number%10)]
    elif number == 100:
        return trans[str(100)]
    elif number <= 999 and string_num[1] == '0':
        if number%10%10 == 0:
            return trans[str(number//100)] + ' ' + trans[str(100)]
        else:
            return trans[str(number//100)] + ' ' + trans[str(100)] + ' ' + trans[str(0)] + ' ' + trans[str(number%100)]
    elif number <= 999 and string_num[1] != 0:
        if number%10%10 == 0:
            return trans[str(number//100)] + ' ' + trans[str(100)] + ' ' + trans[str(number%100//10)] + ' ' + trans[str(10)] 
        else:
            return trans[str(number//100)] + ' ' + trans[str(100)] + ' ' + trans[str(number%100//10)] + ' ' + trans[str(10)] + ' ' + trans[str(number%10%10)]


# For testing
def main():
    print(speak_Chinese(36))
    print('In Chinese: 36 = san shi liu')
    print(speak_Chinese(20))
    print('In Chinese: 20 = er shi')
    print(speak_Chinese(16))
    print('In Chinese: 16 = shi liu')
    print(speak_Chinese(200))
    print('In Chinese: 200 = er bai')
    print(speak_Chinese(109))
    print('In Chinese: 109 = yi bai ling jiu')
    print(speak_Chinese(999))
    print('In Chinese: 999 = jiu bai jiu shi jiu')

if __name__ == '__main__':
    main()
