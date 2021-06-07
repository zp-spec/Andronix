from os import *
from time import sleep
import webbrowser
class main :
	gr, r, g, y, b, p, c, w=[
	'\033[1;30m',
	'\033[1;31m',
	'\033[1;32m',
	'\033[1;33m',
	'\033[1;34m',
	'\033[1;35m',
	'\033[1;36m',
	'\033[1;37m' ] 
	print(r)
	system("figlet Andronix")
	print("  ")
	sleep(2)
	print(f"{r}[{g}1{r}]{g} Ubuntu")
	print(f"{r}[{g}2{r}]{g} Kali Linux")
	print(f"{r}[{g}3{r}]{g} Debian")
	print(f"{r}[{g}4{r}]{g} Arch")
	print(f"{r}[{g}5{r}]{g} Manjaro")
	print(f"{r}[{g}6{r}]{g} Fedora")
	print(f"{r}[{g}7{r}]{g} Void")
	print(f"{r}[{g}8{r}]{g} Alpinr")
	print(f"{r}[{g}9{r}]{g} Fix-All")
	print(f"{r}[{g}10{r}]{g} Info")
	print(f"{r}[{g}11{r}]{g} programer instagram account")
	Andronix=input(f"{r}locas {g}~# ")
	
	if Andronix == "1" :
		system("figlet Ubuntu")
		print("   ")
		print(f"{r}[{g}1{r}]{g} Ubuntu/18.04")
		print(f"{r}[{g}2{r}]{g} Ubuntu/20.04")
		Ubuntu=input(f"{r}Locas{g}/{r}Ubuntu {g}~# ")
		if Ubuntu == "1" :
			system("clear")
			system("pkg update -y && pkg install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Ubuntu/ubuntu.sh | bash")
		if Ubuntu == "2" :
			system("clear")
			system("pkg update -y && pkg install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Ubuntu20/ubuntu20.sh | bash")
	if Andronix == "2" :
		system("clear")
		system("pkg update -y && pkg install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Kali/kali.sh | bash")
		system("pkg update -y && pkg install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Kali/kali-xfce.sh | bash")
		system("pkg update -y && pkg install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Kali/kali-lxde.sh | bash")
		system("pkg update -y && pkg install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Kali/kali-lxqt.sh | bash")
	if Andronix == "3" :
		system("clear")
		system("pkg update -y && pkg install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Debian/debian.sh | bash")
	if Andronix == "4" :
		system("clear")
		system("pkg update -y && pkg install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Arch/armhf/arch.sh | bash")
	if Andronix == "5" :
		system("clear")
		system("pkg update -y && pkg install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Manjaro/manjaro.sh | bash")
	if Andronix == "6" :
		system("clear")
		system("pkg update -y && pkg install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Fedora/fedora.sh | bash")
	if Andronix == "7" :
		system("clear")
		system("pkg update -y && pkg install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Void/void.sh | bash")
	if Andronix == "8" :
		system("clear")
		system("pkg update -y && pkg install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Alpine/alpine.sh | bash")
	if Andronix == "9" :
		system("pkg update -y && pkg install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Kali/kali-xfce.sh | bash")
		system("pkg update -y && pkg install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Kali/kali-lxde.sh | bash")
		system("pkg update -y && pkg install curl proot tar -y && curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Kali/kali-lxqt.sh | bash")
	if Andronix == "10" :
		system("clear")
		print("Andronix is a tool make you install every linux system at termux and fix it")
	if Andronix == "11" :
		webbrowser.open("https://instagram.com/_zp_m?utm_medium=copy_link")