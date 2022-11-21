def bset(opr, mask): #or
    ans = ''
    for i in range(len(mask)):
        if mask[i] == '1' or opr[i] == '1':
            ans += '1'
        else:
            ans += '0'
    print(ans)

def bclr(opr, mask): #and
    ans = ''
    for i in range(len(mask)):
        if mask[i] == '1' and opr[i] == '1':
            ans += '1'
        else:
            ans += '0'
    print(ans)

bclr('00000000', 
     '10000000')

bset('00000000', 
     '10000000')
