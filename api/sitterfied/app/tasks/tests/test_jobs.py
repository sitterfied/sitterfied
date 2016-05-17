# -*- coding: utf-8 -*-
from django.db import transaction
from hamcrest import *

from sitterfied.app.tasks import jobs


def test_check_for_completed_jobs():
    transaction.set_autocommit(False)
    try:
        count = len(jobs.get_jobs_completed_since(time.now()))
        assert_that(jobs.check_for_completed_jobs(), is_(count))
    finally:
        transaction.rollback()
        transaction.set_autocommit(True)


def test_check_for_canceled_jobs_with_incorrect_status():
    transaction.set_autocommit(False)
    try:
        count = len(jobs.get_canceled_jobs_with_incorrect_status())
        assert_that(jobs.check_for_canceled_jobs_with_incorrect_status(), is_(count))
    finally:
        transaction.rollback()
        transaction.set_autocommit(True)
