###
### Author: Sherali Ozodov
### Description:
###
import os
def main():
    color = str(input('Enter color channel\n'))
    valid_color(color)
    channel = float(input('Enter color channel difference\n'))
    valid_channel(channel)
    gs_file = input('Enter greenscreen image file name\n')
    fi_file = input('Enter fill image file name\n')
    
    size_a=get_image_dimensions_string(gs_file)
    size_b=get_image_dimensions_string(fi_file)
    if size_a!=size_b:
        print('Images not the same size. Will exit.')
        os._exit(0)
    output_file = str(input('Enter output file name\n'))
    
    pixels_a = load_image_pixels_a(gs_file)
    pixels_b = load_image_pixels_a(fi_file)
    
    size_a=get_image_dimensions_string(gs_file)
    size_b=get_image_dimensions_string(gs_file)
    
    image_file = get_image_dimensions_string(gs_file)
    color=valid_color(color)
    channel=valid_channel(channel)
    index, unfilled_a_3d = compare(pixels_a, pixels_b, color, channel)
    ready_list = complete_list_3d(pixels_a, pixels_b, index, unfilled_a_3d)
    ppm_write(output_file,ready_list)
    print('Output file written. Exiting.')

def get_image_dimensions_string(file_name):
    image_file = open(file_name, 'r')
    image_file.readline()
    return image_file.readline().strip('\n')


def load_image_pixels_a(file_name):
    pixels = []
    image_file = open(file_name, 'r')

    image_file.readline()
    image_file.readline()
    image_file.readline()

    width_height = get_image_dimensions_string(file_name)
    width_height = width_height.split(' ')
    width = int(width_height[0])
    height = int(width_height[1])

    for line in image_file:
        line = line.strip('\n ')
        rgb_row = line.split(' ')
        row = []
        for i in range(0, len(rgb_row), 3):
            pixel = [int(rgb_row[i]), int(rgb_row[i + 1]), int(rgb_row[i + 2])]
            row.append(pixel)
        pixels.append(row)
    return pixels


def compare(pixels_a, pixels_b, color, channel):
    index = []
    unfilled_a_3d = []
    unfilled_a_2d = []

    for i in pixels_a:
        for d in range(len(i)):
            if i[d][int(color)] > channel * i[d][int(color) - 1] and i[d][int(color)] > channel * i[d][int(color) - 2]:
                indexes = [pixels_a.index(i), (i.index(i[d]))]
                index.append(indexes)
                unfilled_a_2d.append([])
            else:
                unfilled_a_2d.append(i[d])

    for i in range(0, len(unfilled_a_2d), len(pixels_a[0])):
        unfilled_a_3d.append(unfilled_a_2d[i:i + len(pixels_a[0])])

    return index, unfilled_a_3d


def complete_list_3d(pixels_a, pixels_b, index, unfilled_a_3d):
    ready_list = pixels_a

    for i in pixels_a:
        taken_b = []
        for ind in index:
            l = ind[0]
            ll = ind[1]
            taken_b.append(pixels_b[l][ll])

    for i in range(len(unfilled_a_3d)):
        for n in range(len(taken_b)):
            ready_list[index[n][0]][index[n][1]] = taken_b[n]
    return ready_list

def valid_color(color):
    if color == 'r':
        color = 0
    elif color == 'g':
        color = 1
    elif color == 'b':
        color = 2
    elif color!='r' and color!='g' and color!='b':
        print('Channel must be r, g, or b. Will exit.')
        os._exit(0)
    return color
    
def valid_channel(channel):
    if not 1.0 < channel < 10.0:
        print('Invalid channel difference. Will exit.')
        os._exit(0)
    return channel


def ppm_write(output_file,ready_list):
    file=open(output_file,'w')
    width=len(ready_list[0])
    height=len(ready_list)
    file.write('P3'+'\n')
    file.write(str(width)+' ' + str(height) + '\n')
    file.write(str(255)+'\n')
    new=[]
    for i in range(len(ready_list)):
        for b in range(len(ready_list[i])):
            for c in range(len(ready_list[i][b])):
                new.append(str(ready_list[i][b][c]))

    for i in range(0,len(new),len(ready_list[0])*3):
        a=file.write(' '.join(new[i:i+len(ready_list[0]*3)])+'\n')
    file.close()
    return a

main()