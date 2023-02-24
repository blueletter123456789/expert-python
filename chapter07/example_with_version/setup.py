from setuptools import setup
import os


def get_version(version_tuple):
    # アルファ(α), ベータ(β), リリース候補(rc)
    # というタグを取り扱うためのコード
    # バージョンスキーマによっては簡略化可能
    if not isinstance(version_tuple[-1], int):
        return '.'.join(
            map(str, version_tuple[:-1])
        ) + version_tuple[-1]
    return '.'.join(map(str, version_tuple))

# プロジェクトのソースツリー内のパッケージ
# __init__モジュールへのパス
init = os.path.join(
    os.path.dirname(__file__), 'src', 'some_package',
    '__init__.py'
)

with open(init, encoding='utf-8') as f:
    version_line = [L for L in f if L.startswith("VERSION")][0]

# VERSIONはタプルのため、version_lineをevalする必要がある
# このパッケージがインストール前にもimportが可能であれば、
# 単純にimportする方法も使える
PKG_VERSION = get_version(eval(version_line.split('=')[-1]))
setup(
    name='some-package',
    version=PKG_VERSION,
    # ...
)
