def target_method1(arg1, arg2, arg3):
    print(f"arg1: {arg1}, arg2: {arg2}, arg3: {arg3}")

def target_method2(arg1, arg2, *, arg3):
    print(f"arg1: {arg1}, arg2: {arg2}, arg3: {arg3}")

def target_method3(arg1, arg2, *args):
    print(f"arg1: {arg1}, arg2: {arg2}, args: {args}")
    
def target_method4(arg1, arg2, **args):
    print(f"arg1: {arg1}, arg2: {arg2}, args: {args}")

def practice_function_arguments():
    target_method1(1, 2, 3) # arg1: 1, arg2: 2, arg3: 3
    target_method2(1, 2, arg3=3) # arg1: 1, arg2: 2, arg3: 3
    target_method3(1, 2, 3, 4, 5) # arg1: 1, arg2: 2, args: (3, 4, 5)
    target_method4(1, 2, arg3=3, arg4=4, arg5=5) # arg1: 1, arg2: 2, args: {'arg3': 3, 'arg4': 4, 'arg5': 5}

practice_function_arguments()

# target_method2(arg3=3)
# TypeError: target_method2() missing 2 required positional arguments: 'arg1' and 'arg2'
