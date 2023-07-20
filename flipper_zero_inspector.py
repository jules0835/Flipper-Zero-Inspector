# Disclaimer: This is a work in progress, it is not finished yet. I am not a professional developer, it is possible that there are errors in the code. If you find any errors, please let me know.
# Based on : https://github.com/wh00hw/pyFlipper made by wh00hw
# Flipper Zero Inspector 0.1.0
# Made by Jules0835

from pyflipper.pyflipper import PyFlipper
import time
import glob


def auto_select_port():
    while True:
        ports = glob.glob('/dev/tty.usbmodemflip*')
        if len(ports) > 0:
            port = ports[0]
            print("Flipper Zero device found on port", port)
            return port
        else:
            print("Waiting for Flipper Zero device", end='')
            for _ in range(5):
                print('.', end='', flush=True)
                time.sleep(0.3)
            print()


def select_flipper():
    flipper = None
    while flipper is None:
        port = auto_select_port()
        try:
            flipper = PyFlipper(com=port)
        except Exception as e:
            print("Error connecting to Flipper Zero:", str(e))
            print("Retrying...")
            time.sleep(1)
    return flipper


def welcome():
    print("         ╔══════════════════════╗")
    print("         ║    ＦＬＩＰＰＥＲ    ║")
    print("         ║       ＺＥＲＯ       ║")
    print("         ║  ＩＮＳＰＥＣＴＯＲ  ║")
    print("         ║                      ║")
    print("         ║by Jules0835          ║")
    print("         ╚══════════════════════╝")
    print("Welcome to Flipper Zero Inspector!")
    print("We are going to inspect your Flipper Zero device and check if it is working properly.")
    print("Press Ctrl+C to exit\n\n")


def reboot(flipper):
    print("We are going to reboot your Flipper Zero device")
    try:
        flipper.power.reboot()
    except Exception as e:
        print("Reboot Ok ! Unplug your Flipper Zero device")


def blue_led(flipper):
    flipper.led.set(led='b', value=255)
    flipper.led.set(led='r', value=0)
    flipper.led.set(led='g', value=0)


def red_led(flipper):
    flipper.led.set(led='b', value=0)
    flipper.led.set(led='r', value=255)
    flipper.led.set(led='g', value=0)


def green_led(flipper):
    flipper.led.set(led='b', value=0)
    flipper.led.set(led='r', value=0)
    flipper.led.set(led='g', value=255)


def check_leds(flipper):
    print("\nWe are going to check each LED one by one\n")

    green_led(flipper)
    print("Green LED is on")
    greenAnsw = input("\nIs the green LED on? y/n: ")
    if greenAnsw == "n":
        problems.append("redled")
        print("\033[31m" + "Green LED is not working" + "\033[0m")
    else :
        print("\033[32m" + "Green LED is working" + "\033[0m")

    blue_led(flipper)
    print("Blue LED is on")
    blueAnsw = input("\nIs the blue LED on? y/n : ")
    if blueAnsw == "n":
        problems.append("redled")
        print("\033[31m" + "Blue LED is not working" + "\033[0m")
    else :
        print("\033[32m" + "Blue LED is working" + "\033[0m")

    red_led(flipper)
    print("Red LED is on")
    redAnsw = input("\nIs the red LED on? y/n : ")
    if redAnsw == "n":
        problems.append("redled")
        print("\033[31m" + "Red LED is not working" + "\033[0m")
    else : 
        print("\033[32m" + "Red LED is working" + "\033[0m")
    

def vibro_3times(flipper):
    flipper.vibro.on()
    time.sleep(0.2)
    flipper.vibro.off()
    time.sleep(0.2)
    flipper.vibro.on()
    time.sleep(0.2)
    flipper.vibro.off()
    time.sleep(0.2)
    flipper.vibro.on()
    time.sleep(0.2)
    flipper.vibro.off()


def check_vibro(flipper):
    print("We are going to check the vibration motor")
    vibro_3times(flipper)
    print("You should have felt 3 vibrations")
    vibroAnsw = input("\nIs the vibration motor working? y/n : ")
    if vibroAnsw == "n":
        problems.append("vibro")
        print("\033[31m" + "Vibration motor is not working" + "\033[0m")
    else :
        print("\033[32m" + "Vibration motor is working" + "\033[0m")


def play_sound(flipper):
    flipper.music_player.beep()
    rttl_song = "Littleroot Town - Pokemon:d=4,o=5,b=100:8c5,8f5,8g5,4a5,8p,8g5,8a5,8g5,8a5,8a#5,8p,4c6,8d6,8a5,8g5,8a5,8c#6,4d6,4e6,4d6,8a5,8g5,8f5,8e5,8f5,8a5,4d6,8d5,8e5,2f5,8c6,8a#5,8a#5,8a5,2f5,8d6,8a5,8a5,8g5,2f5,8p,8f5,8d5,8f5,8e5,4e5,8f5,8g5"
    flipper.music_player.play(rtttl_code=rttl_song, duration=3)


# def check_sound(flipper):
#     print("We are going to check the speaker")
#     play_sound(flipper)
#     soundAnsw = input("\nDid you hear the Flipper Zero sound? y/n : ")
#     if soundAnsw == "n":
#         problems.append("sound")


def device_info(flipper):
    device_info = flipper.device_info.info()
    hardware_model = device_info['hardware_model']
    hardware_uid = device_info['hardware_uid']
    firmware_version = device_info['firmware_version']
    radio_ble_mac = device_info['radio_ble_mac']
    device_name = device_info['hardware_name']
    firmware_origin_fork = device_info.get('firmware_origin_fork', 'N/A')
    if firmware_origin_fork == 'Official':
        firmware_origin_fork = 'True'
    else:
        firmware_origin_fork = 'False'

    print('Device model:', hardware_model)
    print('Device name:', device_name)
    print('Firmware version:', firmware_version)
    print('Serial number:', hardware_uid)
    print('Bluetooth MAC:', radio_ble_mac)
    print('Official firmware:', firmware_origin_fork)
    print('\n\n')


def power_off(flipper):
    reppoweroff = input("Do you want to power off your Flipper Zero? y/n : ")
    if reppoweroff == "y":
        flipper.power.off()
    

def nfc_detect(flipper):
    print("We are going to check if your Flipper Zero can detect a NFC card")
    print("Please put a NFC card on the back of your Flipper Zero")
    nfc_detected = flipper.nfc.detect()
    if nfc_detected == True: 
        print("NFC detected")
    else:
        print("Error : NFC not detected")


# def nfc_emulate(flipper):
#     flipper.nfc.emulate()
    

# def check_nfc(flipper):
#     print("We are going to check the NFC")


def ir_receive(flipper):
    r = flipper.ir.rx(timeout=5)
    if r is None:
        print("No IR signal received")
        retry = input("Do you want to retry? y/n : ")
        if retry == "y":
            ir_receive()
        
    else:
        print("IR signal received")


def ir_send(flipper):
    print("We are going to send an IR signal")
    flipper.ir.tx(protocol="Samsung32", hex_address="C000FFEE", hex_command="DEADBEEF")
    print("Sending ir signal", end='')
    for _ in range(10):
        print('.', end='', flush=True)
        time.sleep(1)
    print()


def ir_check(flipper):
    print("We are going to check the IR")
    ir_receive(flipper)
    ir_send(flipper)


def screen_brightness(flipper):
    nbrtst = 0
    while nbrtst <= 0:
        for i in range(255, 0, -1):
            flipper.led.set(led='bl', value=i)

        for i in range(0, 255):
            flipper.led.set(led='bl', value=i)

        nbrtst += 1


# def detect_nfc(flipper):
#     nfc_detected = flipper.nfc.detect()
#     print("nfc detected : ", nfc_detected)
#     if nfc_detected == True:
#         print("NFC detected")
#     else:
#         print("NFC not detected")



# def check_nfc(flipper):
#     flipper.nfc.emulate()

def check_screen(flipper):
    print("We are going to check the screen")
    screen_brightness(flipper)
    print("You should have seen the screen brightness changing")
    screenAnsw = input("\nIs the screen working? y/n : ")
    if screenAnsw == "n":
        problems.append("screen")
        print("\033[31m Screen problem \033[0m")
    else:
        print("\033[32m Screen OK \033[0m")




welcome()
while True:
    problems = []
    flipper = select_flipper()
    print("---------------------------------------------------\n\n")
    device_info(flipper)
    input("Press Enter to start the inspection...")
    check_screen(flipper)
    check_vibro(flipper)
    check_leds(flipper)
    print("\n---------------------------------------------------\n")
    if problems == []:
        print("\033[32m" + "Your Flipper Zero is working perfectly" + "\033[0m")
    else:
        print("\033[31m" + "Your Flipper Zero has problems" + "\033[0m")
        print("Problems : ", problems)
        
    reboot(flipper)
    continueAnsw = input("\nDo you want to inspect another Flipper Zero device? y/n : ")
    if continueAnsw == "n":
        break
    else:   
        input("Connect your Flipper Zero device and press Enter to start the inspection...")

