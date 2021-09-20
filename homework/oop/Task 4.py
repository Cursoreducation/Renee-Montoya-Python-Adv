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
    def webcam(self):
        raise NotImplementedError

    @abstractmethod
    def ports(self):
        raise NotImplementedError

    @abstractmethod
    def dynamics(self):
        raise NotImplementedError


class HPLaptop(Laptop):
    def __init__(self, screen1, keyboard1, touchpad1, webcam1, ports1, dynamics1):
        self.screen1 = screen1
        self.keyboard1 = keyboard1
        self.touchpad1 = touchpad1
        self.webcam1 = webcam1
        self.ports1 = ports1
        self.dynamics1 = dynamics1

    def screen(self):
        return f"Screen:{self.screen1}\n"

    def keyboard(self):
        return f"Keyboard:{self.keyboard1}\n"

    def touchpad(self):
        return f'Touchpad:{self.touchpad1}\n'

    def webcam(self):
        return f'Webcam:{self.webcam1}\n'

    def ports(self):
        return f'Ports:{self.ports1}\n'

    def dynamics(self):
        return f'Dynamics:{self.dynamics1}\n'


hp = HPLaptop('14', 'eng/ukr/rus', 'touchpad', 'hd webcam', 'usb 3.0', 'logitech')

print(hp.screen(), hp.keyboard(), hp.touchpad(), hp.webcam(), hp.ports(), hp.dynamics())
