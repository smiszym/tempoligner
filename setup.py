from setuptools import setup, find_packages

setup(
    name="tempoligner",
    version="0.1",
    packages=find_packages(),
    install_requires=['pydub==0.21.0'],
    author="Michał Szymański",
    author_email="smiszym@gmail.com",
    description="Automatic song tempo aligner",
    license="MIT",
    url="https://github.com/smiszym/tempoligner"
)
