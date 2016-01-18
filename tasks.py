from invoke import run, task

from bash import git

from toolbelt import VERSION

# Utilities

def run_venv(cmd):
    run('source env/bin/activate && %s' % cmd)

# Tasks

@task
def bootstrap():
    print('Configuring application')
    run('virtualenv env -p python3.4')
    deps()
    print('Bootstrap success')

@task
def deps():
    run_venv('pip install -r requirements.txt')

@task
def clean():
    run('rm -rf ~*')
    run('rm -rf *.pyc *.pyo')
    run('rm -rf data/')
    run('rm -rf *.egg-info')
    run('rm -rf dist/')

@task
def test():
    run('tox')

@task
def tag():
    git.create_tag(VERSION)

@task
def reset_tag():
    git.reset_tag(VERSION)

@task
def first_publish():
    run_venv('python setup.py sdist')
    run_venv('python setup.py register')
    publish()

@task
def publish():
    tag()
    # http://guide.python-distribute.org/quickstart.html
    # python setup.py sdist
    # python setup.py register
    # Create a .pypirc file in ~ dir (cp .pypirc ~)
    # python setup.py sdist upload
    # Manual upload to PypI
    # http://pypi.python.org/pypi/THE-PROJECT
    # Go to 'edit' link
    # Update version and save
    # Go to 'files' link and upload the file
    run_venv('python setup.py sdist upload')

@task
def republish():
    reset_tag()
    publish()
