# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SourceFeed'
        db.create_table(u'storage_sourcefeed', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('stock_symbol', self.gf('django.db.models.fields.CharField')(max_length=20, db_index=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=200, db_index=True)),
        ))
        db.send_create_signal(u'storage', ['SourceFeed'])

        # Adding model 'News'
        db.create_table(u'storage_news', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sourcefeed', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['storage.SourceFeed'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('published_datetime', self.gf('django.db.models.fields.DateTimeField')()),
            ('retweets', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'storage', ['News'])


    def backwards(self, orm):
        # Deleting model 'SourceFeed'
        db.delete_table(u'storage_sourcefeed')

        # Deleting model 'News'
        db.delete_table(u'storage_news')


    models = {
        u'storage.news': {
            'Meta': {'object_name': 'News'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'published_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'retweets': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sourcefeed': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['storage.SourceFeed']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'storage.sourcefeed': {
            'Meta': {'object_name': 'SourceFeed'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'stock_symbol': ('django.db.models.fields.CharField', [], {'max_length': '20', 'db_index': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'db_index': 'True'})
        }
    }

    complete_apps = ['storage']