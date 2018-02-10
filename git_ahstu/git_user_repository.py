import requests
from bs4 import BeautifulSoup
url1 = 'https://git.ahstu.cc/explore/users?page='
m = 9
users_name = []
for x in range(1,m):
    res1 = requests.get(url1+str(x))
    soup1 = BeautifulSoup(res1.text,'html.parser')
    for i in soup1.select('.item'):
        if len(i.select('.header a')) > 0:
            users_name.append(i.select('.header a')[0].text)
#get all user            
         
url2 = 'https://git.ahstu.cc/'
n = 4
#假设仓库数最多的用户不超过三页仓库
repositorys = []
for y in users_name:
    user_rep = 1
    print(y)
    for z in range(1,n):
        res2 = requests.get(url2+y+'?page='+str(z))
        soup2 = BeautifulSoup(res2.text,'html.parser')
        for i in soup2.select('.item'):
            if len(i.select('.name')) > 0:
                print('**********'+str(user_rep)+": "+i.select('.name')[0].text)
                user_rep = user_rep+1;
                repositorys.append(i.select('.name')[0].text)
    print('\n')
len(repositorys)


'''
git
**********1: MarkdownEditor_Node
**********2: CleanCodeOfJS
**********3: AcmEditor
**********4: Vim
**********5: NginxConf
**********6: guidetodatamining
**********7: Python-DHT
**********8: helper
**********9: SchoolVR
**********10: MiniUpload
**********11: AutoScript
**********12: BaiduShare
**********13: OJAssistant
**********14: Judge_client


acm


Tortoise


cuining


zj
**********1: cprogrammingII
**********2: JavaWeb
**********3: eq
**********4: CoreJava
**********5: ACMProgramming
**********6: cprogramming
**********7: Golang
**********8: AlgorithmDesign
**********9: blogs
**********10: python
**********11: GATspSolver
**********12: zjTools
**********13: OJDataMakerTools
**********14: math
**********15: AndroidProgramming
**********16: chess
**********17: learn


jiajl
**********1: attendance
**********2: attendancr


1881130216
**********1: jsp2
**********2: jsp


dyf
**********1: hehe


1881130..7
**********1: jsp


wangside
**********1: exam1


1881130206
**********1: jsp


1881130227


1881130333
**********1: jsp2
**********2: jsp


1884130103
**********1: jsp


ahkjxy_git
**********1: zm


dingweiqing
**********1: C
**********2: JSP


1884130111
**********1: KJS
**********2: jsp


1884130113
**********1: sama
**********2: tomo


1884130104
**********1: rui


1884130127
**********1: zyq


1884130219
**********1: TJ


1884130118
**********1: jsp
**********2: html
**********3: iindex
**********4: index


1884130124
**********1: html
**********2: sgs
**********3: jsp


heke
**********1: yuuka
**********2: tano


1884130116
**********1: lny
**********2: dd
**********3: ndd
**********4: jsp


1884130107
**********1: hhy


1884130105
**********1: nicaicai


1884130209


Ikaros


1884130109


1884130106
**********1: fhj


1884130117
**********1: shh


1884130123
**********1: ez


1884130119


1884130125


1884130218


1884130202


1884130210
**********1: ls1884130210
**********2: lsve


1884130225


1884130224
**********1: jsp1


1884130120
**********1: java


1884130212


1881130116
**********1: ahstugit
**********2: Ahstu_Libray


1881140207


Joker


bill


zhijzan
**********1: ACMProgramming
**********2: usaco-training
**********3: UG-Tower


wfy


Fan
**********1: AcmQuestions
**********2: JudgeOnline
**********3: helper
**********4: AndroidProgramming
**********5: AlgorithmDesign


1881130208


aoj-wzl


cdy


HK


LI
**********1: JAVACode


dearvee
**********1: Crawler
**********2: Web
**********3: Course
**********4: Android


hj


wzy
**********1: wzy


1881140224


corki
**********1: Android-notes
**********2: Java-class


canglingyue
**********1: demo


zhang0ZGC


byqs


malone_ding


txl


pmathticol
**********1: ajstu_oj_code


hzy767596742


CJ2701150103


LDQ
**********1: everyday
**********2: startMove
**********3: 1-webBuilding


88888888


vyoung
**********1: oj
**********2: php
**********3: shell
**********4: mywebproject


hanqianqian


sf


Jy


SMILE-TO-YOU


2701160208


geh
**********1: C_Course


zjq
**********1: AKOJ


1881130221


ContestSolution


Neo


PengrongDai


wangjun


2304150240


dazhi


lgb
**********1: acm


chshru
**********1: acm


2604150210


ZTZ


2703150231


forging


dfy123


694995658


Jarvis
**********1: Webs
**********2: Web
**********3: Android


jal


17375365520


songchaochen


fire


liuyanyan


zly


winer


tang


chzu2016211786


wangqiqi


ac_loser


echo


JK


weixiaobi


1887140107


1887140232


1887140141


China_Good_Code
**********1: JSP_Course_zj
**********2: Java_OJ


1887140233


gaoru188


1881140216


zrqking


1881140213


cURL
**********1: AcmLab
**********2: lec
**********3: canvas
**********4: domains
**********5: calculator


IcewithaT


Beyound_zain
**********1: Oj
**********2: test
**********3: CLASS


1881140136


X


741741


nihuifeima


Wang


Windows


xh


1884140111


1884140139


1884140138


1884140117


1884140227


rzx1884140136


nickJacky


1884140222


duanyafei


1884140102


wang-feng


1881140235


ChenZJ


方博飞


1887140140


YuanLD


Jerry


1884140228


yishengchen


Belmode
**********1: AHSTU_OJ
**********2: WiFiViewer


bfmiaodi


lgs


1884140137


wildbird


dongjie
**********1: java
**********2: AOJ


LIDie
**********1: SharedPreferencesTest
**********2: Broadcast


1881140107


124


'''