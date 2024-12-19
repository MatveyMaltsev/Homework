import numpy as np
import matplotlib.pyplot as plt

m = 5  
v = np.linspace(0, 10, 100)  
ke = 0.5 * m * v**2  

plt.figure(figsize=(10, 6))
plt.plot(v, ke, label='KE = 0.5 * m * v^2', color='red', linewidth=2)
plt.title('Зависимость кинетической энергии от скорости', fontsize=16)
plt.xlabel('Скорость (м/с)', fontsize=14)
plt.ylabel('Кинетическая энергия (Дж)', fontsize=14)
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.legend()
plt.xlim(0, 10)
plt.ylim(0, 0.5 * m * 10**2)
plt.show()
