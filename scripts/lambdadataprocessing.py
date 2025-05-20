import boto3
import json

BUCKET_NAME = 'icebergpro-data'
LAMBDA_FUNCTION_NAME = "IcebergDataProcessor"

def trigger_data_processing():
    """
    Trigger the Lambda function for data processing.
    """
    lambda_client = boto3.client('lambda')

    event_payload = {
        "Records": [
            {
                "s3": {
                    "bucket": {"name": BUCKET_NAME},
                    "object": {"key": "2021Icebergs.json"}
                }
            }
        ]
    }

    try:
        response = lambda_client.invoke(
            FunctionName=LAMBDA_FUNCTION_NAME,
            InvocationType='RequestResponse',
            Payload=json.dumps(event_payload)
        )

        # Simplified response handling
        payload = response['Payload'].read().decode('utf-8')
        print(f"Lambda Response: {payload}")

    except Exception as e:
        print(f"Error triggering Lambda: {e}")
