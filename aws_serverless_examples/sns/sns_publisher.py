import boto3

class SNSPublisher:
    def __init__(self, sns_client):
        self.__sns_client = sns_client
    
    def create_topic(self, topic_name: str, fifo_type: bool == False) -> dict:
        """
            Create topic if it doesn't exist. 
            This defaults to creating a standard topic which will allow Subscription protocols: SQS, Lambda, HTTP, SMS, email, mobile application endpoints.
            As opposed to FIFO, which only allows SQS subscription protocol.

            Parameters:
                    topic_name (str): Name of the topic
                    fifo_type (bool): True to set this as FIFO, which will only allow SQS subscripters. False for Standard topic

            Returns:
                    response: {
                        'TopicArn': 'string'
                    }
        """
        return self.__sns_client.create_topic(
            Name = topic_name,
            Attributes = {
                'DisplayName': 'aws_serverless_example',
                'FifoTopic': fifo_type
            },
            Tags = [
                {
                    'Key': 'created_by',
                    'Value': 'sns_publisher'
                },
            ]
        )
    
    def publish_to_topic(self, topic_arn: str, subject: str, message: str) -> dict:
        """
            Publish to  topic if it doesn't exist.

            Parameters:
                    topic_arn (str): arn of the topic
                    subject (str): subject
                    message (str): Payload message

            Returns:
                    Response: {
                        'MessageId': 'string',
                        'SequenceNumber': 'string'
                    }
        """
        return self.__sns_client.publish(
            TopicArn = topic_arn,
            Message = subject,
            Subject = message,
        )


        