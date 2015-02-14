#!/bin/bash -x

# Export environment variables
export TEST_SITTERFIED_WEBSITE_CELERY_CONCURRENCY=2
export TEST_SITTERFIED_WEBSITE_CELERY_DEFAULT_QUEUE=sitterfied-test
export TEST_SITTERFIED_WEBSITE_CELERY_QUEUE_NAME_PREFIX=test-
export TEST_SITTERFIED_WEBSITE_CELERY_WORKERS=2
export TEST_SITTERFIED_WEBSITE_DATABASE_HOST=website-test-website-server-database.cd92rfe8vffs.us-east-1.rds.amazonaws.com 
export TEST_SITTERFIED_WEBSITE_DATABASE_PASSWORD=^uM*e3xj79eFLrc
export TEST_SITTERFIED_WEBSITE_DEBUG=True
export TEST_SITTERFIED_WEBSITE_ELASTICACHE_ENDPOINT=website-test.ug6jhv.0001.use1.cache.amazonaws.com:6379 
export TEST_SITTERFIED_WEBSITE_LOG_LEVEL=DEBUG
export TEST_SITTERFIED_WEBSITE_SERVER_EMAIL=no-reply@test.sitterfied.com
export TEST_SITTERFIED_WEBSITE_SESSION_COOKIE_NAME=sitterfied-test

# switch the confd key prefix from production to test and reprocess all templates
if [[ -f /etc/confd/confd.toml ]]; then
	/bin/sed -i 's|"/production"|"/test"|' /etc/confd/confd.toml
	/usr/local/bin/confd -onetime
fi

# Restart services that depend on the Django settings file
service beatcop restart
service celery restart

exit 0
