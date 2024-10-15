import asyncio # The telegram API documentation directed to use async in each place I did
import winreg
import telegram
import requests
import hashlib

JPG_POSSIBLE_SIGNATURES = [b'\xFF\xD8\xFF\xE0', b'\xFF\xD8\xFF\xEE', b'\xFF\xD8\xFF\xE1'] # Theoretically, just checking for 0xFFD8FF would be enough, but might as well

async def main():
    registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Environment', 0, winreg.KEY_READ)
    api_token, _ = winreg.QueryValueEx(registry_key, "JPEG_HASH_BOT_API_KEY")
    winreg.CloseKey(registry_key)
    
    hash_bot = telegram.Bot(api_token)
    update_offset = 0
    
    async with hash_bot:
        while True:
            # Offset helps mark handled updates, if get_update sends an offset all updates with an id smaller than
            # the offset are marked as handled and do not get sent again
            updates = (await hash_bot.get_updates(offset= update_offset, timeout= 1000000000)) # Don't want a timeout, but for some reason it forces you to have it

            for update in updates: # Might receive multiple updates at once
                update_offset = update.update_id + 1
                if update.message.text != None: # Text sent
                    await hash_bot.send_message(chat_id= update.message.chat.id, text= "ERROR: This bot does not accept text, please only send jpg files.")
                    continue

                if len(update.message.photo) != 0: # Sent as photo
                    file_id = update.message.photo[0].file_id
                    
                elif update.message.document != None: # Sent as document, not checking extension here since I have to do it again later anyway
                    file_id = update.message.document.file_id

                else:
                    await hash_bot.send_message(chat_id= update.message.chat.id, text= "ERROR: This bot only accepts jpg files.")
                    continue

                is_jpg = False
                photo_download_data = await hash_bot.get_file(file_id) # Getting the url of the file for download
                print(photo_download_data)
                
                if photo_download_data.file_path.endswith((".jpg", ".jpeg")): # Checking if the photo is a jpg/jpeg by checking the extension
                    curr_photo = requests.get(photo_download_data.file_path).content

                    for signature in JPG_POSSIBLE_SIGNATURES: # Making sure the file is a jpg/jpeg by checking the signature
                        if curr_photo.startswith(signature):
                            is_jpg = True
                            sha256 = hashlib.sha256(curr_photo)
                            await hash_bot.send_message(chat_id= update.message.chat.id, text= f"The sha256 hash of the photo is:\n{sha256.hexdigest()}")
                            break
                
                if not is_jpg:
                    await hash_bot.send_message(chat_id= update.message.chat.id, text= "ERROR: This bot only accepts jpg files.")




if __name__ == '__main__':
    asyncio.run(main())