import re
def replace_space(s):
    return s.replace(' ', '%20')

def replace_space(s0):
    s = list(s0)
    for i,e in enumerate(s):
        if e==' ':
            s[i] = '%'
            s.insert(i+1, '2')
            s.insert(i+2, '0')
    return ''.join(s)
    

if __name__ == '__main__':
    yes = [
        ['ab cd  ef', 'ab%20cd%20%20ef'],
            ]
    for t in yes:
        if t[1] != replace_space(t[0]):
            print('Error', t)

