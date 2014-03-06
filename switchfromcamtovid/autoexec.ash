######################################################
#  Take a photo burst, switch to video for 9s, off   #
#             http://cam-do.com/SOBM                 #
######################################################

sleep 3
t app appmode photo
sleep 2
t app button shutter PR
sleep 5
t app appmode video
sleep 2
t app button shutter PR
sleep 9
t app button shutter PR
sleep 5
poweroff yes
reboot yes

