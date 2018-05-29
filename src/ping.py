import mousike.api
import mousike.exception


def lambda_handler(event, context):
    """Handle the ping API method
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
