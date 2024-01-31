import os
import subprocess

from macOS.macgenerator import generateMacAddress

interface = os.getenv("NETWORK_INTERFACE") or "en0"
command = "ifconfig"
mac_address = generateMacAddress()


def rotatehardware():
    try:
        subprocess.run(["sudo", "-S", command, interface, "lladdr", mac_address], check=True, stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE, text=True)
        print(f"MAC address rotated successfully to: {mac_address}")
    except subprocess.CalledProcessError as e:
        print("Command execution failed with return code", e.returncode)
        print("Error:", e.stderr)
