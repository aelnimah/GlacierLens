# 🧊 GlacierLens – Advanced Data Analytics & Visualization

Transform raw iceberg sighting data into structured, queryable datasets with interactive visualizations. Designed for researchers, analysts, and environmental monitoring projects.

## 🚀 Core Technologies

### ☁️ AWS Infrastructure
![Lambda](https://img.shields.io/badge/AWS_Lambda-FF9900?style=for-the-badge&logo=awslambda&logoColor=white)
![DynamoDB](https://img.shields.io/badge/Amazon_DynamoDB-4053D6?style=for-the-badge&logo=amazondynamodb&logoColor=white)
![S3](https://img.shields.io/badge/Amazon_S3-569A31?style=for-the-badge&logo=amazons3&logoColor=white)

### 📊 Data & Visualization
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Leaflet](https://img.shields.io/badge/Leaflet-199900?style=for-the-badge&logo=leaflet&logoColor=white)
![Folium](https://img.shields.io/badge/Folium-77B829?style=for-the-badge&logo=folium&logoColor=white)

### ⚙️ DevOps
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)

## 🛠️ Tech Stack

* **AWS Lambda:** Serverless data processing for high scalability.
* **DynamoDB:** NoSQL database for structured iceberg data storage.
* **S3:** Data ingestion and cloud storage for JSON datasets.
* **Flask:** Backend API server for data querying and visualization.
* **Leaflet.js:** Dynamic, high-performance map visualization.
* **Boto3:** AWS SDK for Python to interface with S3 and DynamoDB.
* **Pandas:** Data parsing and transformation.
* **Node.js (Future):** Potential for a Node.js API layer for scalability.

## 📂 Project Structure

/IcebergPro/
│── data/
│   └── iceberg_data.csv           # Raw iceberg data (CSV)
│   └── 2021Icebergs.json          # Processed JSON for S3 upload
│── frontend/
│   └── index.html                 # Map visualization
│   └── script.js                  # Interactive map logic
│── scripts/
│   └── jsonconversion.py          # CSV to JSON conversion
│   └── s3upload.py                # S3 upload script
│   └── lambdadataprocessing.py    # Triggers data processing Lambda
│   └── lambdametricsprocessing.py # Triggers metrics processing Lambda
│   └── webapp.py                  # Flask app for map visualization
│── main.py                        # CLI for all functions
│── requirements.txt               # Dependencies
│── README.md                      # Project documentation

## 🚀 Core Features & Functionality

### 1. Data Processing Pipeline (AWS Lambda + DynamoDB)

* Converts raw CSV data into structured JSON format.
* Merges `SIGHTING_DATE` and `SIGHTING_TIME` into a unified `Timestamp` field.
* Assigns unique ID to each iceberg record using `ICEBERG_NUMBER`.
* Uploads processed JSON to S3 for Lambda processing.
* ✅ **Skills Demonstrated:** Data transformation, ETL pipeline, AWS S3 integration, error handling.

### 2. Real-Time Data Processing (IcebergDataProcessor Lambda)

* Processes JSON data from S3 and stores it in the `IcebergData` DynamoDB table.
* Extracts key attributes: `Latitude`, `Longitude`, `Timestamp`, `Size`, `Shape`, `Source`.
* Implements robust error handling for type mismatches and incomplete records.
* ✅ **Skills Demonstrated:** Serverless architecture, DynamoDB integration, data processing optimization.

### 3. Metrics Analysis & Aggregation (IcebergMetricsProcessor Lambda)

* Aggregates data from `IcebergData` DynamoDB table to calculate key metrics:
    * Total Sightings
    * Most Common Shape, Source, and Sighting Method
    * Date with Most Sightings
    * Total Unique Sources and Shapes
* ✅ **Skills Demonstrated:** Data aggregation, serverless analytics, AWS Lambda processing.

### 4. Interactive Map Visualization (Leaflet.js + Flask)

* Displays iceberg data as interactive map markers with detailed popups.
* Allows querying by `ID`, `Size`, and `Date Range`.
* Implements clustering to handle large datasets effectively (6,000+ markers).
* ✅ **Skills Demonstrated:** Data visualization, frontend optimization, dynamic mapping.

## ⚙️ AWS Configuration & Setup

### 1. S3 Bucket Setup:

* **Bucket Name:** `icebergpro-data`
* **Region:** `us-east-2`
* **Event Trigger:** All Object Create Events → Triggers `IcebergDataProcessor` Lambda.

### 2. DynamoDB Tables:

* **IcebergData Table:**
    * **Partition Key:** `ID` (String)
    * **Sort Key:** `Timestamp` (String)
    * **Attributes:**
        * `ID`: Unique identifier for each iceberg.
        * `Timestamp`: Unified date and time field.
        * `Latitude` / `Longitude`: Geographic coordinates.
        * `Size`: Iceberg size (SML, MED, LRG, VLG).
        * `Shape`: Iceberg shape (Tabular, Dome, etc.).
        * `Source`: Data source (e.g., RCM1, FBPZ).
        * `SightingMethod`: Method of sighting (e.g., SAT, VIS).
* **IcebergStats Table:**
    * **Partition Key:** `Metric` (String)
    * **Attributes:**
        * `Metric`: The calculated metric (e.g., "Total Sightings").
        * `Value`: Corresponding value.

### 3. IAM Role Setup:

* **Role Name:** `IcebergDataProcessorRole`
* **Attached Policies:**
    * `AmazonS3FullAccess`
    * `AmazonDynamoDBFullAccess`
    * `AWSLambdaBasicExecutionRole`

### 4. Lambda Functions:

* **IcebergDataProcessor Lambda:**
    * **Runtime:** Python 3.11
    * **Handler:** `lambda_function.lambda_handler`
    * **Memory:** 256MB
    * **Timeout:** 30s
* **IcebergMetricsProcessor Lambda:**
    * **Runtime:** Python 3.11
    * **Handler:** `metrics_function.lambda_handler`
    * **Memory:** 128MB
    * **Timeout:** 5s

## ⚡ How to Run the Project

### 1. Install Dependencies:
* pip install -r requirements.txt
### 2. Run CLI:
* python main.py

### Options:
1: Convert CSV to JSON
2: Upload JSON to S3
3: Trigger Data Processing Lambda
4: Trigger Metrics Processing Lambda
5: Start Map Visualization
6: Exit

## 🔍 Monitoring and Debugging

- **AWS CloudWatch**: Track Lambda execution logs for `IcebergDataProcessor` and `IcebergMetricsProcessor`
- **DynamoDB**: Verify data entries in `IcebergData` and calculated metrics in `IcebergStats`
- **S3 Console**: Confirm JSON upload to `icebergpro-data` bucket

## 🚀 Future Enhancements

- Implement data export in CSV/JSON format
- Advanced heatmap visualization for iceberg density analysis
- Implement predictive analytics for iceberg size and movement
- Add authentication and user management for secure data access

## ❓ Why IcebergPro?

IcebergPro is more than just a data processing tool – it's a comprehensive data pipeline that showcases:
- Advanced AWS integration
- Dynamic data visualization
- Robust backend architecture

It's a full-stack data engineering project that leverages modern cloud services to turn raw data into actionable insights.o?
IcebergPro is more than just a data processing tool – it’s a comprehensive data pipeline that showcases advanced AWS integration, dynamic data visualization, and robust backend architecture. It’s a full-stack data engineering project that leverages modern cloud services to turn raw data into actionable insights.