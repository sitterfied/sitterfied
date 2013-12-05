from django.conf import settings

import hmac, hashlib

def generate_intercom_user_hash(user_id_or_email):
    return hmac.new(settings.INTERCOM_API_SECRET, user_id_or_email, digestmod=hashlib.sha256).hexdigest()