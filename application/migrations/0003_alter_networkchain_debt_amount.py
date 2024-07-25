# Generated by Django 5.0.7 on 2024-07-21 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_remove_networkchain_contacts_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='networkchain',
            name='debt_amount',
            field=models.DecimalField(decimal_places=2, max_digits=30, verbose_name='Задолженность перед поставщиком'),
        ),
    ]
