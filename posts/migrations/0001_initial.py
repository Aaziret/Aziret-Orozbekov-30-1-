

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('create_data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='')),
                ('title', models.CharField(max_length=24)),
                ('description', models.TextField(blank=True, null=True)),
                ('rate', models.FloatField()),
                ('prize', models.FloatField(max_length=1000000)),
                ('create_data', models.DateTimeField(auto_now_add=True)),
                ('modified_data', models.DateTimeField(auto_now=True)),
                ('phone_number', models.FloatField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shops.category')),
            ],
        ),
    ]