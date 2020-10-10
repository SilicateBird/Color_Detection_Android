import csv
import math
import matplotlib.pyplot as plt
from pylab import *

# constant lol
h = 6.62607004 * (10 ** (-34))
c = 299792458
kB = 1.3806488 * (10 ** (-23))


def blackbodytest(temperature):
    # input temp
    # temperature = int(input('Temperature(K) : '))

    # import file table
    # output should be x, y, z value in 2deg
    x_lambda = []
    y_lambda = []
    z_lambda = []
    with open('D:/Work/Project2/all_data/black_body/wavelength_cie.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        # print('x y z value retrieve from table')
        for row in csv_reader:
            # print(f'\t{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}')
            x_lambda.append(row[1])
            y_lambda.append(row[2])
            z_lambda.append(row[3])

    # loop to calculate x, y, z for all wavelength
    x_sum = 0
    y_sum = 0
    z_sum = 0
    sum_intensity = 0
    for wavelength in range(380, 760, 10):
        # black body radiation formula
        count = int((wavelength - 360) / 10)
        wavelength = wavelength * (10 ** -9)
        intensity = (2 * math.pi * h * (c ** 2)) / (
                (wavelength ** 5) * (math.e ** ((h * c) / (wavelength * kB * temperature)) - 1))
        sum_intensity = sum_intensity + intensity
        x_sum = x_sum + (intensity * float(x_lambda[count]))
        y_sum = y_sum + (intensity * float(y_lambda[count]))
        z_sum = z_sum + (intensity * float(z_lambda[count]))
        # print(wavelength, intensity)

    # find mean of x, y, z
    x_bar = x_sum / sum_intensity
    y_bar = y_sum / sum_intensity
    z_bar = z_sum / sum_intensity
    # print(x_bar, y_bar, z_bar)

    # normalize
    x = x_bar / (x_bar + y_bar + z_bar)
    y = y_bar / (x_bar + y_bar + z_bar)
    z = z_bar / (x_bar + y_bar + z_bar)
    x = "{:.3f}".format(x)
    y = "{:.3f}".format(y)
    z = "{:.3f}".format(z)
    print('Result of temp', temperature, '\t:\t', x, y, z)
    return x, y


temp_test = [1000, 1500, 2000, 2500, 3000, 3500, 4000, 6000, 10000]
xy = dict()
x_axis = []
y_axis = []
for i in temp_test:
    # xy[blackbodytest(i)[0]] = blackbodytest(i)[1]
    blackbodytest(i)

'''
for key in sorted(xy.keys()):
    x_axis.append(key)
    y_axis.append(xy[key])

print(x_axis, y_axis)

plt.plot(x_axis, y_axis, color='green', linestyle='dashed', linewidth = 3,
         marker='o', markerfacecolor='blue', markersize=12)
# plt.axis([0, 1, 0, 1])
plt.show()

scatter(x_axis, y_axis, s=100 ,marker='o')
show()

'''
