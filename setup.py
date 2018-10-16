from setuptools import setup, find_packages

setup(
    name='road_mapping',
    version='0.1.0',
    license='',
    description='',
    author='Raphael Chan',
    url='https://github.com/riffraph/road-mapping',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    setup_requires=["pytest-runner"],
    tests_require=["pytest"]
)