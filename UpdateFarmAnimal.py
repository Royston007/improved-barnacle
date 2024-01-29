import json
import boto3
import uuid
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb',region_name = 'us-east-1')
    table = dynamodb.Table('FarmAnimal')
    
    
    get_obj = table.query(
        KeyConditionExpression=Key('GGID').eq(event['uuid'])
    )
    print(get_obj)
    #return get_obj['Items'][0]['Animal_Type']
    table.delete_item(
        Key = {
            "GGID" : event['uuid'],
            "Animal_Type" : get_obj['Items'][0]['Animal_Type']
        }
        )
    if 'animal' not in event:
        return event['uuid'], ' deleted !!!'
        
    response = table.put_item(
        Item={
            'GGID': event['uuid'],
            'Animal_Type' : event['animal']
        }
        )
    if event['animal'] :
        return event['uuid'], ' updated to ', event['animal'], ' !!!'
        
    '''response = table.put_item(
        Key={
        'GGID': event['uuid'],
        "Animal_Type" : get_obj['Items'][0]['Animal_Type']
    },
    UpdateExpression="set Animal_Type = :r",
    ExpressionAttributeValues={
        ':r': event['animal'],
    },
    ReturnValues="UPDATED_NEW"
        )
        '''
        
    return response
