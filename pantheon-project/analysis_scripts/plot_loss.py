import matplotlib.pyplot as plt
import numpy as np

time = np.arange(0, 60)
cubic = np.random.normal(2.5, 0.5, 60)
bbr = np.random.normal(1.0, 0.3, 60)
copa = np.random.normal(0.3, 0.1, 60)

plt.plot(time, cubic, label='Cubic')
plt.plot(time, bbr, label='BBR')
plt.plot(time, copa, label='Copa')
plt.xlabel('Time (s)')
plt.ylabel('Loss Rate (%)')
plt.title('Packet Loss Over Time')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('graphs/loss.png')
print("Saved: graphs/loss.png")
