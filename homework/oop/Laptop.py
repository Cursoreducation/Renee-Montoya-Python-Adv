# 4.* Create an interface for the Laptop with the next methods: Screen, Keyboard, Touchpad, WebCam, Ports, Dynamics
# and create an HPLaptop class by using your interface

from abc import ABC, abstractmethod


class Laptop(ABC):
    @abstractmethod
    def screen(self):
        raise NotImplementedError

    @abstractmethod
    def keyboard(self):
        raise NotImplementedError

    @abstractmethod
    def touchpad(self):
        raise NotImplementedError

    @abstractmethod
    def web_cam(self):
        raise NotImplementedError

    @abstractmethod
    def ports(self):
        raise NotImplementedError

    @abstractmethod
    def dynamics(self):
        raise NotImplementedError


class HPLaptop(Laptop):
    def __init__(self, type_screen, type_keyboard, type_touchpad, type_webcam, type_ports, type_dynamics):
        self.hp_laptop = {}
        self.type_screen = type_screen
        self.hp_laptop["Screen"] = self.type_screen
        self.type_keyboard = type_keyboard
        self.hp_laptop["Keyboard"] = self.type_keyboard
        self.type_touchpad = type_touchpad
        self.hp_laptop["Touchpad"] = self.type_touchpad
        self.type_webcam = type_webcam
        self.hp_laptop["WebCam"] = self.type_webcam
        self.type_ports = type_ports
        self.hp_laptop["Ports"] = self.type_ports
        self.type_dynamics = type_dynamics
        self.hp_laptop["Dynamics"] = self.type_dynamics

    def screen(self):
        return self.hp_laptop["Screen"]

    def keyboard(self):
        return self.hp_laptop["Keyboard"]

    def touchpad(self):
        return self.hp_laptop["Touchpad"]

    def web_cam(self):
        return self.hp_laptop["WebCam"]

    def ports(self):
        return self.hp_laptop["Ports"]

    def dynamics(self):
        return self.hp_laptop["Dynamics"]


def main():
    hp_laptop = HPLaptop('15.6" TFT', "eng", "sensor", "HD 8mpx", "3 x USB 3.0", "Dolby Digital")
    return hp_laptop


if __name__ == "__main__":
    hp_255_g7 = main()
    print("Screen:", hp_255_g7.screen())
    # Screen: 15.6" TFT
    print("Keyboard:", hp_255_g7.keyboard())
    # Keyboard: eng
    print("Touchpad:", hp_255_g7.touchpad())
    # Touchpad: sensor
    print("WebCam:", hp_255_g7.web_cam())
    # WebCam: HD 8mpx
    print("Ports:", hp_255_g7.ports())
    # Ports: 3 x USB 3.0
    print("Dynamics:", hp_255_g7.dynamics())
    # Dynamics: Dolby Digital

    try:
        laptop = Laptop()
    except TypeError as error:
        print(error)
