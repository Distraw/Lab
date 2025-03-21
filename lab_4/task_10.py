import sys
import platform
import os
import argparse

def print_environment():
    for variable, value in os.environ.items():
        print(variable, ': ', value)

def print_environment_variable(variable: str):
    if os.environ.get(variable) is None:
        print('No such variable in the environment')
        return

    print(variable, ': ', os.environ.get(variable))

def set_environment_variable(input_str: str):
    if '=' in input_str:
        variable, value = input_str.split('=', 1)
        os.environ[variable] = value
        print(variable, ' was set to: ', os.environ.get(variable))
    else:
        print('Format unrecognized. Use <VAR=VALUE> instead')

def assign_environment_variable(variable: str, value: str):
    if variable:
        os.environ[variable] = value
        print(variable, ' was set to: ', os.environ.get(variable))

def delete_environment_variable(variable: str):
    if variable in os.environ:
        del os.environ[variable]
        print(variable, ' was deleted')
    else:
        print(variable, ' does not exist')

def clear_environment():
    os.environ.clear()
    print('Environment was cleared')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('-i', '--info', metavar='VAR', help='Show value of a variable')
    parser.add_argument('-s', '--set', metavar='VAR=VALUE', help='Set a variable')
    parser.add_argument('-a', '--assign', metavar='VAR', help='Assign a variable')
    parser.add_argument('-v', '--value', metavar='VALUE', help='Value for assigned variable')
    parser.add_argument('-d', '--del', metavar='VAR', help='Delete a variable')
    parser.add_argument('-c', '--clear', action='store_true', help='Clear environment')

    args = vars(parser.parse_args())

    if not any(args.values()):
        print_environment()

    elif args['info'] is not None:
        print_environment_variable(args['info'])

    elif args['set'] is not None:
        set_environment_variable(args['set'])

    elif args['assign'] is not None:
        assign_environment_variable(args['assign'], args['value'] if args['value'] is not None else '')

    elif args['del'] is not None:
        delete_environment_variable(args['del'])

    elif args['clear'] is not None:
        clear_environment()