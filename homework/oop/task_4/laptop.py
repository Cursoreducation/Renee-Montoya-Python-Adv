class Laptop:
    def get_screen(self):
        pass

    def get_keyboard(self):
        pass

    def get_touchpad(self):
        pass

    def get_web_cam(self):
        pass

    def get_ports(self):
        pass

    def get_dynamics(self):
        pass


class HPLaptop(Laptop):
    def get_screen(self):
        return '1200x900'

    def get_keyboard(self):
        return 'us 101'

    def get_touchpad(self):
        return 'SynPad'

    def get_web_cam(self):
        return 'CAM'

    def get_ports(self):
        return 'RS485, RS232'

    def get_dynamics(self):
        return '---'
