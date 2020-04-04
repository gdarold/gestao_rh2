# Generated by Django 3.0.5 on 2020-04-04 02:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0003_auto_20200403_2322'),
        ('documentos', '0002_documento_pertence'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='pertence',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='funcionarios.Funcionario'),
            preserve_default=False,
        ),
    ]
