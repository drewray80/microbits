# Battery Tester Lesson

I separate this lesson into 2 parts:
- Battery Tester: variables, math equations, inputs  
- If Battery Tester: adding conditionals to the previous activity

Materials: partners work well with this, or individual  
- microbits
- alligator clips
- bag of AA or AAA batteries or some of each (some dead and some good) 

## Battery Tester  
I basically follow this activity:  
https://makecode.microbit.org/courses/ucp-science/electricity  
This link has very helpful step by step explanations for the teacher, and helped me understand so I could lead discussions by asking leading questions.  
https://docs.google.com/document/d/15Xry9jFsIzHHG7RpaIomLodl9pBjTiKDvtjkd227b7Y/edit?tab=t.0#heading=h.psmccwuvnuvx  

- We start by discussing what we will doing. Testing voltage to see if a battery is good. I explain that batteries still have volt even if they are dead. We say that less than 1.25 volts is dead.  
- We talk about the GPIO pins and connect our alligator clips. This allows for a discussion about GPIO, electricity, ground...    
- Then we jump in an start testing and problem solving. We create a on_button_A pressed block with a show number block inside. We insert analog_read_pin P0 into the show number.
- This will read out will give us a number that is way too large. This sets up a discussion about voltage, and what the GPIO pins is actually collecting.
- This challenge leads us to have a need to create a variable, so we can add and equation to the code.
- Once we get our equation and output working correctly, we test several batteries.

## If Battery Tester  
When we start our unit on conditionals, we come back to this project to improve our battery tester.  
I start by asking students if they remember the voltage limit between a good and bad battery.  
And I ask them if they want to need to remember that number to be able to test a simple battery.  

We usually do this after I have introduced conditionals, so I usually just let them figure out what to do.  
This gives them time to come up with an original solution. Students often like coming up the funny ways to show a bad battery.  
I also walk around and help students by asking leading questions.  
![image](if_battery_tester.png)
