import sys


def f_ellips(center_x, center_y, radius_x, radius_y, point_x, point_y):
    normalized_x = point_x - center_x
    normalized_y = point_y - center_y
    res = (normalized_x ** 2) / (radius_x ** 2) + (normalized_y ** 2) / (radius_y ** 2)
    if abs(res - 1) < 1e-10:
        return 0
    elif res < 1:
        return 1
    else:
        return 2



ellips = []
dots = []
with open(sys.argv[1]) as f:
    for line in f:
        ellips.append([])
        ellips[-1].append([int(x) for x in line.split()][0])
        ellips[-1].append([int(x) for x in line.split()][1])
with open(sys.argv[2]) as f:
    for line in f:
        dots.append([])
        dots[-1].append([int(x) for x in line.split()][0])
        dots[-1].append([int(x) for x in line.split()][1])

for i in range(0,len(dots)):
    print(f_ellips(ellips[0][0],ellips[0][1],ellips[1][0],ellips[1][1],dots[i][0],dots[i][1]))
