# Generated by Django 2.2.4 on 2020-06-15 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('python_lotto_app', '0002_auto_20200608_0607'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lottoboard',
            name='id',
        ),
        migrations.AlterField(
            model_name='lottoboard',
            name='round',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]