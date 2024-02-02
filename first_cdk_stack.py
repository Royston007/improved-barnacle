from aws_cdk import (
    Duration,
    Stack,
    aws_sqs as sqs,
    aws_lambda as lambda_,
    aws_dynamodb as dynamodb,
    aws_iam as iam,
    aws_apigateway as api_gateway,
    aws_apigatewayv2_integrations as integration
    
)
from aws_cdk.aws_apigatewayv2 import HttpApi, HttpMethod
from aws_cdk.aws_apigatewayv2_integrations import HttpLambdaIntegration

from constructs import Construct

class FirstCdkStack(Stack): 

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        role = iam.Role(self,"InsertFarmAnimal-role", assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"))
        role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("AmazonDynamoDBFullAccess"))
        role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("AWSLambdaInvocation-DynamoDB"))
        #role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("AWSLambdaBasicExecutionRole"))
        #role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("AmazonAPIGatewayPushToCloudWatchLogs"))
        

        insert_fn = lambda_.Function(self,'InsertFarmAnimal',role= role,
                              runtime = lambda_.Runtime.PYTHON_3_9,
                              handler="InsertFarmAnimal.lambda_handler",
                              code=lambda_.Code.from_asset('/home/royston.dsilva/Downloads/InsertFarmAnimal.zip'))

        update_fn = lambda_.Function(self,'UpdateFarmAnimal', role = role,
                              runtime = lambda_.Runtime.PYTHON_3_9,
                              handler="UpdateFarmAnimal.lambda_handler",
                              code=lambda_.Code.from_asset('/home/royston.dsilva/Downloads/UpdateFarmAnimal.zip'))
        insert_fn.add_permission('invoke_lambda',principal=iam.ServicePrincipal('apigateway.amazonaws.com'),action='lambda:InvokeFunction')
        update_fn.add_permission('invoke_lambda',principal=iam.ServicePrincipal('apigateway.amazonaws.com'),action='lambda:InvokeFunction')
        
        table = dynamodb.TableV2(self, "FarmAnimal", partition_key=dynamodb.Attribute(name="GGID", type=dynamodb.AttributeType.STRING),sort_key = dynamodb.Attribute(name="Animal_Type", type=dynamodb.AttributeType.STRING))

        
        

        
        '''
        api = api_gateway.LambdaRestApi(self, "FarmAnimals",
            handler=insert_fn,
            proxy=False
        )
        add_animal = api.root.add_resource("addanimal")
        add_animal.add_method("POST",api_gateway.LambdaIntegration(insert_fn)) #Use PUT

        update_animal = api.root.add_resource("updateanimal")
        update_animal.add_method("POST",api_gateway.LambdaIntegration(update_fn)) #Use DELETE
        '''
        
        add_animal_integration = integration.HttpLambdaIntegration("AddAnimal",insert_fn)
        update_animal_integration = integration.HttpLambdaIntegration("UpdateAnimal",update_fn)
        http_api = HttpApi(self, "FarmAnimalsHttpApi")
        http_api.add_routes(
            path ='/addanimal',
            methods = [HttpMethod.PUT],
            integration = add_animal_integration
        )
        http_api.add_routes(
            path ='/updateanimal',
            methods = [HttpMethod.DELETE],
            integration = update_animal_integration
        )

