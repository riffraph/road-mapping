import io
from setuptools import setup, find_packages

setup(
    name='road_mapping',
    version='0.1.0',
    license='GNU General Public License v3.0',
    description='',
    author='Raphael Chan',
    url='https://github.com/riffraph/road-mapping',
    packages=find_packages(),
    platforms='any',
    long_description=io.open('README.md', encoding='utf-8').read()
)