# Generated by Django 5.1.2 on 2024-11-02 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Burgers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=999)),
            ],
        ),
    ]