# (c) @PredatorHackerzZ || @TeleRoidGroup

import os

class Config(object):
	API_ID = int(os.environ.get("API_ID", "28421635"))
	API_HASH = os.environ.get("API_HASH", "a4856de5fec0b9b3601ff06425f3f58e")
	BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
	BOT_USERNAME = os.environ.get("BOT_USERNAME", "@PediaDrivexRobot")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002498165944"))
	SHORTLINK_URL = os.environ.get('SHORTLINK_URL')
	SHORTLINK_API = os.environ.get('SHORTLINK_API')
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "1534632634"))
	DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://PrimeRp:JNTymVXjKzBbDtiv@cluster0.rydwk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002098787584")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", None)
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
	OTHER_USERS_CAN_SAVE_FILE = [int(id) for id in os.environ.get("OTHER_USERS_CAN_SAVE_FILE", "").split(",") if id.strip()]
	ABOUT_BOT_TEXT = f"""
Ram Ram Bhagat 🙏 {first_name}

This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ **🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅**]────⍟
│
├🔸 **My Name:** [FileStore Bot](https://t.me/{PediaDrivexRobot})
│
├🔸 **Language:** [Python 3](https://www.python.org)
│
├🔹 **Library:** [Pyrogram](https://docs.pyrogram.org)
│
├🔹 **Hosted On:** Seenode
│
├🔸 **Developer:** [@Itsofficial_RP](http://t.me/Itsofficials_RP)
│
├🔹 **Bot Support:** [Support Group](https://t.me/animepediaextra)
│
├🔸 **Bot Updates:** [Bots Channel](https://t.me/Sigma_officials)
│
╰──────[ 😎 ]───────────⍟
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿:** [@Itsofficials_RP]

	HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.
