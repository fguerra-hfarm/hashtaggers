import os
import setuptools


"""Hashtagger Analytics Package full details and requirements."""

with open(os.path.dirname(os.path.abspath(__file__))
          + '/README.md', 'r') as ld:
    long_description = ld.read()

setuptools.setup(
    name='hashtagger_analytics',
    version='1.0',
    description='Service to extrapolate insights regarding hashtags '
                'used on Twitter! ''Provided under paid license of the '
                'Hashtagify API for best accuracy',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/fguerra-hfarm/hashtaggers',
    license='GNU General Public License v3.0',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: End Users/Desktop',
        'Natural Language :: English',
        'Topic :: Social Analytics :: Hashtags :: Twitter hashtag insights',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3'],
    keywords='hashtagify, analytics, twitter, hashtags, '
             'university, api, python',
    packages=setuptools.find_packages(
        include=['hashtagify_package', 'hashtagify_package.*',
                 'use_csv_package', 'use_csv_package.*']),
    python_requires='>=3',
    install_requires=['argparse', 'tabulate', 'setuptools',
                      'requests', 'datapackage']
)
