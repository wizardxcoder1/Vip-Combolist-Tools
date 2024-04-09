import os
from rich.panel import Panel
from rich.console import Console
#--------------RENKLER---------------#
P = '\033[2;35m' #PEMBE
B = '\033[1;97m' #BEYAZ
K = '\033[1;31m' #KIRMIZI
Y = '\033[2;32m' #YEŞİL
S = '\033[1;33m' #SARI
by = '@pythonwizard | @wizardxcoder' #YAPIMCI
BGreen = '\x1b[1;32m' #PARLAK YEŞİL
BYellow = '\x1b[1;33m' #PARLAK SARI
BBlue = '\x1b[1;34m' #MOR
BPurple = '\x1b[1;35m' #PARLAK PEMBE
BCyan = '\x1b[1;36m' #PARLAK MAVİ 
BWhite = '\x1b[1;37m' #PARLAK BEYAZ
M = '\033[2;36m' #MAVİ
#--------------RENKLER---------------#
console = Console()
try:
 from cfonts import render, say
except:
 os.system('pip install python-cfonts')
output = render('COMBO  TOOL', colors=['white', 'blue'], align='center')
print(output)
Info = Panel('''[bold white]~ Programmer : @wizardxcoder | Channel : @pythonwizard ~''',border_style="bold yellow")
tools = Panel('''[bold white]                    ~ Get Combolist Tools ~''',border_style="bold yellow")
console.print(tools)
console.print(Info)
class vipcombolog():
	def main():
		li = input(f"{K} 𖣔  {S}𝐶𝑜𝑚𝑏𝑜 𝐶̧𝑒𝑘𝑚𝑒𝑘 𝐼𝑠𝑡𝑒𝑑𝑖𝑔̆𝑖𝑛𝑖𝑧 𝑆𝑖𝑡𝑒𝑛𝑖𝑛 𝐿𝑖𝑛𝑘 𝐺𝑖𝑟𝑖𝑛𝑖𝑧 : {M}").lower()
		hesap_sayisi = int(input(f"{K} 𖣔  {S}𝐾𝑎𝑐̧ 𝐴𝑑𝑒𝑡 𝐻𝑒𝑠𝑎𝑝 𝐶̧𝑒𝑘𝑖𝑙𝑠𝑖𝑛 :  {M}"))
		with open("viplog.txt", "r") as viplog:
			if any(li in hesap for hesap in viplog):
				with open(f"{li}.txt", "a") as k:
					viplog.seek(0)
					hs = 0
					for hesap in viplog:
						if li in hesap:
							k.write(hesap)
							hs += 1
							if hs == hesap_sayisi:
								break
			else:
			 	 print(f"{K} 𖣔  {K}𝐻𝑒𝑠𝑎𝑝 𝐵𝑢𝑙𝑢𝑛𝑎𝑚𝑎𝑑𝚤. {M}")
		try:
			 open(f"{li}.txt","r")
			 sonuc = Panel(f'''[bold green]𝑇𝑜𝑝𝑙𝑎𝑚 {hesap_sayisi} 𝐻𝑒𝑠𝑎𝑝 {li}.txt 𝐴𝑑𝑙𝚤 𝐷𝑜𝑠𝑦𝑎𝑦𝑎 𝐾𝑎𝑦𝑑𝑒𝑑𝑖𝑙𝑑𝑖''',border_style="bold yellow")
			 console.print(sonuc)
		except:
			pass
vipcombolog.main()
