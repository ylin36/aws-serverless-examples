# for any files sibling to this file, import relative to the module, 
# because we're going to be installing this main module.
from aws_serverless_examples.sns import *
import boto3

def main():
    client = boto3.client('sns')
    publisher = SNSPublisher(client)
    response = publisher.create_topic("yang_test")
    topic_arn = response['TopicArn'] if response else None
    if (topic_arn):
        response = publisher.publish_to_topic(topic_arn, "test subject", "test message")
        print(response)

    subscriber = SNSSubscriber(client)
    # the subscription policy is set to allow owner to pub sub the topic
    # which basically allows principal AWS * but looks for AWS:SourceOwner conditon to match the account
    email_address = ""
    # response = subscriber.subscribe_to_topic(topic_arn, "email", email_address)
    print(response)

if __name__ == "__main__":
    main()