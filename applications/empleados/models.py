from django.db import models
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField

# Create your models here.
class habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name='Habilidad'
        verbose_name_plural = 'Habilidades empleados'

    def __str__(self):
        return str(self.id) + '-' + self.habilidad

class Empleado (models.Model):

    JOB_CHOICES = (
    ('0', 'Contable'),
    ('1', 'Administrador'),
    ('2', 'Economista'),
    ('3', 'Otro'),
)


    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellidos', max_length=60)
    full_name= models.CharField('Nombre completo', max_length=120, blank=True)
    job = models.CharField('Trabajo', max_length=50, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='media/empleado', blank=True, null=True)
    habilidades = models.ManyToManyField(habilidades)
    hoja_vida=RichTextField(blank=True) 

    class Meta:
        verbose_name='Mi empleado'
        verbose_name_plural = 'Empleados de la empresa'
        ordering=['-first_name', 'last_name']
        unique_together = ('first_name', 'departamento')

    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name
