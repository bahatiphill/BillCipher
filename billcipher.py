import socket
import os
import requests
import platform

def back():
    print()
    back = input('\033[92mDo you want to contunue? [Yes/No]: ')
    if back[0].upper() == 'Y':
        print()
        iseeverything()
    elif back[0].upper() == 'N':
        print('\033[92mRemember https://GitHackTools.blogspot.com')
        exit
    else:
        print('\033[92m?')
        exit

def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def bill():
    clear()
    print("""\033[93m ######                   #####                                
 #     # # #      #      #     # # #####  #    # ###### #####  
 #     # # #      #      #       # #    # #    # #      #    # 
 ######  # #      #      #       # #    # ###### #####  #    # 
 #     # # #      #      #       # #####  #    # #      #####  
 #     # # #      #      #     # # #      #    # #      #   #  
 ######  # ###### ######  #####  # #      #    # ###### #    # 2.0
 Information Gathering tool for a Website or IP address""")
    print()

def banner():
    print("""\033[96m
 1) DNS Lookup        11) Find Shared DNS Servers
 2) Whois Lookup      12) Get Robots.txt
 3) GeoIP Lookup      13) Host DNS Finder
 4) Subnet Lookup     14) Reserve IP Lookup
 5) Port Scanner      15) Email Gathering (use Infoga)
 6) Page Links        16) Subdomain listing (use Sublist3r)
 7) Zone Transfer     17) Find Admin login site (use Breacher)
 8) HTTP Header       18) Check and Bypass CloudFlare (use HatCloud)
 9) Host Finder       19) About BillCipher
 10) IP-Locator       20) Fuck Out Of Here (Exit)""")
    print()

def iseeverything():
    try:
        what = input('\033[92mAre you want to collect information of website or IP address? [website/IP]: ')
        if what[0].upper() == 'W':
            victim = input('Enter the website address: ')
            banner()
        elif what[0].upper() == 'I':
            victim = input('Enter the IP address (or domain to get IP address of this domain): ')
            victim = socket.gethostbyname(victim)
            print('The IP address of target is:',victim)
            banner()
        else:
            print('?')
            print()

        choose = input('What information would you like to collect? (1-20): ')

        if choose == '1':
            dnslook = 'https://api.hackertarget.com/dnslookup/?q='+victim
            info = requests.get(dnslook)
            print('\033[91m',info.text)
            back()

        elif choose == '2':
            whois = 'https://api.hackertarget.com/whois/?q='+victim
            info = requests.get(whois)
            print('\033[91m',info.text)
            back()

        elif choose == '3':
            ipgeo = 'https://api.hackertarget.com/geoip/?q='+victim
            info = requests.get(ipgeo)
            print('\033[91m',info.text)
            back()

        elif choose == '4':
            subnet = 'http://api.hackertarget.com/subnetcalc/?q='+victim
            info = requests.get(subnet)
            print('\033[91m',info.text)
            back()

        elif choose == '5':
            port = 'https://api.hackertarget.com/nmap/?q='+victim
            info = requests.get(port)
            print('\033[91m',info.text)
            back()

        elif choose == '6':
            pagelink = 'https://api.hackertarget.com/pagelinks/?q='+victim
            info = requests.get(pagelink)
            print('\033[91m',info.text)
            back()

        elif choose == '7':
            zone = 'https://api.hackertarget.com/zonetransfer/?q='+victim
            info = requests.get(zone)
            print('\033[91m',info.text)
            back()

        elif choose == '8':
            header = 'https://api.hackertarget.com/httpheaders/?q='+victim
            info = requests.get(header)
            print('\033[91m',info.text)
            back()

        elif choose == '9':
            host = 'https://api.hackertarget.com/hostsearch/?q='+victim
            info = requests.get(host)
            print('\033[91m',info.text)
            back()

        elif choose == '10':
            iplt = 'https://ipinfo.io/'+victim+'/json'
            info = requests.get(iplt)
            print('\033[91m',info.text)
            back()

        elif choose == '11':
            shared = 'https://api.hackertarget.com/findshareddns/?q='+victim
            info = requests.get(shared)
            print('\033[91m',info.text)
            back()

        elif choose == '12':
            robots ='http://'+victim+'/robots.txt'
            info = requests.get(robots)
            print('\033[91m',info.text)
            back()

        elif choose == '13':
            hostdns = 'https://api.hackertarget.com/mtr/?q='+victim
            info = requests.get(hostdns)
            print('\033[91m',info.text)
            back()

        elif choose == '14':
            reserve = 'https://api.hackertarget.com/reverseiplookup/?q='+victim
            info = requests.get(reserve)
            print('\033[91m',info.text)
            back()

        elif choose == '15':
            clear()
            os.system('python3 ./modules/Infoga/infoga.py --domain '+victim)
            back()

        elif choose == '16':
            clear()
            os.system('python3 ./modules/Sublist3r/sublist3r.py -d '+victim)
            back()

        elif choose == '17':
            clear()
            os.system('python ./modules/Breacher/breacher.py -u '+victim)
            back()

        elif choose == '18':
            clear()
            os.system('ruby ./modules/HatCloud/hatcloud.rb -b '+victim)
            back()

        elif choose == '19':
            print("""\033[93mBillCipher 2.0 - Information Gathering of a Website or IP address

AUTHOR: https://GitHackTools.blogspot.com
        https://twitter.com/SecureGF#
        https://fb.com/TVT618
        https://plus.google.com/+TVT618""")
            back()

        elif choose == '20':
            exit

        else:
            print('?')
            iseeverything()
            
    except socket.gaierror:
        print('Name or service not known!\033[93m')
        print()
        iseeverything()
    except UnboundLocalError:
        print('The information you entered is incorrect')
        print()
        iseeverything()
    except requests.exceptions.ConnectionError:
        print('Your Internet Offline')
        exit
    except IndexError:
        print('?')
        print()
        iseeverything()

bill()
iseeverything()