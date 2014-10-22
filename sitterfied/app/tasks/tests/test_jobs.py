# -*- coding: utf-8 -*-
from datetime import datetime

import pytz
from django.db import transaction
from hamcrest import *

from sitterfied.app.tasks import jobs


@transaction.commit_manually
def test_check_for_completed_jobs():
    try:
        count = len(jobs.get_jobs_completed_since(datetime.now(pytz.UTC)))
        assert_that(jobs.check_for_completed_jobs(), is_(count))
    finally:
        transaction.rollback()


@transaction.commit_manually
def test_check_for_canceled_jobs_with_incorrect_status():
    try:
        count = len(jobs.get_canceled_jobs_with_incorrect_status())
        assert_that(jobs.check_for_canceled_jobs_with_incorrect_status(), is_(count))
    finally:
        transaction.rollback()
