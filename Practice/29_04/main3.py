import numpy as np
import matplotlib.pyplot as plt

departments = ['HR', 'Sales', 'IT', 'Marketing']
budget = np.random.randint(10, 51, size=len(departments))

explode = [0] * len(departments)
explode[int(np.argmin(budget))] = 0.1
plt.pie(budget, labels=departments, autopct='%1.1f%%', explode=explode)

plt.title('Кругова діаграма')
plt.axis('equal')

plt.show()