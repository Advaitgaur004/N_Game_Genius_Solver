from itertools import permutations, product

def solve_n_target(nums, target):
    operations = ['+', '-', '*', '/']
    
    num_permutations = list(permutations(nums))
    
    op_combinations = list(product(operations, repeat=len(nums) - 1))
    
    def generate_expressions(nums, ops):
        if len(nums) == 1:
            return [str(nums[0])]
        exprs = []
        for i in range(1, len(nums)):
            left_part = generate_expressions(nums[:i], ops[:i-1])
            right_part = generate_expressions(nums[i:], ops[i-1:])
            for l in left_part:
                for r in right_part:
                    exprs.append(f"({l} {ops[i-1]} {r})")
        return exprs
    
    for num_perm in num_permutations:
        for ops in op_combinations:
            expressions = generate_expressions(num_perm, ops)
            
            for expr in expressions:
                try:
                    if abs(eval(expr) - target) < 1e-6:
                        return expr
                except ZeroDivisionError:
                    continue
    
    return "No solution"
