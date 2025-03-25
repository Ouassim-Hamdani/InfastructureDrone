import packages.KeyPress as kp
from djitellopy import tello
from time import sleep
class drone_controller:
    def __init__(self,connect=True):
        kp.init()
        if connect:
            self.drone = tello.Tello()
            self.drone.connect()
        else:
            self.drone = None
        self.speed_unit = 50
    def input_to_controls(self):
        lr,fb,ud,yv = 0,0,0,0
        if kp.getKey("LEFT"):
            lr = -self.speed_unit
        elif kp.getKey("RIGHT"):
            lr= self.speed_unit
        
        if kp.getKey("UP"):
            fb=self.speed_unit
        elif kp.getKey("DOWN"):
            fb = - int(self.speed_unit/2)
            
        if kp.getKey("w"):
            ud=self.speed_unit
        elif kp.getKey("s"):
            ud = -self.speed_unit
            
        if kp.getKey("a"):
            yv=self.speed_unit
        elif kp.getKey("d"):
            yv = -self.speed_unit
        
        if kp.getKey("SPACE"):
            if not self.drone:
                return "LT" #LAND OR TAKEOFF
            if self.drone.is_flying:
                self.drone.land()
            else:
                self.drone.takeoff()
        if kp.getKey("q"):
            if not self.drone:
                return "L"
            self.drone.land()
        if kp.getKey("LSHIFT"):
            if not self.drone:
                return "UP"
            self.drone.move_up(20)
        if kp.getKey("LCTRL"):
            if not self.drone:
                return "DOWN"
            self.drone.move_down(20)
            
        return [lr,fb,ud,yv]

    def run(self):
        if not self.drone:
            return
        while (1):
            vals = self.input_to_controls()
            self.drone.send_rc_control(vals[0],vals[1],vals[2],vals[3])
            sleep(0.05)
            
if __name__=="__main__":
    dro = drone_controller()
    dro.run()
    