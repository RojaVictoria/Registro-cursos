from django.db import models


class Profesor(models.Model):
    rut = models.CharField(max_length=9, null=False, primary_key=True)
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField(auto_now_add=True)
    modificacion_registro = models.DateField(auto_now=True)
    creado_por = models.CharField(max_length=50)


class Curso(models.Model):
    codigo = models.CharField(max_length=10, null=False, unique=True, primary_key=True)
    nombre = models.CharField(max_length=50, null=False)
    version = models.IntegerField()
    profesor_id = models.ManyToManyField(Profesor, related_name='cursos')


class Estudiante(models.Model):
    rut = models.CharField(max_length=9, null=False, primary_key=True)
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    fecha_nac = models.DateField(null=False)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField(auto_now_add=True)
    modificacion_registro = models.DateField(auto_now=True)
    creado_por = models.CharField(max_length=50)
    curso_id = models.ManyToManyField(Curso, related_name='estudiantes')


class Direccion(models.Model):
    calle = models.CharField(max_length=50, null=False)
    numero = models.CharField(max_length=10, null=False)
    depto = models.CharField(max_length=10)
    comuna = models.CharField(max_length=50, null=False)
    ciudad = models.CharField(max_length=50, null=False)
    region = models.CharField(max_length=50, null=False)
    estudiante_id = models.OneToOneField(Estudiante, on_delete=models.CASCADE, null=False,  unique=True)
