from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in future_academy/__init__.py
from future_academy import __version__ as version

setup(
	name="future_academy",
	version=version,
	description="education app",
	author="omaima",
	author_email="omaima@test.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
