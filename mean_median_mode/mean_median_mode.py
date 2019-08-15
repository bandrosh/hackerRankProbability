import sys


# stdin = sys.stdin.readlines()
#
# # Get arguments using stdin
# N = int(stdin[0])
# x = [int(i) for i in stdin[1].split()]


def execute():
    with open('mean_median_mode/ent') as f:
        content = f.readlines()

    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]

    global N
    global x

    N = int(content[0])
    x = [int(i) for i in content[1].split()]

    # Convert results into strings and add line break
    print_mean = str(my_mean(x, N)) + "\n"
    print_median = str(my_median(x, N)) + "\n"
    print_mode = str(my_mode(x, N)) + "\n"

    # Output arguments using stdout
    sys.stdout.write(print_mean)
    sys.stdout.write(print_median)
    sys.stdout.write(print_mode)

    f.close()


def my_mean(x, N):
    mean = float(sum(x)) / N
    mean_rounded = round(mean, 1)
    return (mean_rounded)


def my_median(x, N):
    x.sort()
    if (N % 2) == 0:
        top = (N // 2)
        bot = top - 1
        median = float((x[top] + x[bot])) / 2
    else:
        middle = (N / 2)
        median = x[middle]
    median_rounded = round(median, 1)
    return (median_rounded)


def my_mode(x, N):
    same = [(x.count(i)) for i in set(x)]
    counts = [(i, x.count(i)) for i in set(x)]
    possible_modes = list()
    for num, count in counts:
        if count == max(same):
            possible_modes.append(num)
    mode = min(possible_modes)
    return (mode)
