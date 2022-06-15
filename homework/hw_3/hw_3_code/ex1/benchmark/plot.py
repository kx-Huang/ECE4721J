import os
import numpy as np
import matplotlib.pyplot as plt

BASE_DIR = "img/"
os.mkdir(BASE_DIR) if not os.path.exists(BASE_DIR) else None

START_EXPONENT = 3
STOP_EXPONENT = 8

student_num = [10**i for i in range(START_EXPONENT, STOP_EXPONENT+1)]

total_time_single = [4.088, 4.826, 5.189, 8.904, 55.917, 534]

total_time_java_1 = [28, 29, 26, 28, 38, 55]
total_time_java_2 = [27, 26, 25, 30, 33, 45]
total_time_java_3 = [27, 24, 26, 31, 33, 40]

total_time_streaming_1 = [25, 21, 21, 24, 47, 107]
total_time_streaming_2 = [21, 20, 22, 24, 40, 96]
total_time_streaming_3 = [22, 20, 23, 22, 45, 95]

total_time_java = []
for i in range(len(total_time_java_1)):
    total_time_java.append(
        (total_time_java_1[i] + total_time_java_2[i] + total_time_java_3[i])/3)

total_time_streaming = []
for i in range(len(total_time_streaming_1)):
    total_time_streaming.append(
        (total_time_streaming_1[i] + total_time_streaming_2[i] + total_time_streaming_3[i])/3)

############################### Java ###############################
coeffs = np.polyfit(np.log(student_num), np.log(total_time_java), deg=4)
poly = np.poly1d(coeffs)

x = np.logspace(START_EXPONENT, 1.01*STOP_EXPONENT, 100)
y = np.exp(poly(np.log(x)))

# Total Time v.s. Number of Students
plt.plot(x, y, 'orange')
plt.scatter(student_num, total_time_java)

plt.xscale('log')
plt.xlabel('Number of Records')
plt.ylabel('Total Time (s)')
plt.legend(['Apache Hadoop'])
plt.title('Total Time v.s. Number of Records')

plt.savefig(os.path.join(BASE_DIR, 'cluster-java.png'))
plt.clf()

######################## Java v.s. Streaming ########################
coeffs_java = np.polyfit(
    np.log(student_num), np.log(total_time_java), deg=3)
coeffs_streaming = np.polyfit(
    np.log(student_num), np.log(total_time_streaming), deg=3)
coeffs_single = np.polyfit(
    np.log(student_num), np.log(total_time_single), deg=3)

poly_java = np.poly1d(coeffs_java)
poly_streaming = np.poly1d(coeffs_streaming)
poly_single = np.poly1d(coeffs_single)


x = np.logspace(START_EXPONENT, 1.01*STOP_EXPONENT, 100)
y_java = np.exp(poly_java(np.log(x)))
y_streaming = np.exp(poly_streaming(np.log(x)))
y_single = np.exp(poly_single(np.log(x)))

# Total Time v.s. Number of Students
plt.plot(x, y_single)
plt.plot(x, y_java)
plt.plot(x, y_streaming)
plt.scatter(student_num, total_time_single)
plt.scatter(student_num, total_time_java)
plt.scatter(student_num, total_time_streaming)

plt.ylim(-20, 550)
plt.xscale('log')
plt.xlabel('Number of Records')
plt.ylabel('Total Time (s)')
plt.legend(['Regular Pipeline', 'Apache Hadoop', 'Hadoop Streaming'])
plt.title('Total Time v.s. Number of Records')

plt.savefig(os.path.join(BASE_DIR, 'benchmark.png'))
plt.clf()
