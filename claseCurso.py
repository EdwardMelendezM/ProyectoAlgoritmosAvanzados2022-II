class ClaseCurso:
    def __init__(self,codAsignatura,nombre,docente,horario):
        self.codAsignatura=codAsignatura
        self.nombre=nombre
        self.docente=docente
        self.horario=horario
    def mostrar(self):
        print(f'{self.codAsignatura} {self.nombre} {self.docente} {self.horario}')
