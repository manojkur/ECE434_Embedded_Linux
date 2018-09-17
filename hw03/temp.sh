#!/bin/sh
temp=`i2cget -y 2 0x49`
temp=$(($temp*1))
temp2=$(($temp*2+32))
echo "Celcius: " $temp
echo "Farhenheit :" $temp2

