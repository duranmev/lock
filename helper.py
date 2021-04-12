import os,sys,readline,subprocess,time

red="\033[1;31m"
grn="\033[1;32m"
yel="\033[1;33m"
blue="\033[1;34m"
prple="\033[1;35m"
cyan="\033[1;36m"
res="\033[0m"

name=subprocess.run("cat ~/.hgto/name", capture_output=True,shell=True).stdout.decode('ascii')

def clear():
	os.system("clear")
	
clear()

def own():
	print(f"""
	_____________________________
{cyan}	HH    HH    GG GG G {red}    22 22
{cyan}	HH    HH   GG       {red}  22    22
{cyan}	HH HH HH  GG    GGG  {red}      22
{cyan}	HH    HH   GG     GG  {red}   22
{cyan}	HH    HH     GG GG  {red}   22 22 22{res}
	_____________________
	 {yel}* {grn}Mevrick Duran {yel}*{res}
	_____________________""")

def menu():
	own()
	print(f"""
 {grn}This tool needs more {cyan}options{grn}, you can give 
 {cyan}suggestions{grn} on what options to add in this tool
 choose option '{yel}c{grn}'{res}

	{red}a   {cyan}Hack Facebook

	{red}b   {cyan}Exit

	{red}c   {cyan}Suggest Options{res}
	
""")
	menuans=input(f" {grn}choice : "+yel)
	
	if menuans == 'a':
		menua()
	elif menuans == 'b':
		print(" Good Bye .")
		exit()
	elif menuans == 'c':
		print(f"""
	{grn}Giving your own suggestions
	is a very big help to this tool
	thank you very much
	I will put your name in the tool.
	message me at facebook{res}
		
	{red}a   {cyan}send suggestiions

	{red}b   {cyan}exit{res}
		""")
		ans=input(f" {grn}choice : "+yel)
		if ans=='a':
			os.system("termux-open-url https://www.facebook.com/lyosowasasosowasa")
		elif ans=='b':
			exit()
	else:
		clear()
		print(f" {red}Invalidd input")
		menu()
def menua():
	clear()
	print(f"""
	
		{red}a   {cyan}I want to recover my account
	
		{red}b   {cyan}I want to Hack someones Account

		{red}c   {cyan}back
{res}
	""")
	menuaans=input(f" {grn}choice : "+yel)
	if menuaans=='a':
		menuaa()
	elif menuaans=='b':
		menuab()
	elif menuaans=='c':
		clear()
		menu()
	else:
		clear()
		print(f"{red} Invalid input")
		menua()
	
def menuaa():
	clear()

	print(f"""
{grn}	You may be able to get back into your 
	Facebook account by using an alternate
	email or mobile phone number listed on
	your account. If you don't know what 
	alternate information you have: 
	Go to {yel}facebook.com/login/identify 
	{grn}and follow the instructions.
		
		{red}a   {cyan}Follow the link

		{red}b   {cyan}back

		{red}c   {cyan}exit
		{res}
	""")
	ans=input(" choice : ")
	if ans=='a':
		os.system("termux-open-url https://facebook.com/login/identify ")
		menuaa()
	elif ans=='b':
		menua()
	elif ans=='c':
		exit()
	else:
		clear()
		print(f"{red} Invalid input")
		menuaa()
	
def menuab():
	clear()
	print(f"""
	{grn}We can hack someone by using the phishing 
	method ,sorry ,brute force method is 
	currently unavailble this time.
		
		{red}a   {cyan}whats does phishing means?
		
		{red}b   {cyan}Install Phishing tool
		
		{red}c   {cyan}back

		{red}d   {cyan}exit
{res}
		""")
		
	ans=input(f" {grn}choice : "+yel)
	if ans=='a':
		clear()
		print(f"""
	{grn}Phishing is a type of social engineering 
	attack often used to steal user data, 
	including login credentials and credit 
	card numbers. It occurs when an attacker, 
	masquerading as a trusted entity, dupes 
	a victim into opening an email, instant 
	message, or text message
	or
	we're going to make a fake login page of 
	any social media apps to get their user 
	and password.
		
		{red}a   {cyan}back

		{red}b   {cyan}exit{res}
		
		""")
		ans=input(f"{grn} choice : "+yel)
		if ans=='a':
			menuab()
		elif ans=='b':
			exit()
		else:
			clear()
			print(f"{red} Invalid input")
			menuab()
	elif ans=='b':
		def menuabb():
			print(f""" 
{grn}	are you sure you want to install 
	the phishing tool?
			
		{red}a   {cyan}yes
	
		{red}b  {cyan} back
	
			""")
		menuabb()
		ans=input(f" {grn}choice : "+yel)
		if ans=='a':
			clear()
			print(f"""
	{grn}here are the commands, it is in single line
	copy and paste it in the command line


	{cyan}cd ; git clone git://github.com/htr-tech/nexphisher.git ; cd nexphisher ; bash tmux_setup ; bash nexphisher
	
	
			{res}""")

		elif ans=='b':
			menuab()
		else:
			clear()
			print(f"{red} Invalid input")
			menuab()
	
	elif ans=='c':
		menua()
	elif ans=='d':
		exit()
	else:
		clear()
		print(f" {red}Invalid input")
		menu()
		
menu()



