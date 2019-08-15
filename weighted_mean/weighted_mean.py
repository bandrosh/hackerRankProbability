import sys


def execute():
    with open('weighted_mean/ent') as f:
        content = f.readlines()

    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]

    global N
    global x
    global y

    N = int(content[0])
    x = [int(i) for i in content[1].split()]
    y = [int(i) for i in content[2].split()]

    print_weighted_mean = str(my_weighted_mean(x, y, N))

    # Output arguments using stdout
    sys.stdout.write(print_weighted_mean + '\n')
    f.close()


def my_weighted_mean(x, y, N):
    sum_categorize = 0
    sum_weight = 0
    for i in range(N):
        sum_categorize += (x[i] * y[i])
        sum_weight += y[i]

    return float(sum_categorize/sum_weight)
