import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='vortexasdk',
    version='0.1.0-dev5',
    author='Vortexa Developers',
    author_email='developers@vortexa.com',
    description='Vortexa SDK',
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    url='https://github.com/V0RT3X4/python-sdk',
    license='Apache License 2.0',
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[
        'pandas==0.25.2',
        'six==1.12.0',
        'requests==2.22.0',
        'flake8==3.7.9',
        'pre-commit==1.20.0',
        'jsons==1.0.0',
        'nose2==0.9.1',
        'flatten-dict==0.2.0',
        'pydoc-markdown==2.0.4'
    ]
)
