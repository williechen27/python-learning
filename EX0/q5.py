import time

total_seconds = int(time.time())

current_second = total_seconds % 60
total_minutes = total_seconds // 60
current_minute = total_minutes % 60
total_hours = total_minutes // 60
current_hour = (total_hours + 8) % 24 #台灣時間(UTC+8)

print(current_hour, ":", current_minute, ":", current_second)
