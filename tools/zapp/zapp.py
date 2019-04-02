# Z80 Assembly Pre Parser
# Parses assembly source code, to generate documentation and provide some higher-level control.
help='''
zapp.py input [output [doc
'''


import sys,os
fc = 0
def docify(l):
    s=''
    for i in l:
        s+=i[0]+'\n'+i[1]+'\n'
    return s
def zapp(s,me='',ind='',bp=''):
    global fc
    fc+=1
    s=s.replace('\r','\n')
    #s=s.replace('\\','\n')
    s=s.split('\n')
    labels=[]           #Keep a running list of labels during the first pass
    incs=[]             #Kepp track of the includes
    src=[]              #Keep track of the stripped down source
    md=[['','']]
    hd=0
    nl=''
    mdh=True
    #print(ind+"Pass 1")
    for i in range(len(s)):
        #   #ifninclude   ;this includes the file if it hasn't been included yet
        if len(s[i])>0:
            t=s[i]
            if t.startswith(';;'):
                h=t[2:]
                if h.startswith("#"):
                    #Search for the matching header and store the index to hd
                    mdh=False
                    n=0
                    hd=0
                    while n<len(md) and hd==0:
                        if h==md[n][0]:
                            hd=n
                        n+=1
                    if n==len(md):
                        hd=n
                        md+=[[h,'']]
                else:
                    #just add it to the previous header
                    if nl!='' and mdh:
                        md[hd][1]+=nl+'\n'
                        mdh=False
                    md[hd][1]+=h+'\n'
            else:
                t=t.split(';')[0].rstrip()     #get rid of comments and trailing whitespace
                if len(t)>0:
                    if t.startswith(' ') or t.startswith('\t'):
                        src+=[t]
                    elif t.startswith('.') or t.startswith('#'):      #Check if the line is a compiler directive
                        if t[1:].lower().startswith("include"):
                            t=bp+t[8:].strip().strip('"').strip("'")
                            t0=t.split('/')
                            t1=''
                            for i in t0[0:-1]:
                              t1+=i+'/'
                            print(ind+t)
                            f=open(t,'r')
                            t=f.read()
                            f.close()
                            (sr,mkd,lbls,inc)=zapp(t,fin,ind+"  ",bp=t1)
                            src+=sr
                            md+=mkd
                            labels+=lbls
                            incs+=inc
                        else:
                            src+=[t]
                        #t=t[1:]
                        #if t.startswith()
                        #pass
                    else:
                        src+=[t]
                        if t.endswith(':'):
                            t=t[0:-1]
                        labels+=[t]
                        nl=t
                        mdh=True
    return (src,md,labels,incs)
s=sys.argv
if len(s)==1:
    print(help)
else:
    fin=s[1]
    t=fin.split('/')
    bp=''
    for i in t[0:-1]:
      bp+=i+'/'
    if len(s)==2:
        fout=fin.split('/')
        fout=fout[-1].split('.')
        t=fout[0]
        for i in fout[1:-1]:
            t+='.'+i
        fout=t+'.z80'
        md=t+'.md'
    else:
        fout=s[2]
        if len(s)==3:
          md=fout.split('/')
          md=md[-1].split('.')
          t=md[0]
          for i in md[1:-1]:
              t+='.'+i
          md=t+'.md'
        else:
          md=s[3]
    f=open(fin,'r')
    s=f.read()
    f.close()
    print(fin,fout,md)
    (s,mkd,lbls,inc)=zapp(s,fin,bp=bp)
    print("%d lines" % (len(s)))
    print("%d files" % (fc))
    f=open(fout,'w')
    for i in s:
        f.write(i+'\n')
    f.close()
    if md!='':
        s=docify(mkd)
        f=open(md,'w')
        f.write(s)
        f.close()
