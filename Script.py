class script(object):
    CMD_LIST = """𝐇𝐢 {},
• /id - get id of a specifed user. 
• /info  - get information about a user. 
• /imdb  - get the film information from IMDb source. 
• /search  - get the film information from various sources. 
• /whois :-give a user full details 

 ᴛʜɪs ɪs ғᴏʀ ᴀᴅᴍɪɴs 

• /logs - to get the rescent errors 
• /stats - to get status of files in db. 
• /delete - to delete a specific file from db. 
• /users - to get list of my users and ids. 
• /chats - to get list of the my chats and ids 
• /leave  - to leave from a chat. 
• /disable  -  do disable a chat. 
• /ban  - to ban a user. 
• /unban  - to unban a user. 
• /channel - to get list of total connected channels 
• /broadcast - to broadcast a message to all users. 
• /connect  - connect a particular chat to your PM. 
• /disconnect  - disconnect from a chat. 
• /connections - list all your connections. 
• /pin :- Pin The Message You Replied To Message To Send A Notification To Group Members. 
• /unpin :- Unpin The Current Pinned Message. If Used As A Reply, Unpins The Replied To Message. 
• /filter - add a filter in chat. 
• /filters - list all the filters of a chat. 
• /del - delete a specific filter in chat. 
• /delall - delete the whole filters in a chat (chat owner only)"""

    HELP_TXT = """𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""
  
    MUSIC_TXT = """𝙷𝙴𝚈 𝙼𝙰𝙽!
𝙷𝙴𝚁𝙴 𝙸𝚂 𝚈𝙾𝚄 𝙲𝙰𝙽 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙼𝚄𝚂𝙸𝙲 𝙱𝚈 𝚃𝙷𝙴 𝙲𝙾𝙼𝙼𝙰𝙽𝙳 /song
NOTE : WORKS ONLY ON GROUP."""

    BOT_TXT = """𝐇𝐢 {},
➪ How To Use This Bot

/update - To Join Our Main Channel, You can use this 😀"""
    UPDATE_CMD = """𝐇𝐢 {}, 
➪ To Working of This Bot, Join the Main Channel Below 

➪ Joining Because of Updates of Bots and All Others are through Main Channel

➪ It is because of Copyright Issue is Very Low Compairing to Other Channels 😀"""
    START_TXT = """Hᴇʏ {},
𝙼𝚈 𝙽𝙰𝙼𝙴 𝙸𝚂 <a href=https://t.me/{}>{}</a>,\n 𝙸 𝙲𝙰𝙽 𝙿𝚁𝙾𝚅𝙸𝙳𝙴 𝙼𝙾𝚅𝙸𝙴𝚂, 𝙹𝚄𝚂𝚃 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙼𝙰𝙺𝙴 𝙼𝙴 𝙰𝙳𝙼𝙸𝙽..."""
    SOURCE_TXT = """<b>NOTE:</b>
- This is a Eva Mari clone Project
- 𝚂𝙾𝚄𝚁𝙲𝙴 𝙲𝙾𝙳𝙴 :<a href=https://github.com/Jeolpaul/George-MalarAutofilter>George-MalarAutofilter</a>
<b>DEV:</b>
- 𝙳𝚎𝚟 <a href=https/t.me/luna0497h>LUNA</a>

<b>💘 Team ➜ <a href=https://t.me/lunamovies007>💫 LUNA 💫</a>\n✯ ━━━━━ ✧ ━━━━━ ✯</b>\n"""

    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. George Malar Bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""

    BUTTON_TXT = """Help: <b>Buttons</b>

- This Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. George Malar Bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/Beta_Bot_Updates)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""

    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""

    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""

    ABOUT_TXT = """𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝙼𝚈 𝙷𝙴𝙻𝙿 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""
    ABOUT_TXT = """<b>✯ 𝙼𝚈 𝙽𝙰𝙼𝙴 : {}
<b>✯ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁 : <a href=https://t.me/JP_Jeol_org>ᴊᴇᴏʟ</a></b>
<b>✯ 𝚄𝙿𝙳𝙰𝚃𝙴𝚂 : <a href=https://t.me/beta_bot_updates>ʙᴇᴛᴀ ᴜᴘᴅᴀᴛᴇs</a></b>
<b>✯ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈 : 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼</b>
<b>✯ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴 : 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹</b>
<b>✯ 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴 : 𝙼𝙾𝙽𝙶𝙾-𝙳𝙱</b>
<b>✯ 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁 : ʜᴇʀᴏᴋᴜ</b>
<b>✯ 𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂 : 𝚅1.0.43 [𝙼𝙰𝙹𝙾𝚁]</b>"""

    STATUS_TXT = """᚛› 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
᚛› 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
᚛› 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
᚛› 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> """
 
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
 
