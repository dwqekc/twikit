import re

from setuptools import setup

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

with open('./twikit/__init__.py') as f:
    version = re.findall(r"__version__ = '(.+)'", f.read())[0]

setup(
    name='twikit',
    version=version,
    install_requires=[
        'httpx[socks]',
        'filetype',
        'beautifulsoup4',
        'pyotp',
        'lxml',
        'webvtt-py',
        'm3u8',
        'js2py @ git+https://github.com/d60/Js2Py.git@py3.12'
    ],
    python_requires='>=3.8',
    description='Twitter API wrapper for python with **no API key required**.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    url='https://github.com/d60/twikit',
    package_data={'twikit': ['py.typed']}
)
