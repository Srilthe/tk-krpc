#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 10:44:57 2021

@author: srilthe

https://krpc.github.io/krpc/

https://github.com/krpc

"""
import krpc

class match():
    global conn, vessel, fuelz, throttle

    def connector():
        global conn, vessel
        conn = krpc.connect(address="192.168.1.5",name='TK Control')
        vessel = conn.space_center.active_vessel
    connector.btn = 'con'
    connector.seq = 0

    def disco():
        conn.close()
    disco.btn = 'disco'
    disco.seq = 1
     
    def throttle_incr():
        print('+')
        vessel.control.throttle = 1
        global returned
        returned = ['match', 0]
    throttle_incr.btn='+throttle'
        
        
    def throttle_decr():
        print('-')
        vessel.control.throttle = 0
        global returned
        returned = ['throt', 1]
    throttle_decr.btn = '-throttle'    

    # Create the globals to add to the match class
    def zGenerate():
        zList = []
        for i in dir(match)[26:-1]:
            if (i != 'send_txt'): zList.append([i])
        return(zList)
