import json
import os
# from linebot import LineBotApi, WebhookHandler
# from linebot.models import TextSendMessage, StickerSendMessage, ImageSendMessage, LocationSendMessage

CHANNEL_SECRET = os.environ.get("CHANNEL_SECRET", "")
CHANNEL_ACCESS_TOKEN = os.environ.get("CHANNEL_ACCESS_TOKEN", "")

def lambda_handler(event, context):
    """
    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    print("ENV_SNAPSHOT:", {k: (v[:4]+"...") for k,v in os.environ.items() if k.startswith("CHANNEL_")})

    print(CHANNEL_SECRET)
    print(CHANNEL_ACCESS_TOKEN)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Line Bot",
        }),
    }
