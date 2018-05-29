import io
import xml.etree.ElementTree

import mousike.auth
import mousike.exception

API_VERSION = '1.0.0'
REQUIRED_PARAMETERS = [
    'u', # username
    'p', # password
    'v', # client API version
    'c', # client identifier
]
XML_NAMESPACE = 'http://subsonic.org/restapi'


def verify_request(parameters: dict):
    """
    """

    for parameter in REQUIRED_PARAMETERS:
        if parameter not in parameters or len(parameters[parameter]) < 1:
            raise mousike.exception.MissingParameter()

    try:
        check_version(parameters['v'][0])
        mousike.auth.authenticate_user(parameters['u'][0], parameters['p'][0])
    except mousike.exception.ApiError as e:
        raise


def check_version(version: str):
    """Checks a client API version for compatibility with the server.

    :param version: Three-part API version supported by the client.
    """

    server_major, server_minor, __ = API_VERSION.split('.')
    client_major, client_minor, __ = version.split('.')

    if client_major > server_major:
        raise mousike.exception.UpgradeServer()

    if client_major == server_major and client_minor > server_minor:
        raise mousike.exception.UpgradeServer()

    if client_major < server_major:
        raise mousike.exception.UpgradeClient()


def build_response(data: xml.etree.ElementTree.Element=None, status: str='ok'):
    """Adds data to a basic response and returns it as a string.

    :param data: XML data to include in the API response.
    :param status: Sets the status in the 'subsonic-response' root element.

    :return: The complete response as an XML-formatted string.
    """

    subsonic_response = xml.etree.ElementTree.Element(
        tag='subsonic-response', attrib={
            'status': status,
            'version': API_VERSION,
            'xmlns': XML_NAMESPACE,
        }
    )
    if data:
        subsonic_response.append(data)
    response_tree = xml.etree.ElementTree.ElementTree(subsonic_response)
    with io.StringIO as temp_buffer:
        response_tree.write(
            temp_buffer, encoding='UTF-8', xml_declaration=True,
            short_empty_elements=False
        )
        xml_string = temp_buffer.getvalue()

    return xml_string


def build_error(exception: mousike.exception.ApiError) -> str:
    """Build an error response from an exception.

    :param exception: API error to build an error response for.

    :return: XML-formatted Subsonic API error.
    """

    error_element = xml.etree.ElementTree.Element(
        tag='error', attrib={
            'code': exception.code,
            'message': exception.message,
        }
    )

    return build_response(error_element, 'failed')
