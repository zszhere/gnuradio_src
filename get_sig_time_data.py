#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from sys import argv

#ori time seq
ori_data = []
#all 01 seq
data = []
#time div
time = 50

def decode_sig(sig):
    #last status
    prv = 0
    #cnt time
    cnt = 0
    #decode per 300us
    decode = ''
    #ori status
    ori_seq = []
    #this status
    seq = []
    
    fin = open(sig,'r')
    for i in fin.read():
        if ord(i) == prv:
            cnt += 1
        else:
            tmp = int(cnt/time)+int(2*cnt/time)%2            
            if prv/255 == 1:
                decode = tmp * '1'
            else:
                decode = tmp * '0' 
            #normal 2000     
            #if cnt > 2000:
            #jpzx 800
            if cnt > 800:
                #print 'seq is %s'%(seq)           
                #print '++mark+++++++++++++++++++++++++++++++++++++++++++'          
                ori_data.append(ori_seq)
                data.append(seq)  
                ori_seq = []                          
                seq = []
            else:
                ori_seq.append(cnt)
                seq.append(decode) 
                #print '%2s for %5s *10us for %5s *300us decode is %10s'%(prv/255,cnt,tmp,seq[-1])
            prv = ord(i)
            cnt = 0
    fin.close()

def decode_str(strs):
    data = ''
    ptr = 0
    start = '10'*212
    #gap   = '0000000000000000000000000000000000000000'
    #gap   = '0000000000000000000000000000000000000'
    while ptr < len(strs):    
        if strs[ptr:ptr+len(start)] == start:
            data += '\nstart_seq\n'
            ptr += len(start)
        else:
            data += strs[ptr]
            ptr += 1
    return data

def decode_2262(strs):
    data = ''
    ptr = 0
    Hpin = '10001000'
    Lpin = '11101110'
    Fpin = '10001110'
    while ptr < len(strs):    
        if strs[ptr:ptr+8] == Hpin:
            data += '1'
            ptr += 8
        elif strs[ptr:ptr+8] == Lpin:
            data += '0'
            ptr += 8
        elif strs[ptr:ptr+8] == Fpin:
            data += 'F'
            ptr += 8
        else:
            data += 'e'
            ptr += 1
    return data
   
decode_sig(argv[1])
print len(ori_data)
print len(data)
for i in xrange(len(data)):
    print '++mark+++++++++++++++++++++++++++++++++++++++++++'
    print '--time len is:%s\n%s'%(len(ori_data[i]),repr(ori_data[i]))
    print '--data len is:%s\n%s'%(len(data[i]),''.join(data[i]))
    #print '--dec str is:\n'+decode_str(strs)+'\n'
    print '--dec str is:\n'+decode_2262(''.join(data[i]))
    print '\n'

'''

10101100 10101101 01010100 10110010 10110101 01001101 01010101 M 01010010 11010101 01001011 00101011 00101100 10101101 01001011 00110011 01001100 10101011010100110010101011010010101101001010110100110011010011001101001

10101100 10101101 01010100 10110010 10110101 01001101 01010101 M 01001010 10101011 00110101 01001011 00101100 10101101 00101100 10110010 10110100 10110011010011001100110011001100110011010100101011010011010100110010101

'''



        
        
