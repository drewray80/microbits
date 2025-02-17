# Automatic Headlights Lesson

The goal of this activity is to have students program a microbit to detect the light level in the room, so that when the light level is low the RVR front lights turn white and the rear lights turn red.  

This activity combines the Sphero RVR and a microbit.  
We use the microbit python editor  https://python.microbit.org/v/3/   
But you should be able to do the same project with MakeCode using the Sphero RVR extension.  
 
I use this activity to allow students to practice using python modules and import statements with a hands on activity.  
I used the sphero SDK microbit python instructions to figure out how to add the sphero.py to the microbit python editor.  
https://github.com/sphero-inc/sphero-sdk-microbit-python  
https://sdk.sphero.com/microbit-setup/microbit-sdk  

We start the activity by opening a new microbit project in python.microbit.org editor.  
I give my students the sphero.py file in a Google Classroom assignment and have them download the file to their computer.  
They need to add sphero.py to the project.  It is import to Add the sphero.py file to the project and not over write the main.py.  
The instructions in the link below provide good step by step images for adding the file.  
https://sdk.sphero.com/microbit-setup/microbit-python-setup  

After we get the sphero.py file in the project, we look at the sphero.py, and discuss the code and what it is doing.  
We talk briefly about how object oriented stucture works.  

We find the function we are looking for to set the leds by rgb (set_rgb_led_by_index(index, red, green, blue)).  
We discuss what code we need to write into our microbit main.py to call that function, so we can control the led colors.  
Then we started trying to get one of the front headlights to change color.  

I have them code with me as we trouble shoot getting the code correct to call the function.  
I get them to the point that one of their RVR lights has changed color.  
I stop coding with them when we get to point that we have code like the headlight_starter.py

After that, I point out the Light Level section in the References of the editor and the read_light_level function.  
Then I let them work with a partner to figure out how to get the RVR to have automatic head lights. 

This activity provides students with a lot of opportunity to problem solve and trouble shoot.  
They learn about importing and using modules.  
The learn about the different ways to use an import statements and how that effects their code.  
(import sphero vs from sphero import RVRLed)
I have found that students do well with this activity with limited instructions. And they enjoy getting it to work.  
