from pytube import YouTube
from aiogram import Bot, Dispatcher, executor, types
import time 
import os
def download(link):
        yt = YouTube(link, use_oauth=True)
        stream = yt.streams.get_by_itag(251)
        return stream.download(filename='podcast.mp3')

class TgBot:
    def __init__(
                        self,
                        token
                        
                    ):
                    
            
            self.bot = Bot(token=token)
            self.dp = Dispatcher(self.bot)

            async def start_command(message: types.Message):
                await message.answer('Вы попали в бота для скачивания аудио-дорожки из видео\n\nДля продолжения введите: /download + ссылка на видео youtube')

            async def download_command(message: types.Message):
                link = message.get_args()
                chat_id = message.chat.id
                await self.bot.send_message(chat_id, "Происходит скачивание, ожидайте...")
                download(link)
                time.sleep(1)
                
                await self.bot.send_document(message.chat.id, document=open('podcast.mp3', 'rb'), caption='Вот ваш подкаст')
                
                
                os.remove('podcast.mp3')

    
            self.dp.register_message_handler(start_command, commands=["start"]) 
            self.dp.register_message_handler(download_command, commands=['download'])
            

    def start(self):
        executor.start_polling(
                                    self.dp,
                                    skip_updates=True
                                    )       