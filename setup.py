import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pystyle',
    version='0.3.0',
    description='A package of plotting functions for pyplot figures',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/JacksonPybus/pystyle',
    author='Jackson Pybus',
    author_email='jrpybus@mit.edu',
    license='MIT',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Database',
        'Topic :: Scientific/Engineering',
        ],
    packages = setuptools.find_packages(),
    python_requires='>=3.7',
    install_requires=['numpy',
                      'matplotlib',                     
                      ]
)
