from setuptools import setup, find_packages

setup(
    name='order_tracker',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Django',
        'djangorestframework',
        'djangorestframework-simplejwt',
        'drf-yasg',
    ],
)
