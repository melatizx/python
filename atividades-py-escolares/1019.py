import math
hrs = 0
min = 0

total_seg = int(input())

if total_seg > 3600:
    hrs = total_seg/3600
    min = (total_seg%3600)/60
    seg = total_seg%60
    print(f'{math.floor(hrs)}:{math.floor(min)}:{math.floor(seg)}')

elif total_seg > 60 and total_seg <3600:
    min = total_seg/60
    seg = total_seg%60
    print(f'{math.floor(hrs)}:{math.floor(min)}:{math.floor(seg)}')
else:
    print(f'{hrs}:{math.floor(min)}:{math.floor(total_seg)}')
