import sys
from dataclasses import dataclass


@dataclass
class Quartiles:
    q1: int
    q2: int
    q3: int


def execute():
    with open('quartiles/ent') as f:
        content = f.readlines()

    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]

    global N
    global x
    global y

    N = int(content[0])
    x = [int(i) for i in content[1].split()]

    q = my_quartile(x, N)

    # Output arguments using stdout
    sys.stdout.write(str(q.q1) + '\n')
    sys.stdout.write(str(q.q2) + '\n')
    sys.stdout.write(str(q.q3) + '\n')
    f.close()


def my_quartile(x, N):
    x.sort()

    list_q1 = x[0:int(N / 2)]
    list_q2 = x[int(N / 2) if (N % 2 == 0) else (int(N / 2) + 1):N]

    q1 = my_median(list_q1, int(N / 2))
    q2 = my_median(x, N)
    q3 = my_median(list_q2, int(N / 2))

    return Quartiles(q1, q2, q3)


def my_median(x, N):
    x.sort()
    if (N % 2) == 0:
        top = (N // 2)
        bot = top - 1
        median = float((x[top] + x[bot])) / 2
    else:
        middle = (int)(N / 2)
        median = x[middle]
    median_rounded = round(median, 1)
    return (median_rounded)
