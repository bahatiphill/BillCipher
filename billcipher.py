import socket
import os
import requests
import platform

def back():
    print()
    back = input('\033[92mDo you want to continue? [Yes/No]: ')
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
 ######  # ###### ######  #####  # #      #    # ###### #    # 2.1
 Information Gathering tool for a Website or IP address""")
    print()

def banner():
    print("""\033[96m
 1) DNS Lookup                 13) Host DNS Finder
 2) Whois Lookup               14) Reserve IP Lookup
 3) GeoIP Lookup               15) Email Gathering (use Infoga)
 4) Subnet Lookup              16) Subdomain listing (use Sublist3r)
 5) Port Scanner               17) Find Admin login site (use Breacher)
 6) Page Links                 18) Check and Bypass CloudFlare (use HatCloud)
 7) Zone Transfer              19) Website Copier (use httrack)
 8) HTTP Header                20) Host Info Scanner (use WhatWeb)
 9) Host Finder                21) About BillCipher
 10) IP-Locator                22) Fuck Out Of Here (Exit)
 11) Find Shared DNS Servers
 12) Get Robots.txt""")
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
            iseeverything()

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
            os.system('cd modules/Infoga && python3 infoga.py --domain '+victim)
            back()

        elif choose == '16':
            clear()
            os.system('cd modules/Sublist3r && python3 sublist3r.py -d '+victim)
            back()

        elif choose == '17':
            clear()
            os.system('cd modules/Breacher && python breacher.py -u '+victim)
            back()

        elif choose == '18':
            clear()
            os.system('ruby ./modules/HatCloud/hatcloud.rb -b '+victim)
            back()

        elif choose == '19':
            os.system('cd websource && mkdir '+victim)
            os.system('cd websource && cd '+victim+' && httrack '+victim)
            print("The website source code was saved in folder 'websource'")
            back()

        elif choose == '20':
            clear()
            os.system('whatweb -v '+victim)
            back()

        elif choose == '21':
            print("""\033[93mBillCipher 2.1 - Information Gathering of a Website or IP address

AUTHOR: https://GitHackTools.blogspot.com
        https://twitter.com/SecureGF#
        https://fb.com/TVT618
        https://plus.google.com/+TVT618""")
            back()

        elif choose == '22':
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
