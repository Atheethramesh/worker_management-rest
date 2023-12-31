# Generated by Django 4.2.5 on 2023-09-08 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='emp_img')),
                ('phone', models.IntegerField(max_length=10)),
                ('stime', models.TimeField(default='10:00:59')),
                ('etime', models.TimeField(default='16:00:59')),
                ('category', models.CharField(choices=[('feild work', 'Feild Work'), ('tree work', 'Tree Work'), ('plantation work', 'Plantation Work'), ('ferilizer', 'Ferilizer'), ('farmer tech', 'Farmer Tech'), ('cunstruction', 'Cunstruction')], max_length=100)),
            ],
        ),
    ]
