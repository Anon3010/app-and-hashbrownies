@echo off
color 0a
title "emergency kit"
@echo on
ipconfig /flushdns
start 192.168.178.1
pause
echo use this only if you have no other choice!!
pause
ipconfig /renew
pause 
