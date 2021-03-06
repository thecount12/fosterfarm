# Generated by Django 2.2.3 on 2019-08-02 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supply', '0002_remove_distillate_strain_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cartridge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=60)),
                ('cartridge_model', models.CharField(blank=True, max_length=60)),
                ('cartridge_type', models.CharField(blank=True, max_length=60)),
                ('sourced_from', models.CharField(blank=True, max_length=60)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, help_text='cartridge review', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='distillate',
            name='unknown',
            field=models.TextField(blank=True, help_text='unknown elements in distillate', null=True),
        ),
    ]
