# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Phone.user'
        db.delete_column(u'app_phone', 'user_id')

        # Adding M2M table for field phone on 'User'
        db.create_table(u'app_user_phone', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'app.user'], null=False)),
            ('phone', models.ForeignKey(orm[u'app.phone'], null=False))
        ))
        db.create_unique(u'app_user_phone', ['user_id', 'phone_id'])


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Phone.user'
        raise RuntimeError("Cannot reverse this migration. 'Phone.user' and its values cannot be restored.")
        # Removing M2M table for field phone on 'User'
        db.delete_table('app_user_phone')


    models = {
        u'app.address': {
            'Meta': {'object_name': 'Address'},
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'state': ('django_localflavor_us.models.USStateField', [], {'max_length': '2'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.User']"}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '9'})
        },
        u'app.booking': {
            'Meta': {'object_name': 'Booking'},
            'booking_status': ('django.db.models.fields.CharField', [], {'default': "'active'", 'max_length': '10'}),
            'child': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['app.Child']", 'symmetrical': 'False'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'emergency_phone': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Phone']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Address']"}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'parent_bookings'", 'to': u"orm['app.User']"}),
            'respond_by': ('django.db.models.fields.DateTimeField', [], {}),
            'sitter': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sitter_bookings'", 'to': u"orm['app.User']"}),
            'start_date_time': ('django.db.models.fields.DateTimeField', [], {}),
            'stop_date_time': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'app.child': {
            'Meta': {'object_name': 'Child'},
            'allergies': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'dob': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.ParentInfo']"}),
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
        u'app.emailsettings': {
            'Meta': {'object_name': 'EmailSettings'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'new_reference': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'new_reference_request': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'new_review': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'upcoming_booking': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['app.User']", 'unique': 'True'})
        },
        u'app.generalavail': {
            'Meta': {'object_name': 'GeneralAvail'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'fri_avail_start': ('django.db.models.fields.TimeField', [], {}),
            'fri_avail_stop': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'mon_avail_start': ('django.db.models.fields.TimeField', [], {}),
            'mon_avail_stop': ('django.db.models.fields.TimeField', [], {}),
            'sat_avail_start': ('django.db.models.fields.TimeField', [], {}),
            'sat_avail_stop': ('django.db.models.fields.TimeField', [], {}),
            'sun_avail_start': ('django.db.models.fields.TimeField', [], {}),
            'sun_avail_stop': ('django.db.models.fields.TimeField', [], {}),
            'thr_avail_start': ('django.db.models.fields.TimeField', [], {}),
            'thr_avail_stop': ('django.db.models.fields.TimeField', [], {}),
            'tue_avail_start': ('django.db.models.fields.TimeField', [], {}),
            'tue_avail_stop': ('django.db.models.fields.TimeField', [], {}),
            'wed_avail_start': ('django.db.models.fields.TimeField', [], {}),
            'wed_avail_stop': ('django.db.models.fields.TimeField', [], {})
        },
        u'app.idverification': {
            'Meta': {'object_name': 'IdVerification'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_scan_path': ('django.db.models.fields.FilePathField', [], {'max_length': '100'}),
            'id_verified': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'})
        },
        u'app.languages': {
            'Meta': {'object_name': 'Languages'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'user': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['app.User']", 'symmetrical': 'False'})
        },
        u'app.mobilesettings': {
            'Meta': {'object_name': 'MobileSettings'},
            'booking_accepted_denied': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message_received': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['app.User']", 'unique': 'True'})
        },
        u'app.parentinfo': {
            'Meta': {'object_name': 'ParentInfo'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'emergency_contact': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'emergencies'", 'unique': 'True', 'to': u"orm['app.Contact']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'parking_area': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'parking_for_sitter': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'physician_contact': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'physicians'", 'unique': 'True', 'to': u"orm['app.Contact']"}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['app.User']", 'unique': 'True'})
        },
        u'app.phone': {
            'Meta': {'object_name': 'Phone'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'phone_type': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'primary': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'app.sitterinfo': {
            'Meta': {'object_name': 'SitterInfo'},
            'biography': ('django.db.models.fields.TextField', [], {}),
            'cats_ok': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'certification': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'current_student': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'dob': ('django.db.models.fields.DateField', [], {}),
            'dogs_ok': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'general_avail': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['app.GeneralAvail']", 'unique': 'True'}),
            'highest_education': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_verification': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['app.IdVerification']", 'unique': 'True'}),
            'infant_exp': ('django.db.models.fields.SmallIntegerField', [], {}),
            'last_school': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'live_zip': ('django.db.models.fields.CharField', [], {'max_length': '9'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'one_child_max_rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'one_child_min_rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'other_animals_ok': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'other_services': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'pre_teen_exp': ('django.db.models.fields.SmallIntegerField', [], {}),
            'preschool_exp': ('django.db.models.fields.SmallIntegerField', [], {}),
            'school_age_exp': ('django.db.models.fields.SmallIntegerField', [], {}),
            'smoker': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'smokers_ok': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'teen_exp': ('django.db.models.fields.SmallIntegerField', [], {}),
            'three_child_max_rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'three_child_min_rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'toddler_exp': ('django.db.models.fields.SmallIntegerField', [], {}),
            'total_exp': ('django.db.models.fields.SmallIntegerField', [], {}),
            'two_child_max_rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'two_child_min_rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['app.User']", 'unique': 'True'}),
            'will_transport': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'work_zip': ('django.db.models.fields.CharField', [], {'max_length': '9'})
        },
        u'app.sitterreview': {
            'Meta': {'unique_together': "(('parent', 'sitter'),)", 'object_name': 'SitterReview'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reviewed'", 'to': u"orm['app.User']"}),
            'rating': ('django.db.models.fields.SmallIntegerField', [], {}),
            'recommended': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'review': ('django.db.models.fields.TextField', [], {}),
            'sitter': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reviews'", 'to': u"orm['app.User']"})
        },
        u'app.user': {
            'Meta': {'object_name': 'User'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'fave_sitters': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'fave_sitters_rel_+'", 'symmetrical': "'false'", 'to': u"orm['app.User']"}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'friends': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'friends_rel_+'", 'to': u"orm['app.User']"}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invited_by': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'invited_by_rel_+'", 'symmetrical': "'false'", 'to': u"orm['app.User']"}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'membership_exp_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'parents_in_network': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'parents_in_network_rel_+'", 'symmetrical': "'false'", 'to': u"orm['app.User']"}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['app.Phone']", 'symmetrical': 'False'}),
            'sitters_in_network': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'sitters_in_network_rel_+'", 'symmetrical': "'false'", 'to': u"orm['app.User']"}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'trial'", 'max_length': '10'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
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