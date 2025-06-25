import os, time, re
from typing import List
id_pattern = re.compile(r'^.\d+$')

class Config(object):
    # pyro client config
    API_ID = os.environ.get("API_ID", "")
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
   
    # database config
    DATABASE_NAME = os.environ.get("DATABASE_NAME","")     
    DATABASE_URL = os.environ.get("DATABASE_URL","")

    # other configs
    BOT_UPTIME = time.time()
    START_PIC = (os.environ.get("START_PIC", "https://envs.sh/N2f.jpg https://envs.sh/N2a.jpg https://envs.sh/N2O.jpg")).split()
    ADMIN = int(os.environ.get("ADMIN", ""))

    # channels
    IS_FSUB = os.environ.get("IS_FSUB", "False").lower() == "true"  # Set "True" For Enable Force Subscribe
    AUTH_CHANNELS = list(map(int, os.environ.get("AUTH_CHANNELS", "").split())) # Add Multiple Channels iD By Space
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))
    BIN_CHANNEL = int(os.environ.get("BIN_CHANNEL", ""))

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))


class Txt(object):
    # part of text configuration
    START_TXT = f"""Hey {{}}, 👋🏻

Time to revamp your files? ✨  
This bot is here to help you:

• Give your files awesome new names 📝  
• Spice things up with eye-catching thumbnails 🖼️  
• Seamlessly convert between video and file formats 🔄  
• Get truly unique with custom thumbnails, captions, prefixes, and suffixes! ✏️

🚨 **Important!**  
Renaming illegal content is a major no-no 🚫.  
Seriously, don't do it — or you'll get banned. ⛔
"""

    ABOUT_TXT = """
<b>❍ ᴍʏ ɴᴀᴍᴇ : <a href='https://telegram.me/FilexRenamerxBot'>Fɪʟᴇ Rᴇɴᴀᴍᴇʀ Bᴏᴛ</a>
❍ ʜᴏsᴛᴇᴅ ᴏɴ : VPS
❍ ᴅᴀᴛᴀʙᴀsᴇ : ᴍᴏɴɢᴏ ᴅʙ
❍ ʟᴀɴɢᴜᴀɢᴇ : ᴘʏᴛʜᴏɴ 𝟹
❍ ᴍʏ ᴄʀᴇᴀᴛᴏʀ : <a href='https://telegram.me/Unknown_RK01'>Rᴀᴠɪ Kᴜᴍᴀʀ</a>

➻ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ꜰᴏʀ ɢᴇᴛᴛɪɴɢ ᴍᴏʀᴇ ɪɴꜰᴏ ᴀʙᴏᴜᴛ ᴍᴇ.</b>
"""
    HELP_TXT = """
<b>ʀᴇɴᴀᴍᴇ ʙᴏᴛ ɪꜱ ᴀ ʜᴀɴᴅʏ ᴛᴏᴏʟ ᴛʜᴀᴛ ʜᴇʟᴘꜱ ʏᴏᴜ ʀᴇɴᴀᴍᴇ ᴀɴᴅ ᴍᴀɴᴀɢᴇ ʏᴏᴜʀ ꜰɪʟᴇꜱ ᴇꜰꜰᴏʀᴛʟᴇꜱꜱʟʏ.

➻ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ꜰᴏʀ ɢᴇᴛᴛɪɴɢ ᴍᴏʀᴇ ɪɴꜰᴏ.</b>
"""

    THUMBNAIL_TXT = """<b>» <u>ᴛᴏ ꜱᴇᴛ ᴄᴜꜱᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ</u></b>
    
➲ ꜱᴇɴᴅ ᴀɴʏ ᴘʜᴏᴛᴏ ᴛᴏ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ꜱᴇᴛ ɪᴛ ᴀꜱ ᴀ ᴛʜᴜᴍʙɴᴀɪʟ.
➲ /delthumb: ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ᴛʜᴜᴍʙɴᴀɪʟ.
➲ /viewthumb: ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴠɪᴇᴡ ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ᴛʜᴜᴍʙɴᴀɪʟ.

<b>ɴᴏᴛᴇ :</b> ɪꜰ ɴᴏ ᴛʜᴜᴍʙɴᴀɪʟ ꜱᴀᴠᴇᴅ ɪɴ ʙᴏᴛ ᴛʜᴇɴ, ɪᴛ ᴡɪʟʟ ᴜꜱᴇ ᴛʜᴜᴍʙɴᴀɪʟ ᴏꜰ ᴛʜᴇ ᴏʀɪɢɪɴɪᴀʟ ꜰɪʟᴇ ᴛᴏ ꜱᴇᴛ ɪɴ ʀᴇɴᴀᴍᴇᴅ ꜰɪʟᴇ"""

    CAPTION_TXT = """<b>» <u>ᴛᴏ ꜱᴇᴛ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ ᴀɴᴅ ᴍᴇᴅɪᴀ ᴛʏᴘᴇ</u></b>
    
<b>ᴠᴀʀɪᴀʙʟᴇꜱ :</b>         
ꜱɪᴢᴇ: {filesize}
ᴅᴜʀᴀᴛɪᴏɴ: {duration}
ꜰɪʟᴇɴᴀᴍᴇ: {filename}

➲ /set_caption: ᴛᴏ ꜱᴇᴛ ᴀ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ.
➲ /see_caption: ᴛᴏ ᴠɪᴇᴡ ʏᴏᴜʀ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ.
➲ /del_caption: ᴛᴏ ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ᴄᴜꜱᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ.

» ᴇx: /set_caption ꜰɪʟᴇ ɴᴀᴍᴇ: {filename}
"""

    PREFIX = """<b>» <u>ᴛᴏ ꜱᴇᴛ ᴄᴜꜱᴛᴏᴍ ᴘʀᴇꜰɪx</u></b>

➲ /set_prefix: ᴛᴏ ꜱᴇᴛ ᴀ ᴄᴜꜱᴛᴏᴍ ᴘʀᴇꜰɪx.
➲ /see_prefix: ᴛᴏ ᴠɪᴇᴡ ʏᴏᴜʀ ᴄᴜꜱᴛᴏᴍ ᴘʀᴇꜰɪx.
➲ /del_prefix: ᴛᴏ ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ᴄᴜꜱᴛᴏᴍ ᴘʀᴇꜰɪx.

» ᴇx: `/set_prefix @BotVerseRavi`
"""

    SUFFIX = """<b>» <u>ᴛᴏ ꜱᴇᴛ ᴄᴜꜱᴛᴏᴍ sᴜꜰꜰɪx</u></b>

➲ /set_suffix: ᴛᴏ ꜱᴇᴛ ᴀ ᴄᴜꜱᴛᴏᴍ sᴜꜰꜰɪx.
➲ /see_suffix: ᴛᴏ ᴠɪᴇᴡ ʏᴏᴜʀ ᴄᴜꜱᴛᴏᴍ sᴜꜰꜰɪx.
➲ /del_suffix: ᴛᴏ ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ᴄᴜꜱᴛᴏᴍ sᴜꜰꜰɪx.

» ᴇx: `/set_suffix @BotVerseRavi`
"""

    PROGRESS_BAR = """\n
 <b>🔗 Size :</b> {1} | {2}
️ <b>⏳️ Done :</b> {0}%
 <b>🚀 Speed :</b> {3}/s
️ <b>⏰️ ETA :</b> {4}
"""

    SEND_METADATA = """<b>» <u>ᴛᴏ ꜱᴇᴛ ᴄᴜꜱᴛᴏᴍ ᴍᴇᴛᴀᴅᴀᴛᴀ</u></b>

➲ /metadata: ᴛᴏ ꜱᴇᴛ ᴀ ᴄᴜꜱᴛᴏᴍ ᴍᴇᴛᴀᴅᴀᴛᴀ

ᴀꜰᴛᴇʀ ᴜsɪɴɢ ᴄᴍᴅ sᴇɴᴅ ᴀɴʏ ᴛᴇxᴛ ɪ ᴡɪʟʟ sᴀᴠᴇ ɪᴛ ᴀs ʏᴏᴜʀ ᴍᴇᴛᴀᴅᴀᴛᴀ

» ᴇx: `@BotVerseRavi`
"""
