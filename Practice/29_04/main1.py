import numpy as np
import matplotlib.pyplot as plt

days = np.arange(1, 30)
visits = np.random.randint(100, 501, size=days.shape)

plt.plot(days, visits, marker='o', linestyle='-', color='b')

plt.title('Відвідуваність по днях')
plt.xlabel('Дні')
plt.ylabel('Кількість відвідувачів')
plt.grid(True)

plt.show()