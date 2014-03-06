######################################################
#  Take a photo, switch to video for 20s, and loop   #
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
sleep 20
t app button shutter PR
sleep 20
d:\autoexec.ash
REBOOT yes

