# Generated by Django 4.0.1 on 2022-01-31 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0003_folder_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='folder',
            old_name='comment',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='document',
            name='description',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='document',
            name='type',
            field=models.CharField(choices=[('1', 'Type 1'), ('2', 'Type 2'), ('3', 'Type 3')], default='1', max_length=5),
        ),
        migrations.AlterField(
            model_name='document',
            name='value',
            field=models.IntegerField(default=0),
        ),
    ]