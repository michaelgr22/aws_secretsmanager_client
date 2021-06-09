from setuptools import setup

VERSION = '0.0.1'
DESCRIPTION = 'client to manage secrets from aws secretsmanager'
LONG_DESCRIPTION = 'client to manage secrets from aws secretsmanager'

# Setting up
setup(
    name="aws_secretsmanager_client",
    version=VERSION,
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=['aws_secretsmanager_client'],
    install_requires=['boto3', 'base64', 'botocore'],
)
