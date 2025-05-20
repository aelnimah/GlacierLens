import boto3
import os

# DynamoDB Configuration
TABLE_NAME = "IcebergData"
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(TABLE_NAME)

def query_by_id(iceberg_id):
    """ Query data by ID using the query operation """
    try:
        response = table.query(
            KeyConditionExpression=boto3.dynamodb.conditions.Key('ID').eq(iceberg_id)
        )
        items = response.get('Items', [])
        return items if items else f"No records found for ID: {iceberg_id}"
    except Exception as e:
        print(f"Error querying by ID: {e}")

def query_by_date_range(start_date, end_date):
    """ Query data by date range """
    try:
        response = table.scan()
        items = response['Items']
        filtered = [item for item in items if start_date <= item['Timestamp'] <= end_date]
        return filtered
    except Exception as e:
        print(f"Error querying by date range: {e}")

def query_by_size(size):
    """ Query data by iceberg size """
    try:
        response = table.scan()
        items = response['Items']
        filtered = [item for item in items if item['Size'] == size]
        return filtered
    except Exception as e:
        print(f"Error querying by size: {e}")

if __name__ == "__main__":
    # Test queries
    print("Query by ID (ICE-22):")
    print(query_by_id("ICE-22"))

    print("\nQuery by Date Range (10/01/20 to 10/03/20):")
    print(query_by_date_range("10/01/20", "10/03/20"))

    print("\nQuery by Size (GEN):")
    print(query_by_size("GEN"))
