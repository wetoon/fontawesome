#!/usr/bin/python3
import requests as G,re,os as A,sys,argparse as P
from bs4 import BeautifulSoup as Q
def R(text):A=re.compile('url\\((.*?)\\)');B=re.findall(A,text);return list(dict.fromkeys(B))
def C(url,format=False):return Q(G.get(url).content,'html.parser')if format else G.get(url).content
H=P.ArgumentParser(description='A script to download and organize FontAwesome assets.')
H.add_argument('--version',type=str,help='Specify the FontAwesome version to use (e.g., 6.4.1). If not provided, the latest version is fetched automatically.')
I=H.parse_args()
if I.version:B='v{0}'.format(I.version)
else:B=re.search('(v\\d+\\.\\d+\\.\\d+)',[A['href']if re.search('/v(\\d+\\.\\d+\\.\\d+)/',A['href'])else None for A in C('https://fontawesome.com/changelog',True).findAll('link',attrs={'rel':'stylesheet'})][2]).group(1)
S=[f"https://ka-f.fontawesome.com/releases/{B}/css/pro.min.css",f"https://ka-f.fontawesome.com/releases/{B}/css/pro-v4-shims.min.css",f"https://ka-f.fontawesome.com/releases/{B}/css/pro-v5-font-face.min.css",f"https://ka-f.fontawesome.com/releases/{B}/css/pro-v4-font-face.min.css"]
T=A.path.dirname(sys.executable)if getattr(sys,'frozen',False)else A.path.dirname(A.path.abspath(__file__))
for J in S:
	K=str(C(J,True));U=[A.replace('../',f"https://ka-f.fontawesome.com/releases/{B}/")for A in R(K)];L=A.path.join(T,'fontawesome',B);D=A.path.join(L,'css')
	if not A.path.exists(D):A.makedirs(D)
	with open(f"{D}/{J.split('/')[-1]}",'w')as E:E.write(K.replace('../webfonts/',f"/fontawesome/{B}/webfonts/"))
	for M in U:
		F=A.path.join(L,'webfonts');V=C(M)
		if not A.path.exists(F):A.makedirs(F)
		with open(f"{F}/{M.split('/')[-1]}",'wb')as E:E.write(V)