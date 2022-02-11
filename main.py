import time
import os
from sys import executable, argv
import atexit
from multiprocessing import Process
from multiprocessing import Pool
import random
import re
try:
 from inputimeout import inputimeout, TimeoutOccurred
except:
 exec(open("./setup.py").read())
if os.name == 'nt':
  import json
if os.name != 'nt':
  import simplejson as json

try:
  import discum
except:
  exec(open("./setup.py").read())
print("""\
░█████╗░░██╗░░░░░░░██╗░█████╗░  ░██████╗███████╗██╗░░░░░███████╗  ██████╗░░█████╗░████████╗
██╔══██╗░██║░░██╗░░██║██╔══██╗  ██╔════╝██╔════╝██║░░░░░██╔════╝  ██╔══██╗██╔══██╗╚══██╔══╝
██║░░██║░╚██╗████╗██╔╝██║░░██║  ╚█████╗░█████╗░░██║░░░░░█████╗░░  ██████╦╝██║░░██║░░░██║░░░
██║░░██║░░████╔═████║░██║░░██║  ░╚═══██╗██╔══╝░░██║░░░░░██╔══╝░░  ██╔══██╗██║░░██║░░░██║░░░
╚█████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝  ██████╔╝███████╗███████╗██║░░░░░  ██████╦╝╚█████╔╝░░░██║░░░
░╚════╝░░░░╚═╝░░░╚═╝░░░╚════╝░  ╚═════╝░╚══════╝╚══════╝╚═╝░░░░░  ╚═════╝░░╚════╝░░░░╚═╝░░░

**Version: 1.1.8**""")
wbm=[13,16]
time.sleep(0.5)
class client:
  commands=[
    "owo hunt",
    "owo hunt",
    "owo battle"
    ]
  stopped = False
  totalcmd = 0
  class color:
    purple = '\033[95m'
    okblue = '\033[94m'
    okcyan = '\033[96m'
    okgreen = '\033[92m'
    warning = '\033[93m'
    fail = '\033[91m'
    reset = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'
    if os.name == "nt":
      purple = ''
      okblue = ''
      okcyan = ''
      okgreen = ''
      warning = ''
      fail = ''
      reset = ''
      bold = ''
      underline = ''
  with open('settings.json', "r") as file:
        data = json.load(file)
        token = data["token"]
        channel = data["channel"]
        gm = data["gm"]
        sm = data["sm"]
        pm = data["pm"]
        om = data["om"]
        ocp = data["prefix"]
        allowedid = data["allowedid"]
  if data["token"] and data["channel"] == 'nothing':
   print(f"{color.fail} !!! [ERROR] !!! {color.reset} Please Enter Information To Continue")
   time.sleep(1)
   exec(open("./newdata.py").read())
  print('=========================')
  print('|                       |')
  print(f'| [1] {color.purple}Load data         {color.reset}|')
  print(f'| [2] {color.purple}Create new data   {color.reset}|')
  print(f'| [3] {color.purple}Info              {color.reset}|')
  print('=========================')
  time.sleep(0.5)
choice = None
try:
 print("Automatically Pick Option [1] In 10 Seconds.")
 choice = inputimeout(prompt='Enter Your Choice: ', timeout=10)
except TimeoutOccurred:
 choice = "1"
if (choice == "1"):
      pass
elif (choice == "2"):
  exec(open("./newdata.py").read())
elif (choice == "3"):
      print(f"{client.color.purple} =========Support========== {client.color.reset}")
      print(f"{client.color.purple}https://discord.gg/3kTrhbBVQm{client.color.reset}")
      print(" ")
      print(f"{client.color.purple} =========Disclaimer========={client.color.reset}")
      print(f"{client.color.purple}This SelfBot Is Only For Education Purpose Only. Deny All Other Promises Or Responsibilities. Use The SelfBot At Your Own Risk.")
      print(" ")
      print(f'{client.color.purple} =========Credit=========={client.color.reset}')
      print(f'{client.color.purple} [Developer] {client.color.reset} Sudo-Nizel')
      print(f'{client.color.purple} [Developer] {client.color.reset} ahihiyou20')
      print(" ")
      print(f'{client.color.purple} =========Selfbot Commands=========={client.color.reset}')
      print("{Prefix}send {Message} [Send Your Provied Message}")
      print("{Prefix}restart [Restart The Selfbot]")
      print("{Prefix}exit [Stop The Selfbot]")
      print(" ")
      print("{Prefix} == Your Prefix")
      time.sleep(15)
      exit()
else:
 print(f'{client.color.fail} !! [ERROR] !! {client.color.reset} Wrong input!')
 time.sleep(2)
 exit()
def at():
  return f'\033[0;43m{time.strftime("%d %b %Y %H:%M:%S", time.localtime())}\033[0;21m'
bot = discum.Client(token=client.token, log=False)
@bot.gateway.command
def on_ready(resp):
    if resp.event.ready_supplemental: #ready_supplemental is sent after ready
        user = bot.gateway.session.user
        print("Logged in as {}#{}".format(user['username'], user['discriminator']))
@bot.gateway.command
def issuechecker(resp):
 if resp.event.message:
   m = resp.parsed.auto()
   if m['channel_id'] == client.channel:
    if m['author']['id'] == '408785106942164992' or m['author']['username'] == 'OwO' or m['author']['discriminator'] == '8456' or m['author']['public_flags'] == '65536':
     if 'captcha' in m['content']:
      print(f'{at()}{client.color.warning} !! [CAPTCHA] !! {client.color.reset} CAPTCHA   ACTION REQUİRED')
      client.stopped = True
      bot.gateway.close()
     if '(2/5)' in m['content']:
      print(f'{at()}{client.color.warning} !! [CAPTCHA] !! {client.color.reset} CAPTCHA   ACTION REQUİRED (2/5)')
      client.stopped = True
      bot.gateway.close()
     if '(3/5)' in m['content']:
      print(f'{at()}{client.color.warning} !! [CAPTCHA] !! {client.color.reset} CAPTCHA   ACTION REQUİRED (3/5)')
      client.stopped = True
      bot.gateway.close()
     if '(4/5)' in m['content']:
      print(f'{at()}{client.color.warning} !! [CAPTCHA] !! {client.color.reset} CAPTCHA   ACTION REQUİRED (4/5)')
      client.stopped = True
      bot.gateway.close()
     if '(5/5)' in m['content']:
      print(f'{at()}{client.color.warning} !! [CAPTCHA] !! {client.color.reset} CAPTCHA   ACTION REQUİRED (5/5)')
      client.stopped = True
      bot.gateway.close()
     if 'banned' in m['content']:
      print(f'{at()}{client.color.fail} !!! [BANNED] !!! {client.color.reset} your account have been banned from owo bot please open a issue on the Support Discord server')
      client.stopped = True
      bot.gateway.close()
     if 'complete your captcha to verify that you are human!'  in m['content']:
      print(f'{at()}{client.color.warning} !! [CAPTCHA] !! {client.color.reset} CAPTCHA   ACTION REQUİRED')
      client.stopped = True
      bot.gateway.close()
     if 'DM' in m['content']:
      print(f'{at()}{client.color.warning} !! [CAPTCHA] !! {client.color.reset} CAPTCHA   ACTION REQUİRED')
      client.stopped = True
      bot.gateway.close()
def runner():
   if client.stopped == True:
     pass
   if client.stopped == False:
        global wbm
        command=random.choice(client.commands)
        command2=random.choice(client.commands)
        bot.typingAction(str(client.channel))
        bot.sendMessage(str(client.channel), command)
        print(f"{at()}{client.color.okgreen} [SENT] {client.color.reset} {command}")
        client.totalcmd = client.totalcmd + 1
        if not command2==command:
          bot.typingAction(str(client.channel))
          time.sleep(13)
          bot.sendMessage(str(client.channel), command2)
          print(f"{at()}{client.color.okgreen} [SENT] {client.color.reset} {command2}")
          client.totalcmd = client.totalcmd + 1
        time.sleep(random.randint(wbm[0],wbm[1]))
def owoexp():
 if client.om == "YES":
  if client.stopped == True:
   pass
  if client.stopped == False:
        global wbm
        cringe = ["owo","uwu"]
        owo=random.choice(cringe)
        bot.typingAction(str(client.channel))
        bot.sendMessage(str(client.channel), owo)
        print(f"{at()}{client.color.okgreen} [SENT] {client.color.reset} {owo}")
        client.totalcmd = client.totalcmd + 1
        time.sleep(random.randint(wbm[0],wbm[1]))
 if client.om == "NO":
        pass
def owopray():
 if client.pm == "YES":
  if client.stopped == True:
   pass
  if client.stopped == False:
    bot.sendMessage(str(client.channel), "owo pray")
    print(f"{at()}{client.color.okgreen} [SENT] {client.color.reset} owo pray")
    client.totalcmd = client.totalcmd + 1
    time.sleep(13)
 if client.pm == "NO":
   pass
def gems():
 if client.gm == "YES":
  if client.stopped == True:
   pass
  if client.stopped == False:
    bot.typingAction(str(client.channel))
    time.sleep(5)
    bot.sendMessage(str(client.channel), "owo inv")
    print(f"{at()}{client.color.okgreen} [SENT] {client.color.reset} owo inv")
    client.totalcmd = client.totalcmd + 1
    time.sleep(7)
    msgs=bot.getMessages(str(client.channel), num=15)
    msgs=json.loads(msgs.text)
    inv = 0
    for msgone in msgs:
      if msgone['author']['id']=='408785106942164992' and 'Inventory' in msgone['content']:
        inv=re.findall(r'`(.*?)`', msgone['content'])
    if not inv:
       time.sleep(5)
       client.totalcmd = client.totalcmd - 1
       return
    else:
      if '50' in inv:
        bot.sendMessage(str(client.channel), "owo lb all")
        print(f"{at()}{client.color.okgreen} [SENT] {client.color.reset} owo lb all")
        time.sleep(13)
        gems()
        return
      if '100' in inv:
        bot.sendMessage(str(client.channel), "owo crate all")
        print(f"{at()}{client.color.okgreen} [SENT] {client.color.reset} owo crate all")
        time.sleep(2)
      for item in inv:
        try: 
          if int(item) > 100:
            inv.pop(inv.index(item)) #weapons
        except: #backgounds etc
          inv.pop(inv.index(item))
      tier = [[],[],[]]
      print(f"{at()}{client.color.okblue} [INFO] {client.color.reset} Found {len(inv)} gems Inventory")
      for gem in inv:
        gem = re.sub(r"[^a-zA-Z0-9]", "", gem)
        gem = int(float(gem))
        if 50 < gem < 58:
          tier[0].append(gem)
        elif 64 < gem < 72:
          tier[1].append(gem)
        elif 71 < gem < 79:
          tier[2].append(gem)
      for level in range(0,3):
        if not len(tier[level]) == 0:
          bot.sendMessage(str(client.channel), "owo use "+str(max(tier[level])))
          print(f"{at()}{client.color.okgreen} [SENT] {client.color.reset} owo use {str(max(tier[level]))}")
          time.sleep(7)
 if client.gm == "NO":
      pass
@bot.gateway.command
def othercommands(resp):
 if client.stopped == False:
  if resp.event.message:
   m = resp.parsed.auto()
   if m['author']['id'] == bot.gateway.session.user['id'] or m['channel_id'] == client.channel and m['author']['id'] == client.allowedid:
    prefix = client.ocp
    if prefix == "None":
     bot.gateway.removeCommand(othercommands)
     return
    if "{}send".format(prefix) in m['content']:
     message = m['content'][6::]
     bot.sendMessage(str(m['channel_id']), message)
     print(f"{at()}{client.color.okgreen} [SENT] {client.color.reset} {message}")
    if "{}restart".format(prefix) in m['content']:
     bot.sendMessage(str(m['channel_id']), "Restarting...")
     print(f"{client.color.okcyan} [INFO] Restarting...  {client.color.reset}")
     time.sleep(1)
     os.execl(executable, executable, *argv)
    if "{}exit".format(prefix) in m['content']:
     bot.sendMessage(str(m['channel_id']), "Exiting...")
     print(f"{client.color.okcyan} [INFO] Exiting...  {client.color.reset}")
     time.sleep(1)
     bot.gateway.close()
 if client.stopped == True:
    pass
@bot.gateway.command
def loopie(resp):
 if resp.event.ready:
  x=True
  pray = 0
  owo=pray
  gem=pray
  main=time.time()
  while x:
      runner()
      if time.time() - pray > random.randint(300, 600):
        owopray()
        pray=time.time()
      if time.time() - owo > random.randint(60, 300):
        owoexp()
        owo=time.time()
      if time.time() - gem > random.randint(300, 600):
        gems()
        gem=time.time()
      if client.sm == "YES":
       if time.time() - main > random.randint(1000, 2000):
        main=time.time()
        time.sleep(random.randint(500, 700))
      if client.sm == "NO":
       pass
def defination1():
  global once
  if not once:
    once=True
    if __name__ == '__main__':
      lol2= Pool(os.cpu_count() - 1)
      lol2.map(loopie)
      lol=Process(target=loopie)
      lol.run()
bot.gateway.run(auto_reconnect=True)
@atexit.register
def atexit():
 print(f"{client.color.purple} [1] Restart {client.color.reset}")
 print(f"{client.color.purple} [2] Support {client.color.reset}")
 print(f"{client.color.purple} [3] Statistics {client.color.reset}")
 print(f"{client.color.purple} [4] Exit    {client.color.reset}")
 time.sleep(0.5)
 client.stopped = True
 choice = input("Enter Your Choice: ")
 if choice == "1":
  os.execl(executable, executable, *argv)
 elif choice == "2":
  print("Having Issue? Tell Us In Our Support Server")
  print(f"{client.color.purple} https://discord.gg/3kTrhbBVQm {client.color.reset}")
 elif choice == "3":
  print(f"Total Number Of Commands Executed: {client.totalcmd}")
 elif choice == "4":
  bot.gateway.close()
 else:
  bot.gateway.close()
