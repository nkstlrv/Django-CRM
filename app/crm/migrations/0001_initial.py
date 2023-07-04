# Generated by Django 4.2.2 on 2023-07-04 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('age', models.PositiveIntegerField(max_length=150)),
                ('email', models.EmailField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
            ],
        ),
    ]
