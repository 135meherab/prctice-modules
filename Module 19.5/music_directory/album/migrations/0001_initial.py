# Generated by Django 4.2.7 on 2023-12-18 05:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('musician', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=80)),
                ('released_date', models.DateTimeField()),
                ('rating', models.CharField(choices=[('1', 'ONE'), ('2', 'TWO'), ('3', 'THREE'), ('4', 'FOUR'), ('5', 'FIVE')], max_length=10)),
                ('musician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musician.musician')),
            ],
        ),
    ]