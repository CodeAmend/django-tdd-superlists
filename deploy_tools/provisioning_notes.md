## Required packages:

* nginx
* Python3
* Git
* pip
* virtualenv

e.g.,, on Ubuntu:

	sudo apt-get install nfinx git puthon3 python3-pip
	sudo pip3 install virtualenv

## Nginx Virtual Host config

* see nginx.template.config
* replace SITENAME with, e.g., staging.my-domain.com

## Upstart Job

* see gunicorn-upstart.template.conf
* replace SITENAME with, e.g., staging.my-domain.com

## Folder structure:
Assume we have a user account at /home/username

/home/username
|__ sites
	|___ SITENAME
		|___ database
		|___ source
		|___ static
		|___ virtualenv
		
