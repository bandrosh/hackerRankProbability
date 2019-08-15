import math
import sys


def execute():
    with open('standard_deviation/ent') as f:
        content = f.readlines()

    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]

    N = int(content[0])
    x = [int(i) for i in content[1].split()]

    print_standard_deviation = str(my_standard_deviation(x, N))

    # Output arguments using stdout
    sys.stdout.write(print_standard_deviation + '\n')
    f.close()


def mean(x, N):
    sum_x = 0.0

    for i in range(0, N):
        sum_x += x[i]

    return round(sum_x / N, 1)


def my_standard_deviation(x, N):
    sum_mean = 0.0
    mean_value = mean(x, N)

    for i in range(0, N):
        sum_mean += math.pow((x[i] - mean_value), 2)

    return round(math.sqrt(sum_mean / N), 1)
