# app/management/commands/update_friends.py
# ./manage.py update_friends

import json
import logging

from ecl_tools.utils import Redis
from app.models import User
from ecl_facebook import Facebook

logger = logging.getLogger(__name__)

r = Redis()
channel = r.pubsub()
channel.subscribe("facebook_friends")
logger.debug("Streaming updates running...")
for message in channel.listen():
    user_id = message['data']
    logger.debug("started")
    logger.debug(user_id)
    try:
        user = User.objects.get(id=user_id)
        fb = Facebook(user.facebook_token)
        response = fb.me.friends()
        for friend in response['data']:
            logger.debug("Friend Retrieved: {}".format(friend['id']))
            try:
                new_user = User.objects.get(facebook_id=friend['id'])
                if new_user:
                    new_user.followers.add(user)
            except:
                pass

    except:
        pass
