# Generated by Django 5.1 on 2024-10-09 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Examenes', '0002_alter_categorias_options_alter_examenes_options'),
        ('Usuarios', '0002_usuarios_genero_usuarios_identificacion_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuarios',
            options={'ordering': ['Nombre'], 'verbose_name': 'Usuario', 'verbose_name_plural': 'Usuarios'},
        ),
        migrations.AddField(
            model_name='usuarios',
            name='Areas_evaluar',
            field=models.ManyToManyField(to='Examenes.categorias'),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='identificacion',
            field=models.CharField(max_length=20, unique=True, verbose_name='Documento de identidad'),
        ),
    ]
