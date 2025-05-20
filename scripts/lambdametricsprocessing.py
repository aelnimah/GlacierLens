import boto3
import json

# Configuration
LAMBDA_FUNCTION_NAME = "IcebergMetricsProcessor"

def trigger_metrics_processing():
    """
    Trigger the Lambda function for metrics processing.
    """
    lambda_client = boto3.client('lambda')

    try:
        # Construct a simple event payload
        event_payload = {
            "action": "process_metrics"
        }

        # Invoke the Lambda function
        response = lambda_client.invoke(
            FunctionName=LAMBDA_FUNCTION_NAME,
            InvocationType='RequestResponse',
            Payload=json.dumps(event_payload)
        )

        # Read the response
        response_payload = json.loads(response['Payload'].read())
        print(f"Lambda response: {response_payload}")

    except Exception as e:
        print(f"Error triggering Lambda metrics processing: {str(e)}")
