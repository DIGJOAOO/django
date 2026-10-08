from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FotoPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='posts/%Y/%m/', verbose_name='Foto')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fotos', to='blogapp.post')),
            ],
            options={
                'verbose_name': 'foto',
                'verbose_name_plural': 'fotos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_key', models.CharField(max_length=40)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='blogapp.post')),
            ],
            options={
                'constraints': [models.UniqueConstraint(fields=('post', 'session_key'), name='like_unico_por_sesion')],
            },
        ),
    ]
