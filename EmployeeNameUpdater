import json
import urllib.parse
import boto3
import csv

print('Loading function')

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    
    try:
        data_object = s3.get_object(Bucket=bucket, Key=key)
        # json_data = data['Body'].read()
        data = data_object['Body'].read().decode('utf-8').splitlines()

        lines = csv.reader(data)
        
        # Set up dynamodb access
        #table name
        table = dynamodb.Table('employees')
        
        for line in lines:
            #print complete line
            print(line)
            #inserting values into table
            response = table.put_item(
               Item={
                    'employeeId': line[0],
                    'EmployeeFname': line[1],
                    'EmployeeLnam': line[2]
                }
            )
            print(response)
        
        return {"statusCode": 200, "body": "OK"}
            
    
    except Exception as e:
        print(e)
        raise e
    
