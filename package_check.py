import pkg_resources
import subprocess
import sys


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


def check_packages():
    installed_packages = {d.project_name: d.version for d in pkg_resources.working_set}
    file = open('required_packages.txt', 'r')
    to_install = []
    for line in file:
        if line.strip() not in installed_packages:
            to_install.append(line.strip())
    if to_install:
        print("\nTo correctly run this program you first need to install these packages: ")
        for i in to_install:
            print("- ", i)
        print("\nWould you like to install these packages?\n")
        while True:
            selection = input("Selection (y/n): ").lower()
            if selection == 'y':
                print("Installing...")
                for i in to_install:
                    install(i)
                    print(str(i), " installed correctly.")
                break
            elif selection == 'n':
                print("\n\nNot able to run the program because packages required.")
                print("Program will interrupt.")
                exit()
            else:
                print("\nPlease, choose between available options\n\n")

    print("All packages are installed correctly. You are ready to roll.")


check_packages()
