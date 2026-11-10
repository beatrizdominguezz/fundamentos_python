"""
Crea tres variables con el nombre de una pelicula, un videojuego y una asignatura. Muestralas
con print() a una de ellas.
"""

nombre_pelicula = input("Ingrese nombre de una pelicula que te haya gustado:")
nombre_videojuego = input("Ingrese nombre de un videojuego que hayas jugado:")
nombre_asignatura = input("Ingrese nombre de tu asignatura preferida:")

print(f"""Pelicula favorita elegida: {nombre_pelicula}
    videojuego elegido: {nombre_videojuego}
    asignatura elegida: {nombre_asignatura}
    tipo de valor: {type(nombre_asignatura)}""")

"""
ya se me olvido, pero era algo de precio, promedio y temperatura jajaja
"""
precio = 12990.50
temperatura = 22.4
promedio = 6.8

print(precio)
print(temperatura)
print(promedio)
print(type(precio))
print(type(promedio))

"""
vas a trabajar con valores booleanos (True o False). Es súper importante que comiencen con mayúscula y 
vayan sin comillas para que Python reconozca que son del tipo booleano y no simple texto.
"""
tienes_internet = True
terminaste_tarea = False
tienes_clases_manana = True

print(tienes_internet)
print(terminaste_tarea)
print(tienes_clases_manana)

print(type(tienes_internet))