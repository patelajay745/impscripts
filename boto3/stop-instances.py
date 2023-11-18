import boto3

def get_running_instances(ec2_client):
    response = ec2_client.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    instances = [instance['InstanceId'] for reservation in response['Reservations'] for instance in reservation['Instances']]
    return instances

def stop_instances(ec2_client, instance_ids):
    if instance_ids:
        ec2_client.stop_instances(InstanceIds=instance_ids)
        print("Stopping instances...")
    else:
        print("No running instances to stop.")

if __name__ == "__main__":
    # Create an EC2 client
    ec2 = boto3.client('ec2')

    # Get running instances
    running_instances = get_running_instances(ec2)

    # Stop instances
    stop_instances(ec2, running_instances)
