import setuptools

requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

readme = ''
with open('README.md') as f:
    readme = f.read()

setuptools.setup(
    name='libavc.py',
    author="tamamu"
    url='https://github.com/iwatepu-cpc/libavc.py',
    version=0.1.0,
    packages=setuptools.find_packages(),
    license='MIT',
    description='AtCoder Virtual Contest Library for Python',
    long_description=readme,
    long_description_content_type='text/markdown',
    include_package_data=True,
    install_requires=requirements,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities', 
    ]
)
