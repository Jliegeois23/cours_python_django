# Generated by Django 4.0.4 on 2022-04-13 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lycee', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cursus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='aucun', max_length=50, null=True)),
                ('year_from_bac', models.SmallIntegerField(default=0, help_text='year since le bac', null=True, verbose_name='year')),
                ('scholar_year', models.CharField(default='0000-00001', max_length=9, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='comments',
            field=models.CharField(blank=True, default='', help_text='some comments about the student', max_length=255, verbose_name='comments'),
        ),
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(default='x@y.z', help_text='phone number of the student', max_length=255, verbose_name='email'),
        ),
        migrations.AddField(
            model_name='student',
            name='last_name',
            field=models.CharField(default='???', help_text='last name of the student', max_length=255, verbose_name='lastname'),
        ),
        migrations.AddField(
            model_name='student',
            name='phone',
            field=models.CharField(default='0999999999', help_text='phone number of the student', max_length=10, verbose_name='phonenumber'),
        ),
        migrations.AddField(
            model_name='student',
            name='cursus',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lycee.cursus'),
        ),
    ]