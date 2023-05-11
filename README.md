# awsAssignment
## Question 1

Create S3 bucket from AWS CLI <br>
<b>a.</b> Create an IAM role with S3 full access.</b>

Providing the role with S3 full access

```
aws iam attach-role-policy --role-name  BucketMaker  --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess

```

<b>b.</b>Create an EC2 instance with above role
Creating an instance profile

```
import boto3

# Connect to the EC2 service
ec2 = boto3.resource('ec2')

# Create an EC2 instance
instance = ec2.create_instances(
    ImageId='ami-014571f1593b7be25', # Specify the ID of the AMI you want to use
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='rahulayush', # Specify the name of your key pair
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'rahulEC2Instance'
                },
            ]
        },
    ]
)


```

<img width="1238" alt="Screenshot 2023-05-09 at 5 14 31 PM" src="https://github.com/rahulsigmoid07/awsAssignment/assets/123542137/ce68c1e0-f7d2-47df-9cb6-741073cb4fcb">

<br>


<b>c.</b>
Creating the bucket

```
import boto3
import logging
from botocore.exceptions import ClientError


def create_bucket(bucket_name, region=None):
    """Create an S3 bucket in a specified region

    If a region is not specified, the bucket is created in the S3 default
    region (us-east-1).

    :param bucket_name: Bucket to create
    :param region: String region to create bucket in, e.g., 'us-west-2'
    :return: True if bucket created, else False
    """

    # Create bucket
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True

def main():
    create_bucket('awsassignbucket1',region='eu-west-3')
    s3 = boto3.client('s3')
    response = s3.list_buckets()

    # Output the bucket names
    print('Existing buckets:')
    for bucket in response['Buckets']:
        print(f'  {bucket["Name"]}')
    
# Print the default region


if __name__ == '__main__':
    main()

```

<img width="1052" alt="Screenshot 2023-05-11 at 2 31 32 PM" src="https://github.com/rahulsigmoid07/awsAssignment/assets/123542137/b622966e-800b-486f-a00b-e1b760d20ac9">


## Question 2

Put files in S3 bucket from lambda <br>

Creating clients

```
import boto3
import json
from botocore.exceptions import ClientError

```


 a. Create custom role for AWS lambda which will have only put object access

```
policy_document = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:PutObject"
            ],
            "Resource": [
                "arn:aws:s3:::awsassignbucket1/*"
            ]
        }
    ]
}

```


<b>b.</b>Add role to generate and access Cloudwatch logs
Creating cloudwatch policy

```
cloudwatch_logs_policy_document = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents",
                "logs:GetLogEvents"
            ],
            "Resource": "*"
        }
    ]
}
```

<b></b>In python script, generate json in given format and save .json file in bucket created<br/>
```
 # Generate JSON in the given format
        transaction_id = 12345
        payment_mode = "card/netbanking/upi"
        Amount = 200.0
        customer_id = 101
        Timestamp = str(datetime.datetime.now())
        transaction_data = {
            "transaction_id": transaction_id,
            "payment_mode": payment_mode,
            "Amount": Amount,
            "customer_id": customer_id,
            "Timestamp": Timestamp
        }
        
        # Save JSON file in S3 bucket
        json_data = json.dumps(transaction_data)
        file_name = key_name.format(Timestamp.replace(" ", "_"))
        s3.Bucket(bucket_name).Object(file_name).put(Body=json_data)
        
```
<b></b>Created a lambda_handler function to save the file in json in format and upload it to the bucket<br/>
<b></b>Schedule the job to run every minute. Stop execution after 3 runs<br/>
<b></b>Using amazon lambda, created a function and uploaded the file created above<br/>

<img width="1440" alt="Screenshot 2023-05-08 at 6 02 20 PM" src="https://github.com/rahulsigmoid07/awsAssignment/assets/123542137/f10565e5-2327-424a-b7f8-936493e3e43e">
<img width="1440" alt="Screenshot 2023-05-08 at 6 02 24 PM" src="https://github.com/rahulsigmoid07/awsAssignment/assets/123542137/21981bf1-52d9-409b-b7c4-4d28e79ecb0f">
<br/>
<br/>
files uploaded in s3 bucket:<br/>
<br>

<img width="1440" alt="Screenshot 2023-05-08 at 6 02 36 PM" src="https://github.com/rahulsigmoid07/awsAssignment/assets/123542137/32af93aa-c703-4a1e-9b95-d7a2664660af">
<br/>
<br/>
The log Files are below <br/>
<br/>

<img width="1440" alt="Screenshot 2023-05-09 at 4 06 26 PM" src="https://github.com/rahulsigmoid07/awsAssignment/assets/123542137/cead7a86-6e9d-4bd2-9325-af663991b146">
<br/>
<br/>
<b>3 a.</b> Modify lambda function to accept parameters and return file name
Modified lambda function is :<br/>
     <b>b.</b>Create a POST API from API Gateway, pass parameters as request body to Lambda
     job. Return filename and status code as response.<br/>
<b>c.</b>Consume API from local machine and pass unique data to lambda.<br/>
<b>d.</b>Check if cloud watch logs are generated

<br/>

To create a post API to feed to lambda job these steps were followed

```
Go to the API Gateway console and click "Create API".
Select "REST API" and click "Build".
Choose "New API" and enter a name for your API. Click "Create API".
Click "Create Resource" to create a new resource under your API.
Enter a name for your resource and click "Create Resource".
Click "Create Method" and select "POST" from the dropdown.
Select "Lambda Function" and check the "Use Lambda Proxy integration" box.
Enter the name of your Lambda function in the "Lambda Function" field and click "Save".
Deploy your API by clicking "Actions" > "Deploy API". Select "New Stage" and enter a name for your stage. Click "Deploy".
Note the URL of your API endpoint

```
<img width="1172" alt="Screenshot 2023-05-09 at 3 12 00 PM" src="https://github.com/rahulsigmoid07/awsAssignment/assets/123542137/cd27bbe8-4eb0-4462-bb7b-295f3916eca1">
<br/>
<br/>
<img width="1069" alt="Screenshot 2023-05-11 at 3 10 48 PM" src="https://github.com/rahulsigmoid07/awsAssignment/assets/123542137/e1cff483-d956-4e9e-9af1-ff8cfb994db9">
 
<br>
<br/>
<br/>
For the sending the file using local machine i used postman
<br/>
<br/>

<img width="895" alt="Screenshot 2023-05-09 at 3 36 16 PM" src="https://github.com/rahulsigmoid07/awsAssignment/assets/123542137/10b0a1ec-bb8b-470d-832c-d906d2772b19">
