import requests ,os #line:1
import threading ,csv ,time #line:2
from glob import glob #line:3
import shutil ,zipfile #line:4
from random import choice #line:5
import random #line:6
from flask import Flask ,render_template ,request ,redirect ,url_for ,jsonify ,send_file #line:7
from apscheduler .schedulers .background import BackgroundScheduler #line:8
from itertools import zip_longest #line:9
stop_sending =False #line:10
background_task_started =True #line:11
def create_allfiles_folder ():#line:13
    O0O0O00OOOOO0O0O0 ='allfiles'#line:14
    os .makedirs ("uploaded",exist_ok =True )#line:15
    if not os .path .exists (O0O0O00OOOOO0O0O0 ):#line:17
        os .makedirs (O0O0O00OOOOO0O0O0 )#line:18
        time .sleep (2 )#line:19
        os .makedirs (O0O0O00OOOOO0O0O0 +"//apifile")#line:20
        print (f"'{O0O0O00OOOOO0O0O0}' folder has been created.")#line:21
    else :#line:22
        print (f"'{O0O0O00OOOOO0O0O0}' folder already exists.")#line:23
def generate_custom_uuid ():#line:25
    O0OOO00000000OO0O ="INV"#line:27
    O00000OOO000O0OO0 =random .randint (100000 ,999999 )#line:30
    O0OOO000OOO0OOOO0 =random .randint (1000 ,9999 )#line:31
    O000OO0OOO000000O =f"{O0OOO00000000OO0O}-{O00000OOO000O0OO0}-{O0OOO000OOO0OOOO0}"#line:33
    return O000OO0OOO000000O #line:35
def new ():#line:36
    try :#line:37
        OO0OOOOOO0OO00OOO =str (os .getcwd ())+'/allfiles'#line:38
        OO000000O0O0OO0O0 =3000 #line:40
        OO0OO0OOOOOO00000 =50 #line:41
        O0000O00O00000OO0 =os .path .join (OO0OOOOOO0OO00OOO ,'checkemail.csv')#line:44
        if not os .path .exists (O0000O00O00000OO0 ):#line:45
            print (f"Error: {O0000O00O00000OO0} does not exist.")#line:46
            return #line:47
        with open (O0000O00O00000OO0 ,'r')as OO0OO0OO0000O0O0O :#line:49
            O0OO0O00OOO0OO0OO =[O00000O0O00OO00OO .strip ()for O00000O0O00OO00OO in OO0OO0OO0000O0O0O .readlines ()if "@"in O00000O0O00OO00OO ]#line:50
        OO00OOOOO0000OOO0 =0 #line:52
        for O000O00O0OOO0000O in os .listdir (OO0OOOOOO0OO00OOO ):#line:55
            O0000O0OO0000O00O =os .path .join (OO0OOOOOO0OO00OOO ,O000O00O0OOO0000O )#line:56
            if os .path .isdir (O0000O0OO0000O00O ):#line:57
                for OOOOO00OOOO00O000 in os .listdir (O0000O0OO0000O00O ):#line:59
                    OOO0OO0OO0OO0OO0O =os .path .join (O0000O0OO0000O00O ,OOOOO00OOOO00O000 )#line:60
                    if OOOOO00OOOO00O000 .startswith ("contact")and OOOOO00OOOO00O000 .endswith ((".txt",".csv")):#line:62
                        with open (OOO0OO0OO0OO0OO0O ,'r')as OO0O00O00O0OOOOOO :#line:64
                            OOO0OOO0O0OO00O0O =csv .reader (OO0O00O00O0OOOOOO )#line:65
                            OOOO0000OO00OO00O =next (OOO0OOO0O0OO00O0O )#line:66
                            OO0O0O000OO0O0000 =list (OOO0OOO0O0OO00O0O )#line:69
                            OO00OO0OO0OO00000 =len (OO0O0O000OO0O0000 )//OO000000O0O0OO0O0 +(1 if len (OO0O0O000OO0O0000 )%OO000000O0O0OO0O0 >0 else 0 )#line:70
                            for O0O0OOOO00000O0OO in range (OO00OO0OO0OO00000 ):#line:72
                                OOOOOO00OO000OOO0 =OO0O0O000OO0O0000 [O0O0OOOO00000O0OO *OO000000O0O0OO0O0 :(O0O0OOOO00000O0OO +1 )*OO000000O0O0OO0O0 ]#line:73
                                O0O0OO00O0OOOOO00 =os .path .join (O0000O0OO0000O00O ,f'lead_{O0O0OOOO00000O0OO + 1}.csv')#line:74
                                with open (O0O0OO00O0OOOOO00 ,'w',newline ='')as O0OOOO0OO0OO00OO0 :#line:76
                                    OO00OO00000O0O000 =csv .writer (O0OOOO0OO0OO00OO0 )#line:77
                                    OO00OO00000O0O000 .writerow (['name','email'])#line:78
                                    for OO0O0O0OOOO0O00OO ,O000O0O00O0O00OO0 in enumerate (OOOOOO00OO000OOO0 ):#line:81
                                        OOOOO000OO0OOOOO0 =generate_custom_uuid ()#line:82
                                        OOOOO000OO0OOOOO0 =str (OOOOO000OO0OOOOO0 )#line:83
                                        if OO0O0O0OOOO0O00OO ==0 and OO00OOOOO0000OOO0 <len (O0OO0O00OOO0OO0OO ):#line:85
                                            OO00OO00000O0O000 .writerow ([OOOOO000OO0OOOOO0 ,O0OO0O00OOO0OO0OO [OO00OOOOO0000OOO0 ]])#line:86
                                            OO00OOOOO0000OOO0 =(OO00OOOOO0000OOO0 +1 )%len (O0OO0O00OOO0OO0OO )#line:87
                                        OO00OO00000O0O000 .writerow (O000O0O00O0O00OO0 )#line:88
                                        if (OO0O0O0OOOO0O00OO +1 )%OO0OO0OOOOOO00000 ==0 and OO00OOOOO0000OOO0 <len (O0OO0O00OOO0OO0OO ):#line:91
                                            OO00OO00000O0O000 .writerow ([OOOOO000OO0OOOOO0 ,O0OO0O00OOO0OO0OO [OO00OOOOO0000OOO0 ]])#line:92
                                            OO00OOOOO0000OOO0 =(OO00OOOOO0000OOO0 +1 )%len (O0OO0O00OOO0OO0OO )#line:93
                        try :#line:95
                            os .remove (OOO0OO0OO0OO0OO0O )#line:96
                        except Exception as OO0O000OO00O0O0O0 :#line:97
                            print (OO0O000OO00O0O0O0 )#line:98
                    elif OOOOO00OOOO00O000 .startswith ("gmail")and OOOOO00OOOO00O000 .endswith ((".txt",".csv")):#line:100
                        with open (OOO0OO0OO0OO0OO0O ,'r')as OO0O00O00O0OOOOOO :#line:102
                            OO0O0O000OO0O0000 =OO0O00O00O0OOOOOO .readlines ()#line:103
                            for O0O0OOOO00000O0OO ,O000O0O00O0O00OO0 in enumerate (OO0O0O000OO0O0000 ):#line:104
                                if "@"not in str (O000O0O00O0O00OO0 ):#line:105
                                    continue #line:106
                                O000OOOOOO0OO0OOO ,O0OO0OO000O0O0OOO =O000O0O00O0O00OO0 .strip ().split (',')#line:107
                                O0O0OO00O0OOOOO00 =os .path .join (O0000O0OO0000O00O ,f'cred{O0O0OOOO00000O0OO + 1}.csv')#line:108
                                with open (O0O0OO00O0OOOOO00 ,'w',newline ='')as O0OOOO0OO0OO00OO0 :#line:109
                                    OO00OO00000O0O000 =csv .writer (O0OOOO0OO0OO00OO0 )#line:110
                                    OO00OO00000O0O000 .writerow (['email','password'])#line:111
                                    OO00OO00000O0O000 .writerow ([O000OOOOOO0OO0OOO ,O0OO0OO000O0O0OOO ])#line:112
                        try :#line:113
                            os .remove (OOO0OO0OO0OO0OO0O )#line:114
                        except :#line:115
                            pass #line:116
        try :#line:118
            OO0OO0OO0000O0O0O .close ()#line:119
            os .remove (O0000O00O00000OO0 )#line:120
        except :#line:121
            pass #line:122
    except Exception as O000O00OOO0O00OOO :#line:124
        print (O000O00OOO0O00OOO )#line:125
def fileuploads (O0OOO0O00OO00OO0O ,contacts_file =None ,subjects_file =None ,gmail_file =None ,html_file =None ):#line:126
    if len (O0OOO0O00OO00OO0O )<2 :#line:127
        print ("no server found")#line:128
    else :#line:129
        try :#line:131
            OOOOO000000000O00 ={'csrftoken':'adfafafasasfasfassdsd',}#line:135
            O00O0OO0O00OOOOO0 ={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Language':'en-US,en;q=0.9,bn;q=0.8,fr;q=0.7','Cache-Control':'max-age=0','Connection':'keep-alive','DNT':'1','Origin':f'http://{O0OOO0O00OO00OO0O}:8000','Referer':f'http://{O0OOO0O00OO00OO0O}:8000/upload-files/?','Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Fetch-Site':'same-origin','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36','sec-ch-ua':'"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"','sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Windows"',}#line:154
            OO0000OOO00OO0OO0 ={}#line:157
            O000O0OO0O0OO00O0 =[]#line:158
            try :#line:159
                if contacts_file :#line:161
                    O0OO0000O0000O00O =open (contacts_file ,'rb')#line:162
                    OO0000OOO00OO0OO0 ['contacts_file']=('contacts.csv',O0OO0000O0000O00O ,'text/csv')#line:163
                    O000O0OO0O0OO00O0 .append (O0OO0000O0000O00O )#line:164
                if subjects_file :#line:167
                    O0OO00OOO00O0OO00 =open (subjects_file ,'rb')#line:168
                    OO0000OOO00OO0OO0 ['subjects_file']=('subjects.csv',O0OO00OOO00O0OO00 ,'text/csv')#line:169
                    O000O0OO0O0OO00O0 .append (O0OO00OOO00O0OO00 )#line:170
                if gmail_file :#line:173
                    OO00O00OOOO00O0O0 =open (gmail_file ,'rb')#line:174
                    OO0000OOO00OO0OO0 ['gmail_file']=('gmail.csv',OO00O00OOOO00O0O0 ,'text/csv')#line:175
                    O000O0OO0O0OO00O0 .append (OO00O00OOOO00O0O0 )#line:176
                if html_file :#line:179
                    OO0000OO000OOOO00 =open (html_file ,'rb')#line:180
                    OO0000OOO00OO0OO0 ['html_file']=('html_code.html',OO0000OO000OOOO00 ,'text/html')#line:181
                    O000O0OO0O0OO00O0 .append (OO0000OO000OOOO00 )#line:182
                if not OO0000OOO00OO0OO0 :#line:185
                    print ("No files to upload.")#line:186
                with requests .Session ()as O0000O0OOOO0O0OOO :#line:189
                    O0000O0OOOO0O0OOO .headers .update (O00O0OO0O00OOOOO0 )#line:190
                    O0O00OOO0O0OOO00O =O0000O0OOOO0O0OOO .post (f'http://{O0OOO0O00OO00OO0O}:8000/upload-files/',files =OO0000OOO00OO0OO0 )#line:191
                    if O0O00OOO0O0OOO00O .status_code ==200 :#line:194
                        for OOOOOO0OO00000O00 in O000O0OO0O0OO00O0 :#line:196
                            OOOOOO0OO00000O00 .close ()#line:197
                        if contacts_file and os .path .exists (contacts_file ):#line:200
                            OO0O000O00O0O00OO =os .path .join ("uploaded",'contact')#line:201
                            os .makedirs (OO0O000O00O0O00OO ,exist_ok =True )#line:202
                            shutil .move (contacts_file ,os .path .join (OO0O000O00O0O00OO ,os .path .basename (contacts_file )))#line:203
                        if subjects_file and os .path .exists (subjects_file ):#line:205
                            OO0O000O00O0O00OO =os .path .join ("uploaded",'subject')#line:206
                            os .makedirs (OO0O000O00O0O00OO ,exist_ok =True )#line:207
                            shutil .move (subjects_file ,os .path .join (OO0O000O00O0O00OO ,os .path .basename (subjects_file )))#line:208
                        if gmail_file and os .path .exists (gmail_file ):#line:210
                            OO0O000O00O0O00OO =os .path .join ("uploaded",'gmail')#line:211
                            os .makedirs (OO0O000O00O0O00OO ,exist_ok =True )#line:212
                            shutil .move (gmail_file ,os .path .join (OO0O000O00O0O00OO ,os .path .basename (gmail_file )))#line:213
                        if html_file and os .path .exists (html_file ):#line:215
                            OO0O000O00O0O00OO =os .path .join ("uploaded",'html')#line:216
                            os .makedirs (OO0O000O00O0O00OO ,exist_ok =True )#line:217
                            shutil .move (html_file ,os .path .join (OO0O000O00O0O00OO ,os .path .basename (html_file )))#line:218
                        print (O0O00OOO0O0OOO00O .status_code ,OO0000OOO00OO0OO0 )#line:220
            except Exception as OO00O0O00OOOO00OO :#line:222
                print (f"Upload failed for server {O0OOO0O00OO00OO0O}: {str(OO00O0O00OOOO00OO)}")#line:223
                if 'response'in locals ():#line:225
                    print (f"Status code: {O0O00OOO0O0OOO00O.status_code}")#line:226
        except Exception as OO0O0000OO0O00O0O :#line:228
            print (f"Error in file upload to server {O0OOO0O00OO00OO0O}: {str(OO0O0000OO0O00O0O)}")#line:229
def runcheck (OOO0OO0OO0000O000 ):#line:233
    O000OO00OO000O000 ={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Language':'en-US,en;q=0.9,bn;q=0.8,fr;q=0.7','Cache-Control':'max-age=0','Connection':'keep-alive','DNT':'1','Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Fetch-Site':'same-origin','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36','sec-ch-ua':'"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"','sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Windows"',}#line:250
    O0OOO00O0O00OOO0O =requests .post (f'http://{OOO0OO0OO0000O000}:8000/stopserver',headers =O000OO00OO000O000 )#line:251
    OOOO00OOO0OO0O0O0 =O0OOO00O0O00OOO0O .text #line:252
def mailsendingmain (OOO0OOOO0OO00O0O0 ):#line:254
    OO00O0OO0O0OOO0O0 ={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Language':'en-US,en;q=0.9,bn;q=0.8,fr;q=0.7','Cache-Control':'max-age=0','Connection':'keep-alive','DNT':'1','Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Fetch-Site':'same-origin','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36','sec-ch-ua':'"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"','sec-ch-ua-mobile':'?0','sec-ch-ua-platform':'"Windows"',}#line:271
    OO0OOO000OOO0O00O =requests .post (f'http://{OOO0OOOO0OO00O0O0}:8000/startsending',headers =OO00O0OO0O0OOO0O0 )#line:272
    O0O000O0OO0OOOOO0 =OO0OOO000OOO0O00O .text #line:273
def run_threads_for_csv (O00O0OOO0O0O0000O ,OOO00OOO00OOO00O0 ):#line:276
    OO000O0OO00OO00O0 =[]#line:277
    OOO0O00O00O0000OO =[]#line:278
    def O00O0O00O000O000O (O0OOO00OO0OO0O000 ,OO000OOO0OO000O00 ,OO00OOO0O0000OO00 ,OOOOO0000O00OOO00 ,OO000O000O000O0O0 ):#line:281
        OOOO0OO00OOOO00OO =fileuploads (O0OOO00OO0OO0O000 ,OO00OOO0O0000OO00 ,OOOOO0000O00OOO00 ,OO000OOO0OO000O00 ,OO000O000O000O0O0 )#line:282
        OOO0O00O00O0000OO .append (OOOO0OO00OOOO00OO )#line:283
    with open (O00O0OOO0O0O0000O ,newline ='')as O0OO000O0OOO00O00 :#line:286
        O00OO0OOO0000OOO0 =csv .reader (O0OO000O0OOO00O00 )#line:287
        for O000O000O0O00OOOO ,O00000O0OO00OOO0O in enumerate (O00OO0OOO0000OOO0 ):#line:288
            O00OO0O0OO0O0O00O =O00000O0OO00OOO0O [0 ]#line:289
            O0OOOO0O0O0O0OO0O =OOO00OOO00OOO00O0 ['gmail_files'][O000O000O0O00OOOO %len (OOO00OOO00OOO00O0 ['gmail_files'])]#line:292
            O000O0OOO00OO000O =OOO00OOO00OOO00O0 ['contacts_files'][O000O000O0O00OOOO %len (OOO00OOO00OOO00O0 ['contacts_files'])]#line:293
            O00OO00000O0O0O0O =OOO00OOO00OOO00O0 ['subjects_files'][O000O000O0O00OOOO %len (OOO00OOO00OOO00O0 ['subjects_files'])]#line:294
            O0000OOOOOOO00OO0 =OOO00OOO00OOO00O0 ['html_files'][O000O000O0O00OOOO %len (OOO00OOO00OOO00O0 ['html_files'])]#line:295
            O0000OOO00O0O00OO =threading .Thread (target =O00O0O00O000O000O ,args =(O00OO0O0OO0O0O00O ,O0OOOO0O0O0O0OO0O ,O000O0OOO00OO000O ,O00OO00000O0O0O0O ,O0000OOOOOOO00OO0 ))#line:298
            OO000O0OO00OO00O0 .append (O0000OOO00O0O00OO )#line:299
            O0000OOO00O0O00OO .start ()#line:300
    for O0000OOO00O0O00OO in OO000O0OO00OO00O0 :#line:303
        O0000OOO00O0O00OO .join ()#line:304
    return OOO0O00O00O0000OO #line:306
def run_threads_stop_server ():#line:308
    OO000OOO0OO00OO00 =[]#line:309
    O0OO0OO0O00OO0OOO =[]#line:310
    def OOO00OO00OO00O000 (O0O0O00OOOO000000 ):#line:311
        O0OOO0OOOO0O0O0OO =runcheck (O0O0O00OOOO000000 ,)#line:312
        O0OO0OO0O00OO0OOO .append (O0OOO0OOOO0O0O0OO )#line:313
    with open ("server.txt",newline ='')as O0OO000O0OOOO0OOO :#line:314
        O00O0OO000OOO0OOO =csv .reader (O0OO000O0OOOO0OOO )#line:315
        for O0OO0000OO0O0OO0O in O00O0OO000OOO0OOO :#line:316
            O0000OO0O00OOO000 =O0OO0000OO0O0OO0O [0 ]#line:317
            OO0OO0O000OO0O0OO =threading .Thread (target =OOO00OO00OO00O000 ,args =(O0000OO0O00OOO000 ,))#line:319
            OO000OOO0OO00OO00 .append (OO0OO0O000OO0O0OO )#line:320
            OO0OO0O000OO0O0OO .start ()#line:321
    for OO0OO0O000OO0O0OO in OO000OOO0OO00OO00 :#line:322
        OO0OO0O000OO0O0OO .join ()#line:323
    return f"Stopted all server"#line:325
def run_threads_sendingall_server ():#line:327
    OO00O00OO0OO000OO =[]#line:328
    O00O0OOO0O000O000 =[]#line:329
    def O00000OOOO00O000O (OOOO00O000OOOO0O0 ):#line:330
        OO0000O000O00000O =mailsendingmain (OOOO00O000OOOO0O0 ,)#line:331
        O00O0OOO0O000O000 .append (OO0000O000O00000O )#line:332
    with open ("server.txt",newline ='')as O0O00O0OO0O0000O0 :#line:333
        OO0O00000O0O0OOO0 =csv .reader (O0O00O0OO0O0000O0 )#line:334
        for O00O0OOOOO000OO00 in OO0O00000O0O0OOO0 :#line:335
            OO0O0O0O0O0O00000 =O00O0OOOOO000OO00 [0 ]#line:336
            O00OO0000000OOOO0 =threading .Thread (target =O00000OOOO00O000O ,args =(OO0O0O0O0O0O00000 ,))#line:338
            OO00O00OO0OO000OO .append (O00OO0000000OOOO0 )#line:339
            O00OO0000000OOOO0 .start ()#line:340
    for O00OO0000000OOOO0 in OO00O00OO0OO000OO :#line:341
        O00OO0000000OOOO0 .join ()#line:342
    return f"Stopted all server"#line:344
def send_thread (O0OO00OOOOO0O0OO0 ,O0O00000000O000O0 ):#line:345
    OOO000OO0O0OOO0O0 =[]#line:346
    O000O00OO0OO0O00O =[]#line:347
    def OOO0OOO0000O0O000 (O0O0O0OOOO00OOO00 ,O0OOOOOO0OOO00OO0 ,O00O00OOO0000O0O0 ):#line:348
        O0O0O00OO0000OO0O =send_email (O0O0O0OOOO00OOO00 ,O0OOOOOO0OOO00OO0 ,O00O00OOO0000O0O0 )#line:349
        O000O00OO0OO0O00O .append (O0O0O00OO0000OO0O )#line:350
    with open ("server.txt",newline ='')as O0O00O0000OOO0OO0 :#line:351
        O000O0OO0OO0OOO00 =csv .reader (O0O00O0000OOO0OO0 )#line:352
        for OO0OOO0OO000O00OO in O000O0OO0OO0OOO00 :#line:353
            OOO00OO0O000O000O =OO0OOO0OO000O00OO [0 ]#line:354
            time .sleep (0.2 )#line:355
            O000OO0O000OO00O0 =threading .Thread (target =OOO0OOO0000O0O000 ,args =(OOO00OO0O000O000O ,O0OO00OOOOO0O0OO0 ,O0O00000000O000O0 ))#line:356
            OOO000OO0O0OOO0O0 .append (O000OO0O000OO00O0 )#line:357
            O000OO0O000OO00O0 .start ()#line:358
    for O000OO0O000OO00O0 in OOO000OO0O0OOO0O0 :#line:360
        O000OO0O000OO00O0 .join ()#line:361
    return "processing"#line:363
def send_email (O0O0000OO000O00O0 ,OO0000O000O00OO0O ,O0OO000O00O00OOOO ):#line:364
        O0OOO000OOOOOO000 ='adfafafasasfasfassdsd'#line:366
        O00OO0OO0OOO0O0O0 ={'csrfmiddlewaretoken':O0OOO000OOOOOO000 ,'conversion_type':OO0000O000O00OO0O ,'sending_method':O0OO000O00O00OOOO }#line:374
        try :#line:375
            OO000O0O0O0O00OOO =requests .post (f"http://{O0O0000OO000O00O0}:8000/send-email/",data =O00OO0OO0OOO0O0O0 )#line:376
            O0OOOO00000O0O00O =OO000O0O0O0O00OOO .json ()#line:377
            print (O0OOOO00000O0O00O )#line:378
            return O0OOOO00000O0O00O #line:379
        except requests .exceptions .RequestException as O000O0OO00O0OO000 :#line:381
            print (f"An error occurred: {O000O0OO00O0OO000}")#line:382
def reset_server (OO0OOO0O0O000OOOO ):#line:385
        try :#line:386
            OOO0OOOOO00000O00 =requests .get (f"http://{OO0OOO0O0O000OOOO}:8000/reset/")#line:387
            OO0O0OO00O00O0000 =OOO0OOOOO00000O00 .json ()#line:388
            return OO0O0OO00O00O0000 #line:389
        except requests .exceptions .RequestException as O0O000O0OO0O0000O :#line:390
            OOO0000O00O0000O0 ='eror in '+str (O0O000O0OO0O0000O )+" server"+str (OO0OOO0O0O000OOOO )#line:391
            return OOO0000O00O0000O0 #line:392
app =Flask (__name__ )#line:395
uploaded_folder ='uploaded'#line:396
another_folders ='allfiles'#line:397
target_folders =['contacts','gmail','html','subjects']#line:398
@app .route ('/allfiles')#line:399
def list_all_files ():#line:400
    ""#line:401
    O000OOOO0O00O000O =get_all_files_without_subfolders (another_folders ,target_folders )#line:402
    return jsonify (O000OOOO0O00O000O )#line:403
def get_all_files_without_subfolders (OOOOO0OO0000O0O00 ,OOO000000O00000O0 ):#line:406
    OO0000OO0000O0O0O =[]#line:407
    for O0O0000O0000OO00O in OOO000000O00000O0 :#line:410
        OO00OOO0000O00OO0 =os .path .join (OOOOO0OO0000O0O00 ,O0O0000O0000OO00O )#line:411
        if os .path .exists (OO00OOO0000O00OO0 )and os .path .isdir (OO00OOO0000O00OO0 ):#line:412
            OOOOO0000OO0OO0OO =os .listdir (OO00OOO0000O00OO0 )#line:414
            OOOOO0000OO0OO0OO =[os .path .join (O0O0000O0000OO00O ,O000OO0O0OO0OO0O0 )for O000OO0O0OO0OO0O0 in OOOOO0000OO0OO0OO if os .path .isfile (os .path .join (OO00OOO0000O00OO0 ,O000OO0O0OO0OO0O0 ))]#line:415
            OO0000OO0000O0O0O .extend (OOOOO0000OO0OO0OO )#line:416
    return {'files':OO0000OO0000O0O0O }#line:418
@app .route ('/download_all')#line:420
def download_all_files ():#line:421
    ""#line:422
    OOOOO0OO000OOO000 ='all_files.zip'#line:423
    zip_all_files (another_folders ,target_folders ,OOOOO0OO000OOO000 )#line:424
    return send_file (OOOOO0OO000OOO000 ,as_attachment =True )#line:425
def concatenate_files_in_folder (OO0O00OOO0OO00000 ,O000O0000OOOOOOOO ):#line:428
    ""#line:429
    OOO0O00OO0OO0000O =True #line:430
    with open (O000O0000OOOOOOOO ,'w')as OO0O0O00OOOOO000O :#line:431
        for O00O00OO0O000000O in os .listdir (OO0O00OOO0OO00000 ):#line:432
            OOOOOO0O0OO0O0000 =os .path .join (OO0O00OOO0OO00000 ,O00O00OO0O000000O )#line:433
            if os .path .isfile (OOOOOO0O0OO0O0000 )and O00O00OO0O000000O .endswith ('.csv'):#line:434
                with open (OOOOOO0O0OO0O0000 ,'r')as O0O0OO0OO000OOOOO :#line:435
                    O0O0O0OOOOO00OOO0 =O0O0OO0OO000OOOOO .readlines ()#line:436
                    if OOO0O00OO0OO0000O :#line:437
                        OO0O0O00OOOOO000O .write (O0O0O0OOOOO00OOO0 [0 ])#line:438
                        OOO0O00OO0OO0000O =False #line:439
                    OO0O0O00OOOOO000O .writelines (O0O0O0OOOOO00OOO0 [1 :])#line:440
def zip_all_files (O0OO00000O0OO0O00 ,OO00OO00OOO0OO0OO ,O00OOOOOO0OO0O0OO ):#line:443
    with zipfile .ZipFile (O00OOOOOO0OO0O0OO ,'w',zipfile .ZIP_DEFLATED )as O0O0OO0O0OO00OOO0 :#line:444
        O0O0O0O00O00O000O =os .path .join (O0OO00000O0OO0O00 ,'gmail')#line:446
        if os .path .exists (O0O0O0O00O00O000O )and os .path .isdir (O0O0O0O00O00O000O ):#line:447
            O00O0O0O00000OO00 =os .path .join (O0OO00000O0OO0O00 ,'gmail_combined.csv')#line:448
            concatenate_files_in_folder (O0O0O0O00O00O000O ,O00O0O0O00000OO00 )#line:449
            O0O0OO0O0OO00OOO0 .write (O00O0O0O00000OO00 ,'gmail/gmail_combined.csv')#line:450
        O000OOOO0O0OOOOOO =os .path .join (O0OO00000O0OO0O00 ,'contacts')#line:453
        if os .path .exists (O000OOOO0O0OOOOOO )and os .path .isdir (O000OOOO0O0OOOOOO ):#line:454
            O0OO00O00000O0000 =os .path .join (O0OO00000O0OO0O00 ,'contact_combined.csv')#line:455
            concatenate_files_in_folder (O000OOOO0O0OOOOOO ,O0OO00O00000O0000 )#line:456
            O0O0OO0O0OO00OOO0 .write (O0OO00O00000O0000 ,'contact/contact_combined.csv')#line:457
        for O0000O0000OO0OO0O in ['html','subjects']:#line:460
            O000000OOOOOOOOOO =os .path .join (O0OO00000O0OO0O00 ,O0000O0000OO0OO0O )#line:461
            if os .path .exists (O000000OOOOOOOOOO )and os .path .isdir (O000000OOOOOOOOOO ):#line:462
                O00000O00O0000O0O =os .listdir (O000000OOOOOOOOOO )#line:463
                for O0OO0OO000000OO00 in O00000O00O0000O0O :#line:464
                    O00OOO000000OO000 =os .path .join (O000000OOOOOOOOOO ,O0OO0OO000000OO00 )#line:465
                    if os .path .isfile (O00OOO000000OO000 ):#line:466
                        OOOO000OO000OOOO0 =os .path .join (O0000O0000OO0OO0O ,O0OO0OO000000OO00 )#line:467
                        O0O0OO0O0OO00OOO0 .write (O00OOO000000OO000 ,OOOO000OO000OOOO0 )#line:468
@app .route ('/listfiles')#line:469
def list_files ():#line:470
    ""#line:471
    O00O0O00O0OO0O0O0 =['contact','gmail','html','subject']#line:472
    O0O0O00OO0OO00OO0 =get_specific_folder_files (uploaded_folder ,O00O0O00O0OO0O0O0 )#line:473
    return jsonify (O0O0O00OO0OO00OO0 )#line:474
def get_specific_folder_files (OO00O00OOOO0O000O ,O00O00O000O0O0O0O ):#line:477
    O00000OO0OO000000 ={}#line:478
    for OO00OOO00O0O000OO in O00O00O000O0O0O0O :#line:481
        OO00OO00O00O0O000 =os .path .join (OO00O00OOOO0O000O ,OO00OOO00O0O000OO )#line:482
        if os .path .exists (OO00OO00O00O0O000 )and os .path .isdir (OO00OO00O00O0O000 ):#line:483
            O00O00OOOO00OO000 =os .listdir (OO00OO00O00O0O000 )#line:484
            O00O00OOOO00OO000 =[OO0O0O0OOOO0OOOO0 for OO0O0O0OOOO0OOOO0 in O00O00OOOO00OO000 if os .path .isfile (os .path .join (OO00OO00O00O0O000 ,OO0O0O0OOOO0OOOO0 ))]#line:486
            O00000OO0OO000000 [OO00OOO00O0O000OO ]={'files':O00O00OOOO00OO000 }#line:489
    return O00000OO0OO000000 #line:491
@app .route ('/download_zip')#line:494
def download_zip ():#line:495
    ""#line:496
    O0OO0000OOOOOOO00 ='uploaded.zip'#line:497
    zip_folder (uploaded_folder ,O0OO0000OOOOOOO00 )#line:498
    return send_file (O0OO0000OOOOOOO00 ,as_attachment =True )#line:499
def concatenate_files_in_folder (O000O0000OOOO00OO ,O00O0O0OO00OOO000 ):#line:502
    ""#line:503
    O00O0O000O00OOO00 =True #line:504
    with open (O00O0O0OO00OOO000 ,'w')as O00OO00O000OOOO0O :#line:505
        for O00O00O0OO0O0O0O0 in os .listdir (O000O0000OOOO00OO ):#line:506
            OOOOOOO0O0O00OOOO =os .path .join (O000O0000OOOO00OO ,O00O00O0OO0O0O0O0 )#line:507
            if os .path .isfile (OOOOOOO0O0O00OOOO )and O00O00O0OO0O0O0O0 .endswith ('.csv'):#line:508
                with open (OOOOOOO0O0O00OOOO ,'r')as O0O0O00O000OO0O0O :#line:509
                    OO0OO0O00000OOO0O =O0O0O00O000OO0O0O .readlines ()#line:510
                    if O00O0O000O00OOO00 :#line:511
                        O00OO00O000OOOO0O .write (OO0OO0O00000OOO0O [0 ])#line:512
                        O00O0O000O00OOO00 =False #line:513
                    O00OO00O000OOOO0O .writelines (OO0OO0O00000OOO0O [1 :])#line:514
def zip_folder (OO00000OO0000OOOO ,OOO0000O000O0000O ):#line:517
    with zipfile .ZipFile (OOO0000O000O0000O ,'w',zipfile .ZIP_DEFLATED )as OO0O00O00OO000000 :#line:518
        O0O00OO0O0O0O0O00 =os .path .join (OO00000OO0000OOOO ,'contact')#line:520
        if os .path .exists (O0O00OO0O0O0O0O00 )and os .path .isdir (O0O00OO0O0O0O0O00 ):#line:521
            O00O0000O00OOO000 =os .path .join (OO00000OO0000OOOO ,'contact_combined.csv')#line:522
            concatenate_files_in_folder (O0O00OO0O0O0O0O00 ,O00O0000O00OOO000 )#line:523
            OO0O00O00OO000000 .write (O00O0000O00OOO000 ,'contact/contact_combined.csv')#line:524
        OOOOO0OO0O0O00000 =os .path .join (OO00000OO0000OOOO ,'gmail')#line:527
        if os .path .exists (OOOOO0OO0O0O00000 )and os .path .isdir (OOOOO0OO0O0O00000 ):#line:528
            OO0OO00000OOO0OOO =os .path .join (OO00000OO0000OOOO ,'gmail_combined.csv')#line:529
            concatenate_files_in_folder (OOOOO0OO0O0O00000 ,OO0OO00000OOO0OOO )#line:530
            OO0O00O00OO000000 .write (OO0OO00000OOO0OOO ,'gmail/gmail_combined.csv')#line:531
        for O0000OO000000OO00 ,O0OO0OO0OO00OO000 ,OOO00O0O0OOO0O0OO in os .walk (OO00000OO0000OOOO ):#line:534
            if O0000OO000000OO00 .endswith ('contact')or O0000OO000000OO00 .endswith ('gmail'):#line:535
                continue #line:536
            for OO0OO000OO0OO0OO0 in OOO00O0O0OOO0O0OO :#line:537
                O0OO000OOOO0O0O00 =os .path .join (O0000OO000000OO00 ,OO0OO000OO0OO0OO0 )#line:538
                O0OOOO0OOOO0OOOOO =os .path .relpath (O0OO000OOOO0O0O00 ,os .path .join (OO00000OO0000OOOO ,'..'))#line:540
                OO0O00O00OO000000 .write (O0OO000OOOO0O0O00 ,O0OOOO0OOOO0OOOOO )#line:541
create_allfiles_folder ()#line:542
def getdata (OOOO00OO0O0O0O00O ):#line:543
    ""#line:544
    try :#line:545
        OOOOOOO000OO0O00O =requests .get (f"http://{OOOO00OO0O0O0O00O}:8000/alldata/")#line:546
        OO0O0O000000O000O =OOOOOOO000OO0O00O .json ()#line:547
        return {OOOO00OO0O0O0O00O :OO0O0O000000O000O }#line:548
    except :#line:549
        return {OOOO00OO0O0O0O00O :"Maybe server not running"}#line:550
@app .route ('/uploadone',methods =['POST'])#line:552
def upload_files_one ():#line:553
    O00O0OO00OO0O00O0 =request .get_json ()#line:554
    O000O0O00OO0OOOOO ={'gmail':O00O0OO00OO0O00O0 .get ('gmail_file'),'contacts':O00O0OO00OO0O00O0 .get ('contacts_file'),'subjects':O00O0OO00OO0O00O0 .get ('subjects_file'),'html':O00O0OO00OO0O00O0 .get ('html_file')}#line:562
    OO000000OOO0O0O0O =O00O0OO00OO0O00O0 .get ('ip_address')#line:563
    if not OO000000OOO0O0O0O or len (OO000000OOO0O0O0O )<=1 :#line:564
        return jsonify ({'status':'error','message':'Invalid IP address. Must be longer than 1 character.'}),400 #line:569
    OO00O0OOOO0OO0000 =None #line:570
    O000OO0O00OOOOO00 =None #line:571
    O0OO00OOO0000OOO0 =None #line:572
    OO0OO0O0O0O0O00O0 =None #line:573
    if O000O0O00OO0OOOOO ['gmail']:#line:574
        OOOOO0OO000O00000 =os .path .join (os .getcwd (),'allfiles','gmail')#line:575
        O000OO000O0OOOOOO =glob (OOOOO0OO000O00000 +"/*")#line:576
        if O000OO000O0OOOOOO :#line:577
            O000OO0O00OOOOO00 =choice (O000OO000O0OOOOOO )#line:578
    if O000O0O00OO0OOOOO ['contacts']:#line:581
        OOOOO0OO000O00000 =os .path .join (os .getcwd (),'allfiles','contacts')#line:583
        O000OO000O0OOOOOO =glob (OOOOO0OO000O00000 +"/*")#line:584
        if O000OO000O0OOOOOO :#line:585
            OO00O0OOOO0OO0000 =choice (O000OO000O0OOOOOO )#line:586
    if O000O0O00OO0OOOOO ['subjects']:#line:589
        OOOOO0OO000O00000 =os .path .join (os .getcwd (),'allfiles','subjects')#line:591
        O000OO000O0OOOOOO =glob (OOOOO0OO000O00000 +"/*")#line:592
        if O000OO000O0OOOOOO :#line:593
            O0OO00OOO0000OOO0 =choice (O000OO000O0OOOOOO )#line:594
    if O000O0O00OO0OOOOO ['html']:#line:596
        OOOOO0OO000O00000 =os .path .join (os .getcwd (),'allfiles','html')#line:598
        O000OO000O0OOOOOO =glob (OOOOO0OO000O00000 +"/*")#line:599
        if O000OO000O0OOOOOO :#line:600
            OO0OO0O0O0O0O00O0 =choice (O000OO000O0OOOOOO )#line:601
    fileuploads (OO000000OOO0O0O0O ,contacts_file =OO00O0OOOO0OO0000 ,subjects_file =O0OO00OOO0000OOO0 ,gmail_file =O000OO0O00OOOOO00 ,html_file =OO0OO0O0O0O0O00O0 )#line:603
    return jsonify ({'status':'success','message':'Files uploaded successfully!','ip_address':OO000000OOO0O0O0O ,'uploaded_files':{'contacts_file':OO00O0OOOO0OO0000 ,'subjects_file':O0OO00OOO0000OOO0 ,'gmail_file':O000OO0O00OOOOO00 ,'html_file':OO0OO0O0O0O0O00O0 }})#line:614
@app .route ("/apidata",methods =['GET'])#line:615
def fetch_data_from_servers ():#line:616
    OO0O0OO000OOO0000 =[]#line:617
    OO000O0OO0OOOOO00 =[]#line:618
    def OO0000OOOOO000OOO (O00OOOOOOO00000O0 ):#line:620
        ""#line:621
        OO0O00OO00OOO0OOO =getdata (O00OOOOOOO00000O0 )#line:622
        OO000O0OO0OOOOO00 .append ({O00OOOOOOO00000O0 :OO0O00OO00OOO0OOO })#line:623
    with open ("server.txt","r")as OO0O0O0OOO0OOOO0O :#line:626
        for O000OOO00OOOO0000 in OO0O0O0OOO0OOOO0O :#line:627
            O0000O000000000O0 =O000OOO00OOOO0000 .strip ()#line:628
            O0OO0OOO0O0OOO0O0 =threading .Thread (target =OO0000OOOOO000OOO ,args =(O0000O000000000O0 ,))#line:629
            OO0O0OO000OOO0000 .append (O0OO0OOO0O0OOO0O0 )#line:630
            O0OO0OOO0O0OOO0O0 .start ()#line:631
    for O0OO0OOO0O0OOO0O0 in OO0O0OO000OOO0000 :#line:634
        O0OO0OOO0O0OOO0O0 .join ()#line:635
    return jsonify (OO000O0OO0OOOOO00 )#line:637
def delete_allfiles_folder ():#line:639
    OO0000O0O0OOOO00O ='allfiles'#line:640
    try :#line:641
        shutil .rmtree (OO0000O0O0OOOO00O )#line:642
    except :#line:643
        pass #line:644
    try :#line:645
        shutil .rmtree ("uploaded")#line:646
    except :#line:647
        pass #line:648
    if os .path .exists (OO0000O0O0OOOO00O )and os .path .isdir (OO0000O0O0OOOO00O ):#line:650
        shutil .rmtree (OO0000O0O0OOOO00O )#line:651
        return {"status":"success","message":f"'{OO0000O0O0OOOO00O}' folder has been deleted."}#line:652
    else :#line:653
        return {"status":"error","message":f"'{OO0000O0O0OOOO00O}' folder does not exist."}#line:654
@app .route ('/reset-all',methods =['POST'])#line:656
def reset_all ():#line:657
    try :#line:658
        os .remove ("server.txt")#line:659
    except :#line:660
        pass #line:661
    O0OO00O000OOOO000 =delete_allfiles_folder ()#line:662
    return jsonify (O0OO00O000OOOO000 )#line:663
@app .route ('/')#line:665
def home ():#line:666
    return render_template ("template/index.html")#line:668
@app .route ('/dash',methods =['GET','POST'])#line:670
def dash ():#line:671
    return render_template ("template/dash.html")#line:672
def clear_allfiles_folder (OOO0O000O00O0OOOO ):#line:677
    if os .path .exists (OOO0O000O00O0OOOO ):#line:678
        shutil .rmtree (OOO0O000O00O0OOOO )#line:679
        print (f"Cleared all contents in '{OOO0O000O00O0OOOO}'.")#line:680
    os .makedirs (OOO0O000O00O0OOOO )#line:682
@app .route ("/resetserver",methods =['POST'])#line:683
def reset_multiple ():#line:684
    if request .method =="POST":#line:685
        O0O0O0000OOOOOO00 =request .get_json ()#line:686
        OOOO0OO000O000OOO =O0O0O0000OOOOOO00 .get ('query')#line:687
        if OOOO0OO000O000OOO =='all':#line:688
                OO0OOOO00O0OOO00O =[]#line:689
                try :#line:690
                    with open ("server.txt",newline ='')as O0OO0O000O0O0O000 :#line:691
                        OOOOOOOO000O0OO00 =csv .reader (O0OO0O000O0O0O000 )#line:692
                        for OOO00O0OOOOOO0OOO in OOOOOOOO000O0OO00 :#line:693
                            if OOO00O0OOOOOO0OOO :#line:694
                                OOOO0OOO0000OOO0O =OOO00O0OOOOOO0OOO [0 ]#line:695
                                OO0000OO0OO00OOO0 =threading .Thread (target =reset_server ,args =(OOOO0OOO0000OOO0O ,))#line:696
                                OO0OOOO00O0OOO00O .append (OO0000OO0OO00OOO0 )#line:697
                                OO0000OO0OO00OOO0 .start ()#line:698
                        for OO0000OO0OO00OOO0 in OO0OOOO00O0OOO00O :#line:700
                            OO0000OO0OO00OOO0 .join ()#line:701
                    return jsonify ({"status":"success"})#line:702
                except Exception as O00O0O00OOO0O00O0 :#line:703
                    return jsonify ({"status":str (O00O0O00OOO0O00O0 )})#line:704
        else :#line:705
            reset_server (OOOO0OO000O000OOO )#line:706
            return jsonify ({"status":"success"})#line:707
@app .route ("/sendmultiple",methods =['POST'])#line:709
def sending_function ():#line:710
    try :#line:711
        O0000OO0O00O0O00O =request .get_json ()#line:712
        O000OOOO0OO0O0O0O =O0000OO0O00O0O00O .get ('query')#line:713
        O0O00OOO0O00OO0O0 =O0000OO0O00O0O00O .get ('conversionType')#line:714
        O00OO00000O00OO0O =O0000OO0O00O0O00O .get ('sendingMethod')#line:715
        if not O000OOOO0OO0O0O0O or not O0O00OOO0O00OO0O0 or not O00OO00000O00OO0O :#line:717
            return jsonify ({"status":"error","message":"Missing parameters"}),400 #line:718
        O00OOOO0O00O0O000 =f"Received query: {O000OOOO0OO0O0O0O}, Conversion Type: {O0O00OOO0O00OO0O0}, Sending Method: {O00OO00000O00OO0O}"#line:720
        if O000OOOO0OO0O0O0O =='all':#line:722
            O0OO0O000O0OOOO0O =[]#line:723
            try :#line:724
                with open ("server.txt",newline ='')as OO00OOO0O0OO0OOO0 :#line:725
                    OO0O00O0O0OO0OO00 =csv .reader (OO00OOO0O0OO0OOO0 )#line:726
                    for OOO00O0O0OO0OO0O0 in OO0O00O0O0OO0OO00 :#line:727
                        if OOO00O0O0OO0OO0O0 :#line:728
                            OOO00O0O0OO0OOOOO =OOO00O0O0OO0OO0O0 [0 ]#line:729
                            O000OOOO0O0O0O0O0 =threading .Thread (target =send_email ,args =(OOO00O0O0OO0OOOOO ,O0O00OOO0O00OO0O0 ,O00OO00000O00OO0O ))#line:730
                            O0OO0O000O0OOOO0O .append (O000OOOO0O0O0O0O0 )#line:731
                            O000OOOO0O0O0O0O0 .start ()#line:732
                    for O000OOOO0O0O0O0O0 in O0OO0O000O0OOOO0O :#line:734
                        O000OOOO0O0O0O0O0 .join ()#line:735
                return jsonify ({"status":"Configuration Saved","message":O00OOOO0O00O0O000 })#line:736
            except FileNotFoundError :#line:737
                return jsonify ({"status":"error","message":"File not found"})#line:739
            except Exception as O0OO00O000OOO0000 :#line:740
                print (O0OO00O000OOO0000 )#line:741
                return jsonify ({"status":"error","message":"Error reading file"})#line:742
        else :#line:744
            send_email (O000OOOO0OO0O0O0O ,O0O00OOO0O00OO0O0 ,O00OO00000O00OO0O )#line:745
            return jsonify ({"status":"success","message":O00OOOO0O00O0O000 })#line:746
    except Exception as O0OO00O000OOO0000 :#line:748
        print (O0OO00O000OOO0000 )#line:749
        return jsonify ({"status":"error","message":"An error occurred"})#line:751
@app .route ("/mulitplestop",methods =['POST'])#line:752
def stop_function ():#line:753
    try :#line:754
        OO00OOO0OO000000O =request .get_json ()#line:755
        OOOO0OOOO00OO0OO0 =OO00OOO0OO000000O .get ('query')#line:756
        O00OOO0OO0O0OO0OO =f"Received query: {OOOO0OOOO00OO0OO0}, status:stopped "#line:757
        if OOOO0OOOO00OO0OO0 =='all':#line:758
            try :#line:760
                run_threads_stop_server ()#line:761
                print ("stopped")#line:762
                return jsonify ({"status":"success","message":"All services are stopping"})#line:763
            except FileNotFoundError :#line:764
                return jsonify ({"status":"success","message":"stopped"})#line:766
            except Exception as OO00O0O0O0OO0O0OO :#line:767
                print (OO00O0O0O0OO0O0OO )#line:768
                return jsonify ({"status":"success","message":"stopped"})#line:769
        else :#line:773
            runcheck (OOOO0OOOO00OO0OO0 )#line:774
            return jsonify ({"status":"success","message":O00OOO0OO0O0OO0OO })#line:775
    except Exception as OO00O0O0O0OO0O0OO :#line:777
        print (OO00O0O0O0OO0O0OO )#line:778
        return jsonify ({"status":"error","message":"An error occurred"})#line:780
@app .route ("/sendingoriginal",methods =['POST'])#line:781
def sendingoriginal_function ():#line:782
    try :#line:783
        O000OO0OOOO0000O0 =request .get_json ()#line:784
        O0OO00000OOO0O00O =O000OO0OOOO0000O0 .get ('query')#line:785
        O0OOOOO00OOOO0O0O =f"Received query: {O0OO00000OOO0O00O}, status:Started "#line:786
        if O0OO00000OOO0O00O =='all':#line:787
            try :#line:789
                run_threads_sendingall_server ()#line:790
                return jsonify ({"status":"success","message":"All services are Started"})#line:791
            except FileNotFoundError :#line:792
                return jsonify ({"status":"success","message":"Started"})#line:794
            except Exception as OO0000OO0OOOO0OOO :#line:795
                print (OO0000OO0OOOO0OOO )#line:796
                return jsonify ({"status":"success","message":"Started"})#line:797
        else :#line:801
            mailsendingmain (O0OO00000OOO0O00O )#line:802
            return jsonify ({"status":"success","message":O0OOOOO00OOOO0O0O })#line:803
    except Exception as OO0000OO0OOOO0OOO :#line:805
        print (OO0000OO0OOOO0OOO )#line:806
        return jsonify ({"status":"error","message":"An error occurred"})#line:808
@app .route ('/uploadall',methods =['POST'])#line:810
def upload_multiple ():#line:811
    O0OO000OOOO0O000O =os .getcwd ()#line:812
    O0O00O0OO0OO0OOOO =os .path .join (O0OO000OOOO0O000O ,'allfiles')#line:815
    O0OO0O0OO0OO00000 =glob (os .path .join (O0O00O0OO0OO0OOOO ,'gmail','*'))#line:818
    OO00OOO00000O00OO =glob (os .path .join (O0O00O0OO0OO0OOOO ,'contacts','*'))#line:819
    OOOO0OO0OOO0OO00O =glob (os .path .join (O0O00O0OO0OO0OOOO ,'subjects','*'))#line:820
    OOO00OO0OO00O0O00 =glob (os .path .join (O0O00O0OO0OO0OOOO ,'html','*'))#line:821
    if not O0OO0O0OO0OO00000 and not OO00OOO00000O00OO and not OOOO0OO0OOO0OO00O and not OOO00OO0OO00O0O00 :#line:824
        return {'message':'All folders are empty'},404 #line:825
    try :#line:828
        with open ("server.txt","r")as O00OOO00O0OOOOOO0 :#line:829
            O0OOO0O0O0O0OO000 =O00OOO00O0OOOOOO0 .read ().splitlines ()#line:830
    except FileNotFoundError :#line:831
        return {'message':'server.txt file not found'},404 #line:832
    if len (O0OOO0O0O0O0OO000 )==0 :#line:835
        return {'message':'No servers available'},400 #line:836
    def O00OO00O00OOO00O0 (OOOO0OO0OO0OOO000 ,O0OOOOO0OO00OO0OO ):#line:839
        ""#line:840
        O00O000OO0OOO0O0O ={O0O0O0O0O0O0OOO00 :[]for O0O0O0O0O0O0OOO00 in O0OOOOO0OO00OO0OO }#line:841
        for OO000OO0OO0OOOOOO ,OO0OOOOOO0OOOO000 in enumerate (OOOO0OO0OO0OOO000 ):#line:842
            O00000OOO0OO0OOO0 =O0OOOOO0OO00OO0OO [OO000OO0OO0OOOOOO %len (O0OOOOO0OO00OO0OO )]#line:843
            O00O000OO0OOO0O0O [O00000OOO0OO0OOO0 ].append (OO0OOOOOO0OOOO000 )#line:844
        return O00O000OO0OOO0O0O #line:845
    OOOOO0O00000OO0OO =O00OO00O00OOO00O0 (O0OO0O0OO0OO00000 ,O0OOO0O0O0O0OO000 )if O0OO0O0OO0OO00000 else {O0O0O0000OO0O0O00 :[]for O0O0O0000OO0O0O00 in O0OOO0O0O0O0OO000 }#line:848
    O0OOOOO0OO0OO0OOO =O00OO00O00OOO00O0 (OO00OOO00000O00OO ,O0OOO0O0O0O0OO000 )if OO00OOO00000O00OO else {OOOOO0OOOO00O0O00 :[]for OOOOO0OOOO00O0O00 in O0OOO0O0O0O0OO000 }#line:849
    O0O00OOO00OOO0OO0 =O00OO00O00OOO00O0 (OOOO0OO0OOO0OO00O ,O0OOO0O0O0O0OO000 )if OOOO0OO0OOO0OO00O else {OOOOO000O0OOO0OO0 :[]for OOOOO000O0OOO0OO0 in O0OOO0O0O0O0OO000 }#line:850
    O0O00OOOO0O00000O =O00OO00O00OOO00O0 (OOO00OO0OO00O0O00 ,O0OOO0O0O0O0OO000 )if OOO00OO0OO00O0O00 else {O00O00O0000OOOO00 :[]for O00O00O0000OOOO00 in O0OOO0O0O0O0OO000 }#line:851
    def O000OOO000O00O00O (*O0OO00OO00O00OO00 ):#line:854
        ""#line:855
        O0OO00000OOO0000O ={}#line:856
        for O00O000O0000000O0 in O0OOO0O0O0O0OO000 :#line:857
            O0OO00000OOO0000O [O00O000O0000000O0 ]={'gmail':OOOOO0O00000OO0OO .get (O00O000O0000000O0 ,[]),'contacts':O0OOOOO0OO0OO0OOO .get (O00O000O0000000O0 ,[]),'subjects':O0O00OOO00OOO0OO0 .get (O00O000O0000000O0 ,[]),'html':O0O00OOOO0O00000O .get (O00O000O0000000O0 ,[])}#line:863
        return O0OO00000OOO0000O #line:864
    O00O0OOOO0OOOO000 =O000OOO000O00O00O (OOOOO0O00000OO0OO ,O0OOOOO0OO0OO0OOO ,O0O00OOO00OOO0OO0 ,O0O00OOOO0O00000O )#line:866
    def O00000000O00000OO (OOO00OOO00O00O000 ,OO00OO0O0O0000OOO ):#line:869
        O0OO0OOOO00OOO00O =OO00OO0O0O0000OOO ['gmail']#line:870
        O0OOOO00O0000OOOO =OO00OO0O0O0000OOO ['contacts']#line:871
        OO00000OO0OO00OOO =OO00OO0O0O0000OOO ['subjects']#line:872
        O0O0O0OOO0OO0OOO0 =OO00OO0O0O0000OOO ['html']#line:873
        for O0O0OOO0O00000O0O ,O00OOOO00O0O0O0O0 ,O0O0O0O000O0OO0O0 ,OO00OO00O00000O0O in zip_longest (O0OO0OOOO00OOO00O ,O0OOOO00O0000OOOO ,OO00000OO0OO00OOO ,O0O0O0OOO0OO0OOO0 ,fillvalue =None ):#line:876
            print (f"Processing files for {OOO00OOO00O00O000}: {O0O0OOO0O00000O0O}, {O00OOOO00O0O0O0O0}, {O0O0O0O000O0OO0O0}, {OO00OO00O00000O0O}")#line:877
            fileuploads (OOO00OOO00O00O000 ,O00OOOO00O0O0O0O0 ,O0O0O0O000O0OO0O0 ,O0O0OOO0O00000O0O ,OO00OO00O00000O0O )#line:878
    O0000O0OO0000OO00 =[]#line:881
    for OOOOOO00000O0OO0O ,O000O0OO0O00O0O00 in O00O0OOOO0OOOO000 .items ():#line:882
        if len (OOOOOO00000O0OO0O )<2 :#line:883
            continue #line:884
        O0OO00O00OOOOO00O =threading .Thread (target =O00000000O00000OO ,args =(OOOOOO00000O0OO0O ,O000O0OO0O00O0O00 ))#line:885
        O0000O0OO0000OO00 .append (O0OO00O00OOOOO00O )#line:886
        O0OO00O00OOOOO00O .start ()#line:887
    for O0OO00O00OOOOO00O in O0000O0OO0000OO00 :#line:890
        O0OO00O00OOOOO00O .join ()#line:891
    return {'message':'All files uploaded successfully'}#line:893
@app .route ('/redirect-home')#line:895
def redirect_home ():#line:896
    new ()#line:897
    return redirect (url_for ('home'))#line:898
@app .route ('/upload',methods =['POST'])#line:900
def upload_files ():#line:901
    OO00OOOO0O0O0OOO0 ="allfiles"#line:902
    OOO00O0OOOO00OO00 ='allfiles'#line:903
    O0OO000O0O0OO00OO =request .files .get ('zip_file')#line:905
    O00OOOO0O0O00000O =request .files .get ('txt_file')#line:906
    O00O00O0OOOO00O00 =""#line:909
    O00O000OOOOO0000O =""#line:910
    clear_allfiles_folder (OOO00O0OOOO00OO00 )#line:911
    create_allfiles_folder ()#line:912
    if O0OO000O0O0OO00OO and O0OO000O0O0OO00OO .filename .endswith ('.zip'):#line:914
        OOO0O000OOO0OOOOO =os .path .join ('allfiles',O0OO000O0O0OO00OO .filename )#line:916
        O0OO000O0O0OO00OO .save (OOO0O000OOO0OOOOO )#line:917
        OOOOOOO00O0OOOOO0 =os .path .join ('allfiles','subjects')#line:920
        O0O000O0000O0O000 =os .path .join ('allfiles','gmail')#line:921
        O0OOOOO0O0OO0OOOO =os .path .join ('allfiles','contacts')#line:922
        OOOOOO0O0O0O000O0 =os .path .join ('allfiles','html')#line:923
        os .makedirs (OOOOOOO00O0OOOOO0 ,exist_ok =True )#line:926
        os .makedirs (O0O000O0000O0O000 ,exist_ok =True )#line:927
        os .makedirs (O0OOOOO0O0OO0OOOO ,exist_ok =True )#line:928
        os .makedirs (OOOOOO0O0O0O000O0 ,exist_ok =True )#line:929
        with zipfile .ZipFile (OOO0O000OOO0OOOOO ,'r')as O00OO0O0O00OO0O00 :#line:932
            for OOOO00OO0OO0OO0OO in O00OO0O0O00OO0O00 .namelist ():#line:933
                if not OOOO00OO0OO0OO0OO .endswith ('/'):#line:935
                    OO00O0OOO0OOO0000 =os .path .basename (OOOO00OO0OO0OO0OO )#line:936
                    if 'subject'in OO00O0OOO0OOO0000 .lower ():#line:939
                        OOO00O0OOOO00OO00 =OOOOOOO00O0OOOOO0 #line:940
                    elif 'gmail'in OO00O0OOO0OOO0000 .lower ():#line:941
                        OOO00O0OOOO00OO00 =O0O000O0000O0O000 #line:942
                    elif 'contact'in OO00O0OOO0OOO0000 .lower ():#line:943
                        OOO00O0OOOO00OO00 =O0OOOOO0O0OO0OOOO #line:944
                    elif OO00O0OOO0OOO0000 .endswith ('.html'):#line:945
                        OOO00O0OOOO00OO00 =OOOOOO0O0O0O000O0 #line:946
                    else :#line:947
                        OOO00O0OOOO00OO00 ='allfiles'#line:948
                    O0O0OO0O0000OO0O0 =os .path .join (OOO00O0OOOO00OO00 ,OO00O0OOO0OOO0000 )#line:951
                    with open (O0O0OO0O0000OO0O0 ,'wb')as O0OOOO0O00000000O :#line:954
                        O0OOOO0O00000000O .write (O00OO0O0O00OO0O00 .read (OOOO00OO0OO0OO0OO ))#line:955
                    print (f"Extracted {OO00O0OOO0OOO0000} to {OOO00O0OOOO00OO00}")#line:957
        O00O00O0OOOO00O00 =f"'{O0OO000O0O0OO00OO.filename}' uploaded and extracted successfully."#line:959
    else :#line:960
        O00O00O0OOOO00O00 ="No valid ZIP file uploaded."#line:961
    if O00OOOO0O0O00000O and (O00OOOO0O0O00000O .filename .endswith ('.txt')or O00OOOO0O0O00000O .filename .endswith ('.csv')):#line:964
        O00O0O0OO0OOOOOOO =os .path .join (os .getcwd (),"server.txt")#line:965
        O00OOOO0O0O00000O .save (O00O0O0OO0OOOOOOO )#line:966
        O00O000OOOOO0000O =f"'{O00OOOO0O0O00000O.filename}' uploaded to root directory successfully."#line:967
    else :#line:968
        O00O000OOOOO0000O ="No valid TXT or CSV file uploaded."#line:969
    OO0O0000OOO000O00 =['contact','gmail','subject']#line:977
    for OO000000O0OOOOOOO in os .listdir (OO00OOOO0O0O0OOO0 ):#line:985
        if os .path .isdir (os .path .join (OO00OOOO0O0O0OOO0 ,OO000000O0OOOOOOO )):#line:988
            continue #line:989
        if "api.zip"in str (OO000000O0OOOOOOO ):#line:990
            print (OO000000O0OOOOOOO )#line:991
            O0O0O00000O000O0O ='allfiles'#line:992
            O0O0OO0O0000OO0O0 =os .getcwd ()+"//allfiles/apidata//"#line:993
            O000O0O00OO0O0OO0 =os .path .join (O0O0O00000O000O0O ,os .path .basename (OO000000O0OOOOOOO ))#line:994
            try :#line:995
                os .makedirs (O0O0OO0O0000OO0O0 )#line:996
            except :#line:997
                pass #line:998
            with zipfile .ZipFile (O000O0O00OO0O0OO0 ,'r')as O0OOOO0O00000000O :#line:999
                        O0OOOO0O00000000O .extractall (O0O0OO0O0000OO0O0 )#line:1000
            O0OOOO0O00000000O .close ()#line:1001
            try :#line:1002
                os .remove (OO000000O0OOOOOOO )#line:1003
            except :#line:1004
                pass #line:1005
        if OO000000O0OOOOOOO .endswith (".zip"):#line:1006
            O000OO0O0OOOOOOO0 =os .path .join (OO00OOOO0O0O0OOO0 ,OO000000O0OOOOOOO )#line:1007
            os .remove (O000OO0O0OOOOOOO0 )#line:1008
        if OO000000O0OOOOOOO .endswith ('.html'):#line:1010
            OOO00O0000OOOO0OO =os .path .join (OO00OOOO0O0O0OOO0 ,OO000000O0OOOOOOO )#line:1012
            OO00OO0OO0OO0OOOO =os .path .join (OOOOOO0O0O0O000O0 ,OO000000O0OOOOOOO )#line:1013
            try :#line:1014
                shutil .move (OOO00O0000OOOO0OO ,OO00OO0OO0OO0OOOO )#line:1015
            except :#line:1016
                pass #line:1017
            print (f"Moved {OO000000O0OOOOOOO} to {OOOOOO0O0O0O000O0}")#line:1018
            continue #line:1019
        for OOO0OO000O00OOOOO in OO0O0000OOO000O00 :#line:1022
            if OOO0OO000O00OOOOO in OO000000O0OOOOOOO :#line:1023
                OO00OO00O0OO0O0O0 =OO000000O0OOOOOOO .split ('.')[0 ]#line:1025
                OOO000O0OOOO00OO0 =os .path .join (OOO00O0OOOO00OO00 ,OO00OO00O0OO0O0O0 )#line:1028
                if not os .path .exists (OOO000O0OOOO00OO0 ):#line:1031
                    os .makedirs (OOO000O0OOOO00OO0 )#line:1032
                OOO00O0000OOOO0OO =os .path .join (OO00OOOO0O0O0OOO0 ,OO000000O0OOOOOOO )#line:1035
                OO00OO0OO0OO0OOOO =os .path .join (OOO000O0OOOO00OO0 ,OO000000O0OOOOOOO )#line:1036
                try :#line:1037
                    shutil .move (OOO00O0000OOOO0OO ,OO00OO0OO0OO0OOOO )#line:1038
                except :#line:1039
                    pass #line:1040
                print (f"Moved {OO000000O0OOOOOOO} to {OOO000O0OOOO00OO0}")#line:1041
                break #line:1042
    new ()#line:1043
    return jsonify ({'message':f"{O00O00O0OOOO00O00} {O00O000OOOOO0000O}"})#line:1044
results =[]#line:1046
def handle_error (OOO0OOO0OO0O0OOOO ,O0O0O0OOOOO0O0O00 ,OO0O00OOOO0O00000 ):#line:1048
    ""#line:1049
    print (f"Error for {OOO0OOO0OO0O0OOOO} at IP {O0O0O0OOOOO0O0O00}: {OO0O00OOOO0O00000}")#line:1050
def check_for_errors (OO0OO0OO0O00O000O ):#line:1052
    ""#line:1053
    for O00000OO0OOOO0OO0 ,OO00O0OO00O0O0OO0 in OO0OO0OO0O00O000O .items ():#line:1054
        print (OO00O0OO00O0O0OO0 )#line:1055
        for O00OO0O0O0OO00OO0 ,O00OOOO0O0OOOOOO0 in OO00O0OO00O0O0OO0 .items ():#line:1056
            if isinstance (O00OOOO0O0OOOOOO0 ,dict ):#line:1057
                for O00O0O00O00OOO000 ,OOO00000OO0OO000O in O00OOOO0O0OOOOOO0 .items ():#line:1059
                    if isinstance (OOO00000OO0OO000O ,dict ):#line:1061
                        if OOO00000OO0OO000O .get ("status")=="error":#line:1062
                            handle_error (O00OO0O0O0OO00OO0 ,OOO00000OO0OO000O )#line:1063
                    elif O00O0O00O00OOO000 =="status"and OOO00000OO0OO000O =="error":#line:1065
                        handle_error (O00OO0O0O0OO00OO0 ,O00OOOO0O0OOOOOO0 )#line:1066
            elif "status"in O00OOOO0O0OOOOOO0 and O00OOOO0O0OOOOOO0 ["status"]=="error":#line:1068
                handle_error (O00OO0O0O0OO00OO0 ,O00OOOO0O0OOOOOO0 )#line:1069
last_execution_time ={}#line:1070
def fetch_data_from_servers ():#line:1071
    if not os .path .isfile ("server.txt"):#line:1072
        print ("File does not exist"," server")#line:1073
    try :#line:1074
        OO0O0O0O0O0OO00OO =[]#line:1075
        OOO0000OOOO000OO0 ={}#line:1076
        def OO0OOOO0OOOOOOO00 (O0OO00O000OO0O00O ):#line:1077
            OOO0O00O0OO0O000O =time .time ()#line:1079
            if O0OO00O000OO0O00O in last_execution_time and OOO0O00O0OO0O000O -last_execution_time [O0OO00O000OO0O00O ]<40 :#line:1082
                return #line:1084
            last_execution_time [O0OO00O000OO0O00O ]=OOO0O00O0OO0O000O #line:1087
            try :#line:1090
                O000O0000O0OO0OO0 =getdata (O0OO00O000OO0O00O )#line:1091
            except :#line:1092
                O000O0000O0OO0OO0 ={}#line:1093
            if O000O0000O0OO0OO0 :#line:1094
                O0OOOOOOO0OOO0O00 =None #line:1095
                OOO000OOOOOO00O0O =None #line:1096
                for O00O00O0O00O0O0O0 ,O00OO0O000O0OOO0O in O000O0000O0OO0OO0 .items ():#line:1099
                    for O00000O000O00O0O0 ,O0OO0000O00OO0O0O in O00OO0O000O0OOO0O .items ():#line:1100
                        if O0OOOOOOO0OOO0O00 is None or O0OO0000O00OO0O0O ['timestamp']>O0OOOOOOO0OOO0O00 :#line:1101
                            try :#line:1102
                                O0OOOOOOO0OOO0O00 =O0OO0000O00OO0O0O ['timestamp']#line:1103
                                OOO000OOOOOO00O0O =O0OO0000O00OO0O0O ['status']#line:1104
                            except :#line:1105
                                O0OOOOOOO0OOO0O00 =None #line:1106
                                OOO000OOOOOO00O0O =None #line:1107
                if O0OOOOOOO0OOO0O00 :#line:1110
                    OOO0000OOOO000OO0 [O0OO00O000OO0O00O ]={"timestamp":O0OOOOOOO0OOO0O00 ,"status":OOO000OOOOOO00O0O }#line:1111
                    if "contacts.csv"in str (OOO0000OOOO000OO0 [O0OO00O000OO0O00O ]["status"])or "all-contact-done"in str (OOO0000OOOO000OO0 [O0OO00O000OO0O00O ]["status"]):#line:1114
                        try :#line:1115
                                    mailsendingmain (O0OO00O000OO0O00O )#line:1117
                                    time .sleep (2 )#line:1118
                                    print (f"File has been successfully processed and removed.")#line:1119
                        except Exception as O0OOO0OO0O0O0OOO0 :#line:1120
                            print (f"Error processing or removing file for IP {O0OO00O000OO0O00O}: {O0OOO0OO0O0O0OOO0}")#line:1121
                    if "gmail.csv"in str (OOO0000OOOO000OO0 [O0OO00O000OO0O00O ]["status"]):#line:1122
                        try :#line:1123
                                    mailsendingmain (O0OO00O000OO0O00O )#line:1125
                                    time .sleep (2 )#line:1126
                                    print (f"File has been successfully processed and removed.")#line:1127
                        except Exception as O0OOO0OO0O0O0OOO0 :#line:1129
                            print (f"Error processing or removing file for IP {O0OO00O000OO0O00O}: {O0OOO0OO0O0O0OOO0}")#line:1130
                    if "subjects.csv"in str (OOO0000OOOO000OO0 [O0OO00O000OO0O00O ]["status"]):#line:1131
                        try :#line:1132
                            O00O000OO0O00OO00 =os .path .join (os .getcwd (),'allfiles','subjects')#line:1134
                            OOO0000O0O0O00O00 =glob (O00O000OO0O00OO00 +"/*")#line:1135
                            if OOO0000O0O0O00O00 :#line:1136
                                    OO000000OOO0O00O0 =choice (OOO0000O0O0O00O00 )#line:1137
                                    mailsendingmain (O0OO00O000OO0O00O )#line:1142
                                    time .sleep (2 )#line:1144
                                    print (f"File has been successfully processed and removed.")#line:1147
                        except Exception as O0OOO0OO0O0O0OOO0 :#line:1148
                            print (f"Error processing or removing file for IP {O0OO00O000OO0O00O}: {O0OOO0OO0O0O0OOO0}")#line:1149
                    if "gmail-auth-error"in str (OOO0000OOOO000OO0 [O0OO00O000OO0O00O ]["status"])or "limit"in str (OOO0000OOOO000OO0 [O0OO00O000OO0O00O ]["status"]):#line:1151
                        try :#line:1153
                                    mailsendingmain (O0OO00O000OO0O00O )#line:1156
                                    time .sleep (2 )#line:1158
                                    print (f"File has been successfully processed and limit.")#line:1160
                        except Exception as O0OOO0OO0O0O0OOO0 :#line:1161
                            print (f"Error processing or removing file for IP {O0OO00O000OO0O00O}: {O0OOO0OO0O0O0OOO0}")#line:1162
                    if "html_code.html"in str (OOO0000OOOO000OO0 [O0OO00O000OO0O00O ]["status"]):#line:1165
                        try :#line:1166
                                    mailsendingmain (O0OO00O000OO0O00O )#line:1170
                                    time .sleep (2 )#line:1171
                                    print (f"File has been successfully processed and removed.")#line:1172
                        except Exception as O0OOO0OO0O0O0OOO0 :#line:1174
                            print (f"Error processing or removing file for IP {O0OO00O000OO0O00O}: {O0OOO0OO0O0O0OOO0}")#line:1175
        with open ("server.txt","r")as OOOO0O0O00OOO0O00 :#line:1177
            for OOOO000OOOOOOO0OO in OOOO0O0O00OOO0O00 :#line:1178
                O0O0O00O0OOO0O00O =OOOO000OOOOOOO0OO .strip ()#line:1179
                OOO0O0O00O0000OO0 =threading .Thread (target =OO0OOOO0OOOOOOO00 ,args =(O0O0O00O0OOO0O00O ,))#line:1180
                OO0O0O0O0O0OO00OO .append (OOO0O0O00O0000OO0 )#line:1181
                OOO0O0O00O0000OO0 .start ()#line:1182
        for OOO0O0O00O0000OO0 in OO0O0O0O0O0OO00OO :#line:1183
            OOO0O0O00O0000OO0 .join ()#line:1184
    except Exception as OOOO0OOO00O0000OO :#line:1187
        print (OOOO0OOO00O0000OO )#line:1188
def getfilesdta (O0OO0OO000O000O00 ):#line:1189
    O0000OO0O0OO0O0OO =requests .get (f"http://{O0OO0OO000O000O00}:8000/email_app/data")#line:1190
    return O0000OO0O0OO0O0OO .text #line:1191
def getfilesdtacredential (OO0OOOOO0000O0O0O ):#line:1193
    OOO00OO0O0O0OOOO0 =requests .get (f"http://{OO0OOOOO0000O0O0O}:8000/email_app/credentials")#line:1194
    return OOO00OO0O0O0OOOO0 .text #line:1195
@app .route ('/vewidata-items',methods =['GET'])#line:1196
def view_data_items ():#line:1197
    O0OO0OO000OOOOOOO =request .args .get ('ip')#line:1198
    if O0OO0OO000OOOOOOO :#line:1200
        O0O0O0OO00OO0O00O =getfilesdta (O0OO0OO000OOOOOOO )#line:1202
        if O0O0O0OO00OO0O00O :#line:1203
            return O0O0O0OO00OO0O00O #line:1204
        else :#line:1205
            return jsonify ({"status":"error","message":"No data found for this IP"}),404 #line:1206
    else :#line:1207
        return jsonify ({"status":"error","message":"No IP provided"}),400 #line:1208
@app .route ('/vivew-credentials',methods =['GET'])#line:1209
def view_data_itemscredential ():#line:1210
    OO00O0000O00O0O0O =request .args .get ('ip')#line:1211
    if OO00O0000O00O0O0O :#line:1213
        OO0O00OO0OO0O00OO =getfilesdtacredential (OO00O0000O00O0O0O )#line:1215
        if OO0O00OO0OO0O00OO :#line:1216
            return OO0O00OO0OO0O00OO #line:1217
        else :#line:1218
            return jsonify ({"status":"error","message":"No data found for this IP"}),404 #line:1219
    else :#line:1220
        return jsonify ({"status":"error","message":"No IP provided"}),400 #line:1221
def start_scheduler ():#line:1223
    O00OOO00O0OOOOO0O =BackgroundScheduler ()#line:1224
    O00OOO00O0OOOOO0O .add_job (func =fetch_data_from_servers ,trigger ="interval",seconds =60 )#line:1225
    O00OOO00O0OOOOO0O .start ()#line:1226
@app .after_request #line:1227
def activate_job (O0O0000OOO0OO0000 ):#line:1228
    global background_task_started #line:1229
    if background_task_started :#line:1230
        print ("schdule started")#line:1231
        start_scheduler ()#line:1232
    return O0O0000OOO0OO0000 #line:1234
if __name__ =='__main__':#line:1236
    app .run (host ='0.0.0.0',port =5000 ,debug =True ,use_reloader =False )#line:1238
