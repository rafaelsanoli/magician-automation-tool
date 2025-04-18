from setuptools import setup, find_packages

setup(
    name="automation-tool",
    version="0.1.0",
    packages=find_packages(include=["core*", "plugins*"]),
    install_requires=[
        "pyautogui",
        "schedule",
        "pytest"
    ],
)
