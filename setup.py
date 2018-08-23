from setuptools import find_packages, setup

setup(
    name='djangocms_random_data_generator',
    version='0.0.1',
    python_requires='',
    url='',
    author='Aikman Ltd',
    author_email='aiky30@yahoo.com',
    description='A data generator for the Django CMS library',
    long_description='README.md',
    license='LGPL',
    packages=[],
    include_package_data=True,
    scripts=[],
    entry_points={'console_scripts': [
        'generate = django.core.management:generate',
    ]},
    install_requires=[
        'django',
        'django-cms'
    ],
    extras_require={},
    zip_safe=False,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    project_urls={
    },
)