from setuptools import setup, find_packages

setup(
    name='JETSON',
    version='0.1',
    packages=find_packages(),
    install_requires=['pyserial'],
    entry_points={
        'console_scripts': [
            'scanSerial = JETSON.scanSerial:main',
        ],
    },
    author='nht',
    author_email='nhthai173@gmail.com',
    description='JETSON package',
    license='MIT',
    keywords='jetson',
    url='https://github.com/nhthai173/JETSON',
)