# Generated by Django 3.0.3 on 2020-03-25 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Namecard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
    ]
