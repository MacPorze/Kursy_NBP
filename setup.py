import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Kursy_NBP",
    version="0.0.1",
    author="Maciej Porzezynski",
    author_email="maciej.porzezynski@runbeachmorning.pl",
    description="Application to show currency rates",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com",
    packages=setuptools.find_packages(),
    install_requires=[
        'pyramid',
        'requests',
        'sqlalchemy',
        'pyramid_chameleon',
    ],
    classifiers=[
        'programming Language :: Python :: 3',
        'Framework :: Pyramid',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    include_package_data=True,
)