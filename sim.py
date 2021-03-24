# cell[20]

import gym
import gym_sns
import matplotlib.pyplot as plt
import numpy as np
import cmath
from IPython import display

env = gym.make('CartPoleAcc-v0')
env._max_episode_steps = 500
thetas = {}

def simulate(k1, k2, t_steps, ax):
    observation = env.reset()
    action = 1
    theta_t = []
    
    img = ax.imshow(env.render(mode='rgb_array'))    
    ax.axis('off')
    
    for t in range(t_steps):
        ax.set_title(f'Simulating for k1 = {k1}, k2 = {k2}\n t= {t}')
        img.set_data(env.render(mode='rgb_array')) 
        display.display(plt.gcf())
        display.clear_output(wait=True)
        observation, reward, done, info = env.step(action)
        theta, theta_dot = observation[2:]
        action = k1*theta + k2*theta_dot
        theta_t.append(theta)
        if done:
            break
    env.close()   

    return theta_t

def sys_pole(k1, k2):
    '''Calculate poles of the system for given K1, K2 values

    Args:
        k1 (int/float): propotional constant.
        k2 (int/float): differential constant. 
    
    Returns:
        p1, p2 (complex float): poles of the system
    
    Use cmath.sqrt, for instances of square roots, to handle the case of square root of negative numbers:
        cmath.sqrt(x)       
    '''
    
    g = 9.8 # acceleration due to gravity (ms-2)
    l = .5 # distance to pole centre of gravity (m)
    
    # EDIT HERE
    p1 = -k2/(2*l) + cmath.sqrt((k2/(2*l))**2 - (k1-g)/l)
    p2 = -k2/(2*l) - cmath.sqrt((k2/(2*l))**2 - (k1-g)/l)
    
    return p1, p2
    

def pole_plot(poles, k1, k2, ax, show=True):      
    
    ax.plot([pole.real  for pole in poles], [pole.imag for pole in poles], 'x', markersize=10, label=f'k1 = {k1}, k2 = {k2}')
    ax.grid(True)
    ax.legend()
    ax.set_xlabel(r'$\Re$')
    ax.set_ylabel(r'$\Im$')
            
    if show:
        plt.show()

def cart_pole_angle_plot(k1, k2, theta_t, ax, show=True):
    ax.plot(theta_t, '-', label = f'k1 = {k1}, k2 = {k2}')
    ax.grid(True)
    ax.legend()
    ax.set_xlabel(r'$t$')
    ax.set_ylabel(r'$\theta$')
    if show:
        plt.show()

def plot_axes(ax, show=True):
    ax.set_xlim([-max(abs(ax.get_xlim()[0]), abs(ax.get_xlim()[1]))-1, max(abs(ax.get_xlim()[0]), abs(ax.get_ylim()[1]))+1])
    ax.set_ylim([-max(abs(ax.get_ylim()[0]), abs(ax.get_ylim()[1]))-1, max(abs(ax.get_ylim()[0]), abs(ax.get_ylim()[1]))+1])
    ax.plot([ax.get_xlim()[0], ax.get_xlim()[1]], [0, 0], 'k')
    ax.plot([0, 0], [ax.get_ylim()[0], ax.get_ylim()[1]], 'k')
    
    if show:
        plt.show()


# cell[21]

# CHANGE HERE
k1 = 10.5 # K1
k2 = 0 # K2

t_steps = 150 # no. of time frames in simulation 

fig, ax = plt.subplots(1, 1, figsize=(18,9))

# simulate the cartpole system
theta_t = simulate(k1, k2, t_steps, ax)
print(len(theta_t))

fig, axes = plt.subplots(1, 2, figsize=(18,9))
poles = sys_pole(k1, k2) # obtain poles for the system
pole_plot(poles, k1, k2, axes[0], show=False) # plot poles of the system 
plot_axes(axes[0], show=False) 
cart_pole_angle_plot(k1, k2, theta_t, axes[1]) # plot theta variation