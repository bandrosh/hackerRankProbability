import sys
from dataclasses import dataclass


@dataclass
class Quartiles:
    q1: int
    q2: int
    q3: int


def execute():
    with open('interquartile_range/ent') as f:
        content = f.readlines()

    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]

    global N
    global x
    global y

    N = int(content[0])
    x = [int(i) for i in content[1].split()]
    y = [int(i) for i in content[2].split()]

    x.sort()

    frequency_list = build_quartile(x, y, N)

    q = my_quartile(frequency_list, len(frequency_list))

    # Output arguments using stdout
    sys.stdout.write(str(round(float(q.q3 - q.q1), 1)) + '\n')
    f.close()


def build_quartile(x, y, N):
    frequency = []
    for i in range(0, N):
        for j in range(0, y[i]):
            frequency.append(x[i])

    return frequency


def my_quartile(x, N):
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
