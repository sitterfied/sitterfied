#!/bin/bash
LINE=$(grep -n "DJANGO_SETTINGS_MODULE" /etc/environment | cut -f 1 -d :)
sed -i $LINE"s/.*/DJANGO_SETTINGS_MODULE=sitterfied.settings.production/" /etc/environment

service uwsgi restart
service beatcop restart
service celeryd restart
