from plyer import notification                 #To get notification on the screen
from tkinter import *
from tkinter.ttk import *
import datetime                                 #to get the date and time
import platform
import winsound                                   #for windows  #for determining Operating System for Beep
type='windows'

window = Tk()
window.title("Clock")                             #giving title as clock
window.geometry('600x250')                         #dimension of clock
timer_counter_num = 66600
timer_running = False
def clock():
        date_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S/%p")                 #make a clock function that controls the Time and Date Labels
        date,time1 = date_time.split()
        time2,time3 = time1.split('/')
        hour,minutes,seconds =  time2.split(':')                                                #split the given input
        if int(hour) > 11 and int(hour) < 24:
                time = str(int(hour)) + ':' + minutes + ':' + seconds                              #printing time as in 24 hours clock
        else:
                time = time2  
        time_label.config(text = time)
        date_label.config(text= date)
        time_label.after(1000, clock)
def alarm():
        main_time = datetime.datetime.now().strftime("%H:%M")                          #make a alarm function that controls the Time and Date Labels
        alarm_time = get_alarm_time_entry.get()
        alarm_time1= alarm_time
        alarm_hour, alarm_minutes = alarm_time1.split(':')                               #split the given input
        main_time1= main_time 
        main_hour1, main_minutes = main_time1.split(':')
        main_hour = str(int(main_hour1))                                                 #taking time as 24 hours clock
        main_hour = main_hour1
        if int(alarm_hour) == int(main_hour) and int(alarm_minutes) == int(main_minutes):              #To  check when the given time is equal to actual time
                for i in range(3):
                        alarm_status_label.config(text='Time Is Up')                                     #To print Time is up
                        if platform.system() == 'Windows':                                                #To give a beep sound
                                winsound.Beep(5000,1000)
                get_alarm_time_entry.config(state='enabled')                                              #to enable the button
                set_alarm_button.config(state='enabled')
                get_alarm_time_entry.delete(0,END)                                                          #to delete the given input
                alarm_status_label.config(text = '')
        else:
                alarm_status_label.config(text='Alarm Has Started')                                          #to print Alarm has started
                get_alarm_time_entry.config(state='disabled')
                set_alarm_button.config(state='disabled')                                                    #to disable the button after clicking the button
        alarm_status_label.after(1000, alarm)

def remainder():
        main_time = datetime.datetime.now().strftime("%H:%M ")                                   #make a remainder function that controls the Time and Date Labels
        remainder_time = get_remainder_time_entry.get()
        title = get_remainder_time_entry1.get()
        message = get_remainder_time_entry2.get()
        remainder_time1 = remainder_time
        remainder_hour, remainder_minutes = remainder_time1.split(':')                              #to split the input by ':'
        main_time1 = main_time
        main_hour1, main_minutes = main_time1.split(':')
        
        main_hour = str(int(main_hour1))                                                           #taking time as 24 hours clock
        main_hour = main_hour1
        if int(remainder_hour) == int(main_hour) and int(remainder_minutes) == int(main_minutes):        #To  check when the given time is equal to actual time
                notification.notify(                                                                     # To get the notification on the screen
                title = title,                                                                           #To get the title as input
                message = message,                                                                       #To get the message as input     
                app_icon=None,  
                timeout=20,  # seconds
                )
                for i in range(3):
                        remainder_status_label.config(text='Time Is Up')                                  #To print Time is up
                        if platform.system() == 'Windows':
                                winsound.Beep(5000,1000)                                                      #To get the beep sound
                        
                get_remainder_time_entry.config(state='enabled')                                             #to enable the button
                set_remainder_button.config(state='enabled')
                get_remainder_time_entry.delete(0,END)
                get_remainder_time_entry1.delete(0,END)                                                        #to delete the given input
                get_remainder_time_entry2.delete(0,END)
                remainder_status_label.config(text = '')
                
                
        else:
                remainder_status_label.config(text='Remainder Has Started')                                   #to print remainder has started
                get_remainder_time_entry.config(state='disabled')                                             #to disable the button after clicking it
                set_remainder_button.config(state='disabled')
        remainder_status_label.after(1000, remainder)
                       
                 
def timer_counter(label):
        def count():
                global timer_running
                if timer_running:
                        global timer_counter_num
                        if timer_counter_num==66600:
                            for i in range(3):
                                    display="Time Is Up"                                                            #to print time is up after timer reaches zero
                                    if platform.system() == 'Windows':                                              #to get beep sound after timer reaches zero
                                        winsound.Beep(5000,1000)
                                    
                            timer_running=False
                            timer('reset')
                        else:
                                tt = datetime.datetime.fromtimestamp(timer_counter_num)                              #make a timer that controls the Time
                                string = tt.strftime("%H:%M:%S") 
                                display=string
                                timer_counter_num -= 1                                                               #to get the time in backward
                        label.config(text=display)
                        label.after(1000, count)
        count()
def timer(work):
         if work == 'start':                                                                  #after clicking start button work== start is initialized
                 global timer_running, timer_counter_num
                 timer_running=True
                 if timer_counter_num == 66600:
                         timer_time_str = timer_get_entry.get()
                         hours,minutes,seconds=timer_time_str.split(':')
                         minutes = int(minutes)  + (int(hours) * 60)                          #to convert the hours into minutes
                         seconds = int(seconds) + (minutes * 60)                              #to convert the minutes into seconds
                         timer_counter_num = timer_counter_num + seconds  
                 timer_counter(timer_label)
                 timer_start.config(state='disabled')                                             #disable the start button after clicking it
                 timer_stop.config(state='enabled')                                               # enable the stop button for use
                 timer_reset.config(state='enabled')                                              # enable the reset button for use
                 timer_get_entry.delete(0,END)
         elif work == 'stop':                                                                       #after clicking stop button work == stop is initialized
                 timer_running=False
                 timer_start.config(state='enabled')                                               #enable the start button for use
                 timer_stop.config(state='disabled')                                               #disable the stop button after clicking it
                 timer_reset.config(state='enabled')                                               #enable the reset button for use
         elif work == 'reset':                                                                       #after clicking reset button work == reset is initialized
                 timer_running=False
                 timer_counter_num=66600
                 timer_start.config(state='enabled')                                                #enable the start button for use   
                 timer_stop.config(state='disabled')                                                #disable the stop button after clicking it
                 timer_reset.config(state='disabled')                                                #disable the reset button after clicking it
                 timer_get_entry.config(state='enabled')
                 timer_label.config(text = 'Timer')                                                  #to label the timer button
tabs_control = Notebook(window)                                          #Adding a Tkinter Tab Controls
clock_tab = Frame(tabs_control)                                          #creating clock tab
alarm_tab = Frame(tabs_control)                                          #creating alarm tab
remainder_tab = Frame(tabs_control)                                      #creating remainder tab
timer_tab = Frame(tabs_control)                                          #creating counter timer tab
tabs_control.add(clock_tab, text="Clock")                                #naming the created tabs
tabs_control.add(alarm_tab, text="Alarm")
tabs_control.add(remainder_tab, text="REMAINDER")
tabs_control.add(timer_tab, text='Timer')
tabs_control.pack(expand = 1, fill ="both")
time_label = Label(clock_tab, font = 'calibri 40 bold', foreground = 'black')     #Here we added Two Labels, Time and Date. Both will get data from a function clock
time_label.pack(anchor='center')
date_label = Label(clock_tab, font = 'calibri 40 bold', foreground = 'black')
date_label.pack(anchor='s')
get_alarm_time_entry = Entry(alarm_tab, font = 'calibri 15 bold')                   #Here we added a  provide the information space to get the input time
get_alarm_time_entry.pack(anchor='center')
alarm_instructions_label = Label(alarm_tab, font = 'calibri 10 bold', text = "Enter Alarm Time. Eg -> 01:30 , 01 -> Hour, 30 -> Minutes")
alarm_instructions_label.pack(anchor='s')
set_alarm_button = Button(alarm_tab, text = "Set Alarm", command=alarm)             #here we add a button to set the alarm
set_alarm_button.pack(anchor='s')
alarm_status_label = Label(alarm_tab, font = 'calibri 15 bold')
alarm_status_label.pack(anchor='s')
remainder_instructions_label = Label(remainder_tab, font = 'calibri 10 bold', text = "Enter the Title of the Remainder :")    #Here we added a Labels to print the information
remainder_instructions_label.pack(anchor='s')
get_remainder_time_entry1 = Entry(remainder_tab, font = 'calibri 15 bold')                        #Here to get the input box
get_remainder_time_entry1.pack(anchor='center')
remainder_instructions_label = Label(remainder_tab, font = 'calibri 10 bold', text = "Enter the Message :")      #Here we added a Labels to print the information
remainder_instructions_label.pack(anchor='s')
get_remainder_time_entry2 = Entry(remainder_tab, font = 'calibri 15 bold')                             
get_remainder_time_entry2.pack(anchor='center')
remainder_instructions_label = Label(remainder_tab, font = 'calibri 10 bold', text = "Enter Remainder Time. Eg -> 01:30 , 01 -> Hour, 30 -> Minutes")   #Here we added a Labels to provide the information in the tab
remainder_instructions_label.pack(anchor='s')
get_remainder_time_entry = Entry(remainder_tab, font = 'calibri 15 bold')
get_remainder_time_entry.pack(anchor='center')
set_remainder_button = Button(remainder_tab, text = "Set Remainder", command=remainder)                 #here we add a button to set the remainder
set_remainder_button.pack(anchor='s')
remainder_status_label = Label(remainder_tab, font = 'calibri 15 bold')                               #Here we added a Labels to provide the information space to get the title as input time
remainder_status_label.pack(anchor='s')
timer_get_entry = Entry(timer_tab, font='calibiri 15 bold')                                           #Here we added a label to get the input
timer_get_entry.pack(anchor='center')
timer_instructions_label = Label(timer_tab, font = 'calibri 10 bold', text = "Enter Timer Time. Eg -> 01:30:30, 01 -> Hour, 30 -> Minutes, 30 -> Seconds")   #Here we added a Labels to provide the information in the tab
timer_instructions_label.pack(anchor='s')
timer_label = Label(timer_tab, font='calibri 40 bold', text='Timer')                              #to name the tab as timer tab
timer_label.pack(anchor='center')
timer_start = Button(timer_tab, text='Start', command=lambda:timer('start'))                        #to add a start button in timer tab
timer_start.pack(anchor='center') 
timer_stop = Button(timer_tab, text='Stop', state='disabled',command=lambda:timer('stop'))          #to add a stop button in timer tab       
timer_stop.pack(anchor='center')
timer_reset = Button(timer_tab, text='Reset', state='disabled', command=lambda:timer('reset'))       #to add a reset button in timer tab
timer_reset.pack(anchor='center')
clock()                           #to call clock function                                                
window.mainloop()                 #to call tkinter window


