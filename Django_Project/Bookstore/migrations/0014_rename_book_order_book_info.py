# Generated by Django 4.1.5 on 2023-01-15 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bookstore', '0013_rename_book_info_order_book'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='book',
            new_name='book_info',
        ),
    ]