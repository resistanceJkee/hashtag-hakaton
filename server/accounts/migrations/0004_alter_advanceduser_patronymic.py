# Generated by Django 3.2.8 on 2021-10-09 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_advanceduser_patronymic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advanceduser',
            name='patronymic',
            field=models.CharField(blank=True, max_length=50, verbose_name='Отчество'),
        ),
    ]
