import json
import datetime
import os

def lambda_handler(event, context):
    """
    Simple Lambda for pipeline deployment testing.
    It returns:
      - Current time
      - Lambda function name
      - Deployment environment (from ENV variable)
      - A test message
    """

    # Example logic: addition test
    def add(a, b):
        return a + b

    result = add(10, 20)

    response = {
        "message": "Lambda deployed successfully via CI/CD pipeline!",
        "function_name": context.function_name if context else "local_test",
        "timestamp": str(datetime.datetime.utcnow()),
        "environment": os.getenv("ENV", "development"),
        "sum_test": result
    }

    print("✅ Pipeline Test Lambda executed successfully")
    print(json.dumps(response, indent=2))

    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }
