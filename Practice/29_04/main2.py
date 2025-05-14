import numpy as np
import matplotlib.pyplot as plt

channels = np.array(['Google', 'Facebook', 'Email', 'Referral'])
leads = np.random.randint(50, 201, size=channels.shape)

plt.bar(channels, leads, color='b')

plt.title('Стовпчаста діаграма')
plt.xlabel('Channels')
plt.ylabel('Leads')

plt.grid(axis='y')
plt.show()