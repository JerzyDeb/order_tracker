from setuptools import setup, find_packages

setup(
    name='ordertracker',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Django',
        'djangorestframework',
        'djangorestframework-simplejwt',
        'drf-yasg==1.21.7',
    ],
)
