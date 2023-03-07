#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: victor
"""
import sys
import pymongo
from pymongo import MongoClient
from datetime import datetime
mongo_url_01="mongodb://administrator:administrator@140.118.151.39:27017/"
def catch_channelbusy(DB,Collection):
    global mongo_url_01
    try:
        conn = MongoClient(mongo_url_01) 
        db = conn[DB]
        collection = db[Collection]
        cursor=collection.find().sort("_id",-1).limit(45)
        data=[d for d in cursor]
        if data==[]:
            return False
        else:
            return data
    except:
        return False
def setup_alarm(B_time= None,E_time= None,data= False):
    if(data!=False):
        
        if(B_time!=None and E_time!=None ):
            time=datetime.now()   #need to check vm time currect or not
            if(B_time<=time and time<=E_time):
                for i in range (len(data)):
                   
                        busy=0
                        data[i]={
                        'ap_name':data[i]['ap_name'],
                        'channel_busy':busy
                        }
            else:
                for i in range (len(data)):
                    if(data[i]['channel_busy']>=0.8):
                        busy=1
                    else:
                        busy=0
                    data[i]={
                        'ap_name':data[i]['ap_name'],
                        'channel_busy':busy
                        }
            
            
        else:
            for i in range (len(data)):
                if(data[i]['channel_busy']>=0.8):
                    busy=1
                else:
                    busy=0
                data[i]={
                    'ap_name':data[i]['ap_name'],
                    'channel_busy':busy
                    }
        return data
    else:
        return False
def get_channel_data():
    data=catch_channelbusy('AP','Controller4')
    data=setup_alarm(data=data)
    return data

    
