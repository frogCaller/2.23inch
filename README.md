# 2.23-inch OLED Hat

<div style="display: flex; gap: 10px;">   
    <img src="images/2.23-inch.gif" width="168">
    <img src="images/draw.gif" width="300">
</div>

# Materials
* [Raspberry Pi 5](https://amzn.to/45zrAKI) / [4](https://amzn.to/3KQlkVv) / [3](https://amzn.to/3xs2iSm) / [Zero 2 WH](https://amzn.to/3VO7eu2)<br />
* [Micro SD Cards](https://amzn.to/4erXgWD)<br />
* [2.23inch OLED HAT](https://amzn.to/3V2gCKb)<br />
<br />
(Amazon affiliate links)<br />


## **Installations**

1. **OS install:**
   - Raspberry Pi 5 / 4 / 3 / Zero 2 WH - RaspberryPi OS 64-bit <br />
   
2. **Enable SPI & I2C:**
   - Open a terminal on your Raspberry Pi.
   - Run `sudo raspi-config`
   - Navigate to Interfacing Options -> SPI -> Enable.
   - Navigate to Interfacing Options -> I2C -> Enable.
     
3. **Clone the repository:**
   ```bash
   sudo apt install -y git
   git clone https://github.com/frogCaller/2.23inch.git
   cd 2.23inch

# Wiring and Setup
1. **Connect OLED HAT to Raspberry Pi:**

2. **Install System and Python Dependencies:**
   ```bash
   chmod +x setup.sh
   ./setup.sh

# Usage Instructions
1. Drawing and Typing:
   - To draw and type with the OLED screen, you need to use the Raspberry Pi desktop environment.
   - Connect a monitor, keyboard, and mouse to your Raspberry Pi and log in to the Raspberry Pi OS desktop environment.
   - Once logged in, navigate to the project directory and run the python scripts to type or draw:
     
     ```
     python3 type.py
     python3 draw.py
     ```
2. Display Messages or Images:
   - Utilize the fortune command to display random quotes or messages on the screen.
     ```
     python3 fortune.py
     ```
   - Display your saved drawings on the screen.
   
     ```
     python3 gallery.py
     ```
3. SSH Access:
   - You can also access your Raspberry Pi remotely using SSH. Use the following command to connect:
   - ssh pi@<your_pi_ip_address>
4. VNC Viewer:
   1. Enable VNC on your Raspberry Pi:
      - Open a terminal on your Raspberry Pi.
      - Run sudo raspi-config.
      - Navigate to Interfacing Options -> VNC -> Enable.
   2. Connect to your Raspberry Pi:
      - Open VNC Viewer on your computer.
      - Enter the IP address of your Raspberry Pi and connect.
   3. Once connected, use the VNC Viewer to interact with the Raspberry Pi UI.

# Troubleshooting
1. Common Issues:
   - Ensure SPI & I2C are enabled in the Raspberry Pi configuration.
   - Check all connections if the screen does not display anything.
   - Verify all required packages are installed correctly.
   - [More Info](https://www.waveshare.com/wiki/2.23inch_OLED_HAT)
