__author__ = 'johan'



def FindMaxPath(m):
    if len(m) <= 1:
        return m[0]

    for row in range(len(m) - 2, -1, -1):
        #print('Row =', row)
        for i in range(len(m[row])):
            m[row][i] = m[row][i] + max(m[row + 1][i], m[row + 1][i + 1])

        #print(m)

    return m[0]

def ReadMatrixFromFile(filename):
    m = []

    with open(filename, 'r') as f:
        temp = f.readline()

        while not temp == '':
            split = temp.split(' ')
            m.append([int(i) for i in split])
            temp = f.readline()

    return m

m = ReadMatrixFromFile('triangle.txt')
a = FindMaxPath(m)
print(a)
