from setuptools import setup

setup(
    name="removesoln",
    version="0.1.0",
    py_modules=['removesoln'],
    install_requires=["texsoup"],
    entry_points='''
        [console_scripts]
        removesoln=removesoln:main
    ''',
)
