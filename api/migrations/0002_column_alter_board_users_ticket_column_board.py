# Generated by Django 4.1.7 on 2023-03-03 01:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.AlterField(
            model_name='board',
            name='users',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.CharField(blank=True, max_length=300)),
                ('column', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.column')),
            ],
        ),
        migrations.AddField(
            model_name='column',
            name='board',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.board'),
        ),
    ]