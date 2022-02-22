import json
from typing import overload
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D 
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

def parse_input(input_path):
    '''
    loads the json input file into a list of dictionaries (each dictionary of the list is a container)

    parameters:
        input_path (str): path to the json input file

    returns:
        input (list of dict): list of dict, each dict of the form:
        {
            'x': {'start': float, 'end': float},
            'y': {'start': float, 'end': float},
            'z': {'start': float, 'end': float},
            'id': int
        }

    '''
    file = open(input_path, 'r')
    input = json.load(file)
    file.close()
    return input


def save_output(output_path, output_list):
    '''
    saves the json output list into an output file in output_path

    parameters:
        output_path (str): path to the json input file
        output_list (list of dict): list of dict, each dict of the form:
        {
            'x': {'start': float, 'end': float},
            'y': {'start': float, 'end': float},
            'z': {'start': float, 'end': float},
            'id': int
        }
    '''
    file = open(output_path, 'w')
    output = json.dump(output_list, file)
    file.close()

def do_overlap(container_1, container_2):
    return (container_1['x']['end'] > container_2['x']['start'] and
            container_1['x']['start'] < container_2['x']['end'] and
            container_1['y']['end'] > container_2['y']['start'] and
            container_1['y']['start'] < container_2['y']['end'] and
            container_1['z']['end'] > container_2['z']['start'] and
            container_1['z']['start'] < container_2['z']['end'])

def do_touch_faces(container_1, container_2):
    pass


def is_mergeable(container_1, container_2):
    '''
    returns true if the two containers (container_1 and container_2) can be merged and false otherwise.

    the conditions for merging are:
    1. the two containers have the same ['y']['start'] value
    2. the two containers have overlaping area
    
    parameters:
        container_1 (dict): dict of the form:
               {
            'x': {'start': float, 'end': float},
            'y': {'start': float, 'end': float},
            'z': {'start': float, 'end': float},
            'id': int
        }
        container_2 (dict): same as container_1

    returns:
        true when containers respect the condition for merging,
        false otherwise
    '''
    return (container_1['y']['start'] == container_2['y']['start'] and do_overlap(container_1, container_2))


def mergeable_area(container_1, container_2):
    pass


def merge(container_1, container_2):
    pass


def calculate_volume(container):
    '''
    calculates the volume of a container being the multiplication of its range in x, y and z since it is a parallelepiped/cuboid.
    
    parameters:
        container (dict): dict of the form:
        {
            'x': {'start': float, 'end': float},
            'y': {'start': float, 'end': float},
            'z': {'start': float, 'end': float},
            'id': int
        }

    returns:
        volume (float)
    '''
    return (abs(container['x']['end']-container['x']['start']) * 
            abs(container['y']['end']-container['y']['start']) * 
            abs(container['z']['end']-container['z']['start']))


def calculate_average_volume(containers):
    '''
    calculates the average volume of a list of containers.
    
    parameters:
        containers (list of dict): dict of the form:
        {
            'x': {'start': float, 'end': float},
            'y': {'start': float, 'end': float},
            'z': {'start': float, 'end': float},
            'id': int
        }

    returns:
        average_volume (float)
    '''
    total_volume = sum([calculate_volume(container) for container in containers])
    average_volume = total_volume / len(containers)
    return average_volume


def cuboid_data(o, size=(1,1,1)):
    # code taken from
    # https://stackoverflow.com/a/35978146/4124317
    # suppose axis direction: x: to left; y: to inside; z: to upper
    # get the length, width, and height
    l, w, h = size
    x = [[o[0], o[0] + l, o[0] + l, o[0], o[0]],  
         [o[0], o[0] + l, o[0] + l, o[0], o[0]],  
         [o[0], o[0] + l, o[0] + l, o[0], o[0]],  
         [o[0], o[0] + l, o[0] + l, o[0], o[0]]]  
    y = [[o[1], o[1], o[1] + w, o[1] + w, o[1]],  
         [o[1], o[1], o[1] + w, o[1] + w, o[1]],  
         [o[1], o[1], o[1], o[1], o[1]],          
         [o[1] + w, o[1] + w, o[1] + w, o[1] + w, o[1] + w]]   
    z = [[o[2], o[2], o[2], o[2], o[2]],                       
         [o[2] + h, o[2] + h, o[2] + h, o[2] + h, o[2] + h],   
         [o[2], o[2], o[2] + h, o[2] + h, o[2]],               
         [o[2], o[2], o[2] + h, o[2] + h, o[2]]]               
    return np.array(x), np.array(y), np.array(z)


def plt_cube(pos=(0,0,0), size=(1,1,1), ax=None, **kwargs):
    # Plotting a cube element at position pos
    if ax !=None:
        X, Y, Z = cuboid_data(pos, size)
        ax.plot_surface(X, Y, Z, rstride=1, cstride=1, **kwargs)


def display(containers):
    plt.interactive(True)
    fig = plt.figure(figsize=(10, 10))
    ax = fig.gca(projection='3d')
    ax.set_box_aspect((1, 1, 1))

    for container in containers:
        x = container['x']['start']
        y = container['y']['start']
        z = container['z']['start']

        size_x = abs(container['x']['end'] - x)
        size_y = abs(container['y']['end'] - y)
        size_z = abs(container['z']['end'] - z)

        plt_cube(pos=(x,y,z), sizes=(size_x, size_y, size_z), ax=ax, color='crimson', alpha=0.5)
    
    plt.ion()
    plt.show()

    # container = containers[0]
    # cuboid = np.array([
    #     [container['x']['start'], container['y']['start'], container['z']['start']],
    #     [container['x']['start'], container['y']['end'], container['z']['start']],
    #     [container['x']['start'], container['y']['end'], container['z']['end']],
    #     [container['x']['start'], container['y']['start'], container['z']['end']],
    #     [container['x']['end'], container['y']['start'], container['z']['start']],
    #     [container['x']['end'], container['y']['end'], container['z']['start']],
    #     [container['x']['end'], container['y']['end'], container['z']['end']],
    #     [container['x']['end'], container['y']['start'], container['z']['end']]
    # ])