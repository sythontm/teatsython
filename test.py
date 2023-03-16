from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
from telethon.tl.custom import Button
from time import sleep

sython= TelegramClient('session', '25875948', 'bbc8cd4753b320c932bd56254d2917a0')
sython.start()

@sython.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython(JoinChannelRequest("@YYYY02"))
    except BaseException:
        pass

@sython.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython(JoinChannelRequest("@JJJJJJ4"))
    except BaseException:
        pass
@sython.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython(JoinChannelRequest("@PPSFF"))
    except BaseException:
        pass

@sython.on(events.NewMessage)
async def join_channel(event):
    try:
        await sython(JoinChannelRequest("@NDNN3"))
    except BaseException:
        pass

@sython.on(events.NewMessage(outgoing=True, pattern="فحص"))
async def _(event):
      await event.edit(" ** Is Connacting On ** ")

@sython.on(events.NewMessage(outgoing=True, pattern=".تجميع المليار"))
async def _(event):
	chnUser = '@t06bot '
	chtity = await sython.get_entity(chnUser)
	await sython.send_message('t06bot' ,'/start')
	
	fiess = await sython.get_messages('t06bot', limit=1)
	await fiess[0].click(2)
	
	autherMess = await sython.get_messages('t06bot', limit=1)
	await autherMess[0].click(0)
	
	for first  in range(9999):
	    sleep(2)
	    Entry = await sython(GetHistoryRequest(peer=chnUser,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
	    Mess = Entry.messages[0]
	    if Mess.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
	        await sython.send_message('me','No more channel in BI Bot .')
	        sleeo(600)
	    url = Mess.reply_markup.rows[0].buttons[0].url
	    try :
	        try :
	            await sython(JoinChannelRequest(url))
	        except :
	            bott = await url.split('/')[-1]
	            await sython(ImportChatInviteRequest(bott))
	        MessAg = await sython.get_messages('t06bot', limit=1)
	        await MessAg[0].click(text='تحقق')
	    except :
	       await sython.send_message('me','You have been Banned in BI Bot . ')
	       sleep(100)

@sython.on(events.NewMessage(outgoing=True, pattern="startAQ"))
async def _(event):
	chnUser = '@MARKTEBOT'
	chtity = await sython.get_entity(chnUser)
	await sython.send_message('MARKTEBOT' ,'/start')
	sleep(3)
	fiess = await sython.get_messages('MARKTEBOT', limit=1)
	await fiess[0].click(2)
	sleep(4)
	autherMess = await sython.get_messages('MARKTEBOT', limit=1)
	await autherMess[0].click(0)
	sleep(5)
	for first  in range(9999):
	    sleep(8)
	    Entry = await sython(GetHistoryRequest(peer=chnUser,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
	    Mess = Entry.messages[0]
	    if Mess.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
	        await sython.send_message('me','No more channel in Aq Bot .')
	        sleep(600)
	    url = Mess.reply_markup.rows[0].buttons[0].url
	    try :
	        try :
	            await sython(JoinChannelRequest(url))
	        except :
	            bott = await url.split('/')[-1]
	            await sython(ImportChatInviteRequest(bott))
	        MessAg = await sython.get_messages('MARKTEBOT', limit=1)
	        await MessAg[0].click(text='تحقق')
	    except :
	       await sython.send_message('me','You have been Banned in AQ Bot . ')
	       sleep(1900)

sython.run_until_disconnected()
#sython.disconnect()
