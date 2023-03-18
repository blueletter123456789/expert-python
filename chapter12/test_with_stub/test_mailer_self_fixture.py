import smtplib

import pytest

from mailer import send


class FakeSMTP(object):

    def __init__(self, *args, **kwargs):
        pass

    def quit(self, *arge, **kwargs):
        pass

    def sendmail(*args, **kwargs):
        return {}


@pytest.fixture()
def patch_smtplib():
    # setup処理: smtplibに対するモンキーパッチ
    old_smtp = smtplib.SMTP
    smtplib.SMTP = FakeSMTP
    yield

    # teardown処理: smtplibをモンキーパッチ適用前に戻す
    smtplib.SMTP = old_smtp


def test_send_message(patch_smtplib):
    res = send(
        sender="john.doe@example.com",
        to="john.doe@example.com",
        subject="topic",
        body="body message"
    )

    assert res == {}
