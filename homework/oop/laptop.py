# 4.* Create an interface for the Laptop with the next methods: Screen, Keyboard, Touchpad, WebCam, Ports, Dynamics
# and create an HPLaptop class by using your interface.

from abc import ABC, abstractmethod


class Laptop(ABC):
    @abstractmethod
    def Screen(self):
        pass

    @abstractmethod
    def Keyboard(self):
        pass

    @abstractmethod
    def Touchpad(self):
        pass

    @abstractmethod
    def WebCam(self):
        pass

    @abstractmethod
    def Ports(self):
        pass

    @abstractmethod
    def Dynamics(self):
        pass


class HPLaptop(Laptop):
    def __init__(self, screen, keyboard, touchpad, webcam, ports, dynamics):
        self.hplaptop = {}
        self.screen = screen
        self.hplaptop["Screen"] = self.screen
        self.keyboard = keyboard
        self.hplaptop["Keyboard"] = self.keyboard
        self.touchpad = touchpad
        self.hplaptop["Touchpad"] = self.touchpad
        self.webcam = webcam
        self.hplaptop["WebCam"] = self.webcam
        self.ports = ports
        self.hplaptop["Ports"] = self.ports
        self.dynamics = dynamics
        self.hplaptop["Dynamics"] = self.dynamics

    def Screen(self):
        print("Screen:", self.hplaptop["Screen"])

    def Keyboard(self):
        print("Keyboard:", self.hplaptop["Keyboard"])

    def Touchpad(self):
        print("Touchpad:", self.hplaptop["Touchpad"])

    def WebCam(self):
        print("Webcam:", self.hplaptop["WebCam"])

    def Ports(self):
        print("Ports:", self.hplaptop["Ports"])

    def Dynamics(self):
        print("Dynamics:", self.hplaptop["Dynamics"])


hp_laptop = HPLaptop("15-inch", "eng/rus", "Synaptics", "HP Retail Integrated Webcam", "2 x USB 3.0", "SPI Dynamics")
hp_laptop.Screen()
hp_laptop.Keyboard()
hp_laptop.Touchpad()
hp_laptop.WebCam()
hp_laptop.Ports()
hp_laptop.Dynamics()
