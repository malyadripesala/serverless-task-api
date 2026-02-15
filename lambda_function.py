import json
import boto3
import uuid
from datetime import datetime
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ.get("TABLE_NAME", "Tasks"))

def lambda_handler(event, context):
    method = event['httpMethod']

    if method == 'POST':
        body = json.loads(event['body'])
        task_id = str(uuid.uuid4())

        item = {
            'taskId': task_id,
            'title': body['title'],
            'description': body.get('description', ''),
            'status': 'PENDING',
            'createdAt': datetime.utcnow().isoformat()
        }

        table.put_item(Item=item)
        return response(201, item)

    elif method == 'GET':
        if event.get('pathParameters'):
            task_id = event['pathParameters']['id']
            result = table.get_item(Key={'taskId': task_id})
            return response(200, result.get('Item'))
        else:
            result = table.scan()
            return response(200, result['Items'])

    elif method == 'PUT':
        task_id = event['pathParameters']['id']
        body = json.loads(event['body'])

        table.update_item(
            Key={'taskId': task_id},
            UpdateExpression="SET title = :t, description = :d, #st = :s",
            ExpressionAttributeNames={
                "#st": "status"
            },
            ExpressionAttributeValues={
                ':t': body['title'],
                ':d': body['description'],
                ':s': body['status']
            }
        )

        return response(200, {"message": "Task updated"})

    elif method == 'DELETE':
        task_id = event['pathParameters']['id']
        table.delete_item(Key={'taskId': task_id})
        return response(200, {"message": "Deleted"})

    return response(400, {"message": "Invalid request"})


def response(status, body):
    return {
        'statusCode': status,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps(body)
    }
