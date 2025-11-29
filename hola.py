class Persona:
    def __init__(self, nombre, edad, ocupacion, ciudad, color_favorito):
        self.nombre = nombre
        self.edad = edad
        self.ocupacion = ocupacion
        self.ciudad = ciudad
        self.color_favorito = color_favorito

    def __str__(self):
        return f"{self.nombre}, {self.edad} años, {self.ocupacion} de {self.ciudad}, color favorito: {self.color_favorito}"


# Crear cinco personas
personas = [
    Persona("María García", 28, "Ingeniera de Software", "Madrid", "Azul"),
    Persona("Carlos Rodríguez", 35, "Profesor", "Barcelona", "Verde"),
    Persona("Ana Martínez", 42, "Doctora", "Valencia", "Rojo"),
    Persona("Luis Fernández", 31, "Arquitecto", "Sevilla", "Naranja"),
    Persona("Elena López", 26, "Diseñadora Gráfica", "Bilbao", "Morado")
]

# Iterar e imprimir cada persona
print("Lista de personas:\n")
for persona in personas:
    print(persona)
