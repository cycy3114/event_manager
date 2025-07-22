cat <<EOT > setup.py
from setuptools import setup, find_packages

setup(
    name="event_manager",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # Add your dependencies here
        "fastapi",
        "sqlalchemy",
        "pydantic",
    ],
)
EOT
