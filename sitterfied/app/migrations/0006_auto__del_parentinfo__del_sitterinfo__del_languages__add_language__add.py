# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'ParentInfo'
        db.delete_table(u'app_parentinfo')

        # Deleting model 'SitterInfo'
        db.delete_table(u'app_sitterinfo')

        # Deleting model 'Languages'
        db.delete_table(u'app_languages')

        # Removing M2M table for field user on 'Languages'
        db.delete_table('app_languages_user')

        # Adding model 'Language'
        db.create_table(u'app_language', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'app', ['Language'])

        # Adding model 'Parent'
        db.create_table(u'app_parent', (
            (u'user_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['app.User'], unique=True, primary_key=True)),
            ('emergency_contact', self.gf('django.db.models.fields.related.OneToOneField')(related_name='emergencies', unique=True, to=orm['app.Contact'])),
            ('physician_contact', self.gf('django.db.models.fields.related.OneToOneField')(related_name='physicians', unique=True, to=orm['app.Contact'])),
            ('parking_area', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('parking_for_sitter', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'app', ['Parent'])

        # Adding model 'Sitter'
        db.create_table(u'app_sitter', (
            (u'user_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['app.User'], unique=True, primary_key=True)),
            ('biography', self.gf('django.db.models.fields.TextField')()),
            ('id_verified', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('id_scan_path', self.gf('django.db.models.fields.FilePathField')(max_length=100)),
            ('live_zip', self.gf('django.db.models.fields.CharField')(max_length=9)),
            ('work_zip', self.gf('django.db.models.fields.CharField')(max_length=9)),
            ('dob', self.gf('django.db.models.fields.DateField')()),
            ('smoker', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('will_transport', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('total_exp', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('infant_exp', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('toddler_exp', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('preschool_exp', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('school_age_exp', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('pre_teen_exp', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('teen_exp', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('highest_education', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('last_school', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('current_student', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('certification', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('other_services', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('one_child_min_rate', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('one_child_max_rate', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('two_child_min_rate', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('two_child_max_rate', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('three_child_min_rate', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('three_child_max_rate', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('smokers_ok', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('dogs_ok', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cats_ok', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('other_animals_ok', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('general_avail', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['app.GeneralAvail'], unique=True)),
        ))
        db.send_create_signal(u'app', ['Sitter'])


        # Changing field 'SitterReview.parent'
        db.alter_column(u'app_sitterreview', 'parent_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Parent']))

        # Changing field 'SitterReview.sitter'
        db.alter_column(u'app_sitterreview', 'sitter_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Sitter']))

        # Changing field 'Booking.parent'
        db.alter_column(u'app_booking', 'parent_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Parent']))

        # Changing field 'Booking.sitter'
        db.alter_column(u'app_booking', 'sitter_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Sitter']))

        # Changing field 'Child.parent'
        db.alter_column(u'app_child', 'parent_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Parent']))
        # Removing M2M table for field friends on 'User'
        db.delete_table('app_user_friends')

        # Adding M2M table for field languages on 'User'
        db.create_table(u'app_user_languages', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'app.user'], null=False)),
            ('language', models.ForeignKey(orm[u'app.language'], null=False))
        ))
        db.create_unique(u'app_user_languages', ['user_id', 'language_id'])


    def backwards(self, orm):
        # Adding model 'ParentInfo'
        db.create_table(u'app_parentinfo', (
            ('physician_contact', self.gf('django.db.models.fields.related.OneToOneField')(related_name='physicians', unique=True, to=orm['app.Contact'])),
            ('emergency_contact', self.gf('django.db.models.fields.related.OneToOneField')(related_name='emergencies', unique=True, to=orm['app.Contact'])),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('parking_area', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['app.User'], unique=True)),
            ('parking_for_sitter', self.gf('django.db.models.fields.BooleanField')(default=False)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal(u'app', ['ParentInfo'])

        # Adding model 'SitterInfo'
        db.create_table(u'app_sitterinfo', (
            ('last_school', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('highest_education', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('smokers_ok', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('will_transport', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('school_age_exp', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('certification', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('id_verified', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('other_animals_ok', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('pre_teen_exp', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('live_zip', self.gf('django.db.models.fields.CharField')(max_length=9)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['app.User'], unique=True)),
            ('preschool_exp', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('total_exp', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('three_child_max_rate', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('biography', self.gf('django.db.models.fields.TextField')()),
            ('work_zip', self.gf('django.db.models.fields.CharField')(max_length=9)),
            ('one_child_min_rate', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('toddler_exp', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('three_child_min_rate', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('current_student', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('teen_exp', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('one_child_max_rate', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('two_child_min_rate', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('id_scan_path', self.gf('django.db.models.fields.FilePathField')(max_length=100)),
            ('cats_ok', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('dob', self.gf('django.db.models.fields.DateField')()),
            ('dogs_ok', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('two_child_max_rate', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('smoker', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('other_services', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('general_avail', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['app.GeneralAvail'], unique=True)),
            ('infant_exp', self.gf('django.db.models.fields.SmallIntegerField')()),
        ))
        db.send_create_signal(u'app', ['SitterInfo'])

        # Adding model 'Languages'
        db.create_table(u'app_languages', (
            ('language', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'app', ['Languages'])

        # Adding M2M table for field user on 'Languages'
        db.create_table(u'app_languages_user', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('languages', models.ForeignKey(orm[u'app.languages'], null=False)),
            ('user', models.ForeignKey(orm[u'app.user'], null=False))
        ))
        db.create_unique(u'app_languages_user', ['languages_id', 'user_id'])

        # Deleting model 'Language'
        db.delete_table(u'app_language')

        # Deleting model 'Parent'
        db.delete_table(u'app_parent')

        # Deleting model 'Sitter'
        db.delete_table(u'app_sitter')


        # Changing field 'SitterReview.parent'
        db.alter_column(u'app_sitterreview', 'parent_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.User']))

        # Changing field 'SitterReview.sitter'
        db.alter_column(u'app_sitterreview', 'sitter_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.User']))

        # Changing field 'Booking.parent'
        db.alter_column(u'app_booking', 'parent_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.User']))

        # Changing field 'Booking.sitter'
        db.alter_column(u'app_booking', 'sitter_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.User']))

        # Changing field 'Child.parent'
        db.alter_column(u'app_child', 'parent_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.ParentInfo']))
        # Adding M2M table for field friends on 'User'
        db.create_table(u'app_user_friends', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_user', models.ForeignKey(orm[u'app.user'], null=False)),
            ('to_user', models.ForeignKey(orm[u'app.user'], null=False))
        ))
        db.create_unique(u'app_user_friends', ['from_user_id', 'to_user_id'])

        # Removing M2M table for field languages on 'User'
        db.delete_table('app_user_languages')


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
        u'app.language': {
            'Meta': {'object_name': 'Language'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'})
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
        u'app.parent': {
            'Meta': {'object_name': 'Parent', '_ormbases': [u'app.User']},
            'emergency_contact': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'emergencies'", 'unique': 'True', 'to': u"orm['app.Contact']"}),
            'parking_area': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'parking_for_sitter': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'physician_contact': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'physicians'", 'unique': 'True', 'to': u"orm['app.Contact']"}),
            u'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['app.User']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'app.phone': {
            'Meta': {'object_name': 'Phone'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'phone_type': ('django.db.models.fields.CharField', [], {'default': "'work'", 'max_length': '10'}),
            'primary': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'app.sitter': {
            'Meta': {'object_name': 'Sitter', '_ormbases': [u'app.User']},
            'biography': ('django.db.models.fields.TextField', [], {}),
            'cats_ok': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'certification': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'current_student': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'dob': ('django.db.models.fields.DateField', [], {}),
            'dogs_ok': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'general_avail': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['app.GeneralAvail']", 'unique': 'True'}),
            'highest_education': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id_scan_path': ('django.db.models.fields.FilePathField', [], {'max_length': '100'}),
            'id_verified': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'infant_exp': ('django.db.models.fields.SmallIntegerField', [], {}),
            'last_school': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'live_zip': ('django.db.models.fields.CharField', [], {'max_length': '9'}),
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
            u'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['app.User']", 'unique': 'True', 'primary_key': 'True'}),
            'will_transport': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'work_zip': ('django.db.models.fields.CharField', [], {'max_length': '9'})
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
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'fave_sitters': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'favored_by'", 'symmetrical': 'False', 'to': u"orm['app.Sitter']"}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invited_by': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'invited_by_rel_+'", 'symmetrical': "'false'", 'to': u"orm['app.User']"}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'languages': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['app.Language']", 'symmetrical': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'membership_exp_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'parents_in_network': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['app.Parent']", 'symmetrical': 'False'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['app.Phone']", 'symmetrical': 'False'}),
            'sitters_in_network': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['app.Sitter']", 'symmetrical': 'False'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'Trial'", 'max_length': '10'}),
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