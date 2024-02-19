import json

def lambda_handler(event, context):
    # Event contains the input data for the Lambda function
    # Context provides runtime information about the Lambda function

    # Extracting information from the event
    name = event.get('name', 'Guest')

    # Creating a response
    response = {
        'statusCode': 200,
        'body': json.dumps({'message': f'Hello, {name}! This is a simple Lambda function.'})
    }

    return response
