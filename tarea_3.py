# Definir una clase llamada animal con 3 atributos y 1 método cualquiera
class Animalx:
    def __init__(self, especie, edad, habitat):
        self.especie = especie
        self.edad = edad
        self.habitat = habitat

    def mostrar_infor(self):
        return f"Tengo un animal y es un {self.especie}, tiene {self.edad} años y duerme en mi {self.habitat}."

class Mascota(Animalx):
    def __init__(self, especie, edad, habitat, nombre, color):
        super().__init__(especie, edad, habitat)
        self.nombre = nombre
        self.color = color

    def mostrar_informacion_completa(self):
        return f"{super().mostrar_infor()} Se llama {self.nombre} y es de color {self.color}."

animaly = Animalx("conejo", 2, "cama")
print(animaly.mostrar_infor())

mascota = Mascota("Perro", 3, "Casa", "firulay", "cafe clarito")
print(mascota.mostrar_informacion_completa())