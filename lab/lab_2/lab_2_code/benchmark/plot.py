import os
import numpy as np
import matplotlib.pyplot as plt

BASE_DIR = "img/"

START_EXPONENT = 3
STOP_EXPONENT = 8

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
