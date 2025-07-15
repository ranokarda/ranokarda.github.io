import numpy as np
import matplotlib.pyplot as plt


x = np.array([1, 2, 3, 4, 5, 6, 7])
y = np.array([32, 35, 39, 45, 51, 54, 60])

x_mean = np.mean(x)
y_mean = np.mean(y)

numerator = np.sum((x-x_mean)*(y-y_mean))
denominator = np.sum((x-x_mean)**2)

w = numerator/denominator
b = y_mean-(w*x_mean)

x_new = 8
y_pred = (w*x_new)+b

x = np.append(x, x_new)
y = np.append(y, y_pred)



plt.scatter(x[:-1], y[:-1], label='Données')  # Points originaux
plt.scatter(x[-1], y[-1], color='green', label='Prédiction (8 ans)')  # Point prédit
plt.plot(x, y, color='red', label='Régression linéaire')  # Ligne de régression
plt.legend()
plt.xlabel("Années d'expérience")
plt.ylabel("Salaire (k€)")
plt.title("Régression linéaire")
plt.grid()
plt.show()


x_line = np.linspace(0, 9, 100)
y_line = w * x_line + b

plt.scatter(x[:-1], y[:-1], label='Données')
plt.plot(x_line, y_line, color='red', label='Régression linéaire')
plt.scatter(x_new, y_pred, color='green', label='Prédiction (8 ans)')
plt.legend()
plt.show()
