class CellPhone:
    """
    Make the class with aggregation
    """

    def __init__(self, screen):
        self.screen = screen

    def __del__(self):
        print('Instance of CellPhone class was destroyed')


class Screen:
    """
    Make the class with aggregation
    """

    def __init__(self):
        pass

    def __del__(self):
        print('Instance of Screen class was destroyed')


def main():
    screen = Screen()
    call_phone = CellPhone(screen)
    print(call_phone)
    # <__main__.CellPhone object at 0x7fdde196eb20>
    print(call_phone.screen)
    # <__main__.Screen object at 0x7fdde196e970>
    del call_phone
    # Instance of CellPhone class was destroyed
    try:
        print(call_phone)
    except UnboundLocalError:
        print("Can't print instance - it was destroy!")
        # Can't print instance - it was destroyed!
    print(screen)  # CellPhone instance was  destroy, but the Screen instance still exists
    # <__main__.Screen object at 0x7fdde196e970>


if __name__ == "__main__":
    main()
# Instance of Screen class was destroyed.
