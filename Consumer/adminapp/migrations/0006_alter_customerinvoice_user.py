# Generated by Django 4.2.10 on 2024-03-07 05:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0005_alter_invoice_status_customerinvoice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerinvoice',
            name='user',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
