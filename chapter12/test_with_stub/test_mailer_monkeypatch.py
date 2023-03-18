import smtplib

from mailer import send


class FakeSMTP(object):

    def __init__(self, *args, **kwargs):
        pass

    def quit(self, *arge, **kwargs):
        pass

    def sendmail(*args, **kwargs):
        return {}


def test_send_message(monkeypatch):
    monkeypatch.setattr(smtplib, "SMTP", FakeSMTP)
    res = send(
        sender="john.doe@example.com",
        to="john.doe@example.com",
        subject="topic",
        body="body message"
    )

    assert res == {}
