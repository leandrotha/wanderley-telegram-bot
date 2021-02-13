import json
import boto3
from telegram import Bot, Update
from telegram.ext import CommandHandler, Dispatcher, Filters, MessageHandler
from handlers import opiniao, meajuda, ideia, start, unknown, caule

#fetch bot token from AWS

ssm_client = boto3.client("ssm")
response = ssm_client.get_parameter(Name="telegramToken", WithDecryption=True)
TELEGRAM_TOKEN = response["Parameter"]["Value"]

bot = Bot(token=TELEGRAM_TOKEN)

dispatcher = Dispatcher(bot, None, use_context = True)
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("opiniao", opiniao))
dispatcher.add_handler(CommandHandler("meajuda", meajuda))
dispatcher.add_handler(CommandHandler("ideia", ideia))
dispatcher.add_handler(CommandHandler("caule", caule))
dispatcher.add_handler(MessageHandler(Filters.command, unknown))

def lambda_handler(event, context):
    dispatcher.process_update(Update.de_json(json.loads(event["body"]), bot))
    return {"statusCode": 200}