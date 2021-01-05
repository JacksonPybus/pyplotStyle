import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pyplotStyle',
    version='0.1.0',
    author='Jackson Pybus',
    author_email='jrpybus@mit.edu',
    description='A package of plotting functions for pyplot figures',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/JacksonPybus/pyplotStyle',
    packages = setuptools.find_packages(),
    python_requires='>=3.7',
    install_requires=['matplotlib',                     
                      ]
)
