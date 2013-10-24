# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'GeneralAvail.mon_avail_start'
        db.delete_column(u'app_generalavail', 'mon_avail_start')

        # Deleting field 'GeneralAvail.tue_avail_stop'
        db.delete_column(u'app_generalavail', 'tue_avail_stop')

        # Deleting field 'GeneralAvail.last_updated'
        db.delete_column(u'app_generalavail', 'last_updated')

        # Deleting field 'GeneralAvail.thr_avail_start'
        db.delete_column(u'app_generalavail', 'thr_avail_start')

        # Deleting field 'GeneralAvail.fri_avail_stop'
        db.delete_column(u'app_generalavail', 'fri_avail_stop')

        # Deleting field 'GeneralAvail.mon_avail_stop'
        db.delete_column(u'app_generalavail', 'mon_avail_stop')

        # Deleting field 'GeneralAvail.thr_avail_stop'
        db.delete_column(u'app_generalavail', 'thr_avail_stop')

        # Deleting field 'GeneralAvail.sun_avail_stop'
        db.delete_column(u'app_generalavail', 'sun_avail_stop')

        # Deleting field 'GeneralAvail.sat_avail_stop'
        db.delete_column(u'app_generalavail', 'sat_avail_stop')

        # Deleting field 'GeneralAvail.wed_avail_start'
        db.delete_column(u'app_generalavail', 'wed_avail_start')

        # Deleting field 'GeneralAvail.fri_avail_start'
        db.delete_column(u'app_generalavail', 'fri_avail_start')

        # Deleting field 'GeneralAvail.tue_avail_start'
        db.delete_column(u'app_generalavail', 'tue_avail_start')

        # Deleting field 'GeneralAvail.sun_avail_start'
        db.delete_column(u'app_generalavail', 'sun_avail_start')

        # Deleting field 'GeneralAvail.sat_avail_start'
        db.delete_column(u'app_generalavail', 'sat_avail_start')

        # Deleting field 'GeneralAvail.wed_avail_stop'
        db.delete_column(u'app_generalavail', 'wed_avail_stop')

        # Adding field 'GeneralAvail.mon_early_morning'
        db.add_column(u'app_generalavail', 'mon_early_morning',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'GeneralAvail.tues_early_morning'
        db.add_column(u'app_generalavail', 'tues_early_morning',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'GeneralAvail.wed_early_morning'
        db.add_column(u'app_generalavail', 'wed_early_morning',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'GeneralAvail.thurs_early_morning'
        db.add_column(u'app_generalavail', 'thurs_early_morning',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'GeneralAvail.fri_early_morning'
        db.add_column(u'app_generalavail', 'fri_early_morning',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'GeneralAvail.sat_early_morning'
        db.add_column(u'app_generalavail', 'sat_early_morning',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'GeneralAvail.sun_early_morning'
        db.add_column(u'app_generalavail', 'sun_early_morning',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'GeneralAvail.mon_late_morning'
        db.add_column(u'app_generalavail', 'mon_late_morning',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'GeneralAvail.tues_late_morning'
        db.add_column(u'app_generalavail', 'tues_late_morning',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'GeneralAvail.wed_late_morning'
        db.add_column(u'app_generalavail', 'wed_late_morning',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'GeneralAvail.thurs_late_morning'
        db.add_column(u'app_generalavail', 'thurs_late_morning',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'GeneralAvail.fri_late_morning'
        db.add_column(u'app_generalavail', 'fri_late_morning',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'GeneralAvail.sat_late_morning'
        db.add_column(u'app_generalavail', 'sat_late_morning',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'GeneralAvail.sun_late_morning'
        db.add_column(u'app_generalavail', 'sun_late_morning',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'GeneralAvail.mon_early_afternoon'
        db.add_column(u'app_generalavail', 'mon_early_afternoon',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'GeneralAvail.tues_early_afternoon'
        db.add_column(u'app_generalavail', 'tues_early_afternoon',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'GeneralAvail.wed_early_afternoon'
        db.add_column(u'app_generalavail', 'wed_early_afternoon',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'GeneralAvail.thurs_early_afternoon'
        db.add_column(u'app_generalavail', 'thurs_early_afternoon',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'GeneralAvail.fri_early_afternoon'
        db.add_column(u'app_generalavail', 'fri_early_afternoon',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'GeneralAvail.sat_early_afternoon'
        db.add_column(u'app_generalavail', 'sat_early_afternoon',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'GeneralAvail.sun_early_afternoon'
        db.add_column(u'app_generalavail', 'sun_early_afternoon',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'GeneralAvail.mon_late_afternoon'
        db.add_column(u'app_generalavail', 'mon_late_afternoon',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'GeneralAvail.tues_late_afternoon'
        db.add_column(u'app_generalavail', 'tues_late_afternoon',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'GeneralAvail.wed_late_afternoon'
        db.add_column(u'app_generalavail', 'wed_late_afternoon',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'GeneralAvail.thurs_late_afternoon'
        db.add_column(u'app_generalavail', 'thurs_late_afternoon',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'GeneralAvail.fri_late_afternoon'
        db.add_column(u'app_generalavail', 'fri_late_afternoon',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'GeneralAvail.sat_late_afternoon'
        db.add_column(u'app_generalavail', 'sat_late_afternoon',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'GeneralAvail.sun_late_afternoon'
        db.add_column(u'app_generalavail', 'sun_late_afternoon',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'GeneralAvail.mon_early_evening'
        db.add_column(u'app_generalavail', 'mon_early_evening',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'GeneralAvail.tues_early_evening'
        db.add_column(u'app_generalavail', 'tues_early_evening',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'GeneralAvail.wed_early_evening'
        db.add_column(u'app_generalavail', 'wed_early_evening',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'GeneralAvail.thurs_early_evening'
        db.add_column(u'app_generalavail', 'thurs_early_evening',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'GeneralAvail.fri_early_evening'
        db.add_column(u'app_generalavail', 'fri_early_evening',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'GeneralAvail.sat_early_evening'
        db.add_column(u'app_generalavail', 'sat_early_evening',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'GeneralAvail.sun_early_evening'
        db.add_column(u'app_generalavail', 'sun_early_evening',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'GeneralAvail.mon_late_evening'
        db.add_column(u'app_generalavail', 'mon_late_evening',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'GeneralAvail.tues_late_evening'
        db.add_column(u'app_generalavail', 'tues_late_evening',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'GeneralAvail.wed_late_evening'
        db.add_column(u'app_generalavail', 'wed_late_evening',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'GeneralAvail.thurs_late_evening'
        db.add_column(u'app_generalavail', 'thurs_late_evening',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'GeneralAvail.fri_late_evening'
        db.add_column(u'app_generalavail', 'fri_late_evening',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'GeneralAvail.sat_late_evening'
        db.add_column(u'app_generalavail', 'sat_late_evening',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'GeneralAvail.sun_late_evening'
        db.add_column(u'app_generalavail', 'sun_late_evening',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'GeneralAvail.mon_overnight'
        db.add_column(u'app_generalavail', 'mon_overnight',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'GeneralAvail.tues_overnight'
        db.add_column(u'app_generalavail', 'tues_overnight',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'GeneralAvail.wed_overnight'
        db.add_column(u'app_generalavail', 'wed_overnight',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'GeneralAvail.thurs_overnight'
        db.add_column(u'app_generalavail', 'thurs_overnight',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'GeneralAvail.fri_overnight'
        db.add_column(u'app_generalavail', 'fri_overnight',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'GeneralAvail.sat_overnight'
        db.add_column(u'app_generalavail', 'sat_overnight',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'GeneralAvail.sun_overnight'
        db.add_column(u'app_generalavail', 'sun_overnight',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'GeneralAvail.mon_avail_start'
        raise RuntimeError("Cannot reverse this migration. 'GeneralAvail.mon_avail_start' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'GeneralAvail.tue_avail_stop'
        raise RuntimeError("Cannot reverse this migration. 'GeneralAvail.tue_avail_stop' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'GeneralAvail.last_updated'
        raise RuntimeError("Cannot reverse this migration. 'GeneralAvail.last_updated' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'GeneralAvail.thr_avail_start'
        raise RuntimeError("Cannot reverse this migration. 'GeneralAvail.thr_avail_start' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'GeneralAvail.fri_avail_stop'
        raise RuntimeError("Cannot reverse this migration. 'GeneralAvail.fri_avail_stop' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'GeneralAvail.mon_avail_stop'
        raise RuntimeError("Cannot reverse this migration. 'GeneralAvail.mon_avail_stop' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'GeneralAvail.thr_avail_stop'
        raise RuntimeError("Cannot reverse this migration. 'GeneralAvail.thr_avail_stop' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'GeneralAvail.sun_avail_stop'
        raise RuntimeError("Cannot reverse this migration. 'GeneralAvail.sun_avail_stop' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'GeneralAvail.sat_avail_stop'
        raise RuntimeError("Cannot reverse this migration. 'GeneralAvail.sat_avail_stop' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'GeneralAvail.wed_avail_start'
        raise RuntimeError("Cannot reverse this migration. 'GeneralAvail.wed_avail_start' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'GeneralAvail.fri_avail_start'
        raise RuntimeError("Cannot reverse this migration. 'GeneralAvail.fri_avail_start' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'GeneralAvail.tue_avail_start'
        raise RuntimeError("Cannot reverse this migration. 'GeneralAvail.tue_avail_start' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'GeneralAvail.sun_avail_start'
        raise RuntimeError("Cannot reverse this migration. 'GeneralAvail.sun_avail_start' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'GeneralAvail.sat_avail_start'
        raise RuntimeError("Cannot reverse this migration. 'GeneralAvail.sat_avail_start' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'GeneralAvail.wed_avail_stop'
        raise RuntimeError("Cannot reverse this migration. 'GeneralAvail.wed_avail_stop' and its values cannot be restored.")
        # Deleting field 'GeneralAvail.mon_early_morning'
        db.delete_column(u'app_generalavail', 'mon_early_morning')

        # Deleting field 'GeneralAvail.tues_early_morning'
        db.delete_column(u'app_generalavail', 'tues_early_morning')

        # Deleting field 'GeneralAvail.wed_early_morning'
        db.delete_column(u'app_generalavail', 'wed_early_morning')

        # Deleting field 'GeneralAvail.thurs_early_morning'
        db.delete_column(u'app_generalavail', 'thurs_early_morning')

        # Deleting field 'GeneralAvail.fri_early_morning'
        db.delete_column(u'app_generalavail', 'fri_early_morning')

        # Deleting field 'GeneralAvail.sat_early_morning'
        db.delete_column(u'app_generalavail', 'sat_early_morning')

        # Deleting field 'GeneralAvail.sun_early_morning'
        db.delete_column(u'app_generalavail', 'sun_early_morning')

        # Deleting field 'GeneralAvail.mon_late_morning'
        db.delete_column(u'app_generalavail', 'mon_late_morning')

        # Deleting field 'GeneralAvail.tues_late_morning'
        db.delete_column(u'app_generalavail', 'tues_late_morning')

        # Deleting field 'GeneralAvail.wed_late_morning'
        db.delete_column(u'app_generalavail', 'wed_late_morning')

        # Deleting field 'GeneralAvail.thurs_late_morning'
        db.delete_column(u'app_generalavail', 'thurs_late_morning')

        # Deleting field 'GeneralAvail.fri_late_morning'
        db.delete_column(u'app_generalavail', 'fri_late_morning')

        # Deleting field 'GeneralAvail.sat_late_morning'
        db.delete_column(u'app_generalavail', 'sat_late_morning')

        # Deleting field 'GeneralAvail.sun_late_morning'
        db.delete_column(u'app_generalavail', 'sun_late_morning')

        # Deleting field 'GeneralAvail.mon_early_afternoon'
        db.delete_column(u'app_generalavail', 'mon_early_afternoon')

        # Deleting field 'GeneralAvail.tues_early_afternoon'
        db.delete_column(u'app_generalavail', 'tues_early_afternoon')

        # Deleting field 'GeneralAvail.wed_early_afternoon'
        db.delete_column(u'app_generalavail', 'wed_early_afternoon')

        # Deleting field 'GeneralAvail.thurs_early_afternoon'
        db.delete_column(u'app_generalavail', 'thurs_early_afternoon')

        # Deleting field 'GeneralAvail.fri_early_afternoon'
        db.delete_column(u'app_generalavail', 'fri_early_afternoon')

        # Deleting field 'GeneralAvail.sat_early_afternoon'
        db.delete_column(u'app_generalavail', 'sat_early_afternoon')

        # Deleting field 'GeneralAvail.sun_early_afternoon'
        db.delete_column(u'app_generalavail', 'sun_early_afternoon')

        # Deleting field 'GeneralAvail.mon_late_afternoon'
        db.delete_column(u'app_generalavail', 'mon_late_afternoon')

        # Deleting field 'GeneralAvail.tues_late_afternoon'
        db.delete_column(u'app_generalavail', 'tues_late_afternoon')

        # Deleting field 'GeneralAvail.wed_late_afternoon'
        db.delete_column(u'app_generalavail', 'wed_late_afternoon')

        # Deleting field 'GeneralAvail.thurs_late_afternoon'
        db.delete_column(u'app_generalavail', 'thurs_late_afternoon')

        # Deleting field 'GeneralAvail.fri_late_afternoon'
        db.delete_column(u'app_generalavail', 'fri_late_afternoon')

        # Deleting field 'GeneralAvail.sat_late_afternoon'
        db.delete_column(u'app_generalavail', 'sat_late_afternoon')

        # Deleting field 'GeneralAvail.sun_late_afternoon'
        db.delete_column(u'app_generalavail', 'sun_late_afternoon')

        # Deleting field 'GeneralAvail.mon_early_evening'
        db.delete_column(u'app_generalavail', 'mon_early_evening')

        # Deleting field 'GeneralAvail.tues_early_evening'
        db.delete_column(u'app_generalavail', 'tues_early_evening')

        # Deleting field 'GeneralAvail.wed_early_evening'
        db.delete_column(u'app_generalavail', 'wed_early_evening')

        # Deleting field 'GeneralAvail.thurs_early_evening'
        db.delete_column(u'app_generalavail', 'thurs_early_evening')

        # Deleting field 'GeneralAvail.fri_early_evening'
        db.delete_column(u'app_generalavail', 'fri_early_evening')

        # Deleting field 'GeneralAvail.sat_early_evening'
        db.delete_column(u'app_generalavail', 'sat_early_evening')

        # Deleting field 'GeneralAvail.sun_early_evening'
        db.delete_column(u'app_generalavail', 'sun_early_evening')

        # Deleting field 'GeneralAvail.mon_late_evening'
        db.delete_column(u'app_generalavail', 'mon_late_evening')

        # Deleting field 'GeneralAvail.tues_late_evening'
        db.delete_column(u'app_generalavail', 'tues_late_evening')

        # Deleting field 'GeneralAvail.wed_late_evening'
        db.delete_column(u'app_generalavail', 'wed_late_evening')

        # Deleting field 'GeneralAvail.thurs_late_evening'
        db.delete_column(u'app_generalavail', 'thurs_late_evening')

        # Deleting field 'GeneralAvail.fri_late_evening'
        db.delete_column(u'app_generalavail', 'fri_late_evening')

        # Deleting field 'GeneralAvail.sat_late_evening'
        db.delete_column(u'app_generalavail', 'sat_late_evening')

        # Deleting field 'GeneralAvail.sun_late_evening'
        db.delete_column(u'app_generalavail', 'sun_late_evening')

        # Deleting field 'GeneralAvail.mon_overnight'
        db.delete_column(u'app_generalavail', 'mon_overnight')

        # Deleting field 'GeneralAvail.tues_overnight'
        db.delete_column(u'app_generalavail', 'tues_overnight')

        # Deleting field 'GeneralAvail.wed_overnight'
        db.delete_column(u'app_generalavail', 'wed_overnight')

        # Deleting field 'GeneralAvail.thurs_overnight'
        db.delete_column(u'app_generalavail', 'thurs_overnight')

        # Deleting field 'GeneralAvail.fri_overnight'
        db.delete_column(u'app_generalavail', 'fri_overnight')

        # Deleting field 'GeneralAvail.sat_overnight'
        db.delete_column(u'app_generalavail', 'sat_overnight')

        # Deleting field 'GeneralAvail.sun_overnight'
        db.delete_column(u'app_generalavail', 'sun_overnight')


    models = {
        u'app.address': {
            'Meta': {'object_name': 'Address'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.User']"})
        },
        u'app.booking': {
            'Meta': {'object_name': 'Booking'},
            'booking_status': ('django.db.models.fields.CharField', [], {'default': "'Active'", 'max_length': '10'}),
            'child': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['app.Child']", 'symmetrical': 'False'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'emergency_phone': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Phone']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Address']"}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'bookings'", 'to': u"orm['app.Parent']"}),
            'respond_by': ('django.db.models.fields.DateTimeField', [], {}),
            'sitter': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'bookings'", 'to': u"orm['app.Sitter']"}),
            'start_date_time': ('django.db.models.fields.DateTimeField', [], {}),
            'stop_date_time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'app.certification': {
            'Meta': {'object_name': 'Certification'},
            'certification': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'})
        },
        u'app.child': {
            'Meta': {'object_name': 'Child'},
            'allergies': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'dob': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Parent']"}),
            'school': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'sitter_instructions': ('django.db.models.fields.TextField', [], {}),
            'special_needs': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'app.contact': {
            'Meta': {'object_name': 'Contact'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phone': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Phone']"})
        },
        u'app.generalavail': {
            'Meta': {'object_name': 'GeneralAvail'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'fri_early_afternoon': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fri_early_evening': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fri_early_morning': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fri_late_afternoon': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fri_late_evening': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fri_late_morning': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fri_overnight': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'mon_early_afternoon': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mon_early_evening': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mon_early_morning': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mon_late_afternoon': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mon_late_evening': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mon_late_morning': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mon_overnight': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sat_early_afternoon': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sat_early_evening': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sat_early_morning': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sat_late_afternoon': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sat_late_evening': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sat_late_morning': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sat_overnight': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sitter': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['app.Sitter']", 'unique': 'True'}),
            'sun_early_afternoon': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sun_early_evening': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sun_early_morning': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sun_late_afternoon': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sun_late_evening': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sun_late_morning': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sun_overnight': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'thurs_early_afternoon': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'thurs_early_evening': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'thurs_early_morning': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'thurs_late_afternoon': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'thurs_late_evening': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'thurs_late_morning': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'thurs_overnight': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tues_early_afternoon': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tues_early_evening': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tues_early_morning': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tues_late_afternoon': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tues_late_evening': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tues_late_morning': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tues_overnight': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'wed_early_afternoon': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'wed_early_evening': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'wed_early_morning': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'wed_late_afternoon': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'wed_late_evening': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'wed_late_morning': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'wed_overnight': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'app.group': {
            'Meta': {'object_name': 'Group'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'app.language': {
            'Meta': {'object_name': 'Language'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'})
        },
        u'app.parent': {
            'Meta': {'object_name': 'Parent', '_ormbases': [u'app.User']},
            'emergency_contact': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'emergencies'", 'unique': 'True', 'null': 'True', 'to': u"orm['app.Contact']"}),
            'fave_sitters': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'favored_by'", 'blank': 'True', 'to': u"orm['app.Sitter']"}),
            'parking_area': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'parking_for_sitter': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'physician_contact': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'physicians'", 'unique': 'True', 'null': 'True', 'to': u"orm['app.Contact']"}),
            u'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['app.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'app.phone': {
            'Meta': {'object_name': 'Phone'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'phone_type': ('django.db.models.fields.CharField', [], {'default': "'work'", 'max_length': '10'}),
            'primary': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.User']"})
        },
        u'app.settings': {
            'Meta': {'object_name': 'Settings'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'email_blog': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'email_booking_accepted_denied': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'email_booking_request': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'email_friend_joined': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'email_groups_added_network': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'email_new_review': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'email_news': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'email_upcoming_booking_remind': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobile_booking_accepted_denied': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mobile_booking_request': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mobile_friend_joined': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mobile_groups_added_network': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mobile_new_review': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mobile_upcoming_booking_remind': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['app.User']", 'unique': 'True', 'null': 'True'})
        },
        u'app.sitter': {
            'Meta': {'object_name': 'Sitter', '_ormbases': [u'app.User']},
            'biography': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'cats_ok': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'certifications': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['app.Certification']", 'symmetrical': 'False', 'blank': 'True'}),
            'current_student': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'dob': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime.now'}),
            'dogs_ok': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'extra_exp': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "'female'", 'max_length': '10'}),
            'has_drivers_licence': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'highest_education': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'id_verified': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'infant_exp': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'last_school': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'live_zip': ('django.db.models.fields.CharField', [], {'max_length': '9', 'blank': 'True'}),
            'major': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'occupation': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'one_child_max_rate': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '5', 'decimal_places': '2'}),
            'one_child_min_rate': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '5', 'decimal_places': '2'}),
            'other_animals_ok': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'other_services': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'pre_teen_exp': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'preschool_exp': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'school_age_exp': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'sick': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'smoker': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'smokers_ok': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'special_needs_exp': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'teen_exp': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'three_child_max_rate': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '5', 'decimal_places': '2'}),
            'three_child_min_rate': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '5', 'decimal_places': '2'}),
            'toddler_exp': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'total_exp': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'travel_distance': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'two_child_max_rate': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '5', 'decimal_places': '2'}),
            'two_child_min_rate': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '5', 'decimal_places': '2'}),
            u'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['app.User']", 'unique': 'True', 'primary_key': 'True'}),
            'will_transport': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'work_zip': ('django.db.models.fields.CharField', [], {'max_length': '9', 'blank': 'True'})
        },
        u'app.sitterreview': {
            'Meta': {'unique_together': "(('parent', 'sitter'),)", 'object_name': 'SitterReview'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Parent']"}),
            'rating': ('django.db.models.fields.SmallIntegerField', [], {}),
            'recommended': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'review': ('django.db.models.fields.TextField', [], {}),
            'sitter': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Sitter']"})
        },
        u'app.user': {
            'Meta': {'object_name': 'User'},
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'cell': ('django.db.models.fields.CharField', [], {'max_length': '12', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invited_by': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['app.User']", 'symmetrical': 'False'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'languages': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['app.Language']", 'symmetrical': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'membership_exp_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'parents_in_network': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'parents_in_network'", 'blank': 'True', 'to': u"orm['app.Parent']"}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'sitter_groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['app.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'sitters_in_network': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'sitters_in_network'", 'blank': 'True', 'to': u"orm['app.Sitter']"}),
            'state': ('django_localflavor_us.models.USStateField', [], {'default': "'AZ'", 'max_length': '2', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'Trial'", 'max_length': '10'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '9', 'blank': 'True'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['app']