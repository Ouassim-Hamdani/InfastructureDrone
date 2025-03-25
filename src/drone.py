from djitellopy import tello
import cv2
from YOLO import DroneAi
from packages.KeyDroneController import drone_controller




class Drone:
    """Drone class handler that handles comunciation ith drone, streaming, commands, utilsizes AI here"""
    def __init__(self):
        self.model = DroneAi()
        self.drone = tello.Tello()
        self.drone.connect()
        self.drone.streamon()
        self.drone_control = drone_controller(False)
    def stream(self):
        """Streams Drone video output, process YOLO DIRECTLY, showcases output"""
        while 1:
            frame = self.drone.get_frame_read().frame
            frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            image = self.model.predict(frame,return_img=True)
            cv2.imshow("Output",image)
            
            
            action = self.drone_control.input_to_controls()
            
            self.handle_keyinput(action)
            
            cv2.waitKey(1)
    
    def handle_keyinput(self,action):
        """Function to handle different key inputs command that control drone moving"""
        if isinstance(action,str):
                if action=="LT":
                    if self.drone.is_flying:
                        self.drone.land()
                    else:
                        self.drone.takeoff()
                elif action=="L":
                    if self.drone.is_flying:
                        self.drone.land()
                elif action=="UP":
                    self.drone.move_up(20)
                elif action=="DOWN":
                    self.drone.move_down(20)
        else:
            self.drone.send_rc_control(*action)
            
if __name__=="__main__":
    drone = Drone()
    drone.stream()
    