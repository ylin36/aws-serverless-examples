# for any files sibling to this file, import relative to the module, 
# because we're going to be installing this main module.
from aws_serverless_examples.sns import SNSPublisher
import boto3

def main():
    client = boto3.client('sns')
    publisher = SNSPublisher(client)
    response = publisher.create_topic("yang_test")
    topic_arn = response['TopicArn'] if response else None
    if (topic_arn):
        response = publisher.publish_to_topic(topic_arn, "test subject", "test message")
        print(response)

if __name__ == "__main__":
    main()