


from argparse import ArgumentParser
from importlib import __import__, import_module
import os


def parse_Args():
    args = ArgumentParser()
    args.add_argument('-e','--exercise', type=int, default=1)
    args.add_argument('-p','--part', type=int, default=1)
    args.add_argument('--ex', default=False, action='store_true')
    return args.parse_args()




def main(ex:int, part:int = 1, is_ex:bool = False):

    exercise_folder = f"./days/d{ex}"

    if not os.path.isdir(exercise_folder):
        print(f"Exercise {ex} not found")
        return

    input_file = f'{exercise_folder}/input.txt'
    if is_ex:
        input_file = f'{exercise_folder}/example.txt'
    input = open(input_file, 'r').read()


    # Your code here
    # print(input)

    mod = import_module(f'days.d{ex}.main', package='aoc')
    print(mod)

    if not mod:
        print(f"Exercise {ex} not found")
        return

    output = mod.main(input, part=part)

    print("Output:")
    print(output)

    with open(f'{exercise_folder}/output_{part}{"_ex" if is_ex else ""}.txt','w') as f:
        f.write(f"{output}")

    pass

if __name__ == '__main__':
    args = parse_Args()
    main(args.exercise, args.part, args.ex)