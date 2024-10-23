# Generated by Django 5.1 on 2024-09-26 02:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Preguntas', '0001_initial'),
        ('Usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Respuestas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Código_Opción', models.CharField(max_length=1, verbose_name='respuesta')),
                ('Fecha_Respuesta', models.DateTimeField(auto_now=True)),
                ('ID_Pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Preguntas.preguntas')),
                ('ID_Usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuarios.usuarios')),
            ],
        ),
    ]