# Generated by Django 4.0.4 on 2022-05-03 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_alter_menuitem_imagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='cep',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='pedido',
            name='cidade',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='pedido',
            name='estado',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='pedido',
            name='nome',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='pedido',
            name='rua',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]