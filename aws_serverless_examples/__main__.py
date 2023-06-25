# for any files sibling to this file, import relative to the module, 
# because we're going to be installing this main module.
from aws_serverless_examples.sns import SNSPublisher

def main():
    publisher = SNSPublisher()
    publisher.print()

if __name__ == "__main__":
    main()