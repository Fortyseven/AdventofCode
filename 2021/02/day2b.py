#!/usr/bin/env python3

from day2data import input_data
# from day2sample import input_data

depth = 0
horiz = 0
aim = 0

cmds_horiz = {
    "forward": 1
}

cmds_depth = {
    "up": -1,
    "down": 1
}


def do_command(cmd):
    global horiz, depth, aim

    (cmd_name, quantity) = cmd.split()
    if cmd_name in cmds_horiz:
        horiz += (int(quantity) * cmds_horiz.get(cmd_name))
        depth += aim * int(quantity)
    elif cmd_name in cmds_depth:
        aim += (int(quantity) * cmds_depth.get(cmd_name))


for inp in input_data:
    do_command(inp)

print("depth = ", depth)
print("hoirz = ", horiz)
print("mult = ", depth * horiz)
