import os
import numpy as np
import matplotlib.pyplot as plt

BASE_DIR = "img/"

START_EXPONENT = 3
STOP_EXPONENT = 8

############################### Single ###############################
# Total Time v.s. Number of Students
student_num = [10**i for i in range(START_EXPONENT, STOP_EXPONENT+1)]
total_time = [4.088, 4.826, 5.189, 8.904, 55.917, 534]

coeffs = np.polyfit(np.log(student_num), np.log(total_time), deg=2)
poly = np.poly1d(coeffs)

x = np.logspace(START_EXPONENT, 1.01*STOP_EXPONENT, 100)
y = np.exp(poly(np.log(x)))

plt.scatter(student_num, total_time)
plt.plot(x, y, 'orange')

plt.xscale('log')
plt.xlabel('Number of Students')
plt.ylabel('Total Time (s)')
plt.title('Total Time v.s. Number of Students')

plt.savefig(os.path.join(BASE_DIR, 'single.png'))
plt.clf()

# File Size v.s. Number of Students
file_size = [29, 287, 2.8*1024, 28.7*1024, 286.9*1024, 2.87*1024*1024]

coeffs = np.polyfit(np.log(student_num), np.log(file_size), deg=2)
poly = np.poly1d(coeffs)
y = np.exp(poly(np.log(x)))

plt.scatter(student_num, file_size)
plt.plot(x, y, 'orange')

plt.xscale('log')
plt.xlabel('Number of Students')
plt.ylabel('File Size (KB)')
plt.title('File Size v.s. Number of Students')

plt.savefig(os.path.join(BASE_DIR, 'file.png'))
plt.clf()

############################### Cluster ###############################
student_num = [10**i for i in range(START_EXPONENT, STOP_EXPONENT+1)]

total_time_1 = [25, 21, 21, 24, 47, 107]
total_time_2 = [21, 20, 22, 24, 40, 96]
total_time_3 = [22, 20, 23, 22, 45, 95]

total_time = []
for i in range(len(total_time_1)):
    total_time.append((total_time_1[i] + total_time_2[i] + total_time_3[i])/3)

coeffs = np.polyfit(np.log(student_num), np.log(total_time), deg=3)
poly = np.poly1d(coeffs)

x = np.logspace(START_EXPONENT, 1.01*STOP_EXPONENT, 100)
y = np.exp(poly(np.log(x)))

# Total Time v.s. Number of Students
plt.scatter(student_num, total_time)
plt.plot(x, y, 'orange')

plt.xscale('log')
plt.xlabel('Number of Students')
plt.ylabel('Total Time (s)')
plt.title('Total Time v.s. Number of Students')

plt.savefig(os.path.join(BASE_DIR, 'cluster.png'))
plt.clf()

############################### Both ###############################
student_num = [10**i for i in range(START_EXPONENT, STOP_EXPONENT+1)]

total_time_1 = [25, 21, 21, 24, 47, 107]
total_time_2 = [21, 20, 22, 24, 40, 96]
total_time_3 = [22, 20, 23, 22, 45, 95]

total_time_single = [4.088, 4.826, 5.189, 8.904, 55.917, 534]

total_time_cluster = []
for i in range(len(total_time_1)):
    total_time_cluster.append(
        (total_time_1[i] + total_time_2[i] + total_time_3[i])/3)

coeffs_cluster = np.polyfit(
    np.log(student_num), np.log(total_time_cluster), deg=3)
coeffs_single = np.polyfit(
    np.log(student_num), np.log(total_time_single), deg=3)
poly_cluster = np.poly1d(coeffs_cluster)
poly_single = np.poly1d(coeffs_single)


x = np.logspace(START_EXPONENT, 1.01*STOP_EXPONENT, 100)
y_cluster = np.exp(poly_cluster(np.log(x)))
y_single = np.exp(poly_single(np.log(x)))

# Total Time v.s. Number of Students
plt.plot(x, y_single)
plt.scatter(student_num, total_time_single)
plt.plot(x, y_cluster)
plt.scatter(student_num, total_time_cluster)

plt.ylim(-20, 550)
plt.xscale('log')
plt.xlabel('Number of Students')
plt.ylabel('Total Time (s)')
plt.title('Total Time v.s. Number of Students')

plt.savefig(os.path.join(BASE_DIR, 'benchmark.png'))
plt.clf()
