import os

from fabric.api import task, run, require, put, local, env


env.hosts = ['root@107.174.234.66']


class __Deploy:
    def deploy(self):
        self.just_test()
        # self.checkout_code()
        # self.install_system_packages()
        # self.install_python_requirements()
        # self.migrate_database()
        # self.collect_statics()
        # #self.test_new_deploy()
        # self.map_new_deployment()


    def checkout_code(self):
        datetime = 1
        run("cd ~/deploy")
        run("git clone github-link ~/deploy/deploy-" + datetime)
        self.deploy_dir = "~/deploy/deploy-" + datetime

    def install_system_packages(self):
        packages = ""
        run("apt-get install " + packages)

    def install_python_requirements(self):
        run("pip install -r {}requirements.txt")

    def migrate_database(self):
        run("python manage.py migrate")

    def collect_statics(self):
        run("python manage.py collectstatics")

    def map_new_deployment(self):
        run("rm ~/deploy/production")
        run("ln -sn ~/deploy/production {}".format(self.deploy_dir))
        run("restart supervisor")

def deploy():
    __Deploy().deploy()
