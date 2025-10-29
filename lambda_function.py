import json

def lambda_handler(event, context):
    # TODO implement
    def add(a, b):
        return a + b
        
    print("Sum:", add(5, 7))

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
