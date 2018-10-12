import matplotlib.pyplot as plt
import numpy as np

# x = np.linspace(0, 10, 1000)
# y = np.sin(x)+1
# z = np.cos(x ** 2)+1
# m=np.tan(x)+1
# plt.figure(figsize=(8, 4))
# plt.plot(x, y, label='$\sin x+1$', color='red', linewidth=2)
# plt.plot(x, z, 'b--', label='$\cos x^2+1$')
# plt.plot(x, m, 'y--', label='$\ tan x+1$')
# plt.xlabel('Time(s) ')
# plt.ylabel('Volt')
# plt.title('A simple Example')
# plt.ylim(0,2.2)
# plt.legend()
# plt.show()

n = np.linspace(1, 100, 100)
y = (np.add(1, np.true_divide(1, n))) ** n
plt.plot(n, y, 'b--', label='$\ n (1 + 1/n)^n$')
plt.legend()
plt.show()
