Web VPython 3.2   

scene = canvas(title="Soma de Vetores", width=600, height=400, background=color.black)  

x1 = float(input("Digite a componente X do primeiro vetor: "))  
y1 = float(input("Digite a componente Y do primeiro vetor: "))  
x2 = float(input("Digite a componente X do segundo vetor: "))  
y2 = float(input("Digite a componente Y do segundo vetor: "))  
vetor1 = vec(x1, y1, 0)  
vetor2 = vec(x2, y2, 0) 
vetor_soma = vetor1 + vetor2  

seta1 = arrow(pos=vec(0, 0, 0), axis=vetor1, color=color.red, shaftwidth=0.1, opacity=0.7)  
seta2 = arrow(pos=vetor1, axis=vetor2, color=color.blue, shaftwidth=0.1, opacity=0.7)  
seta_soma = arrow(pos=vec(0, 0, 0), axis=vetor_soma, color=color.orange, shaftwidth=0.1) 

label(pos=vec(2, 5, 0), text="Soma de Vetores Completa!", height=15, color=color.purple)
