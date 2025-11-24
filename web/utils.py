def slice_list(my_list, limit):
    ''' Funcion utilitaria que divide una lista en slices de largo limit, el ultimo slice puede tener un largo inferior'''
    return [my_list[index:index+limit] for index in range(0,len(my_list),limit)]

def calificacion_promedio(calificaciones):
    promedio = None
    if calificaciones:
        promedio = sum(calificaciones) / len(calificaciones)

    return promedio
