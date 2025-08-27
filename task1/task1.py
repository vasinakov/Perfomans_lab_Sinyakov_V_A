import sys
def f(n, m):
    mas = [1]
    res = "1"
    while True:
        mas.append((mas[-1] + m - 1) % n)
        if (mas[-1] == 1):
            break
        res += str(mas[-1])
    res = res.replace('0', str(n))
    return res


print(f(int(sys.argv[1]),int(sys.argv[2])) + f(int(sys.argv[3]), int(sys.argv[4])))
