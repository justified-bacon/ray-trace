import numpy as np
from PIL import Image
import vectormath

def trace():
    global sphere_pos

    clr_line = []
    for i in range(720):
        for j in range(1280):
            ray = vectormath.line(camera_pos, cam_frame[i][j] - camera_pos)
            # ray.vector = cam_frame[i][j] - camera_pos
            j += 1
            # print(ray.vector)
            if vectormath.distLinePoint(ray, sphere_pos[1]) <= sphere_radius[1]:
                clr_line.append((255,255,255))
                # clr_line.append(((255/sphere_radius[0]) * (4 - vectormath.distLinePoint(ray, sphere_pos[0])), (255/sphere_radius[0]) * (4 - vectormath.distLinePoint(ray, sphere_pos[0])), (255/sphere_radius[0]) * (4 - vectormath.distLinePoint(ray, sphere_pos[0]))))
            elif vectormath.distLinePoint(ray, sphere_pos[0]) <= sphere_radius[0]:
                clr_line.append((255,0,0))
            else:
                clr_line.append((0,0,0))
        clr_array.append(clr_line)
        clr_line = []


            
        i +=1
        j = 0

cam_frame = []

i=0
j=0

for i in range(720):
    a = []
    for j in range(1280):
        a.append([14, (-640/720) + (1/1440) + (j/720), (360/720) - (1/1440) - (i/720)])
        j += 1

    
    cam_frame.append(a)
    j = 0
    i += 1

# cam_frame = np.array(cam_frame)
# print(cam_frame[0][0])
cam_frame = np.array(cam_frame)
# print (cam_frame[359])

cam_frame.flags.writeable = False

camera_pos = np.array([15,0,0]) #use np.array([], dtype=np.float64) to convert to floats

lights = np.array([[0,0,7], [2,0,6]])

# print(type(camera_pos[0]))
# print(camera_pos.dtype)

sphere_pos = np.array([[0,0,-.5], [0,1,.5]])

sphere_radius = np.array([1, 1])

pix = []

pic = []

i=0
j=0
'''
for i in range(720):
    for j in range(1280):
        pix.append((round(j * (255/2560) + i * (255/1440)), round((1280-j) * (255/2560) + (720-i) * (255/1440)), round(((2 * j) if j<641 else (2560 - (2 * j))) * (255/2560) + ((2 * i) if i<361 else (1440 - (2 * i))) * (255/1440))))
        j +=1
    i+=1
    j=0
    pic.append(pix)
    pix=[]



for i in range(720):
    for j in range(1280):
        pix.append((round((1280 - j) * (255/2560) + (720 - i) * (255/1440)),round(((2 * j) if j<641 else (2560 - (2 * j))) * (255/2560) + (720 - i)) * (255/1440), round((1280 - j) * (255/2560) + (720 - i) * (255/1440))))
        j +=1
    i+=1
    j=0
    pic.append(pix)
    pix=[]


for i in range(720):
    for j in range(1280):
        pix.append((round(j * (255/1280)), round(j * (255/1280)), round(j * (255/1280))))
        j +=1
    j = 0
    i +=1
    pic.append(pix)
    pix=[]
'''
# print(pic)

# img_arr = np.array(pic, dtype=np.uint8)

# image = Image.fromarray(img_arr)

# image.show()
# image.save("img5.png")

# ray = vectormath.line(camera_pos, )
# ray.point = camera_pos

clr_array = []
clr_line = []
'''
for i in range(720):
    for j in range(1280):
        ray.vector = cam_frame[i][j] - camera_pos
        j += 1
        # print(ray.vector)
        if vectormath.distLinePoint(ray, sphere_pos[0]) <= sphere_radius[0] or vectormath.distLinePoint(ray, sphere_pos[1]) <= sphere_radius[1]:
            clr_line.append((255,255,255))
        else:
            clr_line.append((0,0,0))
    clr_array.append(clr_line)
    clr_line = []


        
    i +=1
    j = 0
'''
# for i in range(720):
#     for j in range(1280):
#         ray = vectormath.line(camera_pos, cam_frame[i][j] - camera_pos)
#         # ray.vector = cam_frame[i][j] - camera_pos
#         j += 1
#         # print(ray.vector)
#         if vectormath.distLinePoint(ray, sphere_pos[0]) <= sphere_radius[0]:
#             clr_line.append((255,255,255))
#             # clr_line.append(((255/sphere_radius[0]) * (4 - vectormath.distLinePoint(ray, sphere_pos[0])), (255/sphere_radius[0]) * (4 - vectormath.distLinePoint(ray, sphere_pos[0])), (255/sphere_radius[0]) * (4 - vectormath.distLinePoint(ray, sphere_pos[0]))))
#         else:
#             clr_line.append((0,0,0))
#     clr_array.append(clr_line)
#     clr_line = []


        
#     i +=1
#     j = 0

# print(clr_array[360])
for i in range(200):
    clr_array = []

    sphere_pos[1][1] = np.sin(np.arange(200)*np.pi/100)[i]
    sphere_pos[0][1] = -np.sin(np.arange(200)*np.pi/100)[i]
    trace()

    clr_array = np.array(clr_array, dtype=np.uint8)

    image = Image.fromarray(clr_array)
    # image.show()
    if i<10:
        image.save(f"anim/anim00{i}.png")
    elif i<100:
        image.save(f"anim/anim0{i}.png")
    else:
        image.save(f"anim/anim{i}.png")

    print(f"frame {i+1} of 200")

'''
a = vectormath.line()
a.point = np.array([0,0,0])
a.vector = np.array([0,0,1])

print(vectormath.distLinePoint(a, np.array([1,1,0])))
'''
