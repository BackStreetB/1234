import boto3
import json
import random
import time

kinesis_client = boto3.client('kinesis', region_name='ap-southeast-1')

while True:
    # Simulate call data
    call_data = {
        'call_id': str(random.randint(1000, 9999)),
        'duration': random.randint(1, 300),  # Duration in seconds
        'timestamp': time.time()
    }
    # Send data to Kinesis
    response = kinesis_client.put_record(
        StreamName='CallDataStream',
        Data=json.dumps(call_data),
        PartitionKey=call_data['call_id']
    )
    print(f"Sent record: {call_data}, Response: {response}")  # Print response
    time.sleep(1)  # Send a record every second