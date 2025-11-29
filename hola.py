class Persona:
    def __init__(self, nombre, edad, ocupacion, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ocupacion = ocupacion
        self.ciudad = ciudad

    def __str__(self):
        return f"{self.nombre}, {self.edad} años, {self.ocupacion} de {self.ciudad}"


# Crear cinco personas
personas = [
    Persona("María García", 28, "Ingeniera de Software", "Madrid"),
    Persona("Carlos Rodríguez", 35, "Profesor", "Barcelona"),
    Persona("Ana Martínez", 42, "Doctora", "Valencia"),
    Persona("Luis Fernández", 31, "Arquitecto", "Sevilla"),
    Persona("Elena López", 26, "Diseñadora Gráfica", "Bilbao")
]

# Iterar e imprimir cada persona
print("Lista de personas:\n")
for persona in personas:
    print(persona)
