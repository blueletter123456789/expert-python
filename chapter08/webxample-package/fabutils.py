import os

# 'devpi'を使って専用のパッケージインデックスを作ったとします
PYPI_URL = 'http://devpi.webxample.example.com'

# リリース版をインストールするリモートサーバーのパス
# リリースディレクトリはプロジェクトのバージョンごとに分かれており、
# それぞれが独立した仮想環境ディレクトリ。
# 'current' は最後にデプロイされたバージョンを指すシンボリックリンク。
# このシンボリックリンクはプロセス監視ツールなどで参照されるディレクトリパス。
# 例:
# .
# ├── 0.0.1
# ├── 0.0.2
# ├── 0.0.3
# ├── 0.1.0
# └── current -> 0.1.0/

REMOTE_PROJECT_LOCATION = "/var/projects/webxample"


def prepare_release(c):
    """ 新しいリリースのために、ソース配布物を作って専用の
    パッケージインデックスにアップロードする
    """
    c.local(f'python setup.py build sdist')
    c.local(f'twine upload --repository-url {PYPI_URL}')

def get_version(c):
    """ setuptools経由で、現在のバージョンを取得
    """
    return c.local('python setup.py --version').stdout.strip()

def switch_versions(c, version):
    """ シンボリックリンクを差し替えることでアトミックにバージョンを切り替える
    """
    new_version_path = os.path.join(REMOTE_PROJECT_LOCATION, version)
    temporary = os.path.join(REMOTE_PROJECT_LOCATION, 'next')
    desired = os.path.join(REMOTE_PROJECT_LOCATION, 'current')

    # すでにある場合も強制的にシンボリックリンクを作成
    c.run(f'ln -fsT {new_version_path} {temporary}')

    # mv -T によりこの操作をアトミックに行う
    c.run(f'mv -Tf {temporary} {desired}')
