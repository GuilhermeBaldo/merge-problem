# merge-problem
Union of the allocatable spaces to find bigger allocatable spaces (containers)

# setup

create virtual environment with python -m venv .venv

# goal
The goal of the problem is to maximize the average merged containers volume



# container
A container is defined by C = [x_start, x_end] x [y_start, y_end] x [z_start, z_end] beloging to R3 where x is the cartesian product. And it is represented by the following example dictionary.

e.g.
{
    "id": 0,
    "x": {"start": 0, "end": 2.38},
    "y": {"start": 0, "end": 2.83},
    "z": {"start": 0, "end": 12.0},
}

Therefore the volume of a container is volume_c = abs(x_start-x_end) * abs(y_start-y_end) * (z_start-z_end).

# input
The input for the problem is provided in a .json file (e.g. case_1_input.json and case_2_input.json) in the form of a list of containers or a list of dictionaries as decrived above.

e.g.
[
    {
        "id": 0,
        "x": {"start": 0, "end": 2.38},
        "y": {"start": 0, "end": 2.83},
        "z": {"start": 0, "end": 12.0},
    },
    ...
]

