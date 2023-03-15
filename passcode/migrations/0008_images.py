# Generated by Django 4.0.3 on 2023-03-14 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passcode', '0007_notice'),
    ]

    operations = [
        migrations.CreateModel(
            name='images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('images', models.ImageField(blank=True, null=True, upload_to='images')),
            ],
        ),
    ]