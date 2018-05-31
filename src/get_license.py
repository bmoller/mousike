import datetime
import os
import xml.etree.ElementTree

import mousike.api
import mousike.exception

LICENSE_EMAIL = os.environ['LICENSE_EMAIL']
LICENSE_VALIDITY = datetime.timedelta(days=90)
TIMESTAMP_FORMAT = '%Y-%m-%dT%H:%M:%S'


def lambda_handler(event: dict, context) -> dict:
    """Handles the `ping` API method.

    Used to test connectivity with the server. Takes no extra parameters.

    Returns an empty `<subsonic-response>` element on success.

    :param event: Passed by AWS Lambda to all function invocations.
    """

    license_expiration = datetime.datetime.now() + LICENSE_VALIDITY
    license_attributes = {
        'email': LICENSE_EMAIL,
        'licenseExpires': license_expiration.strftime(TIMESTAMP_FORMAT),
        'valid': 'true',
    }

    try:
        mousike.api.verify_request(event['queryStringParameters'])
        license_element = xml.etree.ElementTree.Element(
            'license', attrib=license_attributes)
        body = mousike.api.build_response(data=license_element)

    except mousike.exception.ApiError as e:
        body = mousike.api.build_error(e)

    return {
        'body': body,
        'headers': {
            'Content-Type': 'text/xml',
        },
        'statusCode': 200,
    }
