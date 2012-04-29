#!/usr/bin/python
import time
 
# put Port 8 Pin 3 into mode 7 (GPIO)
open('/sys/kernel/debug/omap_mux/gpmc_ad6', 'wb').write("%X" % 7)
 
try:
   # check to see if the pin is already exported
   open('/sys/class/gpio/gpio38/direction').read()
except:
   # it isn't, so export it
#   print("exporting GPIO 38")
   open('/sys/class/gpio/export', 'w').write('38')
 
# set Port 8 Pin 3 for output
open('/sys/class/gpio/gpio38/direction', 'w').write('out')

var = open('value.txt', 'r').read(1)

v = int(var)
if v == 0:
   print ("turn on external LED")
   open('/sys/class/gpio/gpio38/value', 'w').write("1") 

if v == 1:
   # cleanup - remove GPIO38 folder from file system
   open('/sys/class/gpio/gpio38/value', 'w').write('0')

print ("program ended")
