def remove_dup0(s0):
    s = list(s0)
    i = 0
    while i < len(s)-1:
        j = i+1
        while j < len(s):
            if s[i] == s[j]:
                for k in range(j, len(s)-1):
                    s[k] = s[k+1]
                #print(s)
                del s[-1]
            else:
                j += 1
        i += 1
    return ''.join(s)

def remove_dup(s0):
    if len(s0) < 2:
        return s0

    s = list(s0)
    i = 1
    tail = 1
    for i in range(1, len(s)):
        dup = False
        for j in range(0, tail):
            if s[i] == s[j]:
                dup = True
                break
        if dup == False:
            s[tail] = s[i]
            tail += 1
    s[tail] = '0'
    return ''.join(s)

if __name__ == '__main__':
    s = input()
    result = remove_dup(s)
    print(result)

    # testcase 
    if '' != remove_dup(''):
        print('Error: empty')
    if 'a0a' != remove_dup('aaa'):
        print('Error: a')
    if 'ab0' != remove_dup('aba'):
        print('Error: aba')
    if 'abc0a' != remove_dup('abaca'):
        print('Error: abc')
