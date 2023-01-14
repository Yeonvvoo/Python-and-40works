import telegram
import asyncio
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, ContextTypes, ApplicationBuilder
from telegram.ext import MessageHandler, filters

token = '5837049587:AAGjWmtlqiL_0P4RkFNQ2kjbLemifYK0ZlY'
#https://api.telegram.org/bot5837049587:AAGjWmtlqiL_0P4RkFNQ2kjbLemifYK0ZlY/getUpdates
chat_id = 2104119799

#
# async def main(): #실행시킬 함수명 임의지정
#     token = '5837049587:AAGjWmtlqiL_0P4RkFNQ2kjbLemifYK0ZlY'
#     bot = telegram.Bot(token=token)
#     await bot.send_message(chat_id, '자동응답 테스트 입니다. 안녕 또는 뭐해를 입력하여 보세요')
#
#
# async def handler(update: Update, context: ContextTypes):
#
#     bot = telegram.Bot(token=token)
#     message = update.message.text
#     if message == "안녕:":
#         await bot.send_message(chat_id, '안녕하세요')
#     elif message == "뭐해":
#         await bot.send_message(chat_id, '테스트중입니다')
#
#     updater = Updater(token, True)
#     echo_handler = MessageHandler(filters.Message, handler)
#     updater.dispatcher.add_handler(echo_handler)
#     await updater.start_polling()
#     updater.idle()  # 스크립트 멈추기 위해 사용
#
# #     # 봇의 업데이트
# #
# #
# #
# asyncio.run(main()) #봇 실행하는 코드
# asyncio.run(handler())
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='안녕하세요 저는 따라쟁이예요. 아무말이나 입력해주세요')


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

if __name__ == '__main__':
    application = ApplicationBuilder().token(token).build()

    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)

    application.add_handler(start_handler)
    application.add_handler(echo_handler)

    application.run_polling()