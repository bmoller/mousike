class ApiError(Exception):
    """Base class for all API error exceptions.
    """

    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message


class GenericError(ApiError):

    def __init__(self):
        super().__init__(self, 0, 'A generic error.')


class MissingParameter(ApiError):

    def __init__(self):
        super().__init__(self, 10, 'Required parameter is missing.')


class UpgradeClient(ApiError):

    def __init__(self):
        super().__init__(self, 20, 'Incompatible Subsonic REST protocol version. Client must upgrade.')


class UpgradeServer(ApiError):

    def __init__(self):
        super().__init__(self, 30, 'Incompatible Subsonic REST protocol version. Server must upgrade.')


class AuthenticationFailure(ApiError):

    def __init__(self):
        super().__init__(self, 40, 'Wrong username or password.')


class LDAPTokenUnsupported(ApiError):

    def __init__(self):
        super().__init__(self, 41, 'Token authentication not supported for LDAP users.')


class UserUnauthorized(ApiError):

    def __init__(self):
        super().__init__(self, 50, 'User is not authorized for the given operation.')


class ExpiredTrial(ApiError):

    def __init__(self):
        super().__init__(self, 60, 'The trial period for the Subsonic server is over. Please upgrade to Subsonic Premium. Visit subsonic.org for details.')


class DataNotFound(ApiError):

    def __init__(self):
        super().__init__(self, 70, 'The requested data was not found.')
