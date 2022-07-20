from django.contrib import admin
from cursos.models import Profesor, Curso, Estudiante, Direccion


admin.site.register(Profesor)
admin.site.register(Curso)
admin.site.register(Estudiante)
admin.site.register(Direccion)
