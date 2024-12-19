import numpy as np
import matplotlib.pyplot as plt

# Пример данных: 
days = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
prices = np.array([30000, 31000, 32000, 31500, 33000, 34000, 35000, 34500, 36000, 37000])

degree = 3
coefficients = np.polyfit(days, prices, degree)
polynomial = np.poly1d(coefficients)

days_fit = np.linspace(days.min(), days.max(), 200)
prices_fit = polynomial(days_fit)

plt.figure(figsize=(12, 6))
plt.plot(days, prices, 'o', label='Фактическая цена', color='blue')
plt.plot(days_fit, prices_fit, label=f'Полином степени {degree}', color='red', linewidth=2)
plt.title('Аппроксимация цены биткоина', fontsize=16)
plt.xlabel('Дни', fontsize=14)
plt.ylabel('Цена (USD)', fontsize=14)
plt.grid(True)
plt.legend()
plt.show()
