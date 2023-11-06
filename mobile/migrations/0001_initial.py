# Generated by Django 3.2 on 2023-11-06 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('tag', models.CharField(max_length=250)),
                ('price', models.IntegerField(default=100)),
                ('rating', models.IntegerField(default=0)),
            ],
        ),
    ]