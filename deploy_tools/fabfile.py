__author__ = 'ddehertog'

from fabric.contrib.files import append, exists, sed
from fabric.api import env, local, run
import random

REPO_URL = 'https://github.com/dirkDH/awesomesite.git'

def deploy():
    site_folder = '/home/%s/sites/%s' % (env.user, env.host)
    source_folder = site_folder + '/source'
    create_directory_structure_if°necessary(site_folder)
    _get_latest_source(source_folder)
    _update_settings(source_folder, env.host)
    _update_virtualenv(source_folder)
    _update_static_files(source_folder)
    _update_database(source_folder)

def _get_latest_source(source_folder):
        if exists(source_folder + '/.git'):
            run('cd %s && git fetch' % (source_folder,))
        else:
            run('git clone %s %s' % (REPO_URL, source_folder))
        current_commit = local("git log -n 1 --format=%H", capture=True)
        run('cd %s && git reset --hard %s' % (source_folder, current_commit))