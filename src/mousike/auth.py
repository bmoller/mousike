import base64
import hashlib
import os

import boto3

import mousike.exception

DYNAMODB_USERS_TABLE = os.environ['DYNAMODB_USERS_TABLE']

def authenticate_user(username: str, password: str) -> bool:
    """Authenticate a user and password.

    Args:
        username: Username of the user to be authenticated.
        password: Either the password of the user in plain-text, or hex-encoded
            with 'enc:' as a prefix.

    Returns:
        True if the authentication was successful, otherwise False.
    """

    dynamodb = boto3.resource('dynamodb')
    users_table = dynamodb.Table(DYNAMODB_USERS_TABLE)
    user = users_table.get_item(
        Key={
            'username': user,
        }
    ).get('Item')

    if password.startswith('enc:'):
        password = base64.b16decode(password)

    hasher = hashlib.sha256()
    hasher.update(password)
    computed_digest = hasher.hexdigest()

    if computed_digest != user['password']:
        raise mousike.exception.AuthenticationFailure()
