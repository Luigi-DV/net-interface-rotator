# Network Interface Rotator

This project provides a simple script for rotating local hardware addresses on a specified network interface. It uses the `ifconfig` command with elevated privileges to change the MAC address. The primary use case is for educational and testing purposes.

## Usage

1. Install the required Python packages:

   ```bash
   pip install -r requirements.txt

2. Copy the .env.example file
    ```bash
    cp .env.example .env
   ```
   
3. Set up your variables in the .env file

4. Run the script
    ```bash
    python main.py
   ```
   
# Disclaimer

This project is not intended for malicious purposes, including any form of Distributed Denial of Service (DDoS) attacks. The simplicity of the code and the local hardware address rotation feature are designed for educational and testing purposes only. Use this script responsibly and in compliance with the terms of service of any network or website you interact with.

Please be aware of the potential legal and ethical implications of network manipulation, and use this project in a manner that respects the privacy and rights of others.

Note: The use of this script may violate the terms of service of certain websites and networks. Always ensure that your actions comply with the applicable terms and conditions.