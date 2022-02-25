from utils import *
import argparse


def merge_problem(containers):
    '''
    solves the merge problem by recursevely trying to merge each container (container 1) of the list with the best match container (container 2).
    the best match container is the container with each the container 1 when merged results in the greatest increment in average volume (eager solution).

    parameters:
        containers (list dict): dict of the form:
        {
            'x': {'start': float, 'end': float},
            'y': {'start': float, 'end': float},
            'z': {'start': float, 'end': float},
            'id': int
        }

    returns:
        output_containers (list): list with the containers with larger average volume
    '''

    # this variable contains the limitation in the number of containers of the output
    max_num_of_containers = 3 * (len(containers))

    # function that implements recursion
    def recursive_merge_problem(input_containers):
        # list that will carry the output containers
        output_containers = []
        # boolean that will work as a stop criteria (when no merge occurs during execution the recursion stops)
        any_merged = False
        # initial average volume that will work as stop criteria also
        initial_average_volume = calculate_average_volume(input_containers)
        
        # try to find the best merge for every container in input
        while(input_containers):
            # gets the last element of the input containers list to be container_1
            container_1 = input_containers.pop()

            # this loop tries to find the best matching container (container_2) in the list (that will lead to greatest average volume increment)
            maximum_averaged_merged_volume = 0
            container_2_index = None
            for i, c in enumerate(input_containers):
                merged_containers = merge(container_1, c)

                if(merged_containers):
                    averaged_merged_volume = calculate_average_volume(merged_containers)
                    if(averaged_merged_volume > maximum_averaged_merged_volume and averaged_merged_volume > calculate_average_volume([container_1, c])):
                        maximum_averaged_merged_volume = averaged_merged_volume
                        container_2_index = i

            # if a container_2 was found, extend the output_containers with the merge results and remove container_2 from the input_list 
            # otherwise, append container_1 to the output_list
            if(container_2_index):
                any_merged = True
                container_2 = input_containers.pop(container_2_index)
                merged_containers = merge(container_1, container_2)
                output_containers.extend(merged_containers)
            else:
                output_containers.append(container_1)

        # clean possible duplication of containers that are subsets of other containers that were possibly generated in the algorithm
        output_containers = remove_sub_containers(remove_duplicate_containers(output_containers))

        end_average_volume = calculate_average_volume(output_containers)

        # stop criteria when no merging was done and otherwise call the function another time.
        if(not any_merged or end_average_volume < initial_average_volume or len(output_containers) >= max_num_of_containers):
            return output_containers
        else:
            return recursive_merge_problem(output_containers)

    return recursive_merge_problem(containers)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Perform the merge problem in the input provided')
    parser.add_argument("--input_file", dest="input_file", required=True, help="input file with containers", metavar="FILE")
    args = parser.parse_args()

    print(f'Reading the input file {args.input_file}')
    input_containers = parse_input(args.input_file)

    print(f'The input contains {len(input_containers)} containers')

    print(f'Average volume of the input: {calculate_average_volume(input_containers)}')

    print('Performing optimization...')
    output_containers = merge_problem(input_containers)
    print('Done... =)')

    print(f'Average volume of the output: {calculate_average_volume(output_containers)}')
    print(f'The output contains {len(output_containers)} containers')

    output_containers = identify_containers(output_containers)

    output_file = 'output'.join(args.input_file.split('input'))
    print(f'Saving results in {output_file}')
    save_output(output_file, output_containers)
        
