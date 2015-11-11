#!/usr/bin/python

f = open('raid6-10.raw','r')
zone1 = ('1','2','3','4','5','6',
         '13','14','15','16','17','18',
         '25','26','27','28','29','30',
         '37','38','39','40','41','42',
         '49','50','51','52','53','54')

pds = []

pzones = []


curpool =''


for line in f:
  pd = line.split()
  encl = int(pd[0])
  pos = int(pd[1])
  pool = int( pd[9])

  if curpool !=pool:
    curpool = pool
    pzones.append( [0,0,0,0,0,0,0,0,0,0])
  if pd[1] in zone1:
    zone=1 
  else:
    zone=0  
  pzones[pool][(encl-1)*2+zone] +=1
                            

for zone in pzones:
 print(  zone)


'''
for zone in pzones:
 print( pzones[zone])


  pds.append( {'ENCL':pd[0],'POS':pd[1], 'POOL':pd[9]} )
npool = ''
for pd in pds:
    if npool != pd['POOL']:
        npool = pd['POOL']
        print ('\n\n')
    print ("POOL = %s ENCL= %s POS= %s" % (pd['POOL'],pd['ENCL'],pd['POS']))
'''

f.close()
