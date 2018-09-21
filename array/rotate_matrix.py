def rotate_matrix(M):
    l = len(M)
    for i in range(l//2):
        for j in range(l-1-i*2):
            left = i+j, i
            upper = i, l-1-i-j
            right = l-1-i-j, l-1-i
            bottom = l-1-i, i+j
            M[left[0]][left[1]], M[upper[0]][upper[1]], M[right[0]][right[1]], M[bottom[0]][bottom[1]] = \
            M[bottom[0]][bottom[1]], M[left[0]][left[1]], M[upper[0]][upper[1]], M[right[0]][right[1]]
    return M

if __name__ == '__main__':
    src = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9,10,11,12],
        [13,14,15,16]
        ]
    dst = [
        [13, 9, 5, 1],
        [14,10, 6, 2],
        [15,11, 7, 3],
        [16,12, 8, 4]
        ]

    result = rotate_matrix(src)
    fail = False
    for i in range(len(dst)):
        for j in range(len(dst[0])):
            if dst[i][j] != result[i][j]:
                fail = True
                print('Error', i, j)
    for i in range(len(dst)):
        print(result[i])
    if not fail:
        print('Pass')
