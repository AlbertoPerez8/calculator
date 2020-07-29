import math
import sys, os
from numpy import log as ln

class Calculator:
    def __init__(self):
        self.memory = []
        self.clear_screen()
        print("Ready to calculate:\n")
        self.terminal()

# * Arithmetic Functions:

    def add(self,x,y):
        result = x + y
        self.memory.append(f'{x} + {y} = {result}')
        self.memory.append(result)
        return result

    def sub(self,x,y):
        result = x - y
        self.memory.append(f'{x} - {y} = {result}')
        self.memory.append(result)
        return result

    def Multiply(self,x,y):
        result =  x*y
        self.memory.append(f'{x} * {y} = {result}')
        self.memory.append(result)
        return result

    def Divide(self,x,y):        
        if(y == 0):
            self.memory.append(f'{x} / {y} = error')
            self.memory.append(math.nan)
            return 'error'
        else:
            result = x/y
            self.memory.append(f'{x} / {y} = {result}')
            self.memory.append(result)
            return result
    
    def Pow(self,x,y):
        result =  x**y
        self.memory.append(f'{x} ^ {y} = {result}')
        self.memory.append(result)
        return result
    
    def squate_root(self,x):
        result =  math.sqrt(x)
        self.memory.append(f'sqrt({x}) = {result}')
        self.memory.append(result)
        return result

# * Trigonometric Functions:

    def sine(self,x):
        result =  math.sin(x)
        self.memory.append(f'sine({x}) = {result}')
        self.memory.append(result)
        return result

    def cosine(self,x):
        result =  math.cos(x)
        self.memory.append(f'cosine({x}) = {result}')
        self.memory.append(result)
        return result

    def tangent(self,x):
        result =  math.tan(x)
        self.memory.append(f'tangent({x}) = {result}')
        self.memory.append(result)
        return result

# * Exponential Functions:

    def exponential(self,x):
        result =  math.exp(x)
        self.memory.append(f'e ^ ({x}) = {result}')
        self.memory.append(result)
        return result

    # log base 10
    def logarithm(self,x):
        result =  math.log(x)
        self.memory.append(f'log({x}) = {result}')
        self.memory.append(result)
        return result

    def natLog(self,x):
        result = ln(x)
        self.memory.append(f'ln({x}) = {result}')
        self.memory.append(result)
        return result

# * Calculator history functions:

    def show_history(self):
        for i in range(0,len(self.memory),2):
            print(f'{self.memory[i]}, {self.memory[i+1]}')
        print('\n')

    
    def recall_last_op(self):
        print('Last Operation:\t Result:')
        print(f'{self.memory[-2]}\t {self.memory[-1]}\n')

    def clear_memory(self):
        self.memory = []

    def clear_screen(self):
        os.system('clear')
# * Terminal functions:

    def single(self,string):
        op = string.split('(')
        op = op[1].split(')')
        val = float(op[0])
        return val
    
    def multiple(self, string = []):
        a = string[0]
        b = string[2]
        return a,b

    def terminal(self):
        x = input()
        if x == 'clear':
            self.clear_screen()
            self.terminal()

        elif x == 'exit' or x == 'close':
            sys.exit()

        elif x == "clear history":
            self.clear_memory()
            self.terminal()

        elif x == "last":
            self.recall_last_op()
            self.terminal()

        elif x == "history":
            self.show_history()
            self.terminal()

        else:
            op = x.split()
            if len(op) == 1:
                if 'sin' in x:
                    val = self.single(x)
                    result = self.sine(val)
                    print(result,'\n')
                    self.terminal() 
                elif 'cos' in x:
                    val = self.single(x)
                    result = self.cosine(val)
                    print(result,'\n')
                    self.terminal() 
                elif 'tan' in x:
                    val = self.single(x)
                    result = self.tangent(val)
                    print(result,'\n')
                    self.terminal() 
                
                elif 'log' in x:
                    val = self.single(x)
                    result = self.logarithm(val)
                    print(result,'\n')
                    self.terminal() 
                
                elif 'ln' in x:
                    val = self.single(x)
                    result = self.natLog(val)
                    print(result,'\n')
                    self.terminal() 
                
                elif 'sqrt' in x:
                    val = self.single(x)
                    result = self.squate_root(val)
                    print(result, '\n')
                    self.terminal()

                elif 'e' in x:
                    val = self.single(x)
                    result = self.exponential(val)
                    print(result, '\n')
                    self.terminal()
                
                else:
                    print(x)
                    self.terminal()
            
            symbol = op[1]
            if symbol == '+':
                a,b = self.multiple(op)
                result = self.add(a,b)
                print(result, '\n')
                self.terminal()
            
            elif symbol == '-':
                a,b = self.multiple(op)
                result = self.sub(a,b)
                print(result, '\n')
                self.terminal()
            
            elif symbol == '*':
                a,b = self.multiple(op)
                result = self.Multiply(a,b)
                print(result, '\n')
                self.terminal()

            elif symbol == '/':
                a,b = self.multiple(op)
                result = self.Divide(a,b)
                print(result, '\n')
                self.terminal()

            elif symbol == '^':
                a,b = self.multiple(op)
                result = self.Pow(a,b)
                print(result, '\n')
                self.terminal()

            else:
                print('Error')
                self.terminal() 
    


c = Calculator()
