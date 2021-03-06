# Generated by Django 2.2.4 on 2019-08-08 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_auto_20190808_1712'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_email', models.EmailField(max_length=255, verbose_name='Email')),
                ('subject', models.CharField(max_length=255, verbose_name='Nome')),
                ('message', models.TextField(verbose_name='Escreva sua mensagem')),
            ],
        ),
        migrations.DeleteModel(
            name='Parceiro',
        ),
    ]
