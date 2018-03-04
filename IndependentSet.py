# (A)
# 2 1 8 9 8 1

# (B)
# 1 8 6 3 6

# (C)
def main():
    arr = inputA()
    print(arr)
    path = findIS(arr)
    result(path, arr)


def inputA():
    file = open("inputIS.txt", "r")
    array = list(map(int, file.readline().split()))
    return array


def findIS(arr):
    d = list()
    path = list()

    path.append(0)
    path.append(0 if (arr[0] > arr[1]) else 1)
    d.append(0)
    d.append(arr[0])
    d.append(max(arr[0], arr[1]))

    for i in range(2, len(arr)):
        d.append(max(d[i - 1] + arr[i], d[i]))

        if d[i - 1] + arr[i] > d[i]:
            path.append(i)

    print(d[len(d) - 1])

    for i in range(len(path) - 1, 0, -1):
        if path[i] - path[i - 1] < 2:
            path.pop(i - 1)
    return path


def result(path, arr):
    for i in path:
        print('{0}({1})'.format(arr[i], i + 1), end=' ')


main()
