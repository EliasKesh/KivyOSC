#!/usr/bin/python
#---------------------------------------------------------------------
#
#	File: 	main
#
#	Contains: 	
#
#
#	Written By: 	Elias Keshishoglou on Mon Feb 1 05:03:36 PM PST 2021
#
#	Copyright : 	2021 Elias Keshishoglou all rights reserved.
#
#
#---------------------------------------------------------------------#
import sys; 
# sys.stdout.encoding = None
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
# If we will not import this module 
# It will through the error 
from kivy.uix.slider import Slider 

from kivy.utils import platform
from kivy.uix.popup import Popup
import logging
from kivy.logger import Logger
from oscpy.client import OSCClient
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.clock import Clock

class YourApp(App):
    def build(self):
        global HoldValue
        global SliderValue
        global HoldController
        global ControllerValue

        Window.clearcolor = (0.45, 0, 0, 1);

        Logger.info('title: This is a info message.')
        Logger.critical("DEADBEEF = {}")

#        popup = Popup(title='Test popup',
#       content=Label(text=(MyString)))
#        popup.open() # show the popup

        root_widget = BoxLayout(orientation='horizontal')

        # Address of server to receive data
        address = "192.168.2.25"
        port = 15200

        # Testing: oscdump 8000
        osc = OSCClient(address, port)
        print ("osc Found ",osc)

        if platform == 'android':
            print ("android Found")

        if platform == 'linux':
            print ("Linux Found")

        button_symbols = ('1', '2', '3', '4',
                          '5', '6', '7', '8',
                          '9', '10','11', '12',
                          '13', '14', '15', '16')

        button_grid = GridLayout(rows=8, cols=4, size_hint_y=1)
        slider_grid = GridLayout(cols=8, size_hint_y=1, padding=[0,0,0,25])

        # Create the buttons and add them to the grid.
        for symbol in button_symbols:
            button_grid.add_widget(Button(text=symbol, background_normal='DarkDarkRedMarble.png'))
 
        # Set the call back.
        for button in button_grid.children[0:]:  # note use of the
            button.bind(on_press=print_button_text)
 #           print ("button")

        # Create the Sliders
        slider_grid.add_widget(Slider(min = 0, max = 127, value=0, step=5,orientation='vertical',background_vertical='DarkDarkRedMarble.png'))
        slider_grid.add_widget(Slider(min = 0, max = 127, value=0, step=5,orientation='vertical',background_vertical='DarkDarkRedMarble.png'))
        slider_grid.add_widget(Slider(min = 0, max = 127, value=0, step=1,orientation='vertical',background_vertical='DarkDarkRedMarble.png'))
        slider_grid.add_widget(Slider(min = 0, max = 127, value=0, step=1,orientation='vertical',background_vertical='DarkDarkRedMarble.png'))
        slider_grid.add_widget(Slider(min = 0, max = 127, value=0, step=1,orientation='vertical',background_vertical='DarkDarkRedMarble.png'))
        slider_grid.add_widget(Slider(min = 0, max = 127, value=0, step=1,orientation='vertical',background_vertical='DarkDarkRedMarble.png'))

        # Bind the sliders to the call back
        SlideNum=6;
        for slider in slider_grid.children[0:]: 
            slider.bind(value=print_slider_value)
            slider.number=SlideNum
            slider.add_widget(Label(text = str(SlideNum))) 
            Logger.info('slider: ' +  str(SlideNum))
            SlideNum=SlideNum-1
    
#        label_grid = GridLayout(cols=8, height=5, padding=[0,0,0,0])
        # label_grid.add_widget(Label(text="Master"))
        # label_grid.add_widget(Label(text="Slider 2"))
        # label_grid.add_widget(Label(text="Slider 3"))
        # label_grid.add_widget(Label(text="Slider 4"))
        # label_grid.add_widget(Label(text="Slider 5"))
        # label_grid.add_widget(Label(text="Slider 6"))

        def print_button_text(instance):
            osc.send_message(b"/midi", [b"button", int(instance.text) - 1, 1 ])
            Logger.info('Button: ' + instance.text)


        def print_slider_value(instance, value):
            global HoldValue
            global SliderValue
            global HoldController
            global ControllerValue
            SliderValue=int(value)
            ControllerValue=int(instance.number)


        def resize_label_text(label, new_height):
            label.font_size = 0.5*label.height

 #       root_widget.add_widget(label_grid)
        root_widget.add_widget(slider_grid)
        root_widget.add_widget(button_grid)



        def my_callback(dt):
            global HoldValue
            global SliderValue
            global HoldController
            global ControllerValue

            # Logger.info('my_callback: ' + 
            #     str(HoldValue) + ' ' +
            #     str(SliderValue) + ' ' +
            #     str(HoldController) + ' ' +
            #     str(ControllerValue) )

            if ( (SliderValue != 100) and
                (HoldValue == SliderValue) and 
                (HoldController == ControllerValue)):
                osc.send_message(b"/midi", [b"slider", ControllerValue, SliderValue ])

                SliderValue = 100
            else:
                HoldValue = SliderValue
                HoldController = ControllerValue    

        Clock.schedule_interval(my_callback, 0.35)

#        root_widget.add_widget(output_label)
 
        return root_widget



HoldValue=0
SliderValue=100
HoldController=100
ControllerValue=0
YourApp().run()
