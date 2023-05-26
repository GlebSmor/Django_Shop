# Generated by Django 4.2.1 on 2023-05-24 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_tag_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['pk'], 'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterModelOptions(
            name='productimage',
            options={'ordering': ['pk'], 'verbose_name': 'ProductImage', 'verbose_name_plural': 'ProductImages'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['pk'], 'verbose_name': 'Review', 'verbose_name_plural': 'Reviews'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['pk'], 'verbose_name': 'Tag', 'verbose_name_plural': 'Tags'},
        ),
    ]
