# Generated by Django 4.2.2 on 2023-07-07 15:55

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0003_empleado_avatar_empleado_habilidades'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='hoja_vida',
            field=ckeditor.fields.RichTextField(default='Texto'),
            preserve_default=False,
        ),
    ]
