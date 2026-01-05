#Made by YHI547 organization
#Important: 
# Turn on your WiFi before using this tool to avoid problems
import os
import re
from colorama import Fore, Style
import time
m = time.strftime("%H:%M:%S")

st = Style.RESET_ALL
red = Fore.RED
gren = Fore.GREEN
blu = Fore.BLUE

ip_addres = os.popen('ipconfig').read()
reip = re.findall(r"\d.*", ip_addres)
av6a = reip[1]
av4a = reip[2]
av6w = reip[6]
av4w = reip[7]

cpu = os.cpu_count()

system = os.popen('systeminfo').read()
sm = re.findall(r'\w.*', system)
host = sm[0]
osn = sm[1]
reges = sm[6]
instal_data = sm[9]
sysbot = sm[10]
sysfa = sm[11]
sysmod = sm[12]
windir = sm[17]
sysdir = sm[18]
logser = sm[30]
ram = sm[23]


print(f"""                                {red} ({st}{gren} Made by YHI547 organization {st}{red}){st}{blu} ツ {st}
      
    
    {gren}[+]{st}{blu} Windows IP Configuration{st}
    {gren}[+]{st}{blu} Ethernet adapter Ethernet 2:{st}
        {red}[=>]IPv6: {st}{gren}{av6a}{st}
        
        {red}[=>]IPv4: {st}{gren}{av4a}{st}
        
    {gren}[+]{st}{blu} Wireless LAN adapter Wi-Fi:{st}
        {red}[=>]IPv6: {st}{gren}{av6w}{st}
        
        {red}[=>]IPv4: {st}{gren}{av4w}{st}     
    {red}======================{st}{gren}YHI547{st}{red}======================{st}
    {gren}[+]{st}{blu}the number of CPU cores on your system:{st}
        {red}[=>]CPU count: {st}{gren}{cpu}{st}
    {red}======================{st}{gren}YHI547{st}{red}======================{st}
    {gren}[+]{st}{blu}systeminfo :{st}
        {red}[=>]{st} {gren}{host}{st}
        {red}[=>]{st} {gren}{osn}{st}    
        {red}[=>]{st} {gren}{reges}{st}
        {red}[=>]{st} {gren}{instal_data}{st}
        {red}[=>]{st} {gren}{sysbot}{st}
        {red}[=>]{st} {gren}{sysfa}{st}
        {red}[=>]{st} {gren}{sysmod}{st}
        {red}[=>]{st} {gren}{windir}{st}
        {red}[=>]{st} {gren}{sysdir}{st}
        {red}[=>]{st} {gren}{logser}{st}
        {red}[=>]{st} {gren}{ram}{st}
    {red}======================{st}{gren}YHI547{st}{red}======================{st}        
    {red}time : {st}{gren}{m}{st}
    
    
    """
)




