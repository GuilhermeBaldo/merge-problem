import json


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


def is_mergeable(container_1, container_2):
    '''
    returns true if the two containers (container_1 and container_2) can be merged and false otherwise.

    the condition for merging is the two containers have the same ['y']['start'] value
    
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
    return container_1['y']['start'] == container_2['y']['start']


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