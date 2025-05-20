from flask import Flask, jsonify, request, send_from_directory
import boto3
import os

app = Flask(__name__)

# DynamoDB Configuration
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('IcebergData')

@app.route('/')
def serve_index():
    return send_from_directory(os.path.join(os.path.dirname(__file__), '..', 'frontend'), 'index.html')

@app.route('/script.js')
def serve_script():
    return send_from_directory(os.path.join(os.path.dirname(__file__), '..', 'frontend'), 'script.js')

@app.route('/api/data')
def get_data():
    """ Fetch all data """
    try:
        response = table.scan()
        data = response['Items']
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/query')
def query_data():
    """ Query data by ID, Size, and Date Range """
    id_param = request.args.get('id')
    size_param = request.args.get('size')
    start_timestamp = request.args.get('startTimestamp')
    end_timestamp = request.args.get('endTimestamp')

    filter_expression = []
    expression_values = {}
    expression_names = {}

    # ID Filtering
    if id_param:
        filter_expression.append("ID = :id")
        expression_values[":id"] = id_param

    # Size Filtering
    if size_param:
        filter_expression.append("Size = :size")
        expression_values[":size"] = size_param

    # Date Range Filtering
    if start_timestamp and end_timestamp:
        filter_expression.append("#ts BETWEEN :start AND :end")
        expression_values[":start"] = start_timestamp
        expression_values[":end"] = end_timestamp
        expression_names["#ts"] = "Timestamp"

    # Construct Filter Expression
    filter_expr = " and ".join(filter_expression)

    try:
        scan_params = {
            "FilterExpression": filter_expr,
            "ExpressionAttributeValues": expression_values
        }

        if expression_names:
            scan_params["ExpressionAttributeNames"] = expression_names

        response = table.scan(**scan_params) if filter_expr else table.scan()
        data = response['Items']
        return jsonify(data)

    except Exception as e:
        print(f"Error querying data: {str(e)}")
        return jsonify({"error": str(e)}), 500

def start_webapp():
    print("Starting web application...")
    app.run(debug=True, port=5000)

if __name__ == "__main__":
    start_webapp()
