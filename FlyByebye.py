from win32api import *
from win32gui import *
from win32con import *
import random
import time
def Init():
    w = GetSystemMetrics(0)
    h = GetSystemMetrics(1)
    hdc = GetDC(0)
    
    for i in range(5000):
        brush = CreateSolidBrush(RGB(random.randrange(255), random.randrange(255),random.randrange(255)))
        SelectObject(hdc, brush)
        BitBlt(hdc, 0, 0, w, h, hdc, 0, h-30, SRCCOPY)
        BitBlt(hdc, 0, 0, w, h, hdc, 0, -30, SRCCOPY)
        PatBlt(hdc, 0, 0, w, h, PATINVERT)
        DeleteObject(brush)
    for i in range(500):
        PatBlt(hdc, 0, 0, w, h, PATINVERT)
        time.sleep(0.5)
Init()
