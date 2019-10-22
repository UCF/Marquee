# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Slide'
        db.create_table('slides_slide', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2019, 10, 22, 0, 0))),
            ('text', self.gf('django.db.models.fields.TextField')(default='Text to display')),
            ('font', self.gf('django.db.models.fields.CharField')(default='Gotham', max_length='255')),
            ('font_size', self.gf('django.db.models.fields.IntegerField')(default=16)),
            ('color_bg', self.gf('django.db.models.fields.CharField')(default='000000', max_length='6')),
            ('color_font', self.gf('django.db.models.fields.CharField')(default='EBB700', max_length='6')),
            ('display_start', self.gf('django.db.models.fields.DateField')()),
            ('display_end', self.gf('django.db.models.fields.DateField')()),
            ('event_start', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('event_end', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length='255', blank=True)),
            ('org', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('additional', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(default='Pending', max_length='16')),
        ))
        db.send_create_signal('slides', ['Slide'])


    def backwards(self, orm):
        # Deleting model 'Slide'
        db.delete_table('slides_slide')


    models = {
        'slides.slide': {
            'Meta': {'object_name': 'Slide'},
            'additional': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'color_bg': ('django.db.models.fields.CharField', [], {'default': "'000000'", 'max_length': "'6'"}),
            'color_font': ('django.db.models.fields.CharField', [], {'default': "'EBB700'", 'max_length': "'6'"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2019, 10, 22, 0, 0)'}),
            'display_end': ('django.db.models.fields.DateField', [], {}),
            'display_start': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'event_end': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'event_start': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'font': ('django.db.models.fields.CharField', [], {'default': "'Gotham'", 'max_length': "'255'"}),
            'font_size': ('django.db.models.fields.IntegerField', [], {'default': '16'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': "'255'", 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'org': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'Pending'", 'max_length': "'16'"}),
            'text': ('django.db.models.fields.TextField', [], {'default': "'Text to display'"})
        }
    }

    complete_apps = ['slides']