# Generated by Django 4.1.7 on 2023-11-10 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('updated', models.DateField(auto_now=True)),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('slug', models.SlugField(default=None)),
                ('prod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='product.product', verbose_name='product')),
            ],
            options={
                'ordering': ['-updated'],
            },
        ),
    ]