# 2.23-inch OLED Hat

<div style="display: flex; gap: 10px;">   
    <img src="images/2.23-inch.gif" width="168">
    <img src="images/draw.gif" width="300">
</div>

# Materials
* [Raspberry Pi 5](https://amzn.to/45zrAKI) / [4](https://amzn.to/3KQlkVv) / [3](https://amzn.to/3xs2iSm) / [Zero 2 WH](https://amzn.to/3Ov69Dm)<br />
* [Micro SD Cards](https://amzn.to/48bSKY8)<br />
* [2.23inch OLED HAT](https://amzn.to/3V2gCKb)<br />
* [90-degree GPIO extenders](https://amzn.to/3Uooea9)<br />
<br />
(Amazon affiliate links)<br />


## **Installations**

1. **OS install:**
   - Raspberry Pi 4 / 5 / Zero 2 WH - RaspberryPi OS 64-bit <br />

2. **Install fortune:**
   ```
   sudo apt install fortune -y
   ```

3. Setup 2.23inch OLED HAT <br />

   _Make sure to enable SPI & I2C_
   
   ```
   sudo apt-get install python3-pip
   sudo apt-get install python3-pil
   sudo apt-get install python3-numpy
   sudo pip3 install spidev
   sudo pip3 install smbus
   ```   

    _[Source](https://www.waveshare.com/wiki/2.23inch_OLED_HAT)_
   <br />

