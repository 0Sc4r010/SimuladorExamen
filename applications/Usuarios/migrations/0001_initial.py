# Generated by Django 5.1 on 2024-09-26 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=100, verbose_name='Apellidos y nombres')),
                ('Correo', models.EmailField(max_length=254, unique=True)),
                ('Contraseña', models.CharField(max_length=15, verbose_name='contraseña')),
                ('Rol', models.CharField(choices=[('A', 'Administrador'), ('O', 'Orientador'), ('D', 'Docente'), ('E', 'Estudinta')], max_length=1, verbose_name='Roles')),
                ('Fecha_Registro', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
