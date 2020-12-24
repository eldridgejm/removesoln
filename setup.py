from setuptools import setup

setup(
    name="replacesoln",
    version="0.1.0",
    py_modules=['replacesoln'],
    install_requires=["texsoup"],
    entry_points='''
        [console_scripts]
        replacesoln=replacesoln:main
    ''',
)
