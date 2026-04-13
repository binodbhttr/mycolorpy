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

def gen_color(cmap,n,reverse=False):
    '''Generates n distinct color from a given colormap.

    Args:
        cmap(str): The name of the colormap you want to use.
            Refer https://matplotlib.org/stable/tutorials/colors/colormaps.html to choose
            Suggestions:
            For Metallicity in Astrophysics: Use coolwarm, bwr, seismic in reverse
            For distinct objects: Use gnuplot, brg, jet,turbo.

        n(int): Number of colors you want from the cmap you entered.

        reverse(bool): False by default. Set it to True if you want the cmap result to be reversed.

    Returns: 
        colorlist(list): A list with hex values of colors.
    '''
    c_map = plt.cm.get_cmap(str(cmap)) # select the desired cmap
    arr=np.linspace(0,1,n) #create a list with numbers from 0 to 1 with n items
    colorlist=list()
    for c in arr:
        rgba=c_map(c) #select the rgba value of the cmap at point c which is a number between 0 to 1
        clr=colors.rgb2hex(rgba) #convert to hex
        colorlist.append(str(clr)) # create a list of these colors
    
    if reverse==True:
        colorlist.reverse()
    return colorlist


def gen_color_normalized(cmap,data_arr,reverse=False):
    '''Generates n distinct color from a given colormap for an array of desired data.
    Args:
        cmap(str): The name of the colormap you want to use.
            Refer https://matplotlib.org/stable/tutorials/colors/colormaps.html to choose
            
            Some suggestions:
            For Metallicity in Astrophysics: use coolwarm, bwr, seismic in reverse
            For distinct objects: Use gnuplot, brg, jet,turbo.

        data_arr(numpy.ndarray): The numpy array of data for which you want these distinct colors.

        reverse(bool): False by default. Set it to True if you want the cmap result to be reversed.

    Returns: 
        colorlist_normalized(list): A normalized list of colors with hex values for the given array.
    '''
    c_map = plt.cm.get_cmap(str(cmap)) # select the desired cmap
    data_min=np.min(data_arr)
    data_max=np.max(data_arr)
    
    colorlist_normalized=list()
    for c in data_arr:
        norm=(c-data_min)/(data_max-data_min)*0.99
        rgba=c_map(norm) #select the rgba value of the cmap at point c which is a number between 0 to 1
        clr=colors.rgb2hex(rgba) #convert to hex
        colorlist_normalized.append(str(clr)) # create a list of these colors
    
    if reverse==True:
        del colorlist_normalized
        colorlist_normalized=list()
        for c in data_arr:
            norm=(c-data_min)/(data_max-data_min)*0.99
            rgba=c_map(1-norm) #select the rgba value of the cmap at point c which is a number between 0 to 1
            clr=colors.rgb2hex(rgba) #convert to hex
            colorlist_normalized.append(str(clr)) # create a list of these colors
    
    return colorlist_normalized