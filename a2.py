# -*- coding: cp936 -*-
from math import sqrt
from datetime import date
#�ڶ���----�����е���ѧ
#��cȤζ��̡�11-17��
#21:42 2006-11-4
def z11():
    
    #ĳ����1999��9��29������
    #�ʵ�2006��9��29�������˶�����
    a=date(1999,9,29)
    b=date(2006,9,29)
    c=str(b-a).split(" ")
    print int(c[0])
    return int(c[0])

def z12():
    #��λ��ǰ��λ��ͬ������λҲ��ͬ�������Ǹ���Ȼ����ƽ��,���� �Ƕ���
    t=range(1,10)
    for i in t :
        for j in t:
           m=i*1100+j*11
           n=int(sqrt(m))
           if m==n*n and i!=j :
               print m
def z13():
    #������Ϣ0.63%��һ �˴���������ÿ�����ȡ1000������ȡ�꣬�ʵ�һ��Ӧ�ô����
    tl=0
    for i in range(5):
        tl=(tl+1000.0)/(1+0.0063*12)
    print tl
def z14():
    '''������ȡ��Ǯ������1��2��3��5��8������ʷֱ���
    0.63%,0.66%,0.69%,0.75%,0.84%��20��Ǯ��������    �����'''
    l1=[8,5,3,2,1]
    l2=[0.0084,0.0075,0.0069,0.0066,0.0063]
    nn=20
    maxx=0
    l3=map(lambda x,y:  1+12*x*y, l1,l2)
    for i in range(nn/l1[0]+1):
        for j in range(nn/l1[1]+1):
            for a in range(nn/l1[2]+1):
                for b in range(nn/l1[3]+1):
                    t=nn-i*l1[0]-j*l1[1]-a*l1[2]-b*l1[3]
                    if t>=0 :
                        kk=[i,j,a,b,t]
                        kt=reduce(lambda x, y: x*y, map(lambda x,y:  x**y,l3,kk))
                        if kt>maxx :
                            maxx=kt
                            kkk=kk 
    print kkk,2000*maxx
def z15():
    '''���˲���,a�Ƚ����Ϊ5�ݣ��Ѷ����һ�����ˣ������Լ�
��һ�ݣ�bcdeͬ�������ã��������ٶ����� '''
    n=1
    nn=5
    flag=0
    while flag==0 :
        n+=5
        s=n
        for i in range(5):
            s,y=divmod(s-1,5)
            if y==0:
                s*=4
                flag=1
            else :
                flag=0
                break
    print n
def z16():
    '''���㣬��һ������1/2��1/2��
            ��2������1/3��1/3��
            ��3������1/4��1/4��
            ��4������1/5��1/5��
            ����11��
            ��һ��ʼ�Ƕ�����'''
    n=23
    nn=5
    flag=0
    while flag==0 :
        n+=2
        ss=n
        for i in range(1,5):
            s,y=divmod(ss+1,(i+1))
            if y==0:
                ss-=s
                flag=1
            else :
                flag=0
                break
    print n
def z17():
    #21���㣬7������7��룬7��գ��ڲ������������£�����ƽ��Ϊ3��
    k=[]
    for i in range(1,4):
        k+=[[i,7-i*2,i]]
    #print k
    for i in k:
        for j in k:
            for m in k:
                l3=map(lambda x,y,z:x+y+z, i,j,m)
                if i<=j<=m and l3[0]==7 and l3[1]==7:
                    print [i,j,m]
                    
if __name__ == '__main__':
    s=""
    for i in range(11,18):
        s+='z'+str(i)+'()\n'
    exec(s)
    
