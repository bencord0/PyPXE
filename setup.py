from setuptools import setup

setup(
    name="PyPXE",
    version="1.0",
    entry_points={
        'console_scripts': [
            'pypxe = pypxe.__main__:main',
    ]},
)
