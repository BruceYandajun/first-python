from setuptools import setup

setup(
    name="das",
    version="1.0",
    packages=["base"],
    entry_points={
        'console_scripts': ['etl-pipeline = etl_pipeline.core.console:main']
    }
)

