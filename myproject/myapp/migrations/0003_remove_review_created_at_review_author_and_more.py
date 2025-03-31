# Generated by Django 5.1.7 on 2025-03-31 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='created_at',
        ),
        migrations.AddField(
            model_name='review',
            name='author',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.PositiveIntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.TextField(),
        ),
    ]
