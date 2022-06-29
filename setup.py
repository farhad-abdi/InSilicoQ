from setuptools import setup

long_description = open("README.md").read()

setup(
    name='insilicoq',
    version='0.1',
    description='A Python package for Quantum Computation based Drug Desgin.',
    long_description_content_type="text/markdown",
    long_description=long_description,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering :: Chemistry, Physics',
        'Operating System :: Linux',
        'Programming Language :: Python'
        ],
    url='https://github.com/QaiAbdi/InSilicoQ',
    author='Farhad Abdi',
    author_email='qai.abdi@gmail.com',
    license='MIT',
    packages=['insilicoq'],
    install_requires=[],
    include_package_data=True,
    package_data={
        
    },
    zip_safe=False
)