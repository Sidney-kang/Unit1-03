#Created by : Sidney Kang
#Created on : 21 Sept. 2017
#Created for : ICS3UR
# Daily Assignment - Unit1-03
# This program displays the area and perimeter ofa rectangle, but this time user can input value of length and width

import ui

def calculate_button_touch_up_inside(sender):
	  #This calculates area and perimeter  

    #input
    length = int(view['length_textbox'].text)
    width = int(view['width_textbox'].text)

    #process
    area = length*width
    perimeter = 2*(length + width)

    #output
    view['area_label'].text = "Area = "+str(area)+" units"
    view['perimeter_label'].text = "Perimeter = "+str(perimeter)+" units^2"

view = ui.load_view()
view.present('full_screen')
