import boto3
import datetime
import json

s3 = boto3.resource('s3')
bucket_name = 'awsassignbucket1'
key_name = 'rahul{}.json'

def lambda_handler(event, context):
    try:
        # Parse input data
        body = json.loads(event['body'])
        
        # file_content = body['file_content']
        # bucket_name = body['bucket_name']

        # transaction_id = event['transaction_id']
        # payment_mode = event['payment_mode']
        # amount = event['amount']
        # customer_id = event['customer_id']

        # Generate JSON in the given format
        timestamp = str(datetime.datetime.now())
        
        body["timestamp"] = timestamp
        # transaction_data = {
        #     "transaction_id": transaction_id,
        #     "payment_mode": payment_mode,
        #     "amount": amount,
        #     "customer_id": customer_id,
        #     "timestamp": timestamp
        # }

        # Save JSON file in S3 bucket
        json_data = json.dumps(body)
        file_name = key_name.format(timestamp.replace(" ", "_"))
        s3.Object(bucket_name, file_name).put(Body=json_data)

        # Log the S3 object creation event
        print(f"Object created in S3 bucket {bucket_name}: {file_name}")

        return {
            "file_name": file_name,
            "status": "success"
        }

    except Exception as e:
        print(e)
        return {
            "status": "error"
        }