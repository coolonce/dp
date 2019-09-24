# Generated by Django 2.2.5 on 2019-09-21 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('abstractData', '0002_auto_20190921_1818'),
    ]

    operations = [
        migrations.CreateModel(
            name='Composition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('definitionid', models.IntegerField()),
                ('position', models.CharField(choices=[('Control', 'Control'), ('Quality', 'Quality')], default='Quality', max_length=10)),
            ],
            options={
                'unique_together': {('name', 'definitionid')},
            },
        ),
        migrations.CreateModel(
            name='Measurements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('rollenNumber', models.IntegerField()),
                ('value', models.FloatField()),
                ('composition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='abstractData.Composition')),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='abstractData.Machine')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='abstractData.Order')),
                ('parameter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='abstractData.Parameter')),
            ],
        ),
        migrations.AddIndex(
            model_name='measurements',
            index=models.Index(fields=['date'], name='abstractDat_date_0c86c2_idx'),
        ),
    ]