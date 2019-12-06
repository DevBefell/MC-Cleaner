class Main(object):
    def __init__(self):
        # Check if Minecraft is running
        self.processes = str(Popen('tasklist', stdin=PIPE, stderr=PIPE, stdout=PIPE).communicate()[0])
        if "javaw.exe" in self.processes:
            print(Fore.RED + "Minecraft is running please close it to prevent errors")
            system('pause')
            exit()
        # Get username and the file locations
        self.user = getlogin()
        self.paths = [f"C:/Users/{self.user}/AppData/Roaming/.minecraft/assets/skins",
                      f"C:/Users/{self.user}/AppData/Roaming/.minecraft/crash-reports",
                      f"C:/Users/{self.user}/AppData/Roaming/.minecraft/logs"]

        # The file removing part
        for path in self.paths:
            try:
                rmtree(path)
                print(Fore.GREEN, f"{path}:\n\t  -Cleaned Successfully\n")

            except FileNotFoundError:
                print(Fore.RED, f"{path}:\n\t  Already Cleaned\n")

        system('pause')


if __name__ == '__main__':
    from os import getlogin, system
    from colorama import init, Fore
    from shutil import rmtree
    from ctypes import windll
    from subprocess import Popen, PIPE

    init()
    windll.kernel32.SetConsoleTitleW("MC Cleaner")
    Main()
