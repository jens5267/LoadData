# Generated by Django 2.0.7 on 2020-03-18 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20200310_2013'),
    ]

    operations = [
        migrations.CreateModel(
            name='Load',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_input', models.FloatField()),
                ('second_input', models.FloatField()),
            ],
        ),
    ]
