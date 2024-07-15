from setuptools import setup, find_packages

setup(
    name='headerfiles',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
	# add deps here
    ],
    author='Cen Zhang',
    author_email='blbllhy@gmail.com',
    description='Header files inference for C/C++ projects',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/occia/headerfiles',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
