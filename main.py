import nmrglue as ng
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# print(data)

dic, data = ng.jcampdx.read("2-PentanoneHNMR.jdx")

peaks, _ = find_peaks(data, prominence=0.1) # 10000 for CNMR, 0.1 fpr HNMR

plt.plot(data)
print(peaks)

plt.scatter(peaks, data[peaks], color="red", s=50, zorder=5, label="peaks")
plt.savefig("plot_1d.png") 

