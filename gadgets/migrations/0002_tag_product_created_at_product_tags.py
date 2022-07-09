# Generated by Django 4.0.6 on 2022-07-09 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gadgets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(related_name='products', to='gadgets.tag', verbose_name='Tags'),
        ),
    ]
