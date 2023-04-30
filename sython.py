import telethon
from telethon import events
from config import *
import os
import logging
import asyncio
import time
from telethon.tl import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.utils import get_display_name
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors import FloodWaitError
from telethon import TelegramClient, events
from collections import deque
from telethon import functions
from telethon.errors.rpcerrorlist import (
    UserAlreadyParticipantError,
    UserNotMutualContactError,
    UserPrivacyRestrictedError,
)
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import InputPeerUser
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl import functions
from hijri_converter import Gregorian
from telethon.tl.functions.channels import LeaveChannelRequest
import base64
import datetime
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
import requests
# -

sython1.start()
sython2.start()

c = requests.session()
bot_username = '@zmmbot'
bot_usernamee = '@A_MAN9300BOT'

y = datetime.datetime.now().year
m = datetime.datetime.now().month
dayy = datetime.datetime.now().day
day = datetime.datetime.now().strftime("%A")
m9zpi = f"{y}-{m}-{dayy}"
sec = time.time()

LOGS = logging.getLogger(__name__)

DEVS = [
    5159123009,
]



async def join_channel():
    try:
        await sython(JoinChannelRequest("@saythonh"))
    except BaseException:
        pass

@sython1.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit("**جاري الفحص..**")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f'''
╭──⌯𝗦𝗢𝗨𝗥𝗖𝗘 𝗦𝗬𝗧𝗛𝗢𝗡⌯──╮

※ 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 -  𝗦𝗔𝗬𝗧𝗛𝗢𝗡𝗛    ※

※ 𝗩𝗘𝗥𝗦𝗜𝗢𝗡 - 𝟭.𝟬 - 𝗥𝗘𝗩𝗜𝗦𝗘𝗗   ※

※ 𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥 - 𝗛𝗨𝗦𝗔𝗠.𝗙𝗔  ※

╰───⌯𝗦𝗬𝗧𝗛𝗢𝗡 𝗣𝗢𝗜𝗡𝗧⌯───╯
''')


@sython2.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit("**جاري الفحص..**")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(f'''
╭──⌯𝗦𝗢𝗨𝗥𝗖𝗘 𝗦𝗬𝗧𝗛𝗢𝗡⌯──╮

※ 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 -  𝗦𝗔𝗬𝗧𝗛𝗢𝗡𝗛    ※

※ 𝗩𝗘𝗥𝗦𝗜𝗢𝗡 - 𝟭.𝟬 - 𝗥𝗘𝗩𝗜𝗦𝗘𝗗   ※

※ 𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥 - 𝗛𝗨𝗦𝗔𝗠.𝗙𝗔  ※

╰───⌯𝗦𝗬𝗧𝗛𝗢𝗡 𝗣𝗢𝗜𝗡𝗧⌯───╯
''')

    
ownerhson_id = 5159123009

@sython1.on(events.NewMessage(outgoing=False, pattern='/point2'))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await sython1.get_entity(bot_usernamee)
        await sython1.send_message('@A_MAN9300BOT', 'جاري التجميع بواسطة | SOMY TEAM')
        channel_entity = await sython1.get_entity(bot_usernamee)
        await sython1.send_message('@A_MAN9300BOT', '/start')
        await asyncio.sleep(5)
        msg0 = await sython1.get_messages('@A_MAN9300BOT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await sython1.get_messages('@A_MAN9300BOT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await sython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython1.send_message(event.chat_id, f"لايوجد قنوات  في البوت | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython1(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython1(ImportChatInviteRequest(bott))
                msg2 = await sython1.get_messages('@A_MAN9300BOT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await sython1.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await sython1.send_message(event.chat_id, "تم الانتهاء من التجميع !")


@sython1.on(events.NewMessage(outgoing=False, pattern='/point1'))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await sython1.get_entity(bot_username)
        await sython1.send_message('@zmmbot', 'جاري التجميع بواسطة | SOMY TEAM')
        channel_entity = await sython1.get_entity(bot_username)
        await sython1.send_message('@zmmbot', '/start')
        await asyncio.sleep(5)
        msg0 = await sython1.get_messages('@zmmbot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await sython1.get_messages('@zmmbot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await sython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython1.send_message(event.chat_id, f"لايوجد قنوات  في البوت | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython1(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython1(ImportChatInviteRequest(bott))
                msg2 = await sython1.get_messages('@zmmbot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await sython1.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await sython1.send_message(event.chat_id, "تم الانتهاء من التجميع !")

@sython1.on(events.NewMessage(outgoing=True, pattern=r"\.اعادة تشغيل"))
async def update(event):
    await event.edit("• جارِ اعادة تشغيل السورس ..\n• انتضر 1-2 دقيقة  .")
    await sython1.disconnect()
    await sython1.send_message("me", "`اكتملت اعادة تشغيل السورس !`")

@sython1.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع المليار"))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await sython1.get_entity(bot_username)
        await sython1.send_message('@zmmbot', 'جاري التجميع بواسطة | SOMY TEAM')
        channel_entity = await sython1.get_entity(bot_username)
        await sython1.send_message('@zmmbot', '/start')
        await asyncio.sleep(5)
        msg0 = await sython1.get_messages('@zmmbot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await sython1.get_messages('@zmmbot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await sython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython1.send_message(event.chat_id, f"لايوجد قنوات  في البوت | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython1(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython1(ImportChatInviteRequest(bott))
                msg2 = await sython1.get_messages('@zmmbot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await sython1.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await sython1.send_message(event.chat_id, "تم الانتهاء من التجميع !")


##################


@sython1.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع الجوكر"))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await sython1.get_entity(bot_usernamee)
        await sython1.send_message('@A_MAN9300BOT', 'جاري التجميع بواسطة | SOMY TEAM')
        channel_entity = await sython1.get_entity(bot_usernamee)
        await sython1.send_message('@A_MAN9300BOT', '/start')
        await asyncio.sleep(5)
        msg0 = await sython1.get_messages('@A_MAN9300BOT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await sython1.get_messages('@A_MAN9300BOT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await sython1(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython1.send_message(event.chat_id, f"لايوجد قنوات  في البوت | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython1(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython1(ImportChatInviteRequest(bott))
                msg2 = await sython1.get_messages('@A_MAN9300BOT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await sython1.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await sython1.send_message(event.chat_id, "تم الانتهاء من التجميع !")



@sython2.on(events.NewMessage(outgoing=False, pattern='/point2'))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await sython2.get_entity(bot_usernamee)
        await sython2.send_message('@A_MAN9300BOT', 'جاري التجميع بواسطة | SOMY TEAM')
        channel_entity = await sython2.get_entity(bot_usernamee)
        await sython2.send_message('@A_MAN9300BOT', '/start')
        await asyncio.sleep(5)
        msg0 = await sython2.get_messages('@A_MAN9300BOT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await sython2.get_messages('@A_MAN9300BOT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await sython2(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython2.send_message(event.chat_id, f"لايوجد قنوات  في البوت | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython2(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython2(ImportChatInviteRequest(bott))
                msg2 = await sython2.get_messages('@A_MAN9300BOT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await sython2.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await sython2.send_message(event.chat_id, "تم الانتهاء من التجميع !")


@sython2.on(events.NewMessage(outgoing=False, pattern='/point1'))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await sython2.get_entity(bot_username)
        await sython2.send_message('@zmmbot', 'جاري التجميع بواسطة | SOMY TEAM')
        channel_entity = await sython2.get_entity(bot_username)
        await sython2.send_message('@zmmbot', '/start')
        await asyncio.sleep(5)
        msg0 = await sython2.get_messages('@zmmbot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await sython2.get_messages('@zmmbot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await sython2(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython2.send_message(event.chat_id, f"لايوجد قنوات  في البوت | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython2(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython2(ImportChatInviteRequest(bott))
                msg2 = await sython2.get_messages('@zmmbot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await sython2.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await sython2.send_message(event.chat_id, "تم الانتهاء من التجميع !")

@sython2.on(events.NewMessage(outgoing=True, pattern=r"\.اعادة تشغيل"))
async def update(event):
    await event.edit("• جارِ اعادة تشغيل السورس ..\n• انتضر 1-2 دقيقة  .")
    await sython2.disconnect()
    await sython2.send_message("me", "`اكتملت اعادة تشغيل السورس !`")

@sython2.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع المليار"))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await sython2.get_entity(bot_username)
        await sython2.send_message('@zmmbot', 'جاري التجميع بواسطة | SOMY TEAM')
        channel_entity = await sython2.get_entity(bot_username)
        await sython2.send_message('@zmmbot', '/start')
        await asyncio.sleep(5)
        msg0 = await sython2.get_messages('@zmmbot', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await sython2.get_messages('@zmmbot', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await sython2(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython2.send_message(event.chat_id, f"لايوجد قنوات  في البوت | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython2(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython2(ImportChatInviteRequest(bott))
                msg2 = await sython2.get_messages('@zmmbot', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await sython2.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await sython2.send_message(event.chat_id, "تم الانتهاء من التجميع !")


##################


@sython2.on(events.NewMessage(outgoing=True, pattern=r"\.تجميع الجوكر"))
async def _(event):
        await event.edit("حسنا, تأكد من انك مشترك ب قنوات الاشتراك الاجباري لتجنب الأخطأء")
        channel_entity = await sython2.get_entity(bot_usernamee)
        await sython2.send_message('@A_MAN9300BOT', 'جاري التجميع بواسطة | SOMY TEAM')
        channel_entity = await sython2.get_entity(bot_usernamee)
        await sython2.send_message('@A_MAN9300BOT', '/start')
        await asyncio.sleep(5)
        msg0 = await sython2.get_messages('@A_MAN9300BOT', limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(5)
        msg1 = await sython2.get_messages('@A_MAN9300BOT', limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):

            await asyncio.sleep(5)

            list = await sython2(GetHistoryRequest(peer=channel_entity, limit=1,
                                                   offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await sython2.send_message(event.chat_id, f"لايوجد قنوات  في البوت | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await sython2(JoinChannelRequest(url))
                except:
                    bott = url.split('/')[-1]
                    await sython2(ImportChatInviteRequest(bott))
                msg2 = await sython2.get_messages('@A_MAN9300BOT', limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                
            except:
                await sython2.send_message(event.chat_id, f"خطأ من المحتمل تم حظر الانضمام ")
                break
        await sython2.send_message(event.chat_id, "تم الانتهاء من التجميع !")






print("💠 Sython Userbot Running 💠")
sython1.run_until_disconnected()
sython2.run_until_disconnected()