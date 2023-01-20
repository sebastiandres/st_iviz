import numpy as np
from matplotlib import pyplot as plt
from IPython import embed
from matplotlib.animation import FuncAnimation

def initialization_circles():
    """
    Generates the initial structure
    """
    lines = []
    r = .45
    th = np.linspace(0, 2*np.pi, 31)
    circle = r*np.cos(th) + r*np.sin(th)*1j
    for x in range(-2,3,1):
        for y in range(-2,3,1):
            line = {
                    "color":"k", 
                    "data": x + y*1j + circle}
            lines.append(line)
    return lines

def initialization_lines():
    """
    Generates the initial structure
    """
    custom_range = [-2, -1, -.5, -.25, 0, .25, .5, 1, 2]
    lines = []
    for x in custom_range:
        line = {
                "color":"r", 
                "data": (x + np.linspace(-2,2,101)*1j)}
        lines.append(line)
    for y in custom_range:
        line = {
                "color":"b", 
                "data": (np.linspace(-2,2,51) + y*1j)}
        lines.append(line)
    return lines

def evolution(lines, theta_range, f):
    """
    Create the intermediate frames
    """
    N_theta = len(theta_range)
    for line in lines:
        z0 = line["data"]
        fz0 = f(z0)
        Z = np.zeros([N_theta, z0.shape[0]], complex)
        for i, theta in enumerate(theta_range):
            Z[i,:] = theta*fz0 + (1-theta)*z0          
        line["frames"] = Z
        min_x = np.min(np.real(Z))
        max_x = np.max(np.real(Z))
        min_y = np.min(np.imag(Z))
        max_y = np.max(np.imag(Z))
        line["min_x"] = min_x
        line["max_x"] = max_x
        line["min_y"] = min_y
        line["max_y"] = max_y
    plot = {}
    plot["min_x"] = np.min([line["min_x"] for line in lines])
    plot["max_x"] = np.max([line["max_x"] for line in lines])
    plot["min_y"] = np.min([line["min_y"] for line in lines])
    plot["max_y"] = np.max([line["max_y"] for line in lines])
    return lines, plot

def plot_z0(lines):
    for line in lines:
        plt.plot(np.real(line["data"]), np.imag(line["data"]), color=line["color"]) 
    plt.show()

def plot_zi(lines, i):
    for line in lines:
        plt.plot(np.real(line["frames"][i,:]), np.imag(line["frames"][i,:]), color=line["color"]) 
    plt.show()

n_frames = 51
#lines = initialization_lines()
lines = initialization_circles()
theta_range = np.linspace(0.0, 1.0, n_frames)
f = lambda z: np.exp(z)
lines, plot = evolution(lines, theta_range, f)
fig,ax = plt.subplots(figsize=(15,15))
fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=None, hspace=None)
ax.set_xlim(plot["min_x"], plot["max_x"])
ax.set_ylim(plot["min_y"], plot["max_y"])

#plot_zi(lines, 0)
#plot_zi(lines, 10)
#plot_zi(lines, -1)
#plot(lines)


def update(frame):
    i = frame
    plt.cla()
    for line in lines:
        plt.plot(np.real(line["frames"][i,:]), np.imag(line["frames"][i,:]), color=line["color"]) 
    ax.set_xlim(plot["min_x"], plot["max_x"])
    ax.set_ylim(plot["min_y"], plot["max_y"])
    return

animation = FuncAnimation(fig, update, interval=1, frames=n_frames)
animation.save('out.mp4', fps=4)
print("open out.mp4")
"""
# Todo
- Limits! x, y
- Animation
- Colors
- streamlit
"""