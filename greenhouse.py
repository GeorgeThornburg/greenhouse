#import board
#import adafruit_scd30
from time import sleep
from tkinter import *
#import RPi.GPIO as GPIO
import time
import requests
import random, time
import math
import json
import base64
#from picamera import PiCamera
from time import sleep
#i2c = board.I2C()
#scd = adafruit_scd30.SCD30(i2c)
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(19, GPIO.OUT)
#GPIO.setup(18, GPIO.OUT)
#GPIO.setup(23, GPIO.OUT)



root = Tk()
root.title("Green House")
root.geometry('370x500')
def raise_frame(frame):
	frame.tkraise()

f1 = Frame(root) #Main Menu
f2 = Frame(root) #Set Grow Light Hours
f3 = Frame(root) #Set CO2 Limits
f4 = Frame(root) #Set Black Light Hours
f5 = Frame(root) #Set Temperature Limits
f6 = Frame(root) #Set Fresh Air Time
f7 = Frame(root) #Set Humidity Limits
f8 = Frame(root) #Set Water Moisture

for frame in (f1, f2, f3, f4, f5, f6, f7, f8):
	frame.grid(row=0, column=0, sticky='news')

#######SETTINGS#######

powerButtonHeight = 1
powerButtonWidth = 20
customSliderLength = 10
customLength = 25
setButtonWidth = 2
setButtonHeight = 1
indicatorWidth = 9
indicatorHeight = 1
labelWidth = 45
labelHeight = 0
labelBackGroundColor = "green"
farRightLableWidth = 11
farRightHeight = 1


def mainPage():
	#################### Retrieving DATA from Server ###########################
	url = 'http://*.**.***.*.*/parse/classes/Greenhouse/'

	headers = {
	'X-Parse-Application-Id': '*****',
	'Content-Type': 'application/json',
	}
	#r = requests.get(url, headers=headers)
	#t = r.json()	
	#serverIndex = t.get("index")

	#serverLightOnOff = t.get("lightOnOff")
	#serverTempOnOff = t.get("tempOnOff")
	#serverBLightOnOff = t.get("blightOnOff")
	#serverHumidOnOff = t.get("humidOnOff")
	#serverFAOnOff = t.get ("faOnOff")
	#serverCO2OnOff = t.get("co2OnOff")
	#serverSMOnOff = t.get("smOnOff")



	#serverSetTemp = t.get("setTemp")

	#if serverIndex == 2:
	#	HEAT = onButtonHeat.set(serverTempOnOff)
	#	GL = onButtonGrowLight.set(serverLightOnOff)
	#	Temp = setTempOn.set(serverSetTemp)
	

	##########################################################################

	#i2c = board.I2C()
	#scd = adafruit_scd30.SCD30(i2c)
	actualHumidity = 56#scd.relative_humidity
	actualTemperature = 27#scd.temperature
	#actualCO2 = scd.eCO2
	#actualSM =
	hour = time.strftime("%H")
	min = time.strftime("%M")
	sec = time.strftime("%S")
	gtime = "Current Time: " + hour + ":" + min + ":" + sec
	tminus.config(text = gtime)
	
	
	GL = onButtonGrowLight.get()
	CO2 = onButtonCO2.get()
	BL = onButtonBlackLight.get()
	HEAT = onButtonHeat.get()
	FA = onButtonFreshAir.get()
	HUM = onButtonHumidity.get()
	SM = onButtonWater.get()
	GLON = setGrowLightOn.get()
	GLOFF = setGrowLightOff.get()
	CO2 = onButtonCO2.get()
	BLON = setBlackLightOn.get()
	BLOFF = setBlackLightOff.get()
	gCO2 = setCO2Scale.get()
	Temp = setTempOn.get()
	FAHOURS = setFreshAirOnHours.get()
	FASECS = setFreshAirOnSecs.get()
	FAMUSHROOMS = setFreshAirMushrooms.get()
	WATER = setWaterScale.get()
	HUMIDITY = setHumidityScale.get()

	#################### Grow Light Set Up #############


	if GL == 0:
		#GPIO.output(18, GPIO.LOW)
		onButtonGrowLight.config(background = 'red')
		growLightLabelOn.config(text = "Power Off")
			
	if GL == 1:
		onButtonGrowLight.config(background = 'green')
		if GLON < GLOFF:
			if int(hour) > GLON and int(hour) < GLOFF:
				#GPIO.output(18, GPIO.HIGH)
				growLightLabelOn.config(text = "Currently On")
					
			else:
				#GPIO.output(18, GPIO.LOW)
				growLightLabelOn.config(text = "Currently Off")
					
		if GLON > GLOFF:
			if int(hour) > GLON or int(hour) < GLOFF:
				#GPIO.output(18, GPIO.HIGH)
				growLightLabelOn.config(text = "Currently On")
					
			else:
				#GPIO.output(18, GPIO.LOW)
				growLightLabelOn.config(text = "Currently Off")
					

	currentGrowLightButtonOn.config(text = "On " + str(GLON))
	k2currentGrowLightButtonOn.config(text = "Off " + str(GLOFF))
	serverIndex = 1

	#################### CO2 Set Up ###################
	if CO2 == 0:
		onButtonCO2.config(background = 'red')
		co2LabelOn.config(text = "Power Off")
		
	if CO2 ==1:
		onButtonCO2.config(background = 'green')
		co2LabelOn.config(text = "Currently Off")

	currentCO2ButtonOn.config(text = "CO2 Limit")
	k2currentCO2ButtonOn.config(text = str(gCO2) + " BPM")
	
	#################### Black Light Set Up ############
	if BL == 0:
		#GPIO.output(23, GPIO.LOW)
		onButtonBlackLight.config(background = 'red')
		blackLightLabelOn.config(text = "Power Off")
		
	if BL == 1:
		onButtonBlackLight.config(background = 'green')
		if BLON < BLOFF:
			if int(hour) > BLON and int(hour) < BLOFF:
				#GPIO.output(23, GPIO.HIGH)
				blackLightLabelOn.config(text = "Currently On")
				
			else:
				#GPIO.output(23, GPIO.LOW)
				blackLightLabelOn.config(text = "Currently Off")
				
		if BLON > BLOFF:
			if int(hour) > BLON or int(hour) < BLOFF:
				#GPIO.output(23, GPIO.HIGH)
				blackLightLabelOn.config(text = "Currently On")
			else:
				#GPIO.output(23, GPIO.LOW)
				blackLightLabelOn.config(text = "Currently Off")
				

	currentBlackLightButtonOn.config(text = "On " + str(BLON))
	k2currentBlackLightButtonOn.config(text = "Off " + str(BLOFF))
	

	#################### Temperature Set Up ############
	
	if HEAT == 0:
		#GPIO.output(19, GPIO.LOW)
		onButtonHeat.config(background = 'red')
		heatLightLabelOn.config(text = "Power Off")
		
	if actualTemperature != None:
		convertedTemperature = (actualTemperature - 32) / 1.8
		print(actualTemperature)
		convertedTemperature = actualTemperature *(9/5) + 32
		xconvertedTemperature = int(convertedTemperature)
		print(xconvertedTemperature)

		if HEAT == 1:
			onButtonHeat.config(background = 'green')
			if xconvertedTemperature > Temp:
				#GPIO.output(19, GPIO.LOW)
				heatLightLabelOn.config(text = str(xconvertedTemperature) + "F")
			else:
				#GPIO.output(19, GPIO.HIGH)
				heatLightLabelOn.config(text = str(xconvertedTemperature) + "F")

	else:
		print("Sensor Failure")
	currentHeatLightButtonOn.config(text = "Temp Set")
	k2currentHeatLightButtonOn.config(text = str(Temp) + "F")
	
	#################### Fresh Air Set Up ##############
	if FA == 0:
		onButtonFreshAir.config(background = 'red')
		freshAirLabelOn.config(text = "Power Off")
		


	if FA == 1:
		onButtonFreshAir.config(background = 'green')
		freshAirLabelOn.config(text = "Currently Off")
		
		if FAHOURS == 1 and FASECS >= int(sec) and int(min) == 0:
			print("every hour")		
		if FAHOURS == 2 and int(hour) % 2 == 0 and FASECS >= int(sec) and int(min) == 0:
			print("every 2 hours")
		if FAHOURS == 3 and int(hour) % 3 == 0 and FASECS >= int(sec) and int(min) == 0:
			print("every 3 hours")
		if FAHOURS == 4 and int(hour) % 4 == 0 and FASECS >= int(sec) and int(min) == 0:
			print("every 4 hours")
		if FAHOURS == 6 and int(hour) % 6 == 0 and FASECS >= int(sec) and int(min) == 0:
			print("every 6 hours")
		if FAHOURS == 8 and int(hour) % 8 == 0 and FASECS >= int(sec) and int(min) == 0:
			print("every 8 hours")
		if FAHOURS == 12 and int(hour) % 12 == 0 and FASECS >= int(sec) and int(min) == 0:
			print("every 12 hours")
		if FAHOURS == 0 and FASECS >= int(sec) and int(min) == 0:
			print("every 24 hours")
	currentFreshAirButtonOn.config(text = "Every " + str(FAHOURS) + " hours")	
	k2currentFreshAirButtonOn.config(text = "For " + str(FASECS) + " Seconds")
	
	#################### Humidity Set Up ###############
	if HUM == 0:
		onButtonHumidity.config(background = 'red')
		humidityLabelOn.config(text = "Power Off")
	if HUM == 1:
		onButtonHumidity.config(background = 'green')
		humidityLabelOn.config(text = "Power On")
	
	currentHumidityButtonOn.config(text = "Humidity SET")
	k2currentHumidityButtonOn.config(text = str(HUMIDITY) + "%")
	
	#################### Moisture Level Set Up #########
	if SM == 0:
		onButtonWater.config(background = 'red')
		waterLabelOn.config(text = "Power Off")
		
	if SM == 1:
		onButtonWater.config(background = 'green')
		waterLabelOn.config(text = "Power On")

	currentWaterButtonOn.config (text = "Moisture Level")
	k2currentWaterButtonOn.config (text = str(WATER) + "%")

	######################### PI CAMERA #####################
	#camera.start_preview()
    #camera.rotation = 180
    #sleep(2)
    
    #camera.capture('/home/pi/Desktop/image.jpg')
    #camera.stop_preview()
    #with open('/home/pi/Desktop/image.jpg', 'rb') as binary_file:
    #    binary_file_data = binary_file.read()
    #    base64_encoded_data = base64.b64encode(binary_file_data)
    #    base64_message = base64_encoded_data.decode('utf-8')

	####################### SENDING DATA TO SERVER ################################	
 

	tminus.after(5000, mainPage)
		
###################### Grow Light Set Up #################################################
onButtonGrowLight = Scale(f1, background = 'red', width = powerButtonWidth, from_=0, to=1, sliderlength = customSliderLength, length = customLength)
onButtonGrowLight.set(0)
onButtonGrowLight.grid(row=1, column=0, rowspan = 2)

growLightLabelOn = Label(f1, text = "Currently On", width = indicatorWidth, height = indicatorHeight)
growLightLabelOn.grid(row=1, column=1, rowspan = 2)


growLightLabelOn = Label(f1, text = "Power Off", width = indicatorWidth, height = indicatorHeight)
growLightLabelOn.grid(row=1, column=1, rowspan = 2)


growLightLabel = Label(f1, text = "Grow Light", width = labelWidth, height = labelHeight, background = labelBackGroundColor)
growLightLabel.grid(row = 0, column = 0, columnspan = 4)

setGrowLightButtonOn = Button(f1, text = "SET", width = setButtonWidth, height = setButtonHeight, command=lambda:raise_frame(f2))
setGrowLightButtonOn.grid(row=1, column=2, rowspan = 2)

setGrowLightLabel = Label(f2, text = "Grow Light")
setGrowLightLabel.grid(row = 0, column=0, columnspan = 2)

setGrowLightOn = Scale(f2, from_=0, to=24, length=300, tickinterval=1)
setGrowLightOn.set(8)
setGrowLightOn.grid(row=1, column=0)

setGrowLightOff = Scale(f2, from_=0, to=24, length=300, tickinterval=1)
setGrowLightOff.set(16)
setGrowLightOff.grid(row=1, column=1)

currentGrowLightButtonOn = Label(f1, text = "On ", width = farRightLableWidth, height = farRightHeight)
currentGrowLightButtonOn.grid(row=1, column=3)
k2currentGrowLightButtonOn = Label(f1, text = "Off ", width = farRightLableWidth, height = farRightHeight)
k2currentGrowLightButtonOn.grid(row=2, column=3)

backButton = Button(f2, text="Back", width = 15, command=lambda:raise_frame(f1))
backButton.grid(row=3, column=0, columnspan = 5)

#################### CO2 Set Up #############################################################

onButtonCO2 = Scale(f1, background = 'red', width = powerButtonWidth, from_=0, to=1, sliderlength = customSliderLength, length = customLength)
onButtonCO2.set(0)
onButtonCO2.grid(row=4, column=0, rowspan = 2)

co2LabelOn = Label(f1, text = "Power Off", width = indicatorWidth, height = indicatorHeight)
co2LabelOn.grid(row=4, column=1, rowspan = 2)

co2Label = Label(f1, text = "CO2", width = labelWidth, height = labelHeight, background = labelBackGroundColor)
co2Label.grid(row = 3, column = 0, columnspan = 4)

setCO2ButtonOn = Button(f1, text = "SET", width = setButtonWidth, height = setButtonHeight, command=lambda:raise_frame(f3))
setCO2ButtonOn.grid(row=4, column=2, rowspan = 2)

setCO2Label = Label(f3, text = "Set CO2 Level")
setCO2Label.grid(row = 0, column=0, columnspan = 5)

setCO2Scale = Scale(f3, from_=0, to=1600, length=300, tickinterval=100)
setCO2Scale.set(0)
setCO2Scale.grid(row=1, column=0, columnspan =5)

currentCO2ButtonOn = Label(f1, text = "CO2 Limit", width = farRightLableWidth, height = farRightHeight)
currentCO2ButtonOn.grid(row=4, column=3)
k2currentCO2ButtonOn = Label(f1, text = " BPM", width = farRightLableWidth, height = farRightHeight)
k2currentCO2ButtonOn.grid(row=5, column=3)

backButton = Button(f3, text="Back", width = 20, height = 1, bg = "yellow", command=lambda:raise_frame(f1))
backButton.grid(row=2, column=0, columnspan = 5)

########################## Black Light #######################################

onButtonBlackLight = Scale(f1, background = 'red', width = powerButtonWidth, from_=0, to=1, sliderlength = customSliderLength, length = customLength)
onButtonBlackLight.set(0)
onButtonBlackLight.grid(row=7, column=0, rowspan = 2)

blackLightLabelOn = Label(f1, text = "Power Off", width = indicatorWidth, height = indicatorHeight)
blackLightLabelOn.grid(row=7, column=1, rowspan = 2)


growBlackLightLabel = Label(f1, text = "Black Light", width = labelWidth, height = labelHeight, background = labelBackGroundColor)
growBlackLightLabel.grid(row = 6, column = 0, columnspan = 4)

blackLightLabelOn = Label(f1, text = "Currently Off", width = indicatorWidth, height = indicatorHeight)
blackLightLabelOn.grid(row=7, column=1, rowspan = 2)

setBlackLightButtonOn = Button(f1, text = "SET", width = setButtonWidth, height = setButtonHeight, command=lambda:raise_frame(f4))
setBlackLightButtonOn.grid(row=7, column=2, rowspan = 2)

setBlackLightLabel = Label(f4, text = "Black Light")
setBlackLightLabel.grid(row = 0, column=0, columnspan = 2)

setBlackLightOn = Scale(f4, from_=0, to=24, length=300, tickinterval=1)
setBlackLightOn.set(8)
setBlackLightOn.grid(row=1, column=0)

setBlackLightOff = Scale(f4, from_=0, to=24, length=300, tickinterval=1)
setBlackLightOff.set(16)
setBlackLightOff.grid(row=1, column=1)

currentBlackLightButtonOn = Label(f1, text = "On ", width = farRightLableWidth, height = farRightHeight)
currentBlackLightButtonOn.grid(row=7, column=3)
k2currentBlackLightButtonOn = Label(f1, text = "Off ", width = farRightLableWidth, height = farRightHeight)
k2currentBlackLightButtonOn.grid(row=8, column=3)

backButton = Button(f4, text="Back", width = 20, height = 1, bg = "yellow", command=lambda:raise_frame(f1))
backButton.grid(row=2, column=0, columnspan = 5)

####################### HEAT/TEMPERATURE #####################################

onButtonHeat = Scale(f1, background = 'red', width = powerButtonWidth, from_=0, to=1, sliderlength = customSliderLength, length = customLength)
onButtonHeat.set(0)
onButtonHeat.grid(row=10, column=0, rowspan = 2)

heatLightLabelOn = Label(f1, text = "Power Off", width = indicatorWidth, height = indicatorHeight)
heatLightLabelOn.grid(row=10, column=1, rowspan = 2)


growHeat = Label(f1, text = "Temperature", width = labelWidth, height = labelHeight, background = labelBackGroundColor)
growHeat.grid(row = 9, column = 0, columnspan = 4)

setHeatLightButtonOn = Button(f1, text = "SET", width = setButtonWidth, height = setButtonHeight, command=lambda:raise_frame(f5))
setHeatLightButtonOn.grid(row=10, column=2, rowspan = 2)

currentHeatLightButtonOn = Label(f1)
currentHeatLightButtonOn.grid(row=10, column=3)

setTempLabel = Label(f5, text = "Set Temperature Level")
setTempLabel.grid(row = 0, column=0, columnspan = 2)

setTempOn = Scale(f5, from_=50, to=100, length=300, tickinterval=1)
setTempOn.set(8)
setTempOn.grid(row=1, column=0)

currentHeatLightButtonOn = Label(f1, text = "Temp Set", width = farRightLableWidth, height = farRightHeight)
currentHeatLightButtonOn.grid(row=10, column=3)
k2currentHeatLightButtonOn = Label(f1, text = "F", width = farRightLableWidth, height = farRightHeight)
k2currentHeatLightButtonOn.grid(row=11, column=3)

backButton = Button(f5, text="Back", width = 20, height = 1, bg = "yellow", command=lambda:raise_frame(f1))
backButton.grid(row=2, column=0, columnspan = 5)
######################## Fresh Air ############################################

onButtonFreshAir = Scale(f1, background = 'red', width = powerButtonWidth, from_=0, to=1, sliderlength = customSliderLength, length = customLength)
onButtonFreshAir.set(0)
onButtonFreshAir.grid(row=13, column=0, rowspan = 2)

freshAirLabelOn = Label(f1, text = "Power Off", width = indicatorWidth, height = indicatorHeight)
freshAirLabelOn.grid(row=13, column=1, rowspan = 2)


growFreshAir = Label(f1, text = "Fresh Air", width = labelWidth, height = labelHeight, background = labelBackGroundColor)
growFreshAir.grid(row = 12, column = 0, columnspan = 4)

setFreshAirButtonOn = Button(f1, text = "SET", width = setButtonWidth, height = setButtonHeight, command=lambda:raise_frame(f6))
setFreshAirButtonOn.grid(row=13, column=2, rowspan = 2)

setFreshAirMushroomsLabel = Label(f6, text = "CO2 Controlled\nFan for Mushrooms", background = 'red')
setFreshAirMushroomsLabel.grid(row = 0, column=0, columnspan = 1)

setFreshAirHoursLabel = Label(f6, text = "How Often Bring\nFresh Air\n (Every x Hour)", background = 'green')
setFreshAirHoursLabel.grid(row = 0, column=1, columnspan = 1)

setFreshAirSecsLabel = Label(f6, text = "How Many Seconds\ndo you want Fan On", background = 'green')
setFreshAirSecsLabel.grid(row = 0, column=2, columnspan = 1)

setFreshAirMushrooms = Scale(f6, from_=0, to=1, length=300, tickinterval=1, background = 'red')
setFreshAirMushrooms.set(0)
setFreshAirMushrooms.grid(row=1, column=0, rowspan = 1)

setFreshAirOnHours = Scale(f6, from_=0, to=24, length=300, tickinterval=1, background = 'green')
setFreshAirOnHours.set(0)
setFreshAirOnHours.grid(row=1, column=1)

setFreshAirOnSecs = Scale(f6, from_=0, to=60, length=300, tickinterval=1, background = 'green')
setFreshAirOnSecs.set(0)
setFreshAirOnSecs.grid(row=1, column=2)

currentFreshAirButtonOn = Label(f1, text = "Every  hours", width = farRightLableWidth, height = farRightHeight)
currentFreshAirButtonOn.grid(row=13, column=3)
k2currentFreshAirButtonOn = Label(f1, text = "For  Seconds", width = farRightLableWidth, height = farRightHeight)
k2currentFreshAirButtonOn.grid(row=14, column=3)

backButton = Button(f6, text="Back", width = 20, height = 1, bg = "yellow", command=lambda:raise_frame(f1))
backButton.grid(row=2, column=0, columnspan = 5)

#######################  Humidity ############################################

onButtonHumidity = Scale(f1, background = 'red', width = powerButtonWidth, from_=0, to=1, sliderlength = customSliderLength, length = customLength)
onButtonHumidity.set(0)
onButtonHumidity.grid(row=16, column=0, rowspan = 2)

humidityLabelOn = Label(f1, text = "Power Off", width = indicatorWidth, height = indicatorHeight)
humidityLabelOn.grid(row=16, column=1, rowspan = 2)

growHumidity = Label(f1, text = "Humidity", width = labelWidth, height = labelHeight, background = labelBackGroundColor)
growHumidity.grid(row = 15, column = 0, columnspan = 4)

setHumidityButtonOn = Button(f1, text = "SET", width = setButtonWidth, height = setButtonHeight, command=lambda:raise_frame(f7))
setHumidityButtonOn.grid(row=16, column=2, rowspan = 2)

setHumidityLabel = Label(f7, text = "Set Humidity Level")
setHumidityLabel.grid(row = 0, column=0, columnspan = 2)

setHumidityScale = Scale(f7, from_=0, to=100, length=300, tickinterval=1)
setHumidityScale.set(0)
setHumidityScale.grid(row=1, column=0)

currentHumidityButtonOn = Label(f1, text = "Humidity SET", width = farRightLableWidth, height = farRightHeight)
currentHumidityButtonOn.grid(row=16, column=3)
k2currentHumidityButtonOn = Label(f1, text = "%", width = farRightLableWidth, height = farRightHeight)
k2currentHumidityButtonOn.grid(row=17, column=3)

backButton = Button(f7, text="Back", width = 20, height = 1, bg = "yellow", command=lambda:raise_frame(f1))
backButton.grid(row=2, column=0, columnspan = 5)

###################### Soil Moisture ##########################################

onButtonWater = Scale(f1, background = 'red', width = powerButtonWidth, from_=0, to=1, sliderlength = customSliderLength, length = customLength)
onButtonWater.set(0)
onButtonWater.grid(row=19, column=0, rowspan = 2)

waterLabelOn = Label(f1, text = "Power Off", width = indicatorWidth, height = indicatorHeight)
waterLabelOn.grid(row=19, column=1, rowspan = 2)


growWater = Label(f1, text = "Soil Moisture", width = labelWidth, height = labelHeight, background = labelBackGroundColor)
growWater.grid(row = 18, column = 0, columnspan = 4)

setWaterButtonOn = Button(f1, text = "SET", width = setButtonWidth, height = setButtonHeight, command=lambda:raise_frame(f8))
setWaterButtonOn.grid(row=19, column=2, rowspan = 2)

setWaterLabel = Label(f8, text = "Set Soil Moisture Level")
setWaterLabel.grid(row = 0, column=0, columnspan = 2)

setWaterScale = Scale(f8, from_=0, to=100, length=300, tickinterval=1)
setWaterScale.set(0)
setWaterScale.grid(row=1, column=0)

currentWaterButtonOn = Label(f1, text = "Moisture Level", width = farRightLableWidth, height = farRightHeight)
currentWaterButtonOn.grid(row=19, column=3)
k2currentWaterButtonOn = Label(f1, text = "%", width = farRightLableWidth, height = farRightHeight)
k2currentWaterButtonOn.grid(row=20, column=3)

backButton = Button(f8, text="Back", width = 20, height = 1, bg = "yellow", command=lambda:raise_frame(f1))
backButton.grid(row=2, column=0, columnspan = 5)

tminus = Label(f1, text = " ", pady = 10)
tminus.grid(row = 21, column = 0, columnspan = 4)


mainPage()
raise_frame(f1)
root.mainloop()