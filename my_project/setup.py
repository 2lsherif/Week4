from setuptools import setup, find_packages

setup(
    name="my_web_app",
    version="0.1",
    packages=find_packages(),
    install_requires=["flask"],
    entry_points={
        'console_scripts': [
            'run-my-web-app=app.app:main',
        ],
    },
)
