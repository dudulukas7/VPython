Web VPython 3.2   

scene = canvas(title="Multiplicação por um Escalar", width=600, height=400, background=color.black)  

x1 = float(input("Digite a componente X do primeiro vetor (A): "))   
y1 = float(input("Digite a componente X do segundo vetor (B): "))  
escalar = float (input("Digite o escalar: "))

vetor1 = vec(x1, y1, 0)  
vetor_novo = vetor1 * escalar 

seta1 = arrow(pos=vec(0, 0, 0), axis=vetor1, color=color.red, shaftwidth=0.1)   
seta_nova = arrow(pos=vetor1 * escalar , axis=vetor_novo, color=color.orange, shaftwidth=0.1)  

label(pos=vetor1, text="V1", xoffset=10, yoffset=10, height=15, color=color.white, box=False)
label(pos=vetor_novo, text="V1 * escalar", xoffset=10, yoffset=10, height=15, color=color.blue, box=False)
