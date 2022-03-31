import webcolors
import csv
import pandas as pd

def closest_color(color):
	min_colors = {}
	for k, name in webcolors.CSS3_HEX_TO_NAMES.items():
		r, g, b = webcolors.hex_to_rgb(k)
		rr = (r - color[0]) ** 2
		gr = (g - color[1]) ** 2
		br = (b - color[2]) ** 2
		min_colors[(rr+gr+br)] = name
	return min_colors[min(min_colors.keys())]

def get_color_name(color):
	try:
		closest_name = webcolors.rgb_to_name(color)
	except ValueError:
		closest_name = closest_color(color)
	return closest_name

sample_list = [(33, 33, 35), (126, 126, 118), (251, 251, 253), (117, 63, 51), (191, 179, 121), (58, 75, 33), (168, 173, 215)]

color_list = []
for color in sample_list:
	closest_name = get_color_name(color)
	color_list.append(closest_name)

print("closest names:", color_list)

#print(webcolors.CSS3_HEX_TO_NAMES.items())
'''def generic_name(color):
	if (color == "darkred") or (color == "indianred") or (color == "maroon") or (color == "red") or (color == "tomato") or (color == "firebrick"):
		generic = "red"
	elif (color == "darkorange") or (color == "orange") or (color == "orangered") or (color == "peru") or (color == "peachpuff"):
		generic = "orange"
	elif(color == "darkgoldenrod") or (color == "gold") or (color == "lemonchiffon") or (color == "lightgolden"):
		generic = "yellow"
'''

def gen_name(color):
	#with open('color_sheet.csv', 'r') as f:
		#s = f.read()
	data = pd.read_csv('color_sheet1.csv')

	red = data['red'].tolist()
	orange = data['orange'].tolist()
	yellow = data['yellow'].tolist()
	green = data['green'].tolist()
	blue = data['blue'].tolist()
	purple = data['purple'].tolist()
	pink = data['pink'].tolist()
	grey = data['grey'].tolist()
	white = data['white'].tolist()
	black = data['black'].tolist()
	brown = data['brown'].tolist()

	colors = []
	colors.append(red)
	colors.append(orange)
	colors.append(yellow)
	colors.append(green)
	colors.append(blue)
	colors.append(purple)
	colors.append(pink)
	colors.append(grey)
	colors.append(white)
	colors.append(black)
	colors.append(brown)

	#if color in s:
		#print("yes")

	for color_list in colors:
		if color in color_list:
			#print("YES", color_list[0])
			print(color_list[0])

#to run:
for color in color_list:
	gen_name(color)

#print(color_list)

#testing one color:
#gen_name("black")








