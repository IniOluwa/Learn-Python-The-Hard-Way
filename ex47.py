try:
	from setuptools import setup
except ImportError:
	from disutils.core import setup

config = {
	'description': 'ex47 Project',
	'author': 'IniOluwa',
	'url': 'url to get at it',
	'download_url': 'Where to download it'
	'author email': 'inioluwafageyinbo@gmail.com.',
	'version': '0.1',
	'install_requirements': ['nose'],
	'packages': ['ex47'],
	'scripts': [],
	'name': 'IniOluwa\'s project' 
}

setup(**config)

