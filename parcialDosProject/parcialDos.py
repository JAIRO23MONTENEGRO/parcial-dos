#Declaracion de constantes
from statistics import median
def calularBonificacion(salarioBmensual, cargo_Empleado,nivel_desempeno):
    bonificacionDirectivoAlto=0.2
    bonificacionDirectivoMedio=0.1
    bonificacionOperativoAlto=0.15
    bonificacionOperativoMedio=0.05
    bonicacionBajo=0

    salarioBmensual = int(input('Salario base mensual: '))
    cargo_Empleado =input('Cargo empleado: ').lower()
    nivel_desempeno =input('Nivel de desempeño: ').lower()

    if cargo_Empleado=='directivo':
        if nivel_desempeno=='alto':
            bonificacion=bonificacionDirectivoAlto
        elif nivel_desempeno=='medio':
            bonificacion=bonificacionDirectivoMedio
        else:
            bonificacion=bonicacionBajo

    elif cargo_Empleado=='operativo':
        if nivel_desempeno=='alto':
            bonificacion=bonificacionOperativoAlto
        elif nivel_desempeno=='medio':
                bonificacion=bonificacionOperativoMedio
        else:
            bonificacion=bonicacionBajo
    else:
        bonificacion=bonicacionBajo

    calcularBonificacion=salarioBmensual*bonificacion
    total= salarioBmensual+calcularBonificacion
    
    return cargo_Empleado, nivel_desempeno,salarioBmensual,calcularBonificacion,total




def g_mensaje(cargo_Empleado,nivel_desempeno,salarioBmensual,calcularBonificacion,total):

     return(f'Cargo: {cargo_Empleado}\n'
      f'Nivel de desempeño: {nivel_desempeno}\n'
      f'Salario Base: ${salarioBmensual:.0f}\n'
      f'Bonificación ${calcularBonificacion:.0f}\n'
      f'Total a Recibir:${total:.0f}')










