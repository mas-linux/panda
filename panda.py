#!/usr/bin/python

import os
import sys, traceback

def main():
	try:
		print '''
=======================================================================
============Welcome to add tools kali linux for ubuntu=================
==========================created by Panda=============================
================== blog : http://mas-linux.blogspot.com ===============
=============== Email me : Hidayatullah.afif@yahoo.co.id ==============
=======================================================================
                               Vbeta \033[1;m
 \033[1;32m+ -- -- +=[ Author: Panda | Blog: mas-linux.blogspot.com+ -- -- +=\033[1;m
 \033[1;32m+ -- -- +=[ kali linux tools Tools + -- -- +=\033[1;m
			'''
		def inicio1():
			while True:
				print '''
1. Add Key and repo KaliLInux
2. automatis install all tools
3. Install menu kali-linux
4. Help and Note(BACA DULU)
			'''

				opcion0 = raw_input("\033[1;36mPanda |-$ \033[1;m")
			
				while opcion0 == "1":
					print '''
1. Add kali linux repositories
2. Update
3. Open Synaptic package manager for Manual install tools
4. Remove kali linux repositories
5. View the contents of sources.list file
					'''
					repo = raw_input("\033[1;32mSilahkan pilih salah satu+++>|-$ \033[1;m")
					if repo == "1":
						cmd1 = os.system("wget -q -O - http://mas-linux.comze.com/kali.pgp | sudo apt-key add -")
						cmd2 = os.system("echo '# Kali linux repositories | Added by Panda\ndeb http://ppa.launchpad.net/wagungs/kali-linux2/ubuntu raring main\ndeb-src http://ppa.launchpad.net/wagungs/kali-linux2/ubuntu raring main\ndeb http://ppa.launchpad.net/wagungs/kali-linux/ubuntu raring main\ndeb-src http://ppa.launchpad.net/wagungs/kali-linux/ubuntu raring main\ndeb http://ppa.launchpad.net/wagungs/kali-linux1/ubuntu raring main\ndeb-src http://ppa.launchpad.net/wagungs/kali-linux1/ubuntu raring main\n' >> /etc/apt/sources.list")
					elif repo == "2":
						cmd3 = os.system("apt-get update -m")
					elif repo == "3":
						cmd3 = os.system("sudo apt-get install synaptic")
						cmd4 = os.system("synaptic")
					elif repo == "4":
						infile = "/etc/apt/sources.list"
						outfile = "/etc/apt/sources.list"

						delete_list = ["# Kali linux repositories | Added by Panda\n", "deb http://ppa.launchpad.net/wagungs/kali-linux2/ubuntu raring main","deb-src http://ppa.launchpad.net/wagungs/kali-linux2/ubuntu raring main","deb http://ppa.launchpad.net/wagungs/kali-linux/ubuntu raring main","deb-src http://ppa.launchpad.net/wagungs/kali-linux/ubuntu raring main","deb http://ppa.launchpad.net/wagungs/kali-linux1/ubuntu raring main","deb-src http://ppa.launchpad.net/wagungs/kali-linux1/ubuntu raring main"]
						fin = open(infile)
						os.remove("/etc/apt/sources.list")
						fout = open(outfile, "w+")
						for line in fin:
						    for word in delete_list:
						        line = line.replace(word, "")
						    fout.write(line)
						fin.close()
						fout.close()
						print " "
						print "\033[1;31mAll kali linux repositories have been deleted !\033[1;m"
						print " "
					elif repo == "back":
						inicio1()
					elif repo == "gohome":
						inicio1()
					elif repo == "5":
						file = open('/etc/apt/sources.list', 'r')

						print file.read()

					else:
						print ("\033[1;31mSorry, perintah seng koe masukan salah cok!!\033[1;m")  					
						
						
				if opcion0 == "3":
					repo = raw_input("\033[1;32mDo you want to install Kali menu and indicator ? [y/n]> \033[1;m")
					if repo == "y":
						cmd1 = os.system("add-apt-repository ppa:diesch/testing && apt-get update")
						cmd2 = os.system("sudo apt-get install classicmenu-indicator")
						cmd3 = os.system("apt-get install kali-menu")
				elif opcion0 == "4":
					print ''' 
****************** +Commands+ ****************** 
\033[1;32mpilih angka yang disediakan\033[1;m 	
\033[1;32mketik back jika ingin kembali\033[1;m 	
\033[1;32mketik gohome kalau mau kembali ke menu awal \033[1;m 	
\033[1;32mketik grab back kalo mau salah\033[1;m 	
\033[1;32mnjir mau aja u baca ini\033[1;m	
****************** +Note+ ****************** 
\033[1;32mJika anda menginstall tools dengan otomatis\033[1;m 	
\033[1;32mdan mengalami masalah setelahnya maka admin tidak bertanggung jawab\033[1;m 	
\033[1;32mJadi disarankan coba lah dengan manual yang tersedia di pilihan 1 \033[1;m 	
\033[1;32mkarena yang manual itu lebih murni jika ada kesalahan bisa di cegah\033[1;m 	
\033[1;32mSederhana itu indah bro Njir..!!!\033[1;m	
		'''


				def inicio():
					while opcion0 == "2":
						print '''
\033[1;36mAll Tools\033[1;m	
				
\033[1;32mInformation Gathering\033[1;m			
\033[1;32mVulnerability Analysis\033[1;m			
\033[1;32mWireless Attacks\033[1;m				
\033[1;32mWeb Applications\033[1;m				
\033[1;32mSniffing & Spoofing\033[1;m				
\033[1;32mMaintaining Access\033[1;m				
\033[1;32mReporting Tools\033[1;m 				
\033[1;32mExploitation Tools\033[1;m
\033[1;32mForensics Tools\033[1;m
\033[1;32mStress Testing\033[1;m		
\033[1;32mStress Testing\033[1;m			
\033[1;32mPassword Attacks\033[1;m
\033[1;32mReverse Engineering\033[1;m
\033[1;32mHardware Hacking\033[1;m
				
1) Install All Tools
			 '''
						print "\033[1;32mPilih Nomer 1 Jika anda yakin untuk menginstall seluruh tools.\033[1;m"

						print " "
						opcion1 = raw_input("\033[1;36mPanda |-$  \033[1;m")
						if opcion1 == "back":
							inicio1()
						elif opcion1 == "gohome":
							inicio1()
						elif opcion1 == "1":
							cmd1 = os.system("apt-get install acccheck ace-voip amap automater braa casefile cdpsnarf cisco-torch cookie-cadger copy-router-config dmitry dnmap dnsenum dnsmap dnsrecon dnstracer dnswalk dotdotpwn enum4linux enumiax exploitdb fierce firewalk fragroute fragrouter ghost-phisher golismero goofile lbd maltego-teeth masscan metagoofil miranda nmap ntop p0f parsero recon-ng set smtp-user-enum snmpcheck sslcaudit sslsplit sslstrip sslyze thc-ipv6 theharvester tlssled twofi urlcrazy wireshark wol-e xplico ismtp intrace hping3 bbqsql bed cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch copy-router-config doona dotdotpwn greenbone-security-assistant hexorbase inguma jsql lynis nmap ohrwurm openvas-cli openvas-manager openvas-scanner oscanner powerfuzzer sfuzz sidguesser siparmyknife sqlmap sqlninja sqlsus thc-ipv6 tnscmd10g unix-privesc-check yersinia aircrack-ng asleap bluelog blueranger bluesnarfer bully cowpatty crackle eapmd5pass fern-wifi-cracker ghost-phisher giskismet gqrx kalibrate-rtl killerbee kismet mdk3 mfcuk mfoc mfterm multimon-ng pixiewps reaver redfang spooftooph wifi-honey wifitap wifite apache-users arachni bbqsql blindelephant burpsuite cutycapt davtest deblaze dirb dirbuster fimap funkload grabber jboss-autopwn joomscan jsql maltego-teeth padbuster paros parsero plecost powerfuzzer proxystrike recon-ng skipfish sqlmap sqlninja sqlsus ua-tester uniscan vega w3af webscarab webshag websploit wfuzz wpscan xsser zaproxy burpsuite dnschef fiked hamster-sidejack hexinject iaxflood inviteflood ismtp mitmproxy ohrwurm protos-sip rebind responder rtpbreak rtpinsertsound rtpmixsound sctpscan siparmyknife sipp sipvicious sniffjoke sslsplit sslstrip thc-ipv6 voiphopper webscarab wifi-honey wireshark xspy yersinia zaproxy cryptcat cymothoa dbd dns2tcp http-tunnel httptunnel intersect nishang polenum powersploit pwnat ridenum sbd u3-pwn webshells weevely winexe casefile cutycapt dos2unix dradis keepnote magictree metagoofil nipper-ng pipal armitage backdoor-factory cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch crackle jboss-autopwn linux-exploit-suggester maltego-teeth set shellnoob sqlmap thc-ipv6 yersinia beef-xss binwalk bulk-extractor chntpw cuckoo dc3dd ddrescue dff dumpzilla extundelete foremost galleta guymager iphone-backup-analyzer p0f pdf-parser pdfid pdgmail peepdf regripper volatility xplico dhcpig funkload iaxflood inviteflood ipv6-toolkit mdk3 reaver rtpflood slowhttptest t50 termineter thc-ipv6 thc-ssl-dos acccheck burpsuite cewl chntpw cisco-auditing-tool cmospwd creddump crunch findmyhash gpp-decrypt hash-identifier hexorbase john johnny keimpx maltego-teeth maskprocessor multiforcer ncrack oclgausscrack pack patator polenum rainbowcrack rcracki-mt rsmangler sqldict statsprocessor thc-pptp-bruter truecrack webscarab wordlists zaproxy apktool dex2jar python-distorm3 edb-debugger jad javasnoop jd ollydbg smali valgrind yara android-sdk apktool arduino dex2jar sakis3g smali&& wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")	
							cmd2 = os.system("git clone https://github.com/LionSec/wifresti.git && cp wifresti/wifresti.py /usr/bin/wifresti && chmod +x /usr/bin/wifresti && wifresti")
							cmd3 = os.system("apt-get install squid3")
							print " "
						elif opcion2 == "back":
								inicio()
						elif opcion2 == "gohome":
								inicio1()
						
				inicio()
		inicio1() 

	except KeyboardInterrupt:
		print "Cencel"
	except Exception:
		traceback.print_exc(file=sys.stdout)
	sys.exit(0)

if __name__ == "__main__":
    main()					
						
