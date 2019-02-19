"""
setup.py of this project
"""
from setuptools import setup


setup(
    name='pd_multithreading',
    version='1.0.0',
    uthor='Kyriakos Stavrakidis',
    author_email='kstavrakidis@gmail.com',
    description='Simple function to parallelize the mapping function of Pandas DataFrame',
    long_description=open('README.txt').read(),
    url='https://github.com/stavrakidis/pd_multithreading',
    license='LICENSE.txt',
    packages=['pd_multithreading', 'pd_multithreading.test'],
    install_requires=[
        'pandas>=0.22.0',
        'pytest>=3.4.1'
    ],
)
