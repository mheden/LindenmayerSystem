from setuptools import setup, find_packages


def readme():
    with open("README.rst") as f:
        return f.read()


setup(
    name="lindenmayer",
    version="0.9.0",
    description="A simple package for creating Lindenmayer System Curves",
    long_description=readme(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent" "Topic :: Multimedia :: Graphics",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="Lindenmayer l-system lsystem",
    url="http://github.com/mheden/LindenmayerSystem",
    author="Mikael Heden",
    author_email="mikael@heden.net",
    license="BSD",
    packages=find_packages(),
    install_requires=[],
    include_package_data=True,
    zip_safe=False,
)
