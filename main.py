import os
import sys
import json
from scripts.jsonconversion import convert_csv_to_json
from scripts.s3upload import upload_to_s3
from scripts.lambdadataprocessing import trigger_data_processing
from scripts.lambdametricsprocessing import trigger_metrics_processing

def display_menu():
    print("\nSelect an option:")
    print("1. Convert CSV to JSON")
    print("2. Upload JSON to S3")
    print("3. Trigger Lambda Data Processing")
    print("4. Trigger Lambda Metrics Processing")
    print("5. Start Map Visualization")
    print("6. Exit")

def handle_conversion():
    print("\nConverting CSV to JSON...")
    convert_csv_to_json()

def handle_upload():
    print("\nUploading JSON to S3...")
    upload_to_s3()

def handle_data_processing():
    print("\nTriggering Lambda Data Processing...")
    trigger_data_processing()

def handle_metrics_processing():
    print("\nTriggering Lambda Metrics Processing...")
    trigger_metrics_processing()

def handle_visualization():
    print("\nStarting map visualization...")
    os.system("python -m scripts.webapp")

def main():
    while True:
        display_menu()
        choice = input("Enter choice [1-6]: ").strip()

        if choice == '1':
            handle_conversion()
        elif choice == '2':
            handle_upload()
        elif choice == '3':
            handle_data_processing()
        elif choice == '4':
            handle_metrics_processing()
        elif choice == '5':
            handle_visualization()
        elif choice == '6':
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
