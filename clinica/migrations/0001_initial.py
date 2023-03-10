# Generated by Django 4.1.5 on 2023-01-14 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('crm', models.CharField(max_length=13)),
                ('email', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=20)),
                ('especialidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinica.especialidades')),
            ],
        ),
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('hora', models.CharField(choices=[('1', '07:00 ás 08:00'), ('2', '08:00 ás 09:00'), ('3', '09:00 ás 10:00'), ('4', '10:00 ás 11:00'), ('5', '11:00 ás 12:00')], max_length=10)),
                ('medico', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='clinica.medico')),
            ],
        ),
    ]
