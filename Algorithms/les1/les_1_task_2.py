# 2. По введенным пользователем координатам двух точек вывести уравнение прямой
# вида y = kx + b, проходящей через эти точки.

def func_line(Xa, Ya, Xb, Yb):
    b = (Ya * Xb - Yb * Xa) / (Xb - Xa)
    k = (Yb - Ya) / (Xb - Xa)
    print(f'y = {k:.3f} * x + {b:.3f}')


if __name__ == '__main__':
    Ax, Ay = input('Введите координаты точки A через запятую, сначала x потом y: ').split(',')
    Bx, By = input('Введите координаты точки B через запятую, сначала x потом y: ').split(',')
    func_line(int(Ax), int(Ay), int(Bx), int(By))