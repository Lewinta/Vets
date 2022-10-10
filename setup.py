from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in vets/__init__.py
from vets import __version__ as version

setup(
	name="vets",
	version=version,
	description="A Custom app for Veterinary",
	author="Lewin Villar",
	author_email="lewin.villar@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
