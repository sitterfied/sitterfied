# -*- coding: utf-8 -*-
import logging
import re


class IgnoreRegularExpressionFilter(logging.Filter):
    """
    Do not log the message if it can be matched to the given regular expression.

    """
    def __init__(self, pattern, *args, **kwargs):
        self.pattern = re.compile(pattern)
        super(IgnoreRegularExpressionFilter, self).__init__(*args, **kwargs)

    def filter(self, record):
        if self.pattern.search(record.msg):
            return False

        return True
