# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'app_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('is_superuser', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('is_staff', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date_joined', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('home_address', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Address'])),
            ('email_settings', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['app.EmailSettings'], unique=True)),
            ('mobile_settings', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['app.MobileSettings'], unique=True)),
            ('membership_status', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['app.MembershipStatus'], unique=True)),
        ))
        db.send_create_signal(u'app', ['User'])

        # Adding M2M table for field groups on 'User'
        db.create_table(u'app_user_groups', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'app.user'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(u'app_user_groups', ['user_id', 'group_id'])

        # Adding M2M table for field user_permissions on 'User'
        db.create_table(u'app_user_user_permissions', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'app.user'], null=False)),
            ('permission', models.ForeignKey(orm[u'auth.permission'], null=False))
        ))
        db.create_unique(u'app_user_user_permissions', ['user_id', 'permission_id'])

        # Adding M2M table for field parents_in_network on 'User'
        db.create_table(u'app_user_parents_in_network', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_user', models.ForeignKey(orm[u'app.user'], null=False)),
            ('to_user', models.ForeignKey(orm[u'app.user'], null=False))
        ))
        db.create_unique(u'app_user_parents_in_network', ['from_user_id', 'to_user_id'])

        # Adding M2M table for field sitters_in_network on 'User'
        db.create_table(u'app_user_sitters_in_network', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_user', models.ForeignKey(orm[u'app.user'], null=False)),
            ('to_user', models.ForeignKey(orm[u'app.user'], null=False))
        ))
        db.create_unique(u'app_user_sitters_in_network', ['from_user_id', 'to_user_id'])

        # Adding M2M table for field fave_sitters on 'User'
        db.create_table(u'app_user_fave_sitters', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_user', models.ForeignKey(orm[u'app.user'], null=False)),
            ('to_user', models.ForeignKey(orm[u'app.user'], null=False))
        ))
        db.create_unique(u'app_user_fave_sitters', ['from_user_id', 'to_user_id'])

        # Adding M2M table for field friends on 'User'
        db.create_table(u'app_user_friends', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_user', models.ForeignKey(orm[u'app.user'], null=False)),
            ('to_user', models.ForeignKey(orm[u'app.user'], null=False))
        ))
        db.create_unique(u'app_user_friends', ['from_user_id', 'to_user_id'])

        # Adding M2M table for field invited_by on 'User'
        db.create_table(u'app_user_invited_by', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_user', models.ForeignKey(orm[u'app.user'], null=False)),
            ('to_user', models.ForeignKey(orm[u'app.user'], null=False))
        ))
        db.create_unique(u'app_user_invited_by', ['from_user_id', 'to_user_id'])

        # Adding model 'Address'
        db.create_table(u'app_address', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('address1', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('address2', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('state', self.gf('django_localflavor_us.models.USStateField')(max_length=2)),
            ('zip', self.gf('django.db.models.fields.CharField')(max_length=9)),
        ))
        db.send_create_signal(u'app', ['Address'])

        # Adding model 'Phone'
        db.create_table(u'app_phone', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.User'])),
            ('phone_type', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('primary', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'app', ['Phone'])

        # Adding model 'ParentInfo'
        db.create_table(u'app_parentinfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['app.User'], unique=True)),
            ('emergency_contact', self.gf('django.db.models.fields.related.OneToOneField')(related_name='emergencies', unique=True, to=orm['app.Contact'])),
            ('physician_contact', self.gf('django.db.models.fields.related.OneToOneField')(related_name='physicians', unique=True, to=orm['app.Contact'])),
            ('parking_area', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('parking_for_sitter', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'app', ['ParentInfo'])

        # Adding model 'SitterInfo'
        db.create_table(u'app_sitterinfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['app.User'], unique=True)),
            ('biography', self.gf('django.db.models.fields.TextField')()),
            ('id_verification', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['app.IdVerification'], unique=True)),
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
        db.send_create_signal(u'app', ['SitterInfo'])

        # Adding model 'Languages'
        db.create_table(u'app_languages', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'app', ['Languages'])

        # Adding M2M table for field user on 'Languages'
        db.create_table(u'app_languages_user', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('languages', models.ForeignKey(orm[u'app.languages'], null=False)),
            ('user', models.ForeignKey(orm[u'app.user'], null=False))
        ))
        db.create_unique(u'app_languages_user', ['languages_id', 'user_id'])

        # Adding model 'EmailSettings'
        db.create_table(u'app_emailsettings', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('upcoming_booking', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('new_review', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('new_reference', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('new_reference_request', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'app', ['EmailSettings'])

        # Adding model 'MobileSettings'
        db.create_table(u'app_mobilesettings', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('message_received', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('booking_accepted_denied', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'app', ['MobileSettings'])

        # Adding model 'MembershipStatus'
        db.create_table(u'app_membershipstatus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('membership_exp_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'app', ['MembershipStatus'])

        # Adding model 'Child'
        db.create_table(u'app_child', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.ParentInfo'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('dob', self.gf('django.db.models.fields.DateField')()),
            ('school', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('sitter_instructions', self.gf('django.db.models.fields.TextField')()),
            ('special_needs', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('allergies', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'app', ['Child'])

        # Adding model 'Contact'
        db.create_table(u'app_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('phone', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Phone'])),
        ))
        db.send_create_signal(u'app', ['Contact'])

        # Adding model 'GeneralAvail'
        db.create_table(u'app_generalavail', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('mon_avail_start', self.gf('django.db.models.fields.TimeField')()),
            ('mon_avail_stop', self.gf('django.db.models.fields.TimeField')()),
            ('tue_avail_start', self.gf('django.db.models.fields.TimeField')()),
            ('tue_avail_stop', self.gf('django.db.models.fields.TimeField')()),
            ('wed_avail_start', self.gf('django.db.models.fields.TimeField')()),
            ('wed_avail_stop', self.gf('django.db.models.fields.TimeField')()),
            ('thr_avail_start', self.gf('django.db.models.fields.TimeField')()),
            ('thr_avail_stop', self.gf('django.db.models.fields.TimeField')()),
            ('fri_avail_start', self.gf('django.db.models.fields.TimeField')()),
            ('fri_avail_stop', self.gf('django.db.models.fields.TimeField')()),
            ('sat_avail_start', self.gf('django.db.models.fields.TimeField')()),
            ('sat_avail_stop', self.gf('django.db.models.fields.TimeField')()),
            ('sun_avail_start', self.gf('django.db.models.fields.TimeField')()),
            ('sun_avail_stop', self.gf('django.db.models.fields.TimeField')()),
        ))
        db.send_create_signal(u'app', ['GeneralAvail'])

        # Adding model 'IdVerification'
        db.create_table(u'app_idverification', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('id_verified', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('id_scan_path', self.gf('django.db.models.fields.FilePathField')(max_length=100)),
        ))
        db.send_create_signal(u'app', ['IdVerification'])

        # Adding model 'SitterReview'
        db.create_table(u'app_sitterreview', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='reviewed', to=orm['app.User'])),
            ('sitter', self.gf('django.db.models.fields.related.ForeignKey')(related_name='reviews', to=orm['app.User'])),
            ('recommended', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('review', self.gf('django.db.models.fields.TextField')()),
            ('rating', self.gf('django.db.models.fields.SmallIntegerField')()),
        ))
        db.send_create_signal(u'app', ['SitterReview'])

        # Adding unique constraint on 'SitterReview', fields ['parent', 'sitter']
        db.create_unique(u'app_sitterreview', ['parent_id', 'sitter_id'])

        # Adding model 'Booking'
        db.create_table(u'app_booking', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='parent_bookings', to=orm['app.User'])),
            ('sitter', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sitter_bookings', to=orm['app.User'])),
            ('notes', self.gf('django.db.models.fields.TextField')()),
            ('respond_by', self.gf('django.db.models.fields.DateTimeField')()),
            ('start_date_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('stop_date_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('emergency_phone', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Phone'])),
            ('booking_status', self.gf('django.db.models.fields.CharField')(default='active', max_length=10)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Address'])),
        ))
        db.send_create_signal(u'app', ['Booking'])

        # Adding M2M table for field child on 'Booking'
        db.create_table(u'app_booking_child', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('booking', models.ForeignKey(orm[u'app.booking'], null=False)),
            ('child', models.ForeignKey(orm[u'app.child'], null=False))
        ))
        db.create_unique(u'app_booking_child', ['booking_id', 'child_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'SitterReview', fields ['parent', 'sitter']
        db.delete_unique(u'app_sitterreview', ['parent_id', 'sitter_id'])

        # Deleting model 'User'
        db.delete_table(u'app_user')

        # Removing M2M table for field groups on 'User'
        db.delete_table('app_user_groups')

        # Removing M2M table for field user_permissions on 'User'
        db.delete_table('app_user_user_permissions')

        # Removing M2M table for field parents_in_network on 'User'
        db.delete_table('app_user_parents_in_network')

        # Removing M2M table for field sitters_in_network on 'User'
        db.delete_table('app_user_sitters_in_network')

        # Removing M2M table for field fave_sitters on 'User'
        db.delete_table('app_user_fave_sitters')

        # Removing M2M table for field friends on 'User'
        db.delete_table('app_user_friends')

        # Removing M2M table for field invited_by on 'User'
        db.delete_table('app_user_invited_by')

        # Deleting model 'Address'
        db.delete_table(u'app_address')

        # Deleting model 'Phone'
        db.delete_table(u'app_phone')

        # Deleting model 'ParentInfo'
        db.delete_table(u'app_parentinfo')

        # Deleting model 'SitterInfo'
        db.delete_table(u'app_sitterinfo')

        # Deleting model 'Languages'
        db.delete_table(u'app_languages')

        # Removing M2M table for field user on 'Languages'
        db.delete_table('app_languages_user')

        # Deleting model 'EmailSettings'
        db.delete_table(u'app_emailsettings')

        # Deleting model 'MobileSettings'
        db.delete_table(u'app_mobilesettings')

        # Deleting model 'MembershipStatus'
        db.delete_table(u'app_membershipstatus')

        # Deleting model 'Child'
        db.delete_table(u'app_child')

        # Deleting model 'Contact'
        db.delete_table(u'app_contact')

        # Deleting model 'GeneralAvail'
        db.delete_table(u'app_generalavail')

        # Deleting model 'IdVerification'
        db.delete_table(u'app_idverification')

        # Deleting model 'SitterReview'
        db.delete_table(u'app_sitterreview')

        # Deleting model 'Booking'
        db.delete_table(u'app_booking')

        # Removing M2M table for field child on 'Booking'
        db.delete_table('app_booking_child')


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
            'upcoming_booking': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
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
        u'app.membershipstatus': {
            'Meta': {'object_name': 'MembershipStatus'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'membership_exp_date': ('django.db.models.fields.DateField', [], {}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'app.mobilesettings': {
            'Meta': {'object_name': 'MobileSettings'},
            'booking_accepted_denied': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message_received': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'})
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
            'primary': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.User']"})
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
            'email_settings': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['app.EmailSettings']", 'unique': 'True'}),
            'fave_sitters': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'fave_sitters_rel_+'", 'symmetrical': "'false'", 'to': u"orm['app.User']"}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'friends': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'friends_rel_+'", 'to': u"orm['app.User']"}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'home_address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Address']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invited_by': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'invited_by_rel_+'", 'symmetrical': "'false'", 'to': u"orm['app.User']"}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'membership_status': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['app.MembershipStatus']", 'unique': 'True'}),
            'mobile_settings': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['app.MobileSettings']", 'unique': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'parents_in_network': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'parents_in_network_rel_+'", 'symmetrical': "'false'", 'to': u"orm['app.User']"}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'sitters_in_network': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'sitters_in_network_rel_+'", 'symmetrical': "'false'", 'to': u"orm['app.User']"}),
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