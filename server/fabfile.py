import os
from fabric import task
from fabric import Connection
from invoke import run as local

server_dir = '/home/project/blog-server'
web_tmp_dir = '/home/project/blog-server/tmp'
tmp_dir = f'/tmp/blog-server{os.getpid()}/'

def _set_user_dir(c):
    global server_dir
    c.run('id root', warn=True)

def _prepare_local_website(install='true'):
    local(f'mkdir -p {tmp_dir}')
    local(f'cp -v bandwidth_api.py nginx.conf *.sh {tmp_dir}')

@task
def prepare_remote_dirs(c):
    _set_user_dir(c)
    if not c.run(f'test -d {server_dir}', warn=True).ok:
        c.sudo(f'mkdir -p {server_dir}')
    c.sudo(f'chmod -R 755 {server_dir}')
    if not c.run(f'test -d {web_tmp_dir}', warn=True).ok:
        c.sudo(f'mkdir -p {web_tmp_dir}')
    c.sudo(f'chmod -R 777 {web_tmp_dir}')
    c.sudo(f'chown -R root:root {server_dir}')

@task
def chmod_tmp(c):
    c.run(f'chmod -R 777 {web_tmp_dir}')

@task
def chown(c):
    c.sudo(f'chown -R root:root {server_dir}')

def _clean_local_dir():
    local(f'rm -rf {tmp_dir}')

@task
def host_type(c):
    c.run('uname -s')

@task
def deploy(c, install='false'):
    _prepare_local_website(install)
    prepare_remote_dirs(c)
    rsync_command = (f'rsync -avz '
                     f'--rsync-path="sudo rsync" '
                     f'{tmp_dir}/ {c.user}@{c.host}:{server_dir}')
    c.local(rsync_command)
    chmod_tmp(c)
    chown(c)
    _clean_local_dir()

