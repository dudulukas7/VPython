Web VPython 3.2

while True:
    operacao = input("Qual operação você deseja? soma, subtração, multiplicação (ou 'nao' para sair): ").strip().lower()
    
    if operacao == "nao":
        break

    scene = canvas(title=f"Operação: {operacao}", width=600, height=400, background=color.black)
    
    if operacao == "multiplicacao":
        x1 = float(input("Digite a componente X do vetor (A): "))
        y1 = float(input("Digite a componente Y do vetor (A): "))
        escalar = float(input("Digite o escalar: "))

        vetor1 = vec(x1, y1, 0)
        vetor_novo = vetor1 * escalar

        seta1 = arrow(pos=vec(0, 0, 0), axis=vetor1, color=color.red, shaftwidth=0.1)
        seta_nova = arrow(pos=vetor1, axis=vetor_novo - vetor1, color=color.orange, shaftwidth=0.1)

        label(pos=vetor1, text="V1", xoffset=10, yoffset=10, height=15, color=color.white, box=True)
        label(pos=vetor1 + (vetor_novo - vetor1), text="V1 * escalar", xoffset=10, yoffset=10, height=15, color=color.blue, box=True)

    elif operacao == "soma":
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

        label(pos=vetor_soma, text="Soma de Vetores", height=15, color=color.purple)

    elif operacao == "subtracao":
        x1 = float(input("Digite a componente X do vetor A: "))
        y1 = float(input("Digite a componente Y do vetor A: "))
        x2 = float(input("Digite a componente X do vetor B: "))
        y2 = float(input("Digite a componente Y do vetor B: "))

        vetor1 = vec(x1, y1, 0)
        vetor2 = vec(x2, y2, 0)
        vetor_sub = vetor1 - vetor2

        seta1 = arrow(pos=vec(0, 0, 0), axis=vetor1, color=color.red, shaftwidth=0.1, opacity=0.7)
        seta2 = arrow(pos=vec(0, 0, 0), axis=vetor2, color=color.blue, shaftwidth=0.1, opacity=0.7)
        seta_sub = arrow(pos=vetor2, axis=vetor_sub, color=color.orange, shaftwidth=0.1)

        label(pos=vetor2 + vetor_sub, text="Subtração A - B", height=15, color=color.purple)

    else:
        print("Operação inválida. Tente novamente.")