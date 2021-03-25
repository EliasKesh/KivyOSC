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


class YourApp(App):
    def build(self):

 #       Logger.info('DEADBEEF: This is a info message.')
        Logger.critical("DEADBEEF = {}")

        Logger.debug (" ***  DEADBEEF *** ")
#        print("****************")
#        print(MyString)
  #      log.debug (MyString)

#        popup = Popup(title='Test popup',
#       content=Label(text=(MyString)))

#        popup.open() # show the popup
        root_widget = BoxLayout(orientation='vertical')

#        MyString="Elias"
#        output_label = Label(text=MyString)

#        address = "127.0.0.1"
        address = "192.168.2.25"
        port = 8000

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


        button_grid = GridLayout(cols=4, size_hint_y=2)
        slider_grid = GridLayout(cols=8, size_hint_y=1, padding=[0,0,0,25])
        label_grid = GridLayout(cols=8, height=5, padding=[0,0,0,0])

        for symbol in button_symbols:
            button_grid.add_widget(Button(text=symbol))

        slider_grid.add_widget(Slider(min = 0, max = 127, value=0, step=1,orientation='vertical'))
        slider_grid.add_widget(Slider(min = 0, max = 127, value=0, step=1,orientation='vertical'))
        slider_grid.add_widget(Slider(min = 0, max = 127, value=0, step=1,orientation='vertical'))
        slider_grid.add_widget(Slider(min = 0, max = 127, value=0, step=1,orientation='vertical'))
        slider_grid.add_widget(Slider(min = 0, max = 127, value=0, step=1,orientation='vertical'))
        slider_grid.add_widget(Slider(min = 0, max = 127, value=0, step=1,orientation='vertical'))
    
        label_grid.add_widget(Label(text="Master"))
        label_grid.add_widget(Label(text="Slider 2"))
        label_grid.add_widget(Label(text="Slider 3"))
        label_grid.add_widget(Label(text="Slider 4"))
        label_grid.add_widget(Label(text="Slider 5"))
        label_grid.add_widget(Label(text="Slider 6"))

        def print_button_text(instance):
            osc.send_message(b"/Button", [b"hello", int(instance.text), 1 ])
#            osc.send_message('/filter',int(instance.text))

        for button in button_grid.children[1:]:  # note use of the
            button.bind(on_press=print_button_text)
 #           print ("button")

        def print_slider_value(instance, value):
            osc.send_message(b"/Slider", [b"hello", int(instance.number), int(value) ])

        SlideNum=8;
        for slider in slider_grid.children[0:]: 
            slider.bind(value=print_slider_value)
            slider.number=SlideNum
            slider.add_widget(Label(text = str(SlideNum))) 
            SlideNum=SlideNum-1
#            print ("Slider")

        def resize_label_text(label, new_height):
            label.font_size = 0.5*label.height

        root_widget.add_widget(label_grid)
        root_widget.add_widget(slider_grid)
        root_widget.add_widget(button_grid)


#        root_widget.add_widget(output_label)
 
        return root_widget


YourApp().run()
