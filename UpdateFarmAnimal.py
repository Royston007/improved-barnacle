import json
import boto3
import uuid
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb',region_name = 'us-east-1')
    table = dynamodb.Table('FarmAnimal')
    
    ani = ''
    if 'body'  in event:
        ani = json.loads(event["body"])
    else:
        ani = event
    
    get_obj = table.query(
        KeyConditionExpression=Key('GGID').eq(ani['uuid'])
    )
    print(get_obj)
    #return get_obj['Items'][0]['Animal_Type']
    table.delete_item(
        Key = {
            "GGID" : ani['uuid'],
            "Animal_Type" : get_obj['Items'][0]['Animal_Type']
        }
        )
    if 'animal' not in ani:
        return ani['uuid'], ' deleted !!!'
        
    response = table.put_item(
        Item={
            'GGID': ani['uuid'],
            'Animal_Type' : ani['animal']
        }
        )
    if ani['animal'] :
        return ani['uuid'], ' updated to ', ani['animal'], ' !!!'
        
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
