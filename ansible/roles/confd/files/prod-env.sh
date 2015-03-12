#!/bin/bash -x

# Export environment variables
export PRODUCTION_SITTERFIED_WEBSITE_CELERY_BROKER_URL=amqp://skcgsiqg:9elSAgOlB78PubEJso7YyNqgvbKp4dTq@turtle.rmq.cloudamqp.com/skcgsiqg
export PRODUCTION_SITTERFIED_WEBSITE_CELERY_CONCURRENCY=2
export PRODUCTION_SITTERFIED_WEBSITE_CELERY_DEFAULT_QUEUE=sitterfied-production
export PRODUCTION_SITTERFIED_WEBSITE_CELERY_QUEUE_NAME_PREFIX=production-
export PRODUCTION_SITTERFIED_WEBSITE_CELERY_WORKERS=worker1
export PRODUCTION_SITTERFIED_WEBSITE_DATABASE_HOST=website-prod-website-server-database.cd92rfe8vffs.us-east-1.rds.amazonaws.com
export PRODUCTION_SITTERFIED_WEBSITE_DATABASE_PASSWORD=XXcCBqyRsHWA3D2
export PRODUCTION_SITTERFIED_WEBSITE_DEBUG=False
export PRODUCTION_SITTERFIED_WEBSITE_ELASTICACHE_ENDPOINT=website-prod-001.ug6jhv.0001.use1.cache.amazonaws.com:6379
export PRODUCTION_SITTERFIED_WEBSITE_ENVIRONMENT=production
export PRODUCTION_SITTERFIED_WEBSITE_SERVER_EMAIL=no-reply@sitterfied.com
export PRODUCTION_SITTERFIED_WEBSITE_SESSION_COOKIE_NAME=sitterfied-production

# run confd to generate configs
if [[ -f /etc/confd/confd.toml ]]; then
	/usr/local/bin/confd -onetime
fi

# Restart services
service monit restart

exit 0
