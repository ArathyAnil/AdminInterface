# Generated by Django 4.2.10 on 2024-03-08 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0010_alter_testmodel_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testmodel',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
