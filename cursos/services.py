from cursos.models import Profesor, Curso, Estudiante, Direccion


def crear_profesor(rut, nombre, apellido, activo, creado_por):
    profesor = Profesor(rut=rut, nombre=nombre, apellido=apellido, activo=activo, creado_por=creado_por)
    profesor.save()
    print(f"Se ha creado el nuevo profesor {profesor.nombre}\n")
    return profesor


def crear_curso(codigo, nombre, version):
    curso = Curso(codigo=codigo, nombre=nombre, version=version)
    curso.save()
    print(f"Se ha creado el nuevo curso {curso.nombre}\n")
    return curso


def crear_estudiante(rut, nombre, apellido, fecha_nac, activo, creado_por):
    estudiante = Estudiante(rut=rut, nombre=nombre, apellido=apellido, fecha_nac=fecha_nac, activo=activo, creado_por=creado_por)
    estudiante.save()
    print(f"Se ha creado el nuevo estudiante {estudiante.nombre}\n")
    return estudiante


def crear_direccion(calle, numero, depto, comuna, ciudad, region, estudiante_id):
    estudiante = Estudiante.objects.get(rut=estudiante_id)
    direccion = Direccion(calle=calle, numero=numero, depto=depto, comuna=comuna, ciudad=ciudad, region=region, estudiante_id=estudiante)
    direccion.save()
    print(f"Se ha creado la nueva dirección {direccion.calle} {direccion.numero}\n")
    return direccion


def obtiene_estudiante(estudiante):
    return Estudiante.objects.get(rut=estudiante)


def obtiene_profesor(profesor):
    return Profesor.objects.get(rut=profesor)


def obtiene_curso(curso):
    return Curso.objects.get(codigo=curso)


def agrega_profesor_a_curso(agrega_profesor, agrega_curso):
    curso = Curso.objects.get(codigo=agrega_curso)
    profesor = Profesor.objects.get(rut=agrega_profesor)
    curso.profesor_id.add(profesor)
    print(f"Se ha asignado el profesor {profesor.nombre} {profesor.apellido} al curso {curso.nombre}\n")
    return profesor


def agrega_cursos_a_estudiante(agrega_curso, agrega_estudiante):
    estudiante = Estudiante.objects.get(rut=agrega_estudiante)
    curso = Curso.objects.get(codigo=agrega_curso)
    estudiante.curso_id.add(curso)
    print(f"Se ha asignado el curso {curso.nombre} al estudiante {estudiante.nombre} {estudiante.apellido}\n")
    return estudiante


def imprime_estudiante_cursos():
    lista_estudiantes = Estudiante.objects.all()
    for estudiante in lista_estudiantes:
        print(f'-Estudiante: {estudiante.nombre} {estudiante.apellido}, rut: {estudiante.rut}, fecha de nacimiento {estudiante.fecha_nac}, {"activo" if estudiante.activo == True else "no activo"}, creado el {estudiante.creacion_registro}.')
        if estudiante.curso_id.count() == 0:
            print('---No tiene cursos asignados.')
        else:
            lista_cursos = estudiante.curso_id.all()
            print(f'---Tiene los siguientes cursos asignados: ')
            for curso in lista_cursos:
                print(f'-----{curso.nombre}, Version {curso.version}.')
                if curso.profesor_id.count() == 0:
                    print('-----El curso no tiene profesor asignado.')
                else:
                    profesor = curso.profesor_id.all()[0]
                    print(f'-----El profesor del curso es: {profesor.nombre} {profesor.apellido}.')
