
import re













from pyrogram import Client, filters

app = Client(session_name="ssn",bot_token='1043241288:AAEUiI9LT1nHWmap0Yo7VhhJQ3W14yiCU7M',api_id=950979,api_hash="e3135b7af1cd3681d5e9bad56591ff65")
s = -1001165875030
des = -1001483523101
@app.on_message(filters.chat(s) & filters.text & ~filters.edited)
def forward(client,Message):
 f = False
 words = ['dekho','TRUST','join','fix','😱','😳','👆','👇','☝️','https://','😂','🤔','pass','chase','link','suno','member','❓','loss','audio','open',"report",'paid','contact','baazigar','market','load','whatsapp','book','bhai','🐴','only','chut','tennis','teen','lavde','chutiya','bc','kya','line','LUND','WICKET LU','?','loda','telegram','chor',"kama","lakh",' id','स',"kitna"]
 for word in words:
  if word.casefold() in Message.text.casefold():
    return
 x = Message.text
 y = re.search("[0-9][0-9][0-9]?.?.?.?.?.?.?[0-9].?.?.?.?.?👈🏼.?.?.?.?.?🕵🏻.?.?.?.?.?[0-9][0-9]?.?.?.?.?.?.?OVER.?.?.?.?.?🕵🏻",x)
 z = re.search("[0-9][0-9][0-9]?.?.?.?.?.?.?[0-9].?.?.?.?.?🏳️‍🌈🏻.?.?.?.?.?[A-Za-z][A-Za-z][A-Za-z][A-Za-z]?.?.?.?.?.?.?.?.?.?.?.?.?.?.?.?.?.?.?.?.?.?.?🏳️‍🌈🏻",x)
 a = re.search("^[1-9]$", x)
 d = re.search("[1-9]?[1-9]?.?.?.?[0-9]?[0-9]?.?.?.?.?🎾.?.?.?.?[0-9]?[0-9]?[0-9]?.?.?.?.?☎☎?", x)
 d = re.search("[1-9][1-9]?.?.?.?OVER.?.?.?.?.?.?[0-9][0-9]?.?.?.?.?", x)
 for q in [y, z, a, d]:
     try:
         client.send_message(des, str(q.group()))
         print(q.group())
     except Exception as e:
         print(e)
         continue
app.run()
