def main():
    (M, X, R) = inputD()
    findOPT(M,X,R)


def inputD():
    data = []
    with open("inputBB.txt") as f:
        for line in f:
            data.append([int(x) for x in line.split()])
    (K,X,R)=data
    for i in K:
        M=i
    print(M)
    print(X)
    print(R)
    return M,X,R


def findOPT(n, X, R):
    opt = list()
    path = list()

    path.append(0)
    opt.append(0)
    opt.append(R[0])

    for i in range(1, n):
        index = getOPTpoint(X,i)
        opt.append(max(R[i] + opt[index], opt[i]))

        if R[i] + opt[index] > opt[i]:
            path.append(i)

    print(opt[len(opt) - 1])

    printPath(path, X)


def getOPTpoint(X, i):
    index = 0
    while X[i] - X[index] > 5:
        index += 1

    return index


def printPath(path, X):
    for i in range(len(path) - 1, 1, -1):
        if X[path[i]] - X[path[i - 1]] < 6:
            path.pop(i - 1)

    for i in path:
        print(X[i],end=' ')

main()