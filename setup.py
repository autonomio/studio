from setuptools import find_packages, setup

setup(
    name='studio',
    version='0.3.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'keras',
        'tensorflow==1.6',
        'pandas',
        'numpy==1.15.4',
        'talos',
        'sklearn',
        'requests',
        'plotly',
        'tables'
    ],
)
