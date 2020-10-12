import csv
import math
import matplotlib.pyplot as plt
from pylab import *

# constant lol
h = 6.62607004 * (10 ** (-34))
c = 299792458
kB = 1.3806488 * (10 ** (-23))

# standard observer function
x_lambda = dict()
y_lambda = dict()
z_lambda = dict()
count = 0
# path file of that table
with open('D:/Work/Project2/all_data/black_body/wavelength_cie.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    # print('x y z value retrieve from table')
    for row in csv_reader:
        count += 1
        if(count <= 2):
            continue
        # print(f'\t{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}')
        row[0] = int(row[0])
        x_lambda[row[0]] = float(row[1])
        y_lambda[row[0]] = float(row[2])
        z_lambda[row[0]] = float(row[3])

'''print(x_lambda)
print(y_lambda)
print(z_lambda)'''

def estimate_value(wavelength):
    if(wavelength >= 780):
        return 0, 0, 0
    est_wavelength = int(wavelength/10) * 10
    x = x_lambda[est_wavelength] + ((wavelength - est_wavelength) / 10 * (x_lambda[est_wavelength + 10] - x_lambda[est_wavelength]))
    y = y_lambda[est_wavelength] + ((wavelength - est_wavelength) / 10 * (y_lambda[est_wavelength + 10] - y_lambda[est_wavelength]))
    z = z_lambda[est_wavelength] + ((wavelength - est_wavelength) / 10 * (z_lambda[est_wavelength + 10] - z_lambda[est_wavelength]))
    # print(x, y, z)
    return x, y, z

def xyz(file_name):
    # import csv info file
    # output should be x, y, z value corresponding to each row in csv file
    wavelength = []
    intensity = []
    skip = True
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        # print('x y z value retrieve from table')
        for row in csv_reader:
            if(skip):
                skip = False
                continue
            print(f'\t{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}')
            wavelength.append(float(row[0]))
            intensity.append(100000**(-float(row[12])))
    print('intensity : ', intensity)

    x_sum = 0
    y_sum = 0
    z_sum = 0
    sum_intensity = 0
    for data in range(len(wavelength)):
        if(wavelength[data] >= 780):
            break
        x_data = float(intensity[data]) * estimate_value(float(wavelength[data]))[0]
        y_data = float(intensity[data]) * estimate_value(float(wavelength[data]))[1]
        z_data = float(intensity[data]) * estimate_value(float(wavelength[data]))[2]
        sum_intensity += float(intensity[data])
        x_sum += x_data
        y_sum += y_data
        z_sum += z_data
        print(wavelength[data], '\t', intensity[data], '\t', x_data, '\t', y_data, '\t', z_data)
    print(x_sum, y_sum, z_sum)
    x_bar = x_sum / sum_intensity
    y_bar = y_sum / sum_intensity
    z_bar = z_sum / sum_intensity
    x = x_bar / (x_bar + y_bar + z_bar)
    y = y_bar / (x_bar + y_bar + z_bar)
    z = z_bar / (x_bar + y_bar + z_bar)
    print(x_bar, y_bar, z_bar)
    print(x, y, z)

xyz('D:/Work/Project2/all_data/black_body/Abs_FULL.csv')
