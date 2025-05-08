Web VPython 3.2

largura = float(input("Digite a largura inicial (m): "))
temperatura = float(input("Digite a variacao de temperatura (graus Celsius): "))
a = 18e-6

delta_L = largura * a * temperatura
largura_final = largura + delta_L

scene = canvas(title="Dilatação Linear do Cobre", width=600, height=400, background=color.black)

solo = box(pos=vector(0, -1, 0), size=vector(100, 0.2, 10), color=color.blue)

barra = cylinder(pos=vec(-largura/2 - 1, 0, 0), axis=vec(largura, 0, 0), radius=0.5, color=color.cyan)

barra_nova = cylinder(pos=vec(largura_final/2 + 1, 0, 0), axis=vec(largura_final, 0, 0), radius=0.5, color=color.white)


