import boto3


def lambda_handler(event, context):
    info = event.get('info') or {}
    field = info.get('fieldName')
    if not field:
        return "fieldName must be provided in 'info'"
    elif not info:
        return "info and fieldName must be provided"
    elif field == 'ListResources':
        return list_resources()
    else:
        raise Exception("Unknown field, unable to resolve " + field)


def list_resources():
    client = boto3.client('ec2')
    response = client.describe_instances()
    instances = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instances.append({
                'InstanceId': instance['InstanceId'],
                'InstanceType': instance['InstanceType'],
                'State': instance['State']['Name'],
                'PublicIpAddress': instance.get('PublicIpAddress', 'N/A'),
                'PrivateIpAddress': instance.get('PrivateIpAddress', 'N/A'),
            })
    return instances
