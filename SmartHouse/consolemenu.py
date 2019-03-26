import sys


class ConsoleMenu:
    text = input()

    @staticmethod
    def consoleoptions():
        print("choose one of fallowing options:")
        print("(1) Run")
        print("(2) Stop")
        print("(3) Exit")
        return int(input())

    def Run(self):
        pass

    def stop(self):
        pass

    def Exit(self):
        sys.exit()
