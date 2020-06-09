import setuptools
from pathlib import Path

setuptools.setup(
    name="instagram-scraper",
    version="0.1",
    description=('scrapes medias, likes, followers, tags and all metadata'),
    long_description='forked version of igscraper : https://github.com/realsirjoe/instagram-scraper',
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    license="MIT",
    maintainer="realsirjoe, leungwaiban",
    author='realsirjoe, leungwaiban',
    url='https://github.com/Celtcoste/instagram-scraper',
    install_requires=[
        'requests>=2.21.0',
        'python-slugify==3.0.2'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries'
    ],
)
