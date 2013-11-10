from setuptools import setup


setup_args = dict(
    name='gae-sessions',
    version='1.0.7',
    license='Apache',
    description='Fast, lightweight Sessions middleware for Google App Engine '
                '(secure cookies, memcache, or datastore)',
    author='David Underhill',
    author_email='dgu@cs.stanford.edu',
    url='https://github.com/dound/gae-sessions',
    packages=['gaesessions'],
    namespace_packages=['gaesessions'],
    zip_safe=False,
    platforms='any',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: Apache',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)


if __name__ == '__main__':
    setup(**setup_args)
