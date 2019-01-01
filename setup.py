from setuptools import setup, find_packages

setup(
    name='hodl_db',
    version='0.1',
    description='Asynchronous, encrypted database based on sqlite',
    author='pufit',
    packages=find_packages(),
    install_requires=['twisted >= 12.1', 'six']
)
