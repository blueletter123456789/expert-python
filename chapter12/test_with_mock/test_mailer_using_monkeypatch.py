import smtplib
from unittest.mock import MagicMock

from mailer import send


def test_send(monkeypatch):
    smtp_mock = MagicMock()
    smtp_mock.sendmail.return_value = {}
    monkeypatch.setattr(
        smtplib,
        "SMTP",
        MagicMock(return_value=smtp_mock))

    res = send(
        sender="john.doe@example.com",
        to="john.doe@example.com",
        subject="topic",
        body="body message"
    )
    assert res == {}
