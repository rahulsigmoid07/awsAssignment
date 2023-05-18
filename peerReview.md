### peer review for chakradhar <br/>
#### Question 1. <br/>
Task: Create an IAM role with S3 full access<br/>
Create the IAM role using the AWS CLI command:


```
aws iam create-role --role-name chakradhar-q1 --assume-role-policy-document file://trustpolicy.json
```
The trustpolicy.json file should contain the following information:<br/>

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "ec2.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

Attach the S3 full access policy to the IAM role using the AWS CLI command: <br/>

```
aws iam attach-role-policy --role-name chakradhar-q1 --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess
```
Create an EC2 instance with the above role and instance profile:<br/>

Create an instance profile using the AWS CLI command:<br/>

```
aws iam create-instance-profile --instance-profile-name chakradhar_instance_profile_q1
```
Attach the role to the instance profile using the AWS CLI command:<br/>
```
aws iam add-role-to-instance-profile --instance-profile-name chakradhar_instance_profile_q1 --role-name chakradhar-q1
```
Launch the EC2 instance with the specified parameters. <br/>
Task: Create a bucket <br/>
Create an S3 bucket using the AWS CLI command:<br/>
```
aws s3api create-bucket --bucket chakradahars3 --region ap-south-1 --create-bucket-configuration LocationConstraint=ap-south-1
```

#### Question 2 <br/>
Task: Put files in S3 bucket from Lambda <br/>
* Create custom roles and policies for the Lambda function using the AWS SDK: <br/>
    * Create a policy for put object access.<br/>
    * Create a role for the Lambda function and attach the put object policy to it.<br/>
    * Add a role to generate and access CloudWatch logs.<br/>
* Create a new Lambda function using the above role and implement the logic to generate JSON files and save them in the specified S3 bucket. The function should also log the S3 object creation event.<br/>

* Schedule the Lambda function to run every minute using a CloudWatch rule. Stop execution after three runs by setting the function's concurrency to 0. <br/>

* Verify if CloudWatch logs are generated for the Lambda function.

#### Question 3 <br/>
Task: API Gateway - Lambda integration <br/>
* Modify the Lambda function to accept parameters by updating the code to parse the input data and save it as JSON in the S3 bucket.

* Create a POST API from API Gateway that passes parameters as the request body to the Lambda function. Return the filename and status code as a response.

* Consume the API from a local machine by making a POST request with unique data using tools like curl. Verify if the file is created in the S3 bucket. <br/>

### peer review for amit <br/>

#### Question 1. <br/>
Task: Create an IAM role with S3 full access<br/>
Create the IAM role using the AWS CLI command:


```
aws iam create-role --role-name amit --assume-role-policy-document file://policy.json

```
The trustpolicy.json file should contain the following information:<br/>

```
{
    "Version": "2012-10-17",
    "Statement": {
        "Effect": "Allow",
        "Principal": {
            "Service": "s3.amazonaws.com",
            "AWS": "arn:aws:iam::0039*****9674:user/amit"
        },
        "Action": "sts:AssumeRole"
    }
}

```

Attach the S3 full access policy to the IAM role using the AWS CLI command: <br/>

```
aws iam attach-role-policy --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess --role-name amit

```
Create an EC2 instance with the above role and instance profile:<br/>

Create an instance profile using the AWS CLI command:<br/>

```
aws ec2 run-instances --image-id AMI_ID --instance-type INSTANCE_TYPE --key-name amit-ec2 --subnet-id SUBNET_ID --security-group-ids SECURITY_GROUP_IDS --region REGION --profile amit

```
Launch the EC2 instance with the specified parameters. <br/>
Task: Create a bucket <br/>
Create an S3 bucket using the AWS CLI command:<br/>
```
aws s3api create-bucket --bucket BUCKET_NAME --region REGION --create-bucket-configuration LocationConstraint=REGION

```

#### Question 2 <br/>
Task: Put files in S3 bucket from Lambda <br/>
* Create custom roles and policies for the Lambda function using the AWS SDK: <br/>
    * Create a policy for put object access.<br/>
    * Create a role for the Lambda function and attach the put object policy to it.<br/>
    * Add a role to generate and access CloudWatch logs.<br/>
* Create a new Lambda function using the above role and implement the logic to generate JSON files and save them in the specified S3 bucket. The function should also log the S3 object creation event.<br/>
* Schedule the Lambda function to run every minute using a CloudWatch rule. Stop execution after three runs by setting the function's concurrency to 0. <br/>
* Verify if CloudWatch logs are generated for the Lambda function.

#### Question 3 <br/>
Task: API Gateway - Lambda integration <br/>
* Modify the Lambda function to accept parameters by updating the code to parse the input data and save it as JSON in the S3 bucket.
* Create a POST API from API Gateway that passes parameters as the request body to the Lambda function. Return the filename and status code as a response.
* Consume the API from a local machine by making a POST request with unique data using tools like curl. Verify if the file is created in the S3 bucket. 

