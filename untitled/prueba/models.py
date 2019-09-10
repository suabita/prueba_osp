from django.db import models

CHOICES = (
    ('a','a'),
    ('b','b'),
    ('c','c'),
    ('d','d'),

)
class Prueba(models.Model):
    pregunta_uno = models.CharField(verbose_name="pregunta uno", max_length=200)
    respuesta_uno_a = models.CharField(verbose_name="respuesta uno a", max_length=200)
    respuesta_uno_b = models.CharField(verbose_name="respuesta uno b", max_length=200)
    respuesta_uno_c = models.CharField(verbose_name="respuesta uno c", max_length=200)
    respuesta_uno_d = models.CharField(verbose_name="respuesta uno d", max_length=200)
    respuesta_correcta_uno = models.CharField(max_length=1, choices=CHOICES)
    pregunta_dos = models.CharField(verbose_name="pregunta dos", max_length=200)
    respuesta_dos_a = models.CharField(verbose_name="respuesta dos a", max_length=200)
    respuesta_dos_b = models.CharField(verbose_name="respuesta dos b", max_length=200)
    respuesta_dos_c = models.CharField(verbose_name="respuesta dos c", max_length=200)
    respuesta_dos_d = models.CharField(verbose_name="respuesta dos d", max_length=200)
    respuesta_correcta_dos = models.CharField(max_length=1, choices=CHOICES)
    pregunta_tres = models.CharField(verbose_name="pregunta tres", max_length=200)
    respuesta_tres_a = models.CharField(verbose_name="respuesta tres a", max_length=200)
    respuesta_tres_b = models.CharField(verbose_name="respuesta tres b", max_length=200)
    respuesta_tres_c = models.CharField(verbose_name="respuesta tres c", max_length=200)
    respuesta_tres_d = models.CharField(verbose_name="respuesta tres d", max_length=200)
    respuesta_correcta_tres = models.CharField(max_length=1, choices=CHOICES)
    pregunta_cuatro = models.CharField(verbose_name="pregunta cuatro", max_length=200)
    respuesta_cuatro_a = models.CharField(verbose_name="respuesta cuatro a", max_length=200)
    respuesta_cuatro_b = models.CharField(verbose_name="respuesta cuatro b", max_length=200)
    respuesta_cuatro_c = models.CharField(verbose_name="respuesta cuatro c", max_length=200)
    respuesta_cuatro_d = models.CharField(verbose_name="respuesta cuatro d", max_length=200)
    respuesta_correcta_cuatro = models.CharField(max_length=1, choices=CHOICES)
    pregunta_cinco = models.CharField(verbose_name="pregunta cinco", max_length=200)
    respuesta_cinco_a = models.CharField(verbose_name="respuesta cinco a", max_length=200)
    respuesta_cinco_b = models.CharField(verbose_name="respuesta cinco b", max_length=200)
    respuesta_cinco_c = models.CharField(verbose_name="respuesta cinco c", max_length=200)
    respuesta_cinco_d = models.CharField(verbose_name="respuesta cinco d", max_length=200)
    respuesta_correcta_cinco = models.CharField(max_length=1, choices=CHOICES)











