from utils import *
import argparse
import os


def merge_problem(containers):

    max_num_of_containers = 3 * len(containers)

    def recursive_merge_problem(containers):
        output_containers = []
        input_containers = containers.copy()
        any_merged = False
        while(input_containers):
            container_1 = input_containers.pop()
            container_merged = False
            for container_2 in input_containers:
                if(is_mergeable(container_1, container_2)):
                    merged_containers = merge(container_1, container_2)
                    input_containers.remove(container_2)
                    if(merged_containers):
                        container_merged = True
                        any_merged = True
                        output_containers.extend(merged_containers)
                    else:
                        output_containers.extend([container_1, container_2])
        if(not any_merged or len(output_containers) >= max_num_of_containers):
            return output_containers
        else:
            return recursive_merge_problem(output_containers)

    return recursive_merge_problem(containers)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Perform the merge problem in the input provided')
    parser.add_argument("--input_file", dest="input_file", required=True, help="input file with containers", metavar="FILE")
    args = parser.parse_args()

    input_containers = parse_input(args.input_file)

    print(calculate_average_volume(input_containers))

    output_containers = merge_problem(input_containers)

    print(calculate_average_volume(output_containers))

    output_file = 'output'.join(args.input_file.split('input'))
    save_output(output_file, output_containers)
        
