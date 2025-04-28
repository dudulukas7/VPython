Web VPython 3.2

largura =  float(input("Digite a largura inicial (m): "))
temperatura = float(input("Digite a variacao de temperatura (graus Celsius): "))
a = 29e-6
delta_L = largura * a * temperatura
largura_final = largura + delta_L

scene = canvas(title="Dilatação Linear do Chumbo", width=600, height=400, background=color.black)

barra = box(pos=vector(0, 0, 0), size=vector(10, 0.5, 0.5), color=color.red)
solo = box(pos = vector(0,-5,0), size = vector(50, 0.5, 10), color = color.blue) 
barra_nova = box(pos=vector(largura_final/2, 2, 0), size=vector(largura_final, 0.5, 0.5), color=color.yellow)