Web VPython 3.2   

from vpython import *  

scene = canvas(title="Subtração de Vetores", width=600, height=400, background=color.black)  

x1 = float(input("Digite a componente X do primeiro vetor (A): "))  
y1 = float(input("Digite a componente Y do primeiro vetor (A): "))  
x2 = float(input("Digite a componente X do segundo vetor (B): "))  
y2 = float(input("Digite a componente Y do segundo vetor (B): "))  

vetor1 = vec(x1, y1, 0)  
vetor2 = vec(x2, y2, 0)  
vetor_sub = vetor1 - vetor2  

seta1 = arrow(pos=vec(0, 0, 0), axis=vetor1, color=color.red, shaftwidth=0.1, opacity=0.7)  
seta2 = arrow(pos=vec(0, 0, 0), axis=vetor2, color=color.blue, shaftwidth=0.1, opacity=0.7)  
seta_sub = arrow(pos=vetor2, axis=vetor_sub, color=color.orange, shaftwidth=0.1)  

label(pos=vec(2, 5, 0), text="Subtração de Vetores (A - B)!", height=15, color=color.purple)  
