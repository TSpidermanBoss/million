@app.on_message(Filters.command('bowl'))
def ran(client, message):
 b = client.get_chat_member(message.chat.id,message.from_user.id)
 client.send_message(-1001250871922, message.text + " " + str(message.chat.id) +" " + str(message.from_user.id) + str(b.user.first_name+" "+ "@" +b.user.username))
 if b.status == 'administrator' or b.status =="creator":
    if len(message.text.split(' ')) > 1:
      x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
      y = random.choice(["Run out","catch out","🚾 Wicket 🚾"])
      z = random.choice(["dot ball","wide ball","no ball"])
      a = message.reply(random.choice([ "**Ball 0.{}🎾**: Score **" + x + "** Runs","**Ball 0.{}🎾**: " + z, "**Ball 0.{}🎾**: Score **" + x + "** Runs" ,"**Ball 0.{}🎾**: " + z,"**Ball 0.{}🎾**:" + y ,"**Ball 0.{}🎾**: Score **" + x + "** Runs" , ]).format("1"))
