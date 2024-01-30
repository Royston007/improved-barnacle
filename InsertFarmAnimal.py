import json
import boto3
import uuid

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb',region_name = 'us-east-1')
    table = dynamodb.Table('FarmAnimal')
    #print('event ' , json.loads(event["body"]))
    ani = ''
    if 'body'  in event:
        ani = json.loads(event["body"])
    else:
        ani = event
    response = table.put_item(
        Item = {
            "GGID" : str(uuid.uuid1()),
            "Animal_Type" :  ani['animal']
            }
        )
    return response
