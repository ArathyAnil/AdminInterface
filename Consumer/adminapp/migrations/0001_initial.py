# Generated by Django 4.2.10 on 2024-02-22 12:22

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
                ('Address', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('amount', models.FloatField(blank=True, default=0.0, null=True)),
                ('Status', models.CharField(choices=[('Unpaid', 'Unpaid'), ('Paid', 'Paid'), ('Cancelled', 'Cancelled')], default='Unpaid', max_length=10)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_invoice', to='adminapp.customer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin_invoice', to='adminapp.user')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin_customer', to='adminapp.user'),
        ),
    ]
