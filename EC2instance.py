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

print(instance[0].id) # Print the ID of the new instance
