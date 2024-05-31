import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi


RED = "\33[91m"
GREEN = "\033[32m"
RESET = "\033[0m"
YELLOW = "\033[33m"

a = 0  # Нижня межа
b = 2  # Верхня межа

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2


def grafic(random_x, random_y):
    # Створення діапазону значень для x
    x = np.linspace(-0.5, 2.5, 400)
    y = f(x)

    # Створення графіка
    fig, ax = plt.subplots()

    # Малювання функції
    ax.plot(x, y, 'r', linewidth=2)
    ax.scatter(random_x, random_y, color= 'red')

    # Заповнення області під кривою
    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)

    # Налаштування графіка
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')

    # Додавання меж інтегрування та назви графіка
    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')
    ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
    plt.grid()
    plt.show()

def is_inside(a, b, x, y):
    return y <= (b / a) * x

def monte_carlo(a,b,num):
    random_x = np.random.uniform(a,b, num)
    random_y = np.random.uniform(0,f(b), num)
    points = []
    w = b - a
    h = (b - a)**2
    i = 0
    
    while i < num:
        point = [random_x[i],random_y[i]]
        points.append(point)
        i+=1
    
    inside_points = [point for point in points if is_inside(w, h, point[0], point[1])]

    
    N = len(points)
    M = len(inside_points)
    Sm = (M / N) * (w * h)

    result, error = spi.quad(f,a,b)

    print(f'''
Squre of shape under the curve by method {GREEN}Monte Carlo{RESET} is: {RED}{Sm}{RESET}
Squre of shape under the curve by {GREEN}quad{RESET} function is: {RED}{result}{RESET}
''' )
    grafic(random_x, random_y)

for num in [10,100,1000]:
    monte_carlo(a,b,num)

print(f'''{YELLOW}
Method Monte Carlo is based on statistical random selection, 
that's why it needs big count of random data to get more accurate results, 
but it can be used to get indicative results quickly.
      {RESET}''')

