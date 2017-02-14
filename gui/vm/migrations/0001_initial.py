# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-12 21:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import freenasUI.freeadmin.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dtype', models.CharField(choices=[(b'NIC', 'Network Interface'), (b'DISK', 'Disk'), (b'CDROM', 'CD-ROM'), (b'VNC', 'VNC')], max_length=50, verbose_name='Type')),
                ('attributes', freenasUI.freeadmin.models.fields.DictField(editable=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('description', models.CharField(blank=True, max_length=250, verbose_name='Description')),
                ('vcpus', models.IntegerField(default=1, verbose_name='Virtual CPUs')),
                ('memory', models.IntegerField(verbose_name='Memory Size (MiB)')),
                ('bootloader', models.CharField(choices=[(b'UEFI', 'UEFI'), (b'UEFI_CSM', 'UEFI-CSM')], default=b'UEFI', max_length=50, verbose_name='Boot Loader')),
            ],
            options={
                'verbose_name': 'VM',
                'verbose_name_plural': 'VMs',
            },
        ),
        migrations.AddField(
            model_name='device',
            name='vm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vm.VM', verbose_name='VM'),
        ),
    ]
