from tracking import tracking
import requests
import json

track_data = tracking.trackHit()
path = tracking.get_duration(track_data)
angle = tracking.get_angle(path[0], path[1])

swing_info = json.dumps({
    "user": "keerthi",
    "points": track_data
})
x = requests.post('http://10.1.170.242:8080/api/swings', swing_info)
print(x)


# .46, .87
# 655, 564