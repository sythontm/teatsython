from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest
from telethon.tl.custom import Button
from time import sleep

ArsThon= TelegramClient('session', '25875948', 'bbc8cd4753b320c932bd56254d2917a0')
ArsThon.start()

@ArsThon.on(events.NewMessage)
async def join_channel(event):
    try:
        await ArsThon(JoinChannelRequest("@YYYY02"))
    except BaseException:
        pass

@ArsThon.on(events.NewMessage)
async def join_channel(event):
    try:
        await ArsThon(JoinChannelRequest("@JJJJJJ4"))
    except BaseException:
        pass
@ArsThon.on(events.NewMessage)
async def join_channel(event):
    try:
        await ArsThon(JoinChannelRequest("@PPSFF"))
    except BaseException:
        pass

@ArsThon.on(events.NewMessage)
async def join_channel(event):
    try:
        await ArsThon(JoinChannelRequest("@NDNN3"))
    except BaseException:
        pass

@ArsThon.on(events.NewMessage(outgoing=True, pattern="Test"))
async def _(event):
      await event.edit(" ** Is Connacting On ** ")

@ArsThon.on(events.NewMessage(outgoing=True, pattern="startBI"))
async def _(event):
	chnUser = '@t06bot '
	chtity = await ArsThon.get_entity(chnUser)
	await ArsThon.send_message('t06bot' ,'/start')
	
	fiess = await ArsThon.get_messages('t06bot', limit=1)
	await fiess[0].click(2)
	
	autherMess = await ArsThon.get_messages('t06bot', limit=1)
	await autherMess[0].click(0)
	
	for first  in range(9999):
	    sleep(2)
	    Entry = await ArsThon(GetHistoryRequest(peer=chnUser,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
	    Mess = Entry.messages[0]
	    if Mess.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
	        await ArsThon.send_message('me','No more channel in BI Bot .')
	        sleeo(600)
	    url = Mess.reply_markup.rows[0].buttons[0].url
	    try :
	        try :
	            await ArsThon(JoinChannelRequest(url))
	        except :
	            bott = await url.split('/')[-1]
	            await ArsThon(ImportChatInviteRequest(bott))
	        MessAg = await ArsThon.get_messages('t06bot', limit=1)
	        await MessAg[0].click(text='تحقق')
	    except :
	       await ArsThon.send_message('me','You have been Banned in BI Bot . ')
	       sleep(100)

@ArsThon.on(events.NewMessage(outgoing=True, pattern="startAQ"))
async def _(event):
	chnUser = '@MARKTEBOT'
	chtity = await ArsThon.get_entity(chnUser)
	await ArsThon.send_message('MARKTEBOT' ,'/start')
	sleep(3)
	fiess = await ArsThon.get_messages('MARKTEBOT', limit=1)
	await fiess[0].click(2)
	sleep(4)
	autherMess = await ArsThon.get_messages('MARKTEBOT', limit=1)
	await autherMess[0].click(0)
	sleep(5)
	for first  in range(9999):
	    sleep(8)
	    Entry = await ArsThon(GetHistoryRequest(peer=chnUser,limit=1,offset_date=None,offset_id=0,max_id=0,min_id=0,add_offset=0,hash=0))
	    Mess = Entry.messages[0]
	    if Mess.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
	        await ArsThon.send_message('me','No more channel in Aq Bot .')
	        sleep(600)
	    url = Mess.reply_markup.rows[0].buttons[0].url
	    try :
	        try :
	            await ArsThon(JoinChannelRequest(url))
	        except :
	            bott = await url.split('/')[-1]
	            await ArsThon(ImportChatInviteRequest(bott))
	        MessAg = await ArsThon.get_messages('MARKTEBOT', limit=1)
	        await MessAg[0].click(text='تحقق')
	    except :
	       await ArsThon.send_message('me','You have been Banned in AQ Bot . ')
	       sleep(1900)

ArsThon.run_until_disconnected()
#ArsThon.disconnect()
