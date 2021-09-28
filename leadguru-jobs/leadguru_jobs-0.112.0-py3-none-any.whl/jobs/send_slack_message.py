import datetime
from abc import ABC
from typing import List

import pytz
from lgt.common.python.lgt_logging import log
from lgt.common.python.slack_client.slack_client import SlackClient
from lgt.common.python.slack_client.web_client import SlackWebClient, get_slack_credentials
from lgt_data.model import UserBotCredentialsModel, UserModel
from lgt_data.mongo_repository import UserMongoRepository, \
    UserBotCredentialsMongoRepository, DedicatedBotRepository, UserLeadMongoRepository
from pydantic import BaseModel

from ..runner import BackgroundJobRunner
from ..basejobs import BaseBackgroundJobData, BaseBackgroundJob

"""
Send Slack Message
"""
class SendSlackMessageJobData(BaseBackgroundJobData, BaseModel):
    lead_id: str
    user_id: str
    text: str

class SendSlackMessageJob(BaseBackgroundJob):
    @property
    def job_data_type(self) -> type:
        return SendSlackMessageJobData

    def exec(self, data: SendSlackMessageJobData):
        user = UserMongoRepository().get(data.user_id)
        lead = UserLeadMongoRepository().get_lead(user_id=data.user_id, lead_id=data.lead_id)
        if not lead:
            return

        cred = get_slack_credentials(user, lead, update_expired=False)
        if not cred or cred.invalid_creds:
            return

        slack_client = SlackWebClient(cred.token, cred.cookies)
        resp = slack_client.im_open(lead.message.sender_id)
        if not resp['ok']:
            log.warning(f"Unable to open im with user: {resp}")
            return

        channel_id = resp['channel']['id']
        resp = slack_client.post_message(channel_id, data.text)

        if not resp['ok']:
            return  log.warning(f"Unable to open send message: {resp}")