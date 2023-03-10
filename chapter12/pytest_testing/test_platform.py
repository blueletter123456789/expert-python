import sys

import pytest


@pytest.mark.skipif(
    sys.platform == "darwin",
    reason="MacOSX上では実行しない"
)
class TestPosixCalls:
    def test_function(self):
        """ Mac OS X プラットフォームではセットアップや実行は行わない
        """


# あらかじめskipを定義できる
skip_mac = pytest.mark.skipif(
    sys.platform == "darwin",
    reason="MacOSX上では実行しない"
)


@skip_mac
class TestPosixCalls2:
    def test_function(self):
        """ Mac OS X プラットフォームではセットアップや実行は行わない
        """


@pytest.mark.xfail(
    sys.platform == "darwin",
    reason="MacOSXでは実行しない"
)
class TestPosixFail:
    def test_function(self):
        """ Mac OS X では失敗しなければならない
        """
