from interquartile_range import interquartile_range
from mean_median_mode import mean_median_mode
from quartiles import quartiles
from standard_deviation import standard_deviation
from weighted_mean import weighted_mean

print('Day 0: Mean, Median and Mode')
mean_median_mode.execute()

print('Day 0: Weighted Mean')
weighted_mean.execute()

print('Day 1: Quartiles')
quartiles.execute()

print('Day 1: Interquartile Range')
interquartile_range.execute()

print('Day 1: Standard Deviation')
standard_deviation.execute()

# import sys
#
# stdin = sys.stdin.readlines()
#
# # Get arguments using stdin
# N = int(stdin[0])
# x = [int(i) for i in stdin[1].split()]
# y = [int(i) for i in stdin[2].split()]
#
#
# print_weighted_mean = str(myWeightedMean(x, y, N))
#
# # Output arguments using stdout
# sys.stdout.write(print_weighted_mean)
