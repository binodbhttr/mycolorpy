# mycolorpy


Functions to create an array of colors based on a colormap

Installation Instructions:

You can pip install it using:
    

    pip install mycolorpy

You can then do:

    from mycolorpy import colorlist as mcp
    

Example: To create a list of 5 hex strings from cmap "winter" 
    

    color1=mcp.gen_color(cmap="winter",n=5)
    print(color1)

Output:

    ['#0000ff', '#0040df', '#0080bf', '#00c09f', '#00ff80']
    
Another example to generate 16 list of colors from cmap bwr:

    color2=mcp.gen_color(cmap="bwr",n=16)
    print(color2)
Output:

    ['#0000ff', '#2222ff', '#4444ff', '#6666ff', '#8888ff', '#aaaaff', '#ccccff', '#eeeeff', '#ffeeee', '#ffcccc', '#ffaaaa', '#ff8888', '#ff6666', '#ff4444', '#ff2222', '#ff0000']

There is a [python notebook][2] with usage examples to better visualize this.


Say you want to generate a list of colors from a cmap that is normalized to a given data. You can do that using:

    a=random.randint(1000, size=(200))
    a=np.array(a)
    color1=mcp.gen_color_normalized(cmap="seismic",data_arr=a)
    plt.scatter(a,a,c=color1)

Output:
[![enter image description here][3]][3]

You can also reverse the color using:

    color1=mcp.gen_color_normalized(cmap="seismic",data_arr=a,reverse=True)
    plt.scatter(a,a,c=color1)

Output:
[![enter image description here][4]][4]


 
 
   


  [1]: https://github.com/binodbhttr/mycolorpy
  [2]: https://github.com/binodbhttr/mycolorpy/blob/master/usage_example.ipynb
  [3]: https://i.stack.imgur.com/xF9Nm.png
  [4]: https://i.stack.imgur.com/OkWV9.png
