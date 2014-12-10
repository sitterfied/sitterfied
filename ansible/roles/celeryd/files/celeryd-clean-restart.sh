#!/usr/bin/env bash

/usr/bin/pkill -9 -f 'celery worker'
/usr/sbin/service celeryd restart

exit 0
