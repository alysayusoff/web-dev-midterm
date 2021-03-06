# Generated by Django 3.0.3 on 2021-12-26 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('genedata', '0005_auto_20211223_1511'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaxaLinkProtein',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('protein_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='genedata.Protein')),
                ('taxa_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='genedata.Taxonomy')),
            ],
        ),
    ]
