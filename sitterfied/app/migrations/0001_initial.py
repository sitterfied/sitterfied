# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
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
            ('status', self.gf('django.db.models.fields.CharField')(default='Trial', max_length=10)),
            ('membership_exp_date', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('facebook_token', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('facebook_id', self.gf('django.db.models.fields.IntegerField')(unique=True, null=True, blank=True)),
            ('google_imported', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('address1', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('address2', self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(default='AL', max_length=2, blank=True)),
            ('zip', self.gf('django.db.models.fields.CharField')(max_length=9, blank=True)),
            ('timezone', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('cell', self.gf('django.db.models.fields.CharField')(max_length=12, blank=True)),
            ('avatar', self.gf('pyuploadcare.dj.models.ImageField')(blank=True)),
        ))
        db.send_create_signal(u'app', ['User'])

        # Adding M2M table for field groups on 'User'
        m2m_table_name = db.shorten_name(u'app_user_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'app.user'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'group_id'])

        # Adding M2M table for field user_permissions on 'User'
        m2m_table_name = db.shorten_name(u'app_user_user_permissions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'app.user'], null=False)),
            ('permission', models.ForeignKey(orm[u'auth.permission'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'permission_id'])

        # Adding M2M table for field users_in_network on 'User'
        m2m_table_name = db.shorten_name(u'app_user_users_in_network')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_user', models.ForeignKey(orm[u'app.user'], null=False)),
            ('to_user', models.ForeignKey(orm[u'app.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_user_id', 'to_user_id'])

        # Adding M2M table for field friends on 'User'
        m2m_table_name = db.shorten_name(u'app_user_friends')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_user', models.ForeignKey(orm[u'app.user'], null=False)),
            ('to_user', models.ForeignKey(orm[u'app.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_user_id', 'to_user_id'])

        # Adding M2M table for field sitter_groups on 'User'
        m2m_table_name = db.shorten_name(u'app_user_sitter_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'app.user'], null=False)),
            ('group', models.ForeignKey(orm[u'app.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'group_id'])

        # Adding M2M table for field invited_by on 'User'
        m2m_table_name = db.shorten_name(u'app_user_invited_by')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_user', models.ForeignKey(orm[u'app.user'], null=False)),
            ('to_user', models.ForeignKey(orm[u'app.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_user_id', 'to_user_id'])

        # Adding M2M table for field languages on 'User'
        m2m_table_name = db.shorten_name(u'app_user_languages')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'app.user'], null=False)),
            ('language', models.ForeignKey(orm[u'app.language'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'language_id'])

        # Adding model 'Address'
        db.create_table(u'app_address', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.User'])),
        ))
        db.send_create_signal(u'app', ['Address'])

        # Adding model 'Phone'
        db.create_table(u'app_phone', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('phone_type', self.gf('django.db.models.fields.CharField')(default='work', max_length=10)),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('primary', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.User'])),
        ))
        db.send_create_signal(u'app', ['Phone'])

        # Adding model 'Parent'
        db.create_table(u'app_parent', (
            (u'user_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['app.User'], unique=True, primary_key=True)),
            ('emergency_contact_one_name', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('emergency_contact_one_phone', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('emergency_contact_two_name', self.gf('django.db.models.fields.CharField')(max_length=128, blank=True)),
            ('emergency_contact_two_phone', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
        ))
        db.send_create_signal(u'app', ['Parent'])

        # Adding M2M table for field sitter_teams on 'Parent'
        m2m_table_name = db.shorten_name(u'app_parent_sitter_teams')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('parent', models.ForeignKey(orm[u'app.parent'], null=False)),
            ('sitter', models.ForeignKey(orm[u'app.sitter'], null=False))
        ))
        db.create_unique(m2m_table_name, ['parent_id', 'sitter_id'])

        # Adding M2M table for field bookmarks on 'Parent'
        m2m_table_name = db.shorten_name(u'app_parent_bookmarks')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('parent', models.ForeignKey(orm[u'app.parent'], null=False)),
            ('sitter', models.ForeignKey(orm[u'app.sitter'], null=False))
        ))
        db.create_unique(m2m_table_name, ['parent_id', 'sitter_id'])

        # Adding model 'Sitter'
        db.create_table(u'app_sitter', (
            (u'user_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['app.User'], unique=True, primary_key=True)),
            ('biography', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(default='female', max_length=10)),
            ('id_verified', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('dob', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('smoker', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('sick', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('will_transport', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('total_exp', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('infant_exp', self.gf('django.db.models.fields.SmallIntegerField')(blank=True)),
            ('toddler_exp', self.gf('django.db.models.fields.SmallIntegerField')(blank=True)),
            ('preschool_exp', self.gf('django.db.models.fields.SmallIntegerField')(blank=True)),
            ('school_age_exp', self.gf('django.db.models.fields.SmallIntegerField')(blank=True)),
            ('pre_teen_exp', self.gf('django.db.models.fields.SmallIntegerField')(blank=True)),
            ('teen_exp', self.gf('django.db.models.fields.SmallIntegerField')(blank=True)),
            ('special_needs_exp', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('extra_exp', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
            ('highest_education', self.gf('django.db.models.fields.CharField')(default='', max_length=50, null=True, blank=True)),
            ('last_school', self.gf('django.db.models.fields.CharField')(default='', max_length=50, null=True, blank=True)),
            ('major', self.gf('django.db.models.fields.CharField')(default='', max_length=50, null=True, blank=True)),
            ('occupation', self.gf('django.db.models.fields.CharField')(default='', max_length=50, null=True, blank=True)),
            ('current_student', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('one_child_min_rate', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('one_child_max_rate', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('two_child_min_rate', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2, blank=True)),
            ('two_child_max_rate', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2, blank=True)),
            ('three_child_min_rate', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2, blank=True)),
            ('three_child_max_rate', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2, blank=True)),
            ('smokers_ok', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('dogs_ok', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('cats_ok', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('other_animals_ok', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('has_drivers_licence', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('travel_distance', self.gf('django.db.models.fields.IntegerField')(default=10)),
        ))
        db.send_create_signal(u'app', ['Sitter'])

        # Adding M2M table for field other_services on 'Sitter'
        m2m_table_name = db.shorten_name(u'app_sitter_other_services')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('sitter', models.ForeignKey(orm[u'app.sitter'], null=False)),
            ('otherservice', models.ForeignKey(orm[u'app.otherservice'], null=False))
        ))
        db.create_unique(m2m_table_name, ['sitter_id', 'otherservice_id'])

        # Adding M2M table for field certifications on 'Sitter'
        m2m_table_name = db.shorten_name(u'app_sitter_certifications')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('sitter', models.ForeignKey(orm[u'app.sitter'], null=False)),
            ('certification', models.ForeignKey(orm[u'app.certification'], null=False))
        ))
        db.create_unique(m2m_table_name, ['sitter_id', 'certification_id'])

        # Adding model 'Certification'
        db.create_table(u'app_certification', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('certification', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
        ))
        db.send_create_signal(u'app', ['Certification'])

        # Adding model 'OtherService'
        db.create_table(u'app_otherservice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('service', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
        ))
        db.send_create_signal(u'app', ['OtherService'])

        # Adding model 'Language'
        db.create_table(u'app_language', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'app', ['Language'])

        # Adding model 'SpecialNeed'
        db.create_table(u'app_specialneed', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('need', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'app', ['SpecialNeed'])

        # Adding model 'Settings'
        db.create_table(u'app_settings', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['app.User'], unique=True, null=True)),
            ('mobile_booking_accepted_denied', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('mobile_new_review', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('mobile_booking_request', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('mobile_friend_joined', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('mobile_groups_added_network', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('mobile_upcoming_booking_remind', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('email_booking_accepted_denied', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('email_new_review', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('email_booking_request', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('email_friend_joined', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('email_groups_added_network', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('email_upcoming_booking_remind', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('email_news', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('email_blog', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'app', ['Settings'])

        # Adding model 'Child'
        db.create_table(u'app_child', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='children', to=orm['app.Parent'])),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True)),
            ('dob', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('school', self.gf('django.db.models.fields.CharField')(default='', max_length=50, blank=True)),
        ))
        db.send_create_signal(u'app', ['Child'])

        # Adding M2M table for field special_needs on 'Child'
        m2m_table_name = db.shorten_name(u'app_child_special_needs')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('child', models.ForeignKey(orm[u'app.child'], null=False)),
            ('specialneed', models.ForeignKey(orm[u'app.specialneed'], null=False))
        ))
        db.create_unique(m2m_table_name, ['child_id', 'specialneed_id'])

        # Adding model 'Contact'
        db.create_table(u'app_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('phone', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Phone'])),
        ))
        db.send_create_signal(u'app', ['Contact'])

        # Adding model 'Schedule'
        db.create_table(u'app_schedule', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('sitter', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['app.Sitter'], unique=True)),
            ('mon_early_morning', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('tue_early_morning', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('wed_early_morning', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('thu_early_morning', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('fri_early_morning', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('sat_early_morning', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('sun_early_morning', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('mon_late_morning', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('tue_late_morning', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('wed_late_morning', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('thu_late_morning', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('fri_late_morning', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('sat_late_morning', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('sun_late_morning', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('mon_early_afternoon', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('tue_early_afternoon', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('wed_early_afternoon', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('thu_early_afternoon', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('fri_early_afternoon', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('sat_early_afternoon', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('sun_early_afternoon', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('mon_late_afternoon', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('tue_late_afternoon', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('wed_late_afternoon', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('thu_late_afternoon', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('fri_late_afternoon', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('sat_late_afternoon', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('sun_late_afternoon', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('mon_early_evening', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('tue_early_evening', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('wed_early_evening', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('thu_early_evening', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('fri_early_evening', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('sat_early_evening', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('sun_early_evening', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('mon_late_evening', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('tue_late_evening', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('wed_late_evening', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('thu_late_evening', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('fri_late_evening', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('sat_late_evening', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('sun_late_evening', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('mon_overnight', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('tue_overnight', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('wed_overnight', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('thu_overnight', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('fri_overnight', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('sat_overnight', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('sun_overnight', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'app', ['Schedule'])

        # Adding model 'SitterReview'
        db.create_table(u'app_sitterreview', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='reviews', to=orm['app.Parent'])),
            ('sitter', self.gf('django.db.models.fields.related.ForeignKey')(related_name='reviews', to=orm['app.Sitter'])),
            ('recommended', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('rehire', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('review', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'app', ['SitterReview'])

        # Adding unique constraint on 'SitterReview', fields ['parent', 'sitter']
        db.create_unique(u'app_sitterreview', ['parent_id', 'sitter_id'])

        # Adding model 'Booking'
        db.create_table(u'app_booking', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(related_name='bookings', to=orm['app.Parent'])),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('respond_by', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('start_date_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('stop_date_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('num_children', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('emergency_phone', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('address1', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('address2', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(default='AL', max_length=2, blank=True)),
            ('zip', self.gf('django.db.models.fields.CharField')(max_length=9, blank=True)),
            ('rate', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=5, decimal_places=2, blank=True)),
            ('booking_status', self.gf('django.db.models.fields.CharField')(default='Active', max_length=10)),
            ('booking_type', self.gf('django.db.models.fields.CharField')(default='Job', max_length=10)),
            ('accepted_sitter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['app.Sitter'], null=True, blank=True)),
            ('overnight', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('canceled', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'app', ['Booking'])

        # Adding M2M table for field sitters on 'Booking'
        m2m_table_name = db.shorten_name(u'app_booking_sitters')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('booking', models.ForeignKey(orm[u'app.booking'], null=False)),
            ('sitter', models.ForeignKey(orm[u'app.sitter'], null=False))
        ))
        db.create_unique(m2m_table_name, ['booking_id', 'sitter_id'])

        # Adding M2M table for field declined_sitters on 'Booking'
        m2m_table_name = db.shorten_name(u'app_booking_declined_sitters')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('booking', models.ForeignKey(orm[u'app.booking'], null=False)),
            ('sitter', models.ForeignKey(orm[u'app.sitter'], null=False))
        ))
        db.create_unique(m2m_table_name, ['booking_id', 'sitter_id'])

        # Adding model 'IncomingSMSMessage'
        db.create_table(u'app_incomingsmsmessage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('sid', self.gf('django.db.models.fields.CharField')(max_length=34)),
            ('date_created', self.gf('django.db.models.fields.DateTimeField')()),
            ('date_updated', self.gf('django.db.models.fields.DateTimeField')()),
            ('date_sent', self.gf('django.db.models.fields.DateTimeField')()),
            ('to', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('body', self.gf('django.db.models.fields.CharField')(max_length=161)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=12)),
        ))
        db.send_create_signal(u'app', ['IncomingSMSMessage'])

        # Adding model 'Group'
        db.create_table(u'app_group', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal(u'app', ['Group'])


    def backwards(self, orm):
        # Removing unique constraint on 'SitterReview', fields ['parent', 'sitter']
        db.delete_unique(u'app_sitterreview', ['parent_id', 'sitter_id'])

        # Deleting model 'User'
        db.delete_table(u'app_user')

        # Removing M2M table for field groups on 'User'
        db.delete_table(db.shorten_name(u'app_user_groups'))

        # Removing M2M table for field user_permissions on 'User'
        db.delete_table(db.shorten_name(u'app_user_user_permissions'))

        # Removing M2M table for field users_in_network on 'User'
        db.delete_table(db.shorten_name(u'app_user_users_in_network'))

        # Removing M2M table for field friends on 'User'
        db.delete_table(db.shorten_name(u'app_user_friends'))

        # Removing M2M table for field sitter_groups on 'User'
        db.delete_table(db.shorten_name(u'app_user_sitter_groups'))

        # Removing M2M table for field invited_by on 'User'
        db.delete_table(db.shorten_name(u'app_user_invited_by'))

        # Removing M2M table for field languages on 'User'
        db.delete_table(db.shorten_name(u'app_user_languages'))

        # Deleting model 'Address'
        db.delete_table(u'app_address')

        # Deleting model 'Phone'
        db.delete_table(u'app_phone')

        # Deleting model 'Parent'
        db.delete_table(u'app_parent')

        # Removing M2M table for field sitter_teams on 'Parent'
        db.delete_table(db.shorten_name(u'app_parent_sitter_teams'))

        # Removing M2M table for field bookmarks on 'Parent'
        db.delete_table(db.shorten_name(u'app_parent_bookmarks'))

        # Deleting model 'Sitter'
        db.delete_table(u'app_sitter')

        # Removing M2M table for field other_services on 'Sitter'
        db.delete_table(db.shorten_name(u'app_sitter_other_services'))

        # Removing M2M table for field certifications on 'Sitter'
        db.delete_table(db.shorten_name(u'app_sitter_certifications'))

        # Deleting model 'Certification'
        db.delete_table(u'app_certification')

        # Deleting model 'OtherService'
        db.delete_table(u'app_otherservice')

        # Deleting model 'Language'
        db.delete_table(u'app_language')

        # Deleting model 'SpecialNeed'
        db.delete_table(u'app_specialneed')

        # Deleting model 'Settings'
        db.delete_table(u'app_settings')

        # Deleting model 'Child'
        db.delete_table(u'app_child')

        # Removing M2M table for field special_needs on 'Child'
        db.delete_table(db.shorten_name(u'app_child_special_needs'))

        # Deleting model 'Contact'
        db.delete_table(u'app_contact')

        # Deleting model 'Schedule'
        db.delete_table(u'app_schedule')

        # Deleting model 'SitterReview'
        db.delete_table(u'app_sitterreview')

        # Deleting model 'Booking'
        db.delete_table(u'app_booking')

        # Removing M2M table for field sitters on 'Booking'
        db.delete_table(db.shorten_name(u'app_booking_sitters'))

        # Removing M2M table for field declined_sitters on 'Booking'
        db.delete_table(db.shorten_name(u'app_booking_declined_sitters'))

        # Deleting model 'IncomingSMSMessage'
        db.delete_table(u'app_incomingsmsmessage')

        # Deleting model 'Group'
        db.delete_table(u'app_group')


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
            'accepted_sitter': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Sitter']", 'null': 'True', 'blank': 'True'}),
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'booking_status': ('django.db.models.fields.CharField', [], {'default': "'Active'", 'max_length': '10'}),
            'booking_type': ('django.db.models.fields.CharField', [], {'default': "'Job'", 'max_length': '10'}),
            'canceled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'declined_sitters': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'declined_bookings'", 'blank': 'True', 'to': u"orm['app.Sitter']"}),
            'emergency_phone': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'num_children': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'overnight': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'bookings'", 'to': u"orm['app.Parent']"}),
            'rate': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'respond_by': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'sitters': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'bookings'", 'symmetrical': 'False', 'to': u"orm['app.Sitter']"}),
            'start_date_time': ('django.db.models.fields.DateTimeField', [], {}),
            'state': ('django.db.models.fields.CharField', [], {'default': "'AL'", 'max_length': '2', 'blank': 'True'}),
            'stop_date_time': ('django.db.models.fields.DateTimeField', [], {}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '9', 'blank': 'True'})
        },
        u'app.certification': {
            'Meta': {'object_name': 'Certification'},
            'certification': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'})
        },
        u'app.child': {
            'Meta': {'object_name': 'Child'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'dob': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'children'", 'to': u"orm['app.Parent']"}),
            'school': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'special_needs': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['app.SpecialNeed']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'app.contact': {
            'Meta': {'object_name': 'Contact'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phone': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['app.Phone']"})
        },
        u'app.group': {
            'Meta': {'object_name': 'Group'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'app.incomingsmsmessage': {
            'Meta': {'object_name': 'IncomingSMSMessage'},
            'body': ('django.db.models.fields.CharField', [], {'max_length': '161'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'date_sent': ('django.db.models.fields.DateTimeField', [], {}),
            'date_updated': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'sid': ('django.db.models.fields.CharField', [], {'max_length': '34'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'to': ('django.db.models.fields.CharField', [], {'max_length': '16'})
        },
        u'app.language': {
            'Meta': {'object_name': 'Language'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'})
        },
        u'app.otherservice': {
            'Meta': {'object_name': 'OtherService'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'service': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        u'app.parent': {
            'Meta': {'object_name': 'Parent', '_ormbases': [u'app.User']},
            'bookmarks': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'bookmarks'", 'blank': 'True', 'to': u"orm['app.Sitter']"}),
            'emergency_contact_one_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'emergency_contact_one_phone': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'emergency_contact_two_name': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'emergency_contact_two_phone': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'sitter_teams': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'sitter_teams'", 'blank': 'True', 'to': u"orm['app.Sitter']"}),
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
        u'app.schedule': {
            'Meta': {'object_name': 'Schedule'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'fri_early_afternoon': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'fri_early_evening': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'fri_early_morning': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'fri_late_afternoon': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'fri_late_evening': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'fri_late_morning': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'fri_overnight': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'mon_early_afternoon': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'mon_early_evening': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'mon_early_morning': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'mon_late_afternoon': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'mon_late_evening': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'mon_late_morning': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'mon_overnight': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'sat_early_afternoon': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'sat_early_evening': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'sat_early_morning': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'sat_late_afternoon': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'sat_late_evening': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'sat_late_morning': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'sat_overnight': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'sitter': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['app.Sitter']", 'unique': 'True'}),
            'sun_early_afternoon': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'sun_early_evening': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'sun_early_morning': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'sun_late_afternoon': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'sun_late_evening': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'sun_late_morning': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'sun_overnight': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'thu_early_afternoon': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'thu_early_evening': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'thu_early_morning': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'thu_late_afternoon': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'thu_late_evening': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'thu_late_morning': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'thu_overnight': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'tue_early_afternoon': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'tue_early_evening': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'tue_early_morning': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'tue_late_afternoon': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'tue_late_evening': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'tue_late_morning': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'tue_overnight': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'wed_early_afternoon': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'wed_early_evening': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'wed_early_morning': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'wed_late_afternoon': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'wed_late_evening': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'wed_late_morning': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'wed_overnight': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'app.settings': {
            'Meta': {'object_name': 'Settings'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'email_blog': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'email_booking_accepted_denied': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'email_booking_request': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'email_friend_joined': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'email_groups_added_network': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'email_new_review': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'email_news': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'email_upcoming_booking_remind': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobile_booking_accepted_denied': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'mobile_booking_request': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'mobile_friend_joined': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'mobile_groups_added_network': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'mobile_new_review': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'mobile_upcoming_booking_remind': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['app.User']", 'unique': 'True', 'null': 'True'})
        },
        u'app.sitter': {
            'Meta': {'object_name': 'Sitter', '_ormbases': [u'app.User']},
            'biography': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'cats_ok': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'certifications': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['app.Certification']", 'symmetrical': 'False', 'blank': 'True'}),
            'current_student': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'dob': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'dogs_ok': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'extra_exp': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "'female'", 'max_length': '10'}),
            'has_drivers_licence': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'highest_education': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'id_verified': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'infant_exp': ('django.db.models.fields.SmallIntegerField', [], {'blank': 'True'}),
            'last_school': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'major': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'occupation': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'one_child_max_rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'one_child_min_rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'other_animals_ok': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'other_services': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['app.OtherService']", 'symmetrical': 'False', 'blank': 'True'}),
            'pre_teen_exp': ('django.db.models.fields.SmallIntegerField', [], {'blank': 'True'}),
            'preschool_exp': ('django.db.models.fields.SmallIntegerField', [], {'blank': 'True'}),
            'school_age_exp': ('django.db.models.fields.SmallIntegerField', [], {'blank': 'True'}),
            'sick': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'smoker': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'smokers_ok': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'special_needs_exp': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'teen_exp': ('django.db.models.fields.SmallIntegerField', [], {'blank': 'True'}),
            'three_child_max_rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'three_child_min_rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'toddler_exp': ('django.db.models.fields.SmallIntegerField', [], {'blank': 'True'}),
            'total_exp': ('django.db.models.fields.SmallIntegerField', [], {}),
            'travel_distance': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'two_child_max_rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'two_child_min_rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            u'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['app.User']", 'unique': 'True', 'primary_key': 'True'}),
            'will_transport': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'app.sitterreview': {
            'Meta': {'unique_together': "(('parent', 'sitter'),)", 'object_name': 'SitterReview'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reviews'", 'to': u"orm['app.Parent']"}),
            'recommended': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rehire': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'review': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'sitter': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reviews'", 'to': u"orm['app.Sitter']"})
        },
        u'app.specialneed': {
            'Meta': {'object_name': 'SpecialNeed'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'need': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'app.user': {
            'Meta': {'object_name': 'User'},
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'address2': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'avatar': ('pyuploadcare.dj.models.ImageField', [], {'blank': 'True'}),
            'cell': ('django.db.models.fields.CharField', [], {'max_length': '12', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'facebook_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'facebook_token': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'friends': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'friends_rel_+'", 'blank': 'True', 'to': u"orm['app.User']"}),
            'google_imported': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invited_by': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['app.User']", 'symmetrical': 'False', 'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'languages': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'users'", 'blank': 'True', 'to': u"orm['app.Language']"}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'membership_exp_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'sitter_groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['app.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'default': "'AL'", 'max_length': '2', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'Trial'", 'max_length': '10'}),
            'timezone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'users_in_network': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'users_in_network_rel_+'", 'blank': 'True', 'to': u"orm['app.User']"}),
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