#!/usr/bin/python
import sys


# Todo #0 - formatting and description in Output
# Todo #1 - add reading from Console txt file, i mean auto search of PD tables and printing statistics
# TODO #2 - add statistics according to different disk TYPEs
# todo #4  merge with 3 previous todos


def main():
  if len(sys.argv)<2:
    print(' No Filename in parameters.')
    sys.exit(1)
  
  try:
    f = open(sys.argv[1],'r')
  except IOError:
    sys.stderr.write('Error opening file: ' + sys.argv[1])
    sys.exit(1)

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
      pzones.append( [0,0,0,0,0,0,0,0,0,0,'This row for Pool-%d' % (pool)])

    if pd[1] in zone1:
      zone=1 
    else:
      zone=0  

    pzones[pool][(encl-1)*2+zone] +=1

  print ( "Statistics for disk distribution in Zones: ") 
  for zone in pzones:
   print(  zone)

  f.close()

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
  main()
  sys.exit(0)


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


