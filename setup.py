from setuptools import find_packages, setup

with open('README.md', 'r') as readme:
    long_description = readme.read()

setup(
    name='arcpy_logging',
    package_dir={"": "src"},
    packages=find_packages('src'),
    install_requires=['pandas'],
    version='1.0.0-dev0',
    description='Integrating ArcPy messaging into standard Python logging',
    long_description=long_description,
    author='Joel McCune (https://github.com/knu2xs)',
    license='Apache 2.0'
)
