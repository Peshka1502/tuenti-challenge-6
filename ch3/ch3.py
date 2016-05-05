#!/usr/bin/env python
#
# Tuenti Challenge 6 - Challenge 3
# Taras Sotnikov

import sys

class Tape(object):
    def __init__(self,
                 input="",
                 blank_symbol = " "):
        self.__blank_symbol = blank_symbol
        self.__tape = {}
        for i in range(len(input)):
            self.__tape[i] = input[i]

        
    def __str__(self):
        return ''.join(self.__tape.values())
    
   
    def __getitem__(self,index):
        if index in self.__tape:
            return self.__tape[index]
        else:
            return self.__blank_symbol

    def __setitem__(self, pos, char):
        self.__tape[pos] = char 

        
class TuringMachine(object):
    def __init__(self, 
                 tape = "", 
                 blank_symbol = " ",
                 initial_state = "",
                 final_states = [],
                 transition_function = {}):
        self.__tape = Tape(tape, blank_symbol=blank_symbol)
        self.__head_position = 0
        self.__blank_symbol = blank_symbol
        self.__current_state = initial_state
        self.__transition_function = transition_function
        self.__final_states = final_states
        
    def show_tape(self): 
        return self.__tape
    
    def step(self):
        char_under_head = self.__tape[self.__head_position]
        x = (self.__current_state, char_under_head)
        if x in self.__transition_function:
            y = self.__transition_function[x]
            self.__tape[self.__head_position] = y[1]
            if y[2] == "R":
                 self.__head_position += 1
            elif y[2] == "L":
                self.__head_position -= 1
            self.__current_state = y[0]
            return True
        else:
            return False


tapesStart = False
ind_lvl = 0
prev_ind_lvl = 0
current_state, current_char, next_state, next_write, next_move = [None] * 5
tapes = []
transition_function = {}

while True:
    line = sys.stdin.readline()
    if not line:
        break

    if line.startswith("      "):
        ind_lvl = 3
    elif line.startswith("    "):
        ind_lvl = 2
    elif line.startswith("  "):
        ind_lvl = 1
    else:
        ind_lvl = 0

    if (ind_lvl < prev_ind_lvl) and (current_state is not None):
        if next_write is None:
            next_write = current_char
        if next_move is None:
            next_move = "N"
        if next_state is None:
            next_state = current_state

        transition_function[(current_state,current_char)] = (next_state, next_write, next_move)

        if ind_lvl < 2:
            current_state = None
        if ind_lvl < 3:
            current_char, next_move, next_write, next_state = [None] * 4

    prev_ind_lvl = ind_lvl

    line = line.strip()
    
    if line.startswith("tapes"):
        tapesStart = True
        continue

    if tapesStart:
        if ind_lvl is 1:
            aux = line.split(":")[1].strip().strip("'")
            tapes.append(aux)
    else:
        if ind_lvl is 1:
            current_state = line.split(":")[0]
        elif ind_lvl is 2:
            current_char = line.split(":")[0].strip("'")
        elif ind_lvl is 3:
            aux = line.split(":")
            operation = aux[0].strip()
            value = aux[1].strip()

            if operation == "write":
                next_write = value.strip("'")
            elif operation == "move":
                if value == "right":
                    next_move = "R"
                elif value == "left":
                    next_move = "L"
            elif operation == "state":
                next_state = value

initial_state = "start"

for i in range(0,len(tapes)):
    t = TuringMachine(tapes[i], 
                  initial_state = initial_state,
                  transition_function=transition_function)

    limit_steps = 9999999999
    j = 0
    while j < limit_steps:
        j += 1
        if not t.step():
            break

    print "Tape #%d: %s" % (i + 1, t.show_tape())