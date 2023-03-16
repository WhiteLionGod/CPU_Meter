import psutil

print(
    "CPU temperature:", psutil.cpu_percent(interval=0.1), "%",
)