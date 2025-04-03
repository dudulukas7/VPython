Web VPython 3.2   

scene = canvas(title="Soma de Vetores", width=600, height=400, background=color.black)  

x1 = float(input("Digite a componente X do primeiro vetor: "))  
y1 = float(input("Digite a componente Y do primeiro vetor: "))  
x2 = float(input("Digite a componente X do segundo vetor: "))  
y2 = float(input("Digite a componente Y do segundo vetor: "))  
vetor1 = vec(x1, y1, 0)  
vetor2 = vec(x2, y2, 0) 
vetor_soma = vetor1 + vetor2  
 
