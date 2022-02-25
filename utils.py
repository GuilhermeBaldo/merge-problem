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


def are_touching(container_1, container_2):
    '''
    returns true if the container 1 and container 2 are overlapping or touching

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
        true when container 1 and container 2 are overlapping or touching
        false otherwise
    '''
    return (container_1['x']['end'] >= container_2['x']['start'] and
            container_1['x']['start'] <= container_2['x']['end'] and
            container_1['y']['end'] >= container_2['y']['start'] and
            container_1['y']['start'] <= container_2['y']['end'] and
            container_1['z']['end'] >= container_2['z']['start'] and
            container_1['z']['start'] <= container_2['z']['end'])


def is_contained_in(container_1, container_2):
    '''
    returns true if the container 1 is equal or contained to container 2 

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
        true when container 1 is equal or contained in container 2
        false otherwise
    '''
    return (container_1['x']['end'] <= container_2['x']['end'] and
            container_1['x']['start'] >= container_2['x']['start'] and
            container_1['y']['end'] <= container_2['y']['end'] and
            container_1['y']['start'] >= container_2['y']['start'] and
            container_1['z']['end'] <= container_2['z']['end'] and
            container_1['z']['start'] >= container_2['z']['start'])


def is_equal(container_1, container_2):
    '''
    returns true if the container 1 is equal to container 2 

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
        true when container 1 is equal to container 2
        false otherwise
    '''
    return (container_1['x']['end'] == container_2['x']['end'] and
            container_1['x']['start'] == container_2['x']['start'] and
            container_1['y']['end'] == container_2['y']['end'] and
            container_1['y']['start'] == container_2['y']['start'] and
            container_1['z']['end'] == container_2['z']['end'] and
            container_1['z']['start'] == container_2['z']['start'])


def remove_duplicate_containers(containers):
    '''
    iterates over a list of containers and remove duplicate containers 

    parameters:
        containers (list of dict): dict of the form:
        {
            'x': {'start': float, 'end': float},
            'y': {'start': float, 'end': float},
            'z': {'start': float, 'end': float},
            'id': int
        }

    returns:
        filtered_containers (list): list of containers with no duplicates
    '''
    filtered_containers = []
    for container in containers:
        container_is_already_in_filtered_containers = False
        for filtered_container in filtered_containers:
            if is_equal(container, filtered_container):
                container_is_already_in_filtered_containers = True
                break
        if(not container_is_already_in_filtered_containers):
            filtered_containers.append(container)
    return filtered_containers


def remove_sub_containers(containers):
    '''
    iterates over a list of containers and remove the containers that are contained in another 

    parameters:
        containers (list of dict): dict of the form:
        {
            'x': {'start': float, 'end': float},
            'y': {'start': float, 'end': float},
            'z': {'start': float, 'end': float},
            'id': int
        }

    returns:
        filtered_containers (list): list of containers with the sub containers removed
    '''
    filtered_containers = []
    for i in range(len(containers)):
        for j in range(len(containers)):
            container_i_is_contained = False
            if(i != j):
                if is_contained_in(containers[i], containers[j]):
                    container_i_is_contained = True
                    break
        if(not container_i_is_contained):
            filtered_containers.append(containers[i])
    return filtered_containers


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
    return (container_1['y']['start'] == container_2['y']['start'] and are_touching(container_1, container_2))


def merge(container_1, container_2):
    '''
    returns the result of the merge operation of container 1 and container 2

    the condition for merging is checked
    
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
        merged_containers (list): list of containers resulting from the merge operation
    '''
    merged_containers = []

    threshold_volume = calculate_average_volume([container_1, container_2])

    if(is_mergeable(container_1, container_2)):
        merged_containers = [container_1, container_2]
        merged_container_1 = {
            'x': {
                'start': min(container_1['x']['start'], container_2['x']['start']),
                'end': max(container_1['x']['end'], container_2['x']['end']),
            },
            'y': {
                'start': container_1['y']['start'],
                'end': min(container_1['y']['end'], container_2['y']['end']),
            },
            'z': {
                'start': max(container_1['z']['start'], container_2['z']['start']), 
                'end': min(container_1['z']['end'], container_2['z']['end']),
            }
        }
        if(calculate_volume(merged_container_1) > threshold_volume):
            merged_containers.append(merged_container_1)

        merged_container_2 = {
            'x': {
                'start': max(container_1['x']['start'], container_2['x']['start']),
                'end': min(container_1['x']['end'], container_2['x']['end']),
            },
            'y': {
                'start': container_1['y']['start'],
                'end': min(container_1['y']['end'], container_2['y']['end']),
            },
            'z': {
                'start': min(container_1['z']['start'], container_2['z']['start']),
                'end': max(container_1['z']['end'], container_2['z']['end']),
            }
        }
        if(calculate_volume(merged_container_2) > threshold_volume):
            merged_containers.append(merged_container_2)


    return remove_sub_containers(remove_duplicate_containers(merged_containers))


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


def identify_containers(containers):
    '''
    reset container id and add id to containers that dont have it (merged containers)
    
    parameters:
        containers (list of dict): dict of the form:
        {
            'x': {'start': float, 'end': float},
            'y': {'start': float, 'end': float},
            'z': {'start': float, 'end': float},
            'id': int
        }

    returns:
        containers (list of dict): dict of the form:
        {
            'x': {'start': float, 'end': float},
            'y': {'start': float, 'end': float},
            'z': {'start': float, 'end': float},
            'id': int
        }
    '''
    id = 0
    for container in containers:
        container['id'] = id
        id += 1
    return containers