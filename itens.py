import random, eel, itertools
from itertools import combinations

eel.init("web")

def boss(rar) :
    nv1 = ["Baal", "Dealg", "Fenrir", "O Sábio"]
    nv2 = ["Gau"]
    nv3 = ["Oberon"]
    
    if rar == 1 : eel.printDrop(random.choice(nv1))

    elif rar == 2 : eel.printDrop(random.choice(nv2))

    elif rar == 3 : eel.printDrop(random.choice(nv3))

# Início da função de consumíveis
def dropConsu(rar):
    com = ["Bandagem Simples", "Combustível", "Incenso Simples", "Pergaminho de Identificação", "Pergaminho de Magia Comum", "Pomada Mágica" ]
    uncom = ["Bandagem Mediana", "Incenso Mediano", "Mapa Incomum", "Pergaminho de Magia Incomum", "Pergaminho de Treinamento", "Pomada Mágica Mediana", "Saco de Moedas"]
    raro = ["Bandagem Avançada", "Incenso Avançado", "Kit de Costura", "Mapa Raro", "Pergaminho de Magia Rara", "Pergaminho Dourado (Individual)", "Pomada Mágica Avançada", "Saco Grande de Moedas", "Suprimentos"]
    epic = ["Bandagem Superior", "Incenso Superior", "Mapa Épico", "Pergaminho de Magia Épica",  "Pergaminho de Ressurreição", "Pomada Mágica Superior",  "Saco Enorme de Moedas"]
    leg = ["Bandagem Excelente", "Caixa de Suprimentos", "Incenso Excelente", "Mapa do Tesouro", "Mapa Lendário", "Pergaminho de Magia Lendária", "Pergaminho Dourado (Grupo)", "Pergaminho de Ressurreição em Massa", "Pomada Mágica Excelente"]
    
    if rar == 1 : eel.printDrop(random.choice(com))

    elif rar == 2 : eel.printDrop(random.choice(uncom))

    elif rar == 3 : eel.printDrop(random.choice(raro))

    elif rar == 4 : eel.printDrop(random.choice(epic))

    else : eel.printDrop(random.choice(leg))
# Fim da função de consumíveis

# Início da função de armaduras
def dropArmor(rar):
    tipo = ["Armadura Leve", "Armadura Média", "Armadura Pesada","Escudo Pequeno", "Escudo Médio", "Escudo Grande"]
    uncom = ["Atribuída (FOR)", "Atribuída (DES)", "Atribuída (VIT)", "Atribuída (CON)", "Atribuída (INT)", "Atribuída (FÉ)", "Espaço de Runa (+1)", "Resistente (Corte)", "Resistente (Perfuração)", "Resistente (Impacto)", "Resistente (Arcano)", "Resistente (Fogo)", "Resistente (Gelo)", "Resistente (Áureo)", "Resistente (Profano)", "Resistente (Natural)", "Resistente (Sangue)", "Potência (+1)", "Fortificada (PM)", "Fortificada (PV)"]
    raro = ["Ágil", "Espaço de Runa(+2)", "Espinhenta", "Potência (+2)", "Regenerativa (PV)", "Regenerativa (PM)"]
    epic = ["Espaço de Runa(+3)", "Focada", "Potência (+3)", "Prateada"]
    leg = ["Barreira de Mana", "Dimensional", "Instável", "Protetora"]
    virg = ["",", ", ", "]
    
    if rar == 1 : eel.printDrop(random.choice(tipo))

    elif rar == 2 : eel.printDrop(random.choice(tipo) + ": " + random.choice(uncom))

    elif rar == 3 :
        n = random.randint(0, 1)
        eel.printDrop(random.choice(tipo) + ": " + random.choice(raro) + virg[n] + ", ".join(random.choice(list(itertools.combinations([*raro, *uncom], n)))))
    
    elif rar == 4 :
        n = random.randint(0, 2)
        eel.printDrop(random.choice(tipo) + ": " + random.choice(epic) + virg[n] + ", ".join(random.choice(list(itertools.combinations([*epic, *raro, *uncom], n)))))
    
    elif rar == 5 :
        n = random.randint(1, 2)
        eel.printDrop(random.choice(tipo) + ": " + random.choice(leg) + virg[n] + ", ".join(random.choice(list(itertools.combinations([*epic, *raro, *uncom], n)))))
    
    else :
        n = random.randint(1, 2)
        eel.printDrop("Armadura Única: " + ", ".join(random.choice(list(itertools.combinations([*epic, *raro, *uncom], n)))))
# Fim da função de armaduras

# Início da função de armas
def dropWeap(rar):
    tipo = ["Adaga", "Arco", "Besta", "Escopeta", "Espada Reta", "Katana", "Lança", "Machado", "Maça", "Pistola", "Rifle", "Sabre"]
    uncom = ["Composta", "Mágica (Arcano)", "Mágica (Fogo)", "Mágica (Gelo)", "Mágica (Profano)", "Mágica (Primal)", "Mágica (Sangue)", "Espaço de Runa(+1)", "Potência (+1)"]
    raro = ["Aumentada", "Espaço de Runa(+2)", "Mágica (Dourado)", "Potência (+2)", "Sanguinária", "Vampírica"]
    epic = ["Crítica", "Ecoante", "Empuxo", "Espaço de Runa(+3)", "Lancinante", "Potência (+3)", "Praguejado"]
    leg = ["Dimensional", "Enfeitiçada", "Executora", "Fúria dos Ventos", "Senciente", "Vorpal"]
    virg = ["",", ", ", "]
    
    if rar == 1 : eel.printDrop(random.choice(tipo))

    elif rar == 2 : eel.printDrop(random.choice(tipo) + ": " + random.choice(uncom))

    elif rar == 3 :
        n = random.randint(0, 1)
        eel.printDrop(random.choice(tipo) + ": " + random.choice(raro) + virg[n] + ", ".join(random.choice(list(itertools.combinations([*raro, *uncom], n)))))
    
    elif rar == 4 :
        n = random.randint(0, 2)
        eel.printDrop(random.choice(tipo) + ": " + random.choice(epic) + virg[n] + ", ".join(random.choice(list(itertools.combinations([*epic, *raro, *uncom], n)))))
    
    elif rar == 5 :
        n = random.randint(1, 2)
        eel.printDrop(random.choice(tipo) + ": " + random.choice(leg) + virg[n] + ", ".join(random.choice(list(itertools.combinations([*epic, *raro, *uncom], n)))))
    
    else :
        n = random.randint(1, 2)
        eel.printDrop("Arma Única: " + ", ".join(random.choice(list(itertools.combinations([*epic, *raro, *uncom], n)))))
# Fim da função de armas

# Início da função de magias
def dropMag(rar):
    com = ["Chamuscar", "Chicote de Vinhas", "Estaca de Gelo", "Martirizar", "Mísseis Mágicos", "Necrofagia", "Rogar Praga", "Seiva Natural", "Tiro de Sangue"]
    uncom = ["Banhar Arma", "Contra-Mágica", "Cuspe de Wyvern", "Drenagem Venosa", "Encantar Arma", "Estepe Glacial", "Foice Corrompida", "Folha Navalha"]
    raro = ["Adaga Dourada", "Bola de Fogo", "Braços do Flagelo", "Flecha Arcana", "Pacto Maligno", "Selo de Sangue", "Toque de Gelo", "Vinhas"]
    epic = ["Bandagem de Semente", "Barreira de Mana", "Conflagração Rubra", "Definhar", "Erupção", "Lança de Ouro", "Master of Puppets", "Pilar de Gelo", "Toque da Morte", "Transfusão de Sangue"]
    leg = ["Erguer os Mortos", "Florescer da Dor", "Fluxo de Mana", "Fungo Restaurador", "Meteoro", "Nevasca"]
    
    if rar == 1 : eel.printDrop("Magia: " + random.choice(com))

    elif rar == 2 : eel.printDrop("Magia: " + random.choice(uncom))

    elif rar == 3 : eel.printDrop("Magia: " + random.choice(raro))

    elif rar == 4 : eel.printDrop("Magia: " + random.choice(epic))

    elif rar == 5 : eel.printDrop("Magia: " + random.choice(leg))

    else: eel.printDrop("Magia Única")
# Fim da função de magias

# Início da função de runas
def dropRuna(rar):
    com = ["Runa de um Plebeu Comum", "Runa de Arma", "Runa de Feitiço", "Runa de Mana", "Runa de Vida", "Runa de Velocidade", "Runa de Chance", "Runa de Crítico", "Runa de Proteção Física", "Runa de Proteção Mágica"]
    uncom = ["Runa de um Soldado Sem Nome", "Banimento Acumulado", "Caçada Dupla", "Estudar Criatura", "Gun Parry", "Negar Impacto", "Perseguição Implacável", "Projeção Banida", "Sangue Flagelado"]
    raro = ["Runa de um Cavaleiro Orgulhoso", "Cleptomancia", "Fúria Mágica", "Fúria Renovada", "Golpe Debilitante", "Mais Pólvora", "Retribuição", "Trapaceiro Arcano", "Tentáculo Aprimorado"]
    epic = ["Runa de um Bravo Guerreiro", "Backstab", "Duro de Matar", "Fúria Vingativa", "Rip and Tear"]
    leg = ["Runa de um Grande Herói", "Podridão Escarlate", "Smokin' Sexy Style!!"]
    
    if rar == 1 : eel.printDrop("Runa: " + random.choice(com))

    elif rar == 2 : eel.printDrop("Runa: " + random.choice(uncom))

    elif rar == 3 : eel.printDrop("Runa: " + random.choice(raro))

    elif rar == 4 : eel.printDrop("Runa: " + random.choice(epic))

    elif rar == 5 : eel.printDrop("Runa: " + random.choice(leg))

    else : eel.printDrop("Magia Única")
# Fim da função de runas

# Início da função de tipo
def dropTipo(mob, rar):
    if mob == 1 :
    #Drop de criaturas normais
        result = random.randint(1, 100)
        if (result >= 1) and (result <= 40) : dropConsu(rar)

        elif (result >= 41) and (result <= 60) : dropArmor(rar)
            
        elif (result >= 61) and (result <= 80) : dropWeap(rar)
            
        elif (result >= 81) and (result <= 95) : dropMag(rar)
            
        else : dropRuna(rar)
            
            
    else :
    #Drop de boss ou mapa
        result = random.randint(1, 100)
        if (result >= 1) and (result <= 35) : dropArmor(rar)
            
        elif (result >= 36) and (result <= 70) : dropWeap(rar)
            
        elif (result >= 71) and (result <= 90) : dropMag(rar)
            
        else : dropRuna(rar)
# Fim da função de tipo

# Início da função de raridade
def dropRar(mob, qtd):
    while qtd !=0 :
        if mob == 1 :
        #Drop de criaturas normais
            result = random.randint(1, 100)
            if (result >= 1) and (result <= 40) : dropTipo(mob, 1)
                
            elif (result >= 41) and (result <= 70) : dropTipo(mob, 2)
                
            elif (result >= 71) and (result <= 90) : dropTipo(mob, 3)
                
            elif (result >= 91) and (result <= 99) : dropTipo(mob, 4)
                
            else :  dropTipo(mob, 5)
                
            
        else :
        # Drop de boss
            result = random.randint(1, 100)
            if (result >= 1) and (result <= 55) : dropTipo(mob, 3)
                
            elif (result >= 56) and (result <= 89) : dropTipo(mob, 4)
                
            elif (result >= 90) and (result <= 99) : dropTipo(mob, 5)
                
            else :  dropTipo(mob, 6)
                
                
        qtd-= 1
# Fim da função de raridade

# Início da função de quantidade
def dropQtd(mob):
    if mob == 1 :
        result = random.randint(1, 20)
        if (result >= 1) and (result <= 5) : eel.printDrop("Nenhum drop")
            
        elif (result >= 6) and (result <= 14) : dropRar(mob, 1)
            
        elif (result >= 15) and (result <= 18) : dropRar(mob, 2)
            
        else : dropRar(mob, 3)
            
            
    else :
        result = random.randint(1, 20)
        if (result >= 1) and (result <= 10) : dropRar(mob, 1)
            
        elif (result >= 11) and (result <= 16) : dropRar(mob, 2)
            
        else : dropRar(mob, 3)
            
# Fim da função de quantidade

# Início do menu 
@eel.expose
def dropMenu(btn, rar):
    if btn == 1 :
        dropQtd(1)
    elif btn == 2 :
        dropQtd(2)
    elif btn == 3 :
        dropTipo(2, rar)
    elif btn == 4 :
        dropMag(rar)
    elif btn == 5 :
        boss(rar)
# Fim do menu
            
# inicia o arquivo index.html
eel.start("index.html", size=(500, 500))