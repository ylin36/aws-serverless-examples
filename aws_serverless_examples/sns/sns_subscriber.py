class SNSSubscriber:
    def __init__(self, sns_client):
        self.__sns_client = sns_client

    def subscribe_to_topic(self, topic_arn: str, protocol: str, endpoint: str) -> dict:
        """
            Subscribe to topic given the type by providing one of the supported protocol below, and the endpoint to reach that protocol.
            Topics can be filtered by using Attribute field. See boto3 for more details. This method does not use Attribute right now.
            Parameters:
                    topic_arn (str): Arn of the topic
                    protocol (str): http, https, email, email-json, sms, sqs, application, lambda, firehose
                    endpoint (str): http://, https://, a@b.com, a@b.com, phone number, EndpointArn of mobile app, lambda arn, kinesis data firehouse arn

            Returns: arn or pending confirmation
                    response: {
                        'SubscriptionArn': 'string'
                    }
        """

        return self.__sns_client.subscribe(
            TopicArn = topic_arn,
            Protocol = protocol,
            Endpoint = endpoint,
            # Attributes = {
             #   'string': 'string'
            # },
            # Set false, so that if subscription is pending confirmation, ret string is such
            ReturnSubscriptionArn = False 
)
