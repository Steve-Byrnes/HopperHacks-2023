from tracking import tracking
import dbConnect

imgwidth, track_data = tracking.trackHit()
path = tracking.get_duration(track_data)

user = 'Joe'
angle = tracking.get_angle(path[0], path[1])
time_change = tracking.get_time_change(path[0], path[1])
power = tracking.get_power(path[0], path[1])

body = {
    "user": user,
    "start_x": path[0]['x'],
    "start_y": path[0]['y'],
    "end_x": path[1]['x'],
    "end_y": path[1]['y'],
    "duration": time_change,
    "angle": angle,
    "power": power
}
dbConnect.setSwing(body)

# .46, .87
# 655, 564