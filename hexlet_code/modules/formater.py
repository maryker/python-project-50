from generate_diff import gen

def stylish(value, replace=' ', repeat=2):
    
    def diff(dict, val, depth):
        new_diff = []
        if '-' in dict:
            new_diff.append(f'{replace*(depth*repeat-2)}- {val}: ' + to_str(dict['-'], depth+1))
        elif '+' in dict:
            new_diff.append(f'{replace*(depth*repeat-2)}+ {val}: '+ to_str(dict['+'], depth+1))
        else:
            new_diff.append(f'{replace*(depth*repeat-2)}  {val}: ' + to_str(dict, depth+1))
        return '\n'.join(new_diff)
    
    def to_str(item, depth):
        result = []
        if isinstance(item, dict):
            result.append('{\n')
            for key, val in item.items():
                if isinstance(val, dict):
                    result.append(diff(val, key, depth+1) + '\n')
                else:
                    result.append(f'{replace*((depth+1)*repeat-2)}  {key}: {val}\n')
            result.append(f'{replace*repeat*(depth-1)}'+'}')
        else:
            result.append(str(item))
        return ''.join(result)

    return ''.join(to_str(value, 1))

