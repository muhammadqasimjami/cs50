# Generated by Django 3.0.2 on 2020-02-01 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=65)),
                ('last', models.CharField(max_length=65)),
                ('flights', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='passengers', to='flights.Flight')),
            ],
        ),
    ]