from fabric import task

from fabutils import *


@task
def uptime(c):
    """ uptimeコマンドをリモートホストで実行、接続を検証
    """
    c.run('uptime')


@task
def deploy(c):
    """ パッケージを作成してアプリケーションをデプロイ
    """

    version = get_version(c)

    pip_path = os.path.join(
        REMOTE_PROJECT_LOCATION, version, 'bin', 'pip'
    )

    if not c.run(f'test -d {REMOTE_PROJECT_LOCATION}', warn=True):
        # 起動直後のホストに初めてデプロイする場合、ディレクトリがないため作成
        c.run(f'mkdir -p {REMOTE_PROJECT_LOCATION}')
    
    with c.cd(REMOTE_PROJECT_LOCATION):
        # 新しい仮想環境を作成
        c.run(f'python3 -m venv {version}')

        c.run(f'{pip_path} install webxample=={version} --index-url {PYPI_URL}')

    switch_versions(c, version)
    # Circusをプロセス監視ツールとして使っていると仮定
    c.run('circusctl restart webxample')
