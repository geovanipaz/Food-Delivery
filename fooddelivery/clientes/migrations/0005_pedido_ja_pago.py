# Generated by Django 4.0.4 on 2022-05-04 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0004_pedido_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='ja_pago',
            field=models.BooleanField(default=False),
        ),
    ]
