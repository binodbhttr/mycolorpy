import matplotlib.pyplot as plt 
import matplotlib.colors as colors
import numpy as np


'''
Example Concept:
cmap = plt.cm.get_cmap('bwr') #select a cmap

rgba = cmap(0.9) # you now have values between 0 and 1 for the given cmap to generage rgba color code
print(rgba)
clr=colors.rgb2hex(rgba) #convert the rgba to hex
print(clr)
'''

def gen_color(see_map,n):
    '''Generates n distinct color from a given colormap%%!
    Returns: a list with hex values of colors
    '''
    cmap = plt.cm.get_cmap(str(see_map)) # select the desired cmap
    arr=np.linspace(0,1,n) #create a list with numbers from 0 to 1 with n items
    colorlist=list()
    for c in arr:
        rgba=cmap(c) #select the rgba value of the cmap at point c which is a number between 0 to 1
        clr=colors.rgb2hex(rgba) #convert to hex
        colorlist.append(str(clr)) # create a list of these colors
    return colorlist


def gen_color_normalized(see_map,data_arr):
    '''Generates n distinct color from a given colormap for a an array with data
    Returns: a list with hex values of colors
    '''
    cmap = plt.cm.get_cmap(str(see_map)) # select the desired cmap
    data_min=np.min(data_arr)
    data_max=np.max(data_arr)
    
    colorlist_normalized=list()
    for c in data_arr:
        norm=(c-data_min)/(data_max-data_min)*0.99
        rgba=cmap(norm) #select the rgba value of the cmap at point c which is a number between 0 to 1
        clr=colors.rgb2hex(rgba) #convert to hex
        colorlist_normalized.append(str(clr)) # create a list of these colors
    return colorlist_normalized
