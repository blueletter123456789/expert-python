import smtplib
from unittest.mock import patch

from mailer import send


def test_send():
    with patch("smtplib.SMTP") as mock:
        # モックが返す値(SMTPクラスのモック)
        instance = mock.return_value
        # SMTPクラスのモックが返す値
        instance.sendmail.return_value = {}

        res = send(
            sender="john.doe@example.com",
            to="john.doe@example.com",
            subject="topic",
            body="body message"
        )
        assert res == {}
