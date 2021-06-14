from setuptools import setup, find_packages

setup(
    name             = 'pygifconverter',
    version          = '1.0.1',
    description      = 'Test package for distribution',
    author           = 'lih0905',
    author_email     = 'lih0905@gmail.com',
    url              = '',
    download_url     = '',
    install_requires = ['pillow'],
	include_package_data=True,
	packages=find_packages(),
    keywords         = ['GIFCONVERTER', 'gifconverter'],
    python_requires  = '>=3',
    zip_safe=False,
    classifiers      = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
) 