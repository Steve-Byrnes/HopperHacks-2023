from tracking import tracking
import dbConnect

track_data = tracking.trackHit()
path = tracking.get_duration(track_data)
angle = tracking.get_angle(path[0], path[1])



# .46, .87
# 655, 564