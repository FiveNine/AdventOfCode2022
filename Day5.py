input = """[V]     [B]                     [C]
[C]     [N] [G]         [W]     [P]
[W]     [C] [Q] [S]     [C]     [M]
[L]     [W] [B] [Z]     [F] [S] [V]
[R]     [G] [H] [F] [P] [V] [M] [T]
[M] [L] [R] [D] [L] [N] [P] [D] [W]
[F] [Q] [S] [C] [G] [G] [Z] [P] [N]
[Q] [D] [P] [L] [V] [D] [D] [C] [Z]
1   2   3   4   5   6   7   8   9"""
input_instructions = """move 1 from 9 to 2
move 4 from 6 to 1
move 4 from 2 to 6
move 5 from 8 to 7
move 4 from 9 to 2
move 1 from 5 to 8
move 1 from 3 to 1
move 2 from 3 to 1
move 1 from 4 to 2
move 11 from 7 to 2
move 5 from 5 to 1
move 1 from 6 to 8
move 1 from 7 to 6
move 3 from 6 to 7
move 1 from 3 to 2
move 1 from 6 to 8
move 11 from 2 to 1
move 1 from 9 to 8
move 1 from 3 to 7
move 4 from 7 to 9
move 3 from 3 to 7
move 4 from 8 to 2
move 3 from 7 to 6
move 2 from 6 to 3
move 5 from 4 to 1
move 1 from 6 to 5
move 26 from 1 to 7
move 1 from 4 to 6
move 22 from 7 to 5
move 4 from 9 to 1
move 3 from 7 to 3
move 1 from 6 to 3
move 6 from 1 to 7
move 2 from 7 to 5
move 8 from 1 to 9
move 4 from 3 to 4
move 10 from 2 to 7
move 6 from 7 to 4
move 2 from 9 to 5
move 1 from 5 to 1
move 8 from 4 to 1
move 2 from 5 to 9
move 1 from 3 to 6
move 1 from 9 to 1
move 1 from 3 to 6
move 2 from 5 to 2
move 1 from 4 to 2
move 1 from 2 to 3
move 7 from 1 to 4
move 9 from 7 to 4
move 1 from 3 to 4
move 2 from 2 to 4
move 5 from 9 to 6
move 1 from 4 to 5
move 2 from 9 to 3
move 1 from 1 to 6
move 2 from 6 to 1
move 2 from 6 to 5
move 2 from 9 to 7
move 1 from 3 to 9
move 1 from 9 to 5
move 2 from 7 to 3
move 1 from 1 to 7
move 7 from 4 to 5
move 2 from 1 to 2
move 3 from 3 to 8
move 3 from 8 to 9
move 31 from 5 to 8
move 1 from 7 to 1
move 1 from 2 to 1
move 1 from 1 to 5
move 1 from 5 to 6
move 2 from 5 to 7
move 10 from 4 to 9
move 5 from 6 to 2
move 3 from 2 to 6
move 2 from 7 to 8
move 1 from 6 to 3
move 1 from 4 to 1
move 1 from 3 to 6
move 1 from 4 to 2
move 2 from 1 to 2
move 1 from 8 to 7
move 10 from 8 to 2
move 13 from 2 to 9
move 1 from 1 to 5
move 18 from 8 to 2
move 21 from 9 to 6
move 1 from 7 to 8
move 2 from 9 to 7
move 1 from 2 to 3
move 1 from 7 to 8
move 9 from 2 to 4
move 1 from 7 to 8
move 3 from 9 to 1
move 1 from 8 to 1
move 6 from 2 to 3
move 5 from 4 to 7
move 1 from 5 to 8
move 2 from 4 to 3
move 5 from 7 to 3
move 2 from 2 to 7
move 15 from 6 to 1
move 12 from 1 to 2
move 6 from 2 to 9
move 4 from 9 to 5
move 4 from 5 to 6
move 14 from 3 to 9
move 1 from 6 to 7
move 1 from 7 to 2
move 1 from 7 to 8
move 9 from 2 to 6
move 1 from 1 to 6
move 2 from 9 to 8
move 4 from 9 to 7
move 1 from 1 to 5
move 8 from 8 to 3
move 1 from 5 to 4
move 2 from 1 to 2
move 3 from 1 to 4
move 9 from 6 to 2
move 1 from 7 to 4
move 1 from 8 to 2
move 1 from 6 to 4
move 4 from 7 to 8
move 12 from 6 to 8
move 3 from 2 to 1
move 6 from 8 to 7
move 5 from 3 to 6
move 3 from 3 to 6
move 3 from 1 to 3
move 8 from 2 to 9
move 2 from 4 to 5
move 2 from 7 to 2
move 10 from 8 to 5
move 3 from 3 to 2
move 10 from 5 to 3
move 1 from 4 to 3
move 1 from 2 to 1
move 1 from 1 to 7
move 14 from 9 to 6
move 5 from 2 to 4
move 15 from 6 to 5
move 3 from 9 to 3
move 1 from 8 to 6
move 1 from 3 to 8
move 7 from 3 to 8
move 16 from 5 to 1
move 2 from 7 to 1
move 1 from 5 to 9
move 2 from 9 to 3
move 15 from 1 to 5
move 3 from 8 to 2
move 3 from 3 to 1
move 3 from 7 to 3
move 8 from 4 to 6
move 5 from 1 to 6
move 9 from 5 to 7
move 2 from 8 to 3
move 2 from 2 to 7
move 1 from 1 to 4
move 2 from 5 to 8
move 4 from 3 to 1
move 4 from 8 to 1
move 1 from 8 to 6
move 9 from 7 to 6
move 2 from 7 to 5
move 3 from 1 to 8
move 1 from 4 to 8
move 1 from 2 to 4
move 12 from 6 to 2
move 3 from 8 to 6
move 1 from 4 to 7
move 2 from 6 to 8
move 5 from 5 to 9
move 13 from 2 to 9
move 2 from 4 to 7
move 13 from 9 to 5
move 2 from 6 to 5
move 1 from 3 to 9
move 6 from 9 to 4
move 5 from 1 to 3
move 1 from 7 to 9
move 15 from 5 to 8
move 2 from 4 to 7
move 2 from 4 to 6
move 1 from 4 to 6
move 1 from 5 to 7
move 18 from 6 to 2
move 2 from 7 to 3
move 3 from 6 to 7
move 3 from 2 to 8
move 5 from 7 to 3
move 1 from 9 to 6
move 2 from 3 to 8
move 11 from 3 to 2
move 2 from 2 to 9
move 1 from 6 to 2
move 1 from 7 to 5
move 1 from 5 to 9
move 9 from 8 to 4
move 1 from 4 to 6
move 2 from 3 to 1
move 2 from 1 to 5
move 12 from 8 to 3
move 1 from 8 to 2
move 14 from 3 to 4
move 1 from 6 to 4
move 1 from 5 to 4
move 20 from 2 to 7
move 2 from 9 to 5
move 1 from 5 to 3
move 1 from 9 to 2
move 1 from 2 to 8
move 2 from 2 to 3
move 5 from 4 to 5
move 6 from 5 to 7
move 2 from 8 to 2
move 3 from 3 to 9
move 5 from 4 to 5
move 2 from 9 to 7
move 2 from 2 to 3
move 1 from 9 to 3
move 22 from 7 to 3
move 4 from 7 to 4
move 24 from 3 to 6
move 4 from 2 to 6
move 18 from 6 to 9
move 15 from 4 to 6
move 8 from 6 to 3
move 6 from 6 to 1
move 7 from 9 to 6
move 2 from 7 to 4
move 8 from 3 to 9
move 14 from 6 to 3
move 2 from 3 to 9
move 1 from 9 to 6
move 13 from 9 to 1
move 3 from 4 to 5
move 1 from 9 to 6
move 5 from 1 to 8
move 3 from 3 to 9
move 2 from 1 to 5
move 8 from 5 to 8
move 10 from 3 to 5
move 3 from 4 to 6
move 6 from 1 to 9
move 4 from 5 to 3
move 5 from 8 to 2
move 6 from 6 to 3
move 7 from 3 to 6
move 1 from 3 to 4
move 5 from 8 to 7
move 5 from 2 to 6
move 2 from 7 to 3
move 3 from 7 to 3
move 1 from 4 to 9
move 9 from 6 to 9
move 2 from 6 to 2
move 1 from 8 to 2
move 2 from 8 to 7
move 5 from 1 to 5
move 1 from 1 to 4
move 13 from 5 to 7
move 5 from 3 to 7
move 1 from 5 to 6
move 1 from 4 to 6
move 3 from 2 to 8
move 1 from 3 to 5
move 1 from 3 to 8
move 14 from 7 to 4
move 1 from 5 to 6
move 7 from 6 to 9
move 6 from 7 to 9
move 2 from 8 to 9
move 2 from 8 to 1
move 31 from 9 to 1
move 13 from 4 to 2
move 1 from 4 to 3
move 10 from 2 to 7
move 1 from 3 to 4
move 1 from 2 to 7
move 3 from 7 to 8
move 1 from 4 to 1
move 3 from 8 to 5
move 32 from 1 to 5
move 3 from 9 to 7
move 4 from 9 to 6
move 2 from 2 to 7
move 2 from 1 to 7
move 1 from 6 to 1
move 1 from 9 to 4
move 3 from 6 to 4
move 1 from 1 to 8
move 15 from 5 to 1
move 1 from 8 to 4
move 9 from 5 to 7
move 1 from 9 to 8
move 1 from 8 to 1
move 10 from 1 to 9
move 1 from 4 to 2
move 2 from 9 to 5
move 4 from 9 to 6
move 1 from 2 to 7
move 3 from 4 to 2
move 1 from 1 to 5
move 5 from 1 to 5
move 1 from 4 to 9
move 3 from 6 to 7
move 23 from 7 to 6
move 1 from 2 to 4
move 1 from 2 to 5
move 9 from 5 to 4
move 1 from 2 to 5
move 9 from 5 to 6
move 1 from 9 to 7
move 1 from 9 to 3
move 3 from 9 to 4
move 14 from 6 to 3
move 5 from 7 to 4
move 1 from 7 to 5
move 1 from 5 to 9
move 2 from 5 to 6
move 16 from 6 to 2
move 2 from 6 to 1
move 7 from 4 to 8
move 2 from 1 to 2
move 4 from 3 to 5
move 5 from 4 to 7
move 2 from 6 to 7
move 4 from 4 to 1
move 4 from 8 to 9
move 1 from 4 to 5
move 1 from 6 to 8
move 1 from 4 to 9
move 4 from 1 to 7
move 1 from 9 to 4
move 2 from 2 to 7
move 7 from 3 to 9
move 15 from 2 to 3
move 4 from 8 to 6
move 1 from 4 to 7
move 2 from 9 to 7
move 1 from 6 to 8
move 2 from 7 to 2
move 5 from 7 to 2
move 1 from 5 to 2
move 6 from 2 to 9
move 3 from 7 to 1
move 3 from 1 to 2
move 3 from 7 to 1
move 2 from 2 to 9
move 2 from 6 to 9
move 1 from 8 to 3
move 19 from 3 to 9
move 1 from 6 to 3
move 3 from 7 to 4
move 1 from 2 to 5
move 2 from 1 to 9
move 2 from 2 to 3
move 33 from 9 to 7
move 1 from 1 to 7
move 3 from 3 to 7
move 1 from 3 to 2
move 1 from 5 to 8
move 4 from 9 to 7
move 1 from 5 to 2
move 2 from 4 to 9
move 4 from 9 to 7
move 3 from 2 to 1
move 1 from 4 to 3
move 1 from 9 to 7
move 1 from 8 to 3
move 7 from 7 to 3
move 3 from 1 to 9
move 4 from 9 to 7
move 4 from 5 to 8
move 3 from 3 to 4
move 3 from 4 to 5
move 3 from 3 to 6
move 2 from 6 to 5
move 38 from 7 to 5
move 40 from 5 to 3
move 4 from 8 to 9
move 1 from 6 to 9
move 1 from 5 to 1
move 3 from 7 to 6
move 1 from 7 to 5
move 38 from 3 to 8
move 1 from 1 to 9
move 3 from 9 to 6
move 5 from 3 to 9
move 4 from 8 to 6
move 1 from 7 to 1
move 3 from 5 to 9
move 1 from 1 to 2
move 10 from 8 to 3
move 5 from 8 to 1
move 3 from 1 to 2
move 9 from 6 to 7
move 9 from 3 to 5
move 1 from 7 to 6
move 1 from 3 to 8
move 1 from 7 to 9
move 1 from 1 to 5
move 1 from 1 to 3
move 1 from 9 to 2
move 4 from 2 to 3
move 1 from 2 to 4
move 9 from 8 to 1
move 2 from 9 to 5
move 2 from 1 to 2
move 2 from 3 to 4
move 6 from 8 to 6
move 10 from 5 to 3
move 7 from 3 to 2
move 2 from 1 to 2
move 5 from 1 to 7
move 7 from 9 to 6
move 7 from 6 to 5
move 1 from 4 to 3
move 7 from 7 to 4
move 5 from 3 to 9
move 7 from 2 to 6
move 4 from 7 to 8
move 5 from 8 to 9
move 1 from 2 to 6
move 1 from 3 to 5
move 2 from 2 to 8
move 8 from 4 to 6
move 7 from 9 to 7
move 4 from 7 to 9
move 7 from 9 to 3
move 8 from 3 to 1
move 6 from 5 to 9
move 8 from 1 to 8
move 13 from 8 to 4
move 3 from 9 to 6
move 1 from 8 to 6
move 1 from 7 to 3
move 2 from 4 to 1
move 5 from 9 to 1
move 1 from 3 to 7
move 15 from 6 to 1
move 1 from 7 to 9
move 10 from 4 to 7
move 11 from 7 to 5
move 17 from 1 to 6
move 1 from 9 to 3
move 6 from 6 to 1
move 3 from 5 to 3
move 2 from 4 to 5
move 2 from 7 to 8
move 12 from 5 to 3
move 13 from 6 to 9
move 2 from 8 to 2
move 2 from 5 to 1
move 16 from 3 to 8
move 3 from 2 to 3
move 2 from 3 to 7
move 2 from 7 to 9
move 1 from 3 to 7
move 4 from 8 to 4
move 2 from 4 to 8
move 5 from 1 to 5
move 2 from 4 to 7
move 6 from 6 to 8
move 2 from 8 to 5
move 2 from 1 to 4
move 5 from 8 to 7
move 5 from 6 to 3
move 6 from 9 to 8
move 2 from 9 to 2
move 1 from 1 to 7
move 4 from 5 to 3
move 2 from 2 to 3
move 1 from 4 to 9
move 10 from 3 to 6
move 1 from 3 to 7
move 10 from 7 to 2
move 2 from 5 to 3
move 1 from 4 to 2
move 2 from 6 to 8
move 3 from 6 to 5
move 1 from 6 to 1
move 7 from 2 to 3
move 6 from 8 to 7
move 4 from 6 to 3
move 14 from 8 to 6
move 11 from 6 to 8
move 1 from 1 to 4
move 6 from 7 to 2
move 3 from 5 to 8
move 4 from 1 to 7
move 1 from 2 to 8
move 1 from 2 to 6
move 1 from 3 to 4
move 1 from 5 to 6
move 7 from 8 to 6
move 9 from 3 to 2
move 1 from 8 to 5"""

def flip_input():
    lines = input.split('\n')
    reversed_input = ""
    i = len(lines)-1
    while i >= 0:
        reversed_input += lines[i] + '\n'
        i -= 1
    print(reversed_input)

def serialize_stacks():
    lines = input.split('\n')
    
    stacks = []
    for line in lines:
        i = 0
        if line.startswith('1'):
            for num in line.split("  "):
                stacks.append([])
            continue
        
        line = line.replace(' ', '\t')
        line = line.replace('\t\t\t\t', ' ')
        line = line.replace(' ', '\t')
        
        for crate in line.split('\t'):
            if crate != '':
                stacks[i].append(crate.strip('[').strip(']'))
            i += 1
    return stacks
    

def first():
    stacks = serialize_stacks()
    instructions = input_instructions.split('\n')
    
    for instruction in instructions:
        instruction = instruction.replace('move', '').replace('from', '').replace('to', '').split()
        
        n = int(instruction[0])
        _from = int(instruction[1])
        _to = int(instruction[2])
        
        for i in range(n):
            stacks[_to-1].append(stacks[_from-1].pop())
        
    answer = ""
    for stack in stacks:
        answer += stack.pop()
    print(answer)

def second():
    stacks = serialize_stacks()
    instructions = input_instructions.split('\n')
    
    for instruction in instructions:
        instruction = instruction.replace('move', '').replace('from', '').replace('to', '').split()
        
        n = int(instruction[0])
        _from = int(instruction[1])
        _to = int(instruction[2])
    
        new_stack = []
        for i in range(n):
            new_stack.append(stacks[_from-1].pop())
            
        for i in range(len(new_stack)):
            stacks[_to-1].append(new_stack.pop())
                
        
            
    answer = ""
    for stack in stacks:
        if stack:
            answer += stack.pop()
    print(answer)

first()
second()
