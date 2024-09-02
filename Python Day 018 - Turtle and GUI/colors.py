import colorgram
#Take the x most amount of colors from the picture and turn them into a list
colors = colorgram.extract('Painting.png', 20)
all_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.g
    tuple_list = (r,g,b)
    all_colors.append(tuple_list)
