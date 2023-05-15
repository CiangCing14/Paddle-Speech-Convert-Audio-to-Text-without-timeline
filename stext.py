import json,os,time
n=0
while True:
    for a in os.walk('texts'):
        a[2].sort(reverse=True)
        for b in a[2]:
            f=open('%s/%s'%(a[0],b),'r');t=json.loads(f.read());f.close
            f=open('stexts/%s'%b,'w+');f.write('\n'.join(t));f.close()
    n+=1
    print('循环已进行到第%d次……'%n)
    time.sleep(10)
