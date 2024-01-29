import json
import boto3
import uuid

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb',region_name = 'us-east-1')
    table = dynamodb.Table('FarmAnimal')
    response = table.put_item(
        Item = {
            "GGID" : str(uuid.uuid1()),
            "Animal_Type" :  event['animal']
            }
        )
    return response
