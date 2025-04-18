from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='KickISO',
    description='A Python package for interacting with the Kick API to retrieve channel and video data.',
    version='0.3.4',
    packages=find_packages(),
    install_requires=[
        'cloudscraper',
    ],
    license="MIT",
    keywords=['kick', 'api', 'kickapi'],
    long_description=long_description,
    long_description_content_type='text/markdown', 
    author="Tadeo",
    url='https://github.com/ISODev23/KickApiISO',
)
