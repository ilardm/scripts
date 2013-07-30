#!/usr/bin/python

f=open('/proc/eee/temperature', 'r')
t=f.next()
t=t.replace('\n','')
f.close()

f=open('/proc/eee/fan_rpm', 'r')
fr=f.next()
fr=fr.replace('\n','')
f.close()

f=open('/proc/eee/fan_speed', 'r')
fs=f.next()
fs=fs.replace('\n','')
f.close()

print "%s C | %s rpm | %s/100"%(t,fr,fs)
