# Generated by Django 3.1.3 on 2020-12-09 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
