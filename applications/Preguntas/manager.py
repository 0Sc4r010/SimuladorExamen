from django.db import models

class PreguntaManager(models.Manager):
    
    def por_nivel(self, nivel):
        """
        Filtra las preguntas por el nivel de dificultad (Básico, Intermedio, Avanzado).
        """
        return self.filter(Nivel_Dificultad=nivel)

    def por_examen(self, examen_id):
        """
        Filtra las preguntas que pertenecen a un examen específico.
        """
        return self.filter(ID_Examen=examen_id)

    def todas(self):
        """
        Devuelve todas las preguntas sin filtro.
        """
        return self.all()

   