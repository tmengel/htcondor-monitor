# CondorExporter/setup.py
from setuptools import setup, find_packages

setup(
    name="CondorExporter",
    version="0.1",
    packages=find_packages(),  # Automatically finds 'exporter' and its submodules
    install_requires=open("requirements.txt").read().splitlines(),
    entry_points={
        'console_scripts': [
            'condor-exporter=exporter.CondorExporter:main',
        ]
    },
)
