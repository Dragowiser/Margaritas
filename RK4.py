#Creamos el método de Runge- Kutta 4 para una ecuación diferencial a partir de una función
def Runge_Kutta4(f, y_0, h, nPasos):
    k_1 = h * f(y_0)
    k_2 = h * f(y_0 + h/2)