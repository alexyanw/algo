def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    m1, m2 = {}, {}
    for i in range(len(s1)):
        c1, c2 = s1[i], s2[i]
        m1[c1] = m1.get(c1, 0) + 1
        m2[c2] = m2.get(c2, 0) + 1
    return m1 == m2

if __name__ == '__main__':
    yes = [
        ['ab', 'ba'],
        ['aba', 'aab'],
        ['abac', 'baac'],
            ]
    for t in yes:
        if not is_anagram(*t):
            print('Error', t)

    no = [
        ['ab', 'b'],
        ['aba', 'ab'],
        ['ab', 'ac'],
            ]

    for t in no:
        if is_anagram(*t):
            print('Error', t)
