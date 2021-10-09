from bs4 import BeautifulSoup
import requests
import sys
import os

os.system("apt install figlet")
os.system("apt install nmap")
os.system("clear")
os.system("figlet Ip Sorgu")

print("""
**************************
*			 *
*        ST4XOF          *
*       İP SORGU         *
*			 *
**************************

İp Sorgu Toolu toolu

1- İp Sorgula)		2- Nmap Sorgusu)

""")
sec = input("Seçim Yapınız ==> ")
if sec == "1":
	ipaddr = input("İp Giriniz ==> ")
try:
		req = requests.get("http://www.ipsorgu.com/?ip=" + str(ipaddr) + "#sorgu")
		soup = BeautifulSoup(req.text, 'html.parser')
		googlemaps = soup.find("iframe")
		googlemaps = str(googlemaps).split("src=")
		googlemaps = str(googlemaps[1]).split("&")
		googlemaps = str(googlemaps[0]).replace('"', "")
		googlemaps = str(googlemaps).split("=")
		info = soup.find_all("em")
		info1 = str(info).replace('<em style="color:#666">', '')
		info1 = str(info1).replace('</em>', '')
		info1 = info1.split(", ")
		print("Lokasyon : " + str(googlemaps[1]))
		print("Ülke : " + str(info1[0]).replace("[", ""))
		print("Bölge : " + str(info1[1]))
		print("Host : " + str(info1[3]))
except:
	pass
if sec == "2":
	ip = input("İp Giriniz ==> ")
	os.system("nmap -F "+ip)
