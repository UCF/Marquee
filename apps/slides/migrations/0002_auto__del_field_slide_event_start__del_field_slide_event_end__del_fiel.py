# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Slide.event_start'
        db.delete_column('slides_slide', 'event_start')

        # Deleting field 'Slide.event_end'
        db.delete_column('slides_slide', 'event_end')

        # Deleting field 'Slide.location'
        db.delete_column('slides_slide', 'location')


    def backwards(self, orm):
        # Adding field 'Slide.event_start'
        db.add_column('slides_slide', 'event_start',
                      self.gf('django.db.models.fields.DateTimeField')(null=True),
                      keep_default=False)

        # Adding field 'Slide.event_end'
        db.add_column('slides_slide', 'event_end',
                      self.gf('django.db.models.fields.DateTimeField')(null=True),
                      keep_default=False)

        # Adding field 'Slide.location'
        db.add_column('slides_slide', 'location',
                      self.gf('django.db.models.fields.CharField')(default='', max_length='255', blank=True),
                      keep_default=False)


    models = {
        'slides.slide': {
            'Meta': {'object_name': 'Slide'},
            'additional': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'color_bg': ('django.db.models.fields.CharField', [], {'default': "'000000'", 'max_length': "'6'"}),
            'color_font': ('django.db.models.fields.CharField', [], {'default': "'EBB700'", 'max_length': "'6'"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2019, 10, 24, 0, 0)'}),
            'display_end': ('django.db.models.fields.DateField', [], {}),
            'display_start': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'font': ('django.db.models.fields.CharField', [], {'default': "'Gotham'", 'max_length': "'255'"}),
            'font_size': ('django.db.models.fields.IntegerField', [], {'default': '16'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'org': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'Pending'", 'max_length': "'16'"}),
            'text': ('django.db.models.fields.TextField', [], {'default': "'Event\\nDate\\nTime\\nLocation'"})
        }
    }

    complete_apps = ['slides']