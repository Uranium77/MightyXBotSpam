from MightyXSpam import Mig, Mig2, Mig3, Mig4, Mig5, Mig6, Mig7, Mig8, Mig9, Mig10, SUDO_USERS
from telethon import events, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
from MightyXSpam import CMD_HNDLR as hl
    
HELP_PIC = "https://telegra.ph/file/efc9f0fafe82b8cfe255d.jpg"

Mig_Help = "__Click On Below Buttons For Help__"


@Mig.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Mig2.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Mig3.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Mig4.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Mig5.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Mig6.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Mig7.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Mig8.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Mig9.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
@Mig10.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):
    if event.sender_id in SUDO_USERS:
       await event.client.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=Mig_Help,
                                  buttons=[
           [
            Button.inline("• Spam •", data="spam"),
            Button.inline("• Raid •", data="raid"),
           ],
           [
            Button.inline("• Extra •", data="extra"),
           ],
           [    
            Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/ABOUT_THE_URANIUM")
           ],
           [
           Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/URANIUM_FIGHTERS")
           ],
           ],
           )              

  
  
extra_msg = f"""
**Help Extra Cmds**

**Userbot**: Userbot Cmds
Command:
i) {hl}ping 
ii) {hl}alive
iii) {hl}restart
iv) {hl}addsudo <reply to user> || Owner Cmd ||

**Echo**: To Active Echo On Any User
Command:
i) {hl}addecho <reply to user>
ii) {hl}rmecho <reply to user>

**Leave**: To Leave Group/Channel
Command:
i) {hl}leave <group/chat id>
ii) {hl}leave : Type in the Group bot will auto leave that group

**Packspam**: Sticker Pack Spam
i) {hl}packspam (replying to any sticker)

**© @MightyXSupport**
"""

                 
raid_msg = f"""
**Help Raid Cmds**


**Raid:** Activates Raid on Any individual User For Given Range.
Command:
i) {hl}raid <count> <username
ii) {hl}raid <count> <reply to user>

**Delayraid**: Activates Raid on Any individual User For Given Range.
Command:
i) {hl}delayraid <delay> <count> <Username of User>
ii) {hl}delayraid <delay> <count> <reply to a User>

**ReplyRaid:** Activates Reply Raid on The User!!
Command:
i) {hl}replyraid <replying to user>
ii) {hl}dreplyraid <username>

**DReplyRaid:** Deactivates Reply Raid on The User!!
Command:
i) {hl}dreplyraid <replying to user>
ii) {hl}dreplyraid <username>


**© @MightyXSupport**
"""

spam_msg = f"""
**Help Spam Cmds**

**Spam**: Spams a Message For Given Counter(<= 100).
Command:
i) {hl}spam <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
ii) {hl}spam <count> <replying any message>

**Bigspam**: Spams a Message For Given Counter.
Command:
i) {hl}bigspam <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
ii) {hl}bigspam <count> <replying any message>

**Delayspam**: Delay Spam a Text For Given Counter After Given Time.
Command:
i) {hl}delayspam <delay> <count> <message to spam> (you can reply any message if you want bot to reply that message and do spamming)
ii) {hl}delayspam <delay> <count> <replying any message>

**Pornspam**: Pornography Spam.
Command:
i) {hl}pornspam <count>

**Hang**: Spams Hanging Message For Given Counter.
Command:
i) {hl}hang <counter> (you can reply any message if you want bot to reply that message and do spamming)

** © @URANIUM_FIGHTERS**
"""                     
           
           
@Mig.on(events.CallbackQuery(pattern=r"help_back"))
@Mig2.on(events.CallbackQuery(pattern=r"help_back"))
@Mig3.on(events.CallbackQuery(pattern=r"help_back"))
@Mig4.on(events.CallbackQuery(pattern=r"help_back"))
@Mig5.on(events.CallbackQuery(pattern=r"help_back"))
@Mig6.on(events.CallbackQuery(pattern=r"help_back"))
@Mig7.on(events.CallbackQuery(pattern=r"help_back"))
@Mig8.on(events.CallbackQuery(pattern=r"help_back"))
@Mig9.on(events.CallbackQuery(pattern=r"help_back"))
@Mig10.on(events.CallbackQuery(pattern=r"help_back"))
async def helpback(event):
   if event.query.user_id in SUDO_USERS:    
      await event.edit(
            Mig_Help,
            buttons=[
                [
            Button.inline("Spam", data="spam"),
            Button.inline("Raid", data="raid"),
           ],
           [
            Button.inline("Extra", data="extra"),
           ],
           [    
            Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/ABOUT_THE_URANIUM")
           ],
           [
           Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/URANIUM_FIGHTERS")
           ],
           ],
        )           
   else:
        Alert = (
                "Noob !! Make Your Own URANIUM X Spam Bots !! @URANIUM_FIGHTERS"
            )
        await event.answer(Alert, cache_time=0, alert=True)
      
           
                      
@Mig.on(events.CallbackQuery(pattern=r"spam"))
@Mig2.on(events.CallbackQuery(pattern=r"spam"))
@Mig3.on(events.CallbackQuery(pattern=r"spam"))
@Mig4.on(events.CallbackQuery(pattern=r"spam"))
@Mig5.on(events.CallbackQuery(pattern=r"spam"))
@Mig6.on(events.CallbackQuery(pattern=r"spam"))
@Mig7.on(events.CallbackQuery(pattern=r"spam"))
@Mig8.on(events.CallbackQuery(pattern=r"spam"))
@Mig9.on(events.CallbackQuery(pattern=r"spam"))
@Mig10.on(events.CallbackQuery(pattern=r"spam"))
async def help_spam(event):
   if event.query.user_id in SUDO_USERS:    
       await event.edit(
            spam_msg,
            buttons=[
                [
            Button.inline("< Back", data="help_back"),
            ],
            ],
            ) 
   else:
        Alert = (
                "Noob !! Make Your Own URANIUM X Spam Bots !! @URANIUM_FIGHTERS"
            )
        await event.answer(Alert, cache_time=0, alert=True)
                 
                                                       
@Mig.on(events.CallbackQuery(pattern=r"raid"))
@Mig2.on(events.CallbackQuery(pattern=r"raid"))
@Mig3.on(events.CallbackQuery(pattern=r"raid"))
@Mig4.on(events.CallbackQuery(pattern=r"raid"))
@Mig5.on(events.CallbackQuery(pattern=r"raid"))
@Mig6.on(events.CallbackQuery(pattern=r"raid"))
@Mig7.on(events.CallbackQuery(pattern=r"raid"))
@Mig8.on(events.CallbackQuery(pattern=r"raid"))
@Mig9.on(events.CallbackQuery(pattern=r"raid"))
@Mig10.on(events.CallbackQuery(pattern=r"raid"))
async def help_raid(event):
     if event.query.user_id in SUDO_USERS:
        await event.edit(
            raid_msg,
            buttons=[
            [
            Button.inline("< Back", data="help_back"),
            ],
            ],
            )  
     else:
        Alert = (
                "Noob !! Make Your Own URANIUM X Spam Bots !! @URANIUM_FIGHTERS"
            )
        await event.answer(Alert, cache_time=0, alert=True)
       


@Mig.on(events.CallbackQuery(pattern=r"extra"))
@Mig2.on(events.CallbackQuery(pattern=r"extra"))
@Mig3.on(events.CallbackQuery(pattern=r"extra"))
@Mig4.on(events.CallbackQuery(pattern=r"extra"))
@Mig5.on(events.CallbackQuery(pattern=r"extra"))
@Mig6.on(events.CallbackQuery(pattern=r"extra"))
@Mig7.on(events.CallbackQuery(pattern=r"extra"))
@Mig8.on(events.CallbackQuery(pattern=r"extra"))
@Mig9.on(events.CallbackQuery(pattern=r"extra"))
@Mig10.on(events.CallbackQuery(pattern=r"extra"))
async def help_extra(event):
   if event.query.user_id in SUDO_USERS:
        await event.edit(
            extra_msg,
            buttons=[
            [
            Button.inline("< Back", data="help_back"),                        
            ],
            ],
            )
   else:
        Alert = (
                "Noob !! Make Your Own URANIUM X Spam Bots !! @URANIUM_FIGHTERS"
            )
        await event.answer(Alert, cache_time=0, alert=True)

