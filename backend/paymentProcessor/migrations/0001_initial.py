# Generated by Django 4.1.3 on 2023-08-15 09:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_meta', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('order_id', models.CharField(max_length=100, unique=True)),
                ('order_amount', models.PositiveIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]