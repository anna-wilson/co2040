import badger2040
import pimoroni_i2c
import breakout_scd41
import time

def draw_readings(co2, temp, humid):
    display.set_pen(15)
    display.clear()
    display.set_pen(0)
    display.set_font("sans")
    display.text( f"CO2: {co2:.0f} ppm", 20, 20, scale=1 )
    display.text( f"Temp: {temp:.1f} C", 20, 50, scale=1 )
    display.text( f"Humidity: {humid:3.0f}%", 20, 80, scale=1 )
    display.update()
    

display = badger2040.Badger2040()
display.set_update_speed(badger2040.UPDATE_NORMAL)
display.set_thickness(2)

i2c = pimoroni_i2c.PimoroniI2C(4, 5)
breakout_scd41.init(i2c)
breakout_scd41.start()

while True:
    if breakout_scd41.ready():
        display.led(128)
        co2, temp, humid = breakout_scd41.measure()
        print("Got a reading")
        print(f"Reading: {co2}")
        draw_readings(co2, temp, humid)
        display.led(0)
        time.sleep(5)
