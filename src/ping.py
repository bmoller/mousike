import mousike.api
import mousike.exception


def lambda_handler(event: dict, context) -> dict:
    """Handles the `ping` API method.

    Used to test connectivity with the server. Takes no extra parameters.

    Returns an empty `<subsonic-response>` element on success.

    :param event: Passed by AWS Lambda to all function invocations.
    """

    try:
        mousike.api.verify_request(event['queryStringParameters'])
        body = mousike.api.build_response()

    except mousike.exception.ApiError as e:
        body = mousike.api.build_error(e)

    return {
        'body': body,
        'headers': {
            'Content-Type': 'text/xml',
        },
        'statusCode': 200,
    }
