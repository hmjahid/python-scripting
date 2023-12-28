import boto3

ec2 = boto3.resource('ec2')

instance = ec2.create_instance(
    ImageId= 'ami----',
    MinCount = 1,
    MaxCount = 1,
    InstanceType= 't2.micro'
)

print(instance[0].id)

instance_id= 'Ec2instanceID'
instance = ec2.Instance(instance_id)
response = instance.terminate()