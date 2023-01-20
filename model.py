import numpy as np
#import matplotlib.pyplot as plt
#from matplotlib.animation import FuncAnimation

def circle(z,r,n_points=10):
    t = np.linspace(0,2*np.pi,n_points)
    return z + r*np.exp(1.j*t)

def f(z,alpha):
    #return z*(1-alpha)+alpha*z**4
    return z*(1-alpha)+alpha*z**2

def create_lines_from_circles():
    n_points = 10
    n_circles = 10
    radius = 0.1
    x = np.linspace(-10.,10.,n_circles)
    y = np.linspace(-10.,10.,n_circles)
    lines = []
    for i in x:
        for j in y:
            line = {
                    "points":circle(i+1.j*j, radius, n_points),
                    "color":"k",
                    "marker":"",
                   }
            lines.append(line)
    return lines

class Model():

    def __init__(self, function, viz_type, viz_properties):
        # Assign the properties
        self.function = function
        self.viz_type = viz_type
        self.viz_properties = viz_properties
        # Create the requires lines
        if viz_type == "circle":
            self.lines = create_lines_from_circles()

    def evaluate_function():
        mapped = f(circles,0.0)

    def create_animation():
        fig,ax = plt.subplots(figsize=(15,15))
        fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=None, hspace=None)
        ax.set_facecolor("black")
        ax.scatter(np.real(mapped),np.imag(mapped),s=0.05,alpha=0.5, c="white")
        ax.set_aspect('equal', 'box')
        #ax.set_xlim([-5,5])
        #ax.set_ylim([-5,5])
        plt.xticks([]), plt.yticks([])
        plt.show()
        plt.close()

#m1 = Model(f, "circle", {})
#print(m1.lines)
#m1.

"""
alphas = np.zeros(100,dtype=np.float64)
alphas[1:]=np.logspace(start=-5,stop=0,num=99)
mapped = f(circles,0.0)
fig,ax = plt.subplots(figsize=(15,15))
fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=None, hspace=None)
#ax.set_facecolor("black")
im = ax.scatter(np.real(mapped),np.imag(mapped),s=0.05,alpha=1.0, c="black")
ax.set_aspect('equal', 'box')
ax.spines.left.set_visible(False)
ax.spines.bottom.set_visible(False)
ax.spines.right.set_visible(False)
ax.spines.top.set_visible(False)
#ax.set_xlim([-100.,100.])
#ax.set_ylim([-100.,100.])
plt.xticks([]), plt.yticks([])
#plt.savefig("orbit2.png",dpi=300)

def update(frame):
    mapped = f(circles,alphas[frame])
    positions = np.array([np.real(mapped), np.imag(mapped)]).T
    xmin = np.min(positions[:,0])
    xmax = np.max(positions[:,0])
    ymin = np.min(positions[:,1])
    ymax = np.max(positions[:,1])
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    ax.figure.canvas.draw()
    im.set_offsets(positions)
    return im,

animation = FuncAnimation(fig, update, interval=1, frames=100)
#animation.save('out.mp4', fps=25, dpi=160, bitrate=-1, codec="mpeg4",
#                extra_args=['-pix_fmt', 'yuv420p'],
#                metadata={'artist':'Simone Conradi'})
#plt.show()
#st.pyplot(fig)
"""