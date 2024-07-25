# Generated by Django 5.0.7 on 2024-07-21 10:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_alter_networkchain_debt_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='networkchain',
            name='contacts',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='application.contact', verbose_name='Контакты'),
        ),
        migrations.AddField(
            model_name='networkchain',
            name='products',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='application.product', verbose_name='Продукты'),
        ),
    ]
