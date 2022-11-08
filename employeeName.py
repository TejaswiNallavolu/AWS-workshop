import json
import boto3
import csv

dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    
    try:
        #table name
        table = dynamodb.Table('employees')
        #getting values from table
        response = table.get_item(Key={'employeeId': event['pathParameters']["employee-id"]})
        return {"statusCode": 200, "body": str(response["Item"])}
            
    
    except Exception as e:
        print('Employee not found')
        print(e)
        return {"statusCode": 400}

