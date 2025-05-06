class Persona:

  def __init__(self, nombre, apellidos, numeroDocumentoIdentidad, anoNacimiento):
    self.nombre = nombre
    self.apellidos = apellidos
    self.numeroDocumentoIdentidad = numeroDocumentoIdentidad
    self.anoNacimiento = anoNacimiento
  
  def imprimir(self):
    print(f"Nombre = {self.nombre}")
    print(f"Apellidos = {self.apellidos}")
    print(f"Número de documento de identidad = {self.numeroDocumentoIdentidad}")
    print(f"Año de nacimiento = {self.anoNacimiento}")

if __name__ == "__main__":
  p1 = Persona("Pedro", "Pérez", "1053121010", 1998)
  p2 = Persona("Luis", "León", "1053223344", 2001)
  p1.imprimir()
  p2.imprimir()
