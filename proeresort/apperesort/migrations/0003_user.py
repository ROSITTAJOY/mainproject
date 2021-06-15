# Generated by Django 3.2 on 2021-04-29 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apperesort', '0002_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('pincode', models.IntegerField()),
                ('email', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('photo', models.FileField(upload_to='')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apperesort.state')),
            ],
        ),
    ]