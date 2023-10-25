import subprocess

def run():
    # List of packages you want to install
    packages_to_install = ['cv2', 'pytesseract']

    # Loop through the list and install each package
    for package in packages_to_install:
        try:
            subprocess.check_call(['pip', 'install', package])
            print(f'Successfully installed {package}')
        except subprocess.CalledProcessError as e:
            print(f'Failed to install {package}: {e}')
