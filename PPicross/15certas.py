#Miguel Amaral 78694
#Luis Ferreira 83500
#Grupo 88

#VER tabuleiro especificacoes, cria tabuleiro, escreve tabuelrio

#TAD Coordenadas

#cria_coordenada: inteiro x inteiro -> coordenada
#coordenada vai ser um tuplo de 2 elementos, o primeiro a linha, o segundo a coluna
def cria_coordenada(lin,col):
    if isinstance(lin,int) and isinstance(col,int):
        if (lin>0) and (col>0):
            return (lin,col)
    raise ValueError ('cria_coordenada: argumentos invalidos')

#coordenada_linha: coordenada -> inteiro
#seleciona a linha da coordenada
def coordenada_linha(cord):
    return cord[0]

#coordenada_coluna: coordenada -> inteiro
#seleciona a coluna da coordenada
def coordenada_coluna(cord):
    return cord[1]

#e_coordenada: universal -> logico
#verifica se e coordenada
def e_coordenada(arg):
    if isinstance(arg,tuple):
        if len(arg) == 2:
            if isinstance (coordenada_linha(arg),int) and isinstance (coordenada_coluna(arg),int):
                if coordenada_linha(arg)>0 and coordenada_coluna(arg)>0:
                    return True
    return False

#coordenadas_iguais : coordenada x coordenada -> logico
#ve se duas coordenadas sao iguais
def coordenadas_iguais(cord1,cord2):
    return (coordenada_linha(cord1) == coordenada_linha(cord2)) and (coordenada_coluna(cord1) == coordenada_coluna(cord2))

#coordenada_para_cadeia : coordenada -> cadeia de caracteres
def coordenada_para_cadeia(cord):
    return "("+str(coordenada_linha(cord))+" : "+str(coordenada_coluna(cord))+")"
   

#TAD Tabuleiro

#cria_tabuleiro: tuplo -> tabuleiro
#tabuleiro vai ser uma lista de 3 elementos, o primeiro um tuplo correspondende as especificacoes das linhas, o segundo um tuplo correspondente as especificacoes das colunas, e o terceiro, uma lista que vai ser o tabuleiro em si, dentro desta lista, vamos ter n listas com m elementos cada uma, em que as n listas sao as linhas, e os m elementos correspondem as colunas dentro dessa linha. Neste caso e especificado que n vai ser igual a m.
def cria_tabuleiro(tuplo):
    if not isinstance(tuplo,tuple):
        raise ValueError('cria_tabuleiro: argumentos invalidos')
    if not len(tuplo)==2:
        raise ValueError('cria_tabuleiro: argumentos invalidos')
    if len(tuplo[0]) != len(tuplo[1]):
        raise ValueError('cria_tabuleiro: argumentos invalidos')
    for a in (tuplo[0] or tuplo[1]):
        if not isinstance(a,tuple):
            raise ValueError('cria_tabuleiro: argumentos invalidos')
        for b in a:
            if not isinstance(b,int):
                raise ValueError('cria_tabuleiro: argumentos invalidos')
            if b<0:
                raise ValueError('cria_tabuleiro: argumentos invalidos')
            if b==0:
                if len(a)!=1:
                    raise ValueError('cria_tabuleiro: argumentos invalidos')      
    tabuleiro=[]
    cria_lista=[0]
    size=len(tuplo[0])
    for i in range(size):
        tabuleiro=tabuleiro+[cria_lista]
    for e in range(size):
        for i in range(size-1):
            tabuleiro[e]=tabuleiro[e]+cria_lista
    return [tuplo[0],tuplo[1],tabuleiro]

#tabuleiro_dimensoes: tabuleiro -> tuplo
#ve a dimensao do tabuleiro, atravez das especificacoes do tabuleiro
def tabuleiro_dimensoes(tabuleiro):
    return (len(esp_linha(tabuleiro)),len(esp_col(tabuleiro)))

#select_dim_linha
#seleciona a dimensao da linha(que neste caso e sempre e igual a da coluna)
def dim_l(tabuleiro):
    return tabuleiro_dimensoes(tabuleiro)[0]

#select_dim_coluna
#seleciona a dimensao da coluna(que neste caso e sempre e igual a da linha)
def dim_c(tabuleiro):
    return tabuleiro_dimensoes(tabuleiro)[1]

# tabuleiro_especificacoes: tabuleiro -> tuplo
#seleciona as especificacoes do tabuleiro
def tabuleiro_especificacoes(tabuleiro):
    return (tabuleiro[0],tabuleiro[1])

#esp_linha: tabuleiro->tuplo
#seleciona as especificacoes das linhas
def esp_linha(tabuleiro):
    return tabuleiro_especificacoes(tabuleiro)[0]

#esp_col: tabuleiro->tuplo
#seleciona as especificacoes das colunas
def esp_col(tabuleiro):
    return tabuleiro_especificacoes(tabuleiro)[1]

# select_esp_linha: tabuleiro x inteiro -> tuplo
#seleciona a especificacao de uma linha "especificada" pelo inteiro
def select_esp_linha (tabuleiro, linha):
    return esp_linha(tabuleiro)[linha-1]

# select_esp_col: tabuleiro x inteiro -> tuplo
#seleciona a especificacao de uma coluna "especificada" pelo inteiro
def select_esp_col (tabuleiro, col):
    return esp_col(tabuleiro)[col-1]

#select_tabuleiro: tabuleiro-> lista
#seleciona so o tabuleiro em si, sem as especificacoes
def select_tabuleiro(tabuleiro):
    return tabuleiro[2]

# select_linha_tab: tabuleiro x inteiro -> lista
#seleciona a lista correspondente a linha, especificada pelo inteiro
def select_linha_tab (tabuleiro,linha):
    return select_tabuleiro(tabuleiro)[linha-1]

# select_col_tab: tabuleiro x inteiro -> lista
#cria uma lista nova que correspondente a uma coluna, especificada pelo inteiro
def select_col_tab (tabuleiro,coluna):
    col=[]
    for i in range(1,dim_c(tabuleiro)+1):
        col=col+[select_linha_tab(tabuleiro,i)[coluna-1]]
    return col

#tabuleiro_celula: tabuleiro x coordenada-> {0,1,2}
#devolve o valor que uma coordenada tem no tabuleiro
def tabuleiro_celula(tabuleiro,coordenada):
    if not (e_coordenada(coordenada) or e_tabuleiro(tabuleiro)):
        raise ValueError('tabuleiro_celula: argumentos invalidos')
    if coordenada_linha(coordenada)>dim_l(tabuleiro) or coordenada_coluna(coordenada)>dim_l(tabuleiro):
        raise ValueError('tabuleiro_celula: argumentos invalidos')
    return select_linha_tab(tabuleiro,coordenada_linha(coordenada))[coordenada_coluna(coordenada)-1]

#tabuleiro_preenche_celula: tabuleiro x coordenada x {0,1,2} -> tabuleiro
#muda o valor que uma coordenada tem no tabuleiro
def tabuleiro_preenche_celula(tabuleiro,coordenada,val):
    if not e_coordenada(coordenada) or not e_tabuleiro(tabuleiro) or val not in (0,1,2):
        raise ValueError('tabuleiro_preenche_celula: argumentos invalidos')
    if coordenada_linha(coordenada)>dim_l(tabuleiro) or coordenada_coluna(coordenada)>dim_c(tabuleiro):
        raise ValueError('tabuleiro_preenche_celula: argumentos invalidos')  
    select_linha_tab(tabuleiro,coordenada_linha(coordenada))[coordenada_coluna(coordenada)-1]=val
    return tabuleiro
    
   
#e_tabuleiro: universal -> logico
#ve se e um tabuleiro
def e_tabuleiro(tabuleiro):
    if not isinstance(tabuleiro,list):
        return False
    if len(tabuleiro)!=3:
        return False
    if not isinstance(select_tabuleiro(tabuleiro),list) or not isinstance(esp_linha(tabuleiro),tuple) or not isinstance(esp_col(tabuleiro),tuple):
        return False
    if not(dim_l(tabuleiro)==dim_c(tabuleiro)==len(select_tabuleiro(tabuleiro))):
        return False
    for i in range(1,dim_l(tabuleiro)+1):
        if not isinstance(select_linha_tab(tabuleiro,i),list):
            return False
        if not len(select_linha_tab(tabuleiro,i))==dim_c(tabuleiro):
            return False
        for valor in select_linha_tab(tabuleiro,i):
            if valor not in (0,1,2):
                return False
        if not (isinstance(select_esp_linha(tabuleiro,i),tuple) or isinstance(select_esp_col(tabuleiro,i))):
                return False
        for esp in (select_esp_linha(tabuleiro,i)):
                if not (isinstance(esp, int)):
                    return False 
                if esp <0:
                    return False
                if esp==0:
                    if len(select_esp_linha(tabuleiro,i) )!=1:
                        return False
        for esp in (select_esp_col(tabuleiro,i)):
            if not (isinstance(esp, int)):
                return False 
            if esp <0:
                return False
            if esp==0:
                if len(select_esp_linha(tabuleiro,i) )!=1:
                    return False
    return True

#tabuleiro com celulas vazias: tabuleiro ->logico
#ve se o tabuleiro tem celulas vazias (se tiver, devolve True)
def tabuleiro_celulas_vazias(tabuleiro):
    for i in range(1,dim_l(tabuleiro)+1):
        for k in select_linha_tab(tabuleiro,i):
            if not e_valor(k):
                return True
    return False

#lista(linha ou coluna) x esp (linha ou coluna) ->logico
#recebe uma lista(que pode ser uma linha ou uma coluna) e a especificacao dessa lista, e ve se correspondem (criando uma especificacao nova correspondente a lista, e comparando com a real) 
def lista_completa(lista,esp):
    size=len(lista)
    verifica=[0]
    for k in range(size):
        if lista[k]==1:
            if verifica[len(verifica)-1]!=0:
                verifica=verifica+[0]
            if k+1==size:
                if verifica[len(verifica)-1]==0:
                    del verifica[len(verifica)-1]                            
        if lista[k]==2:
            verifica[len(verifica)-1]=verifica[len(verifica)-1]+1
    if tuple(verifica)!=esp:
            return False
        
#tabuleiro_completo: tabuleiro->logico
#ve se as linhas e colunas correspondem a sua especificacao, vendo primeiro se tem valor em branco (funcao tabuleiro_celulas_vazias), e depois se cada uma das linhas/colunas corresponde a especificacao(funcao lista_completa)
def tabuleiro_completo(tabuleiro):
    if tabuleiro_celulas_vazias(tabuleiro):
        return False
    for a in range(dim_l(tabuleiro)):
        if lista_completa(select_linha_tab(tabuleiro,a+1),select_esp_linha(tabuleiro,a+1))==False:
            return False
    for b in range(dim_c(tabuleiro)):
        if lista_completa(select_col_tab(tabuleiro,b+1),select_esp_col(tabuleiro,b+1))==False:
            return False
    return True
          
#tabuleiros iguais: tabuleiro x tabuleiro -> logico
#ve se os tabuleiros sao iguais
def tabuleiros_iguais(tabuleiro1,tabuleiro2):     
    return tabuleiro1==tabuleiro2

#escreve tabuleiro: tabuleiro -> cadeia de caracteres
#recebe um tabuleiro, e escreve-o
def escreve_tabuleiro(tabuleiro):
    cc=''
    b=max_esp_col(esp_col(tabuleiro),1)
    while b!=0:
        for i in range(1,dim_c(tabuleiro)+1):
            if len(select_esp_col(tabuleiro,i))>=b:
                cc=cc+'  '+str(select_esp_col(tabuleiro,i)[len(select_esp_col(tabuleiro,i))-b])+'  ' 
            else:
                cc=cc+'     '
        b=b-1
        cc=cc+'  '+'\n'
    for i in range(1,dim_l(tabuleiro)+1):        
        for d in select_linha_tab(tabuleiro,i):
            if d==0:
                cc=cc+ '[ ? ]'
            if d==1:
                cc=cc+'[ . ]'
            if d==2:
                cc=cc+'[ x ]'
        for p in select_esp_linha(tabuleiro,i):
            cc= cc+' '+str(p)            
        cc=cc+('  '*(max_esp_linhas(esp_linha(tabuleiro),1)-len(select_esp_linha(tabuleiro,i))))+'|\n' 
    return print(cc)

#devolve o valor do maior comprimento das especificacoes das colunas
def max_esp_col(esp_col,b):
    for a in esp_col:
        if len(a)>b:
            b=len(a)
    return b

#devolve o valor do maior comprimento das especificacoes das linhas
def max_esp_linhas(esp_linha,b):
    for a in esp_linha:
        if len(a)>b:
            b=len(a)
    return b        
        
#TAD jogada

#cria_jogada: coordenada x {1,2} -> jogada
#a jogada vai ser um tuplo de dois elementos, o primeiro a coordenada, e o segundo o valor
def cria_jogada(cord,inteiro):
    if not (e_coordenada(cord) or isinstance(inteiro,int)):
        raise ValueError('cria_jogada: argumentos invalidos')
    if not e_valor(inteiro):
        raise ValueError('cria_jogada: argumentos invalidos')
    return (cord,inteiro)

#jogada_coordenada: jogada -> coordenada
#seleciona a coordenada da jogada
def jogada_coordenada(jogada):
    return jogada[0]

#jogada_valor: jogada -> {1,2}
#seleciona o valor da jogada
def jogada_valor(jogada):
    return jogada[1]

#e valor(1,2)->logico
#ve se o valor e 1 ou 2
def e_valor(valor):
    if isinstance(valor, int):
        if valor in (1,2):
            return True
    return False

         
#e_jogada: universal -> logico
#ve se o argumento e uma jogada
def e_jogada(arg):
    if not isinstance(arg,tuple):
        return False
    if len(arg)!=2:
        return False
    if e_coordenada(jogada_coordenada(arg))==False:
        return False
    if e_valor(jogada_valor(arg))==False:
        return False
    return True

#jogadas_iguais: jogada x jogada -> logico
#ve se duas jogadas sao iguais
def jogadas_iguais(jogada1,jogada2):
    return jogada1 == jogada2
   

#jogada_para_cadeia: jogada -> cad. caracteres
#escreve a jogada 
def jogada_para_cadeia(jogada):
    return (coordenada_para_cadeia(jogada_coordenada(jogada))+ " --> " + str(jogada_valor(jogada)))

#Funcoes Adicionais

#le_tabuleiro: cc->tuplo
#recebe o nome do ficheiro, e transforma a string (correspondente ao conteudo do ficheiro) num tuplo com as especificacoes para um tabuleiro
def le_tabuleiro(ficheiro):
    f=open(ficheiro, 'r')
    fich=f.readlines()[0]
    f.close()
    return l_t(fich,1,"",())

#funcao auxiliar da le tabuleiro
def l_t(fich,x,st,esp):
    if len(esp)==2:
        return esp
    for a in range(x,len(fich)):
        if not (fich[a]==fich[a+1]==")"):
            st=st+fich[a]
        else:
            st=st+"))"
            esp=esp+(str_tpl_tpls(st,[]),)
            return l_t(fich,a+3,"",esp)
           

#recebe um tuplo em forma de string, e devolve esse tuplo   
def str_tuple(string,tuplo,n):
    for a in range(1,len(string)):
        if string[a] not in ("(",")",","):
            n=n+eval(string[a])
            if string[a+1] not in ("(",")",",") :
                n=n*10            
            else:
                tuplo=tuplo+(n,)
                n=0
    return tuplo

#recebe um tuplo de tuplos em forma de string, e devolve esse tuplo de tuplos
def str_tpl_tpls(string,lista):
    for a in range(1,len(string)-1):
        if string[a]=="(":
            st="("
            while string[a]!=")":
                st=st+string[a]
                a=a+1
            st=st+")"
            lista=lista+[str_tuple(st,(),0)]
    return tuple(lista)

#pede jogada: tabuleiro->jogada  
#recebe um tabuleiro, e pede input de uma coordenada e de um valor, se a coordenada for uma coordenada, mas que esteja fora das dimensoes do tabuleiro, devolve False, se for uma coordenada um valor corretos, devolve a jogada correspondente, a funcao nao esta definida para os restantes casos
def pede_jogada(tabuleiro):
    coordenada=cadeia_para_cord(input("Introduza a jogada\n- coordenada entre (1 : 1) e "+coordenada_para_cadeia(cria_coordenada(dim_l(tabuleiro),dim_c(tabuleiro)))
+" >> "),())
    valor=eval(input("- valor >> "))
    if e_coordenada(coordenada):
        if e_jogada(cria_jogada(coordenada,valor)):
            if coordenada_linha(coordenada)<=dim_l(tabuleiro) and coordenada_coluna(coordenada)<=dim_l(tabuleiro):
                return cria_jogada(coordenada,valor)
            else:
                return False
            
#recebe um coordenada em forma de string e devolve essa coordenada  
def cadeia_para_cord(cc,coordenada):
    return cad_cord(1,cc,coordenada,"")

#funcao auxiliar da cadeia_para_cord
def cad_cord(x,cc,coordenada,valor):
    if len(coordenada)==2:
        return coordenada
    for a in range(x,len(cc)):
        if cc[a] not in (" ",")"):
            valor=valor+cc[a]
        else:
            return cad_cord(a+3,cc,coordenada+(eval(valor),),"")
#jogo de picross, enquanto o jogo tiver celulas em branco, continua a pedir jogadas, caso contrario, ve se o jogo esta conforme as especificacoes e devolve o resultado correspondente. se a coordenada estiver fora do tabuleiro, pede nova jogada, mas se o valor estiver errado, o cria_jogada da erro e o jogo acaba.
def jogo_picross(ficheiro):
    tabuleiro=cria_tabuleiro(le_tabuleiro(ficheiro))
    print ("JOGO PICROSS")
    escreve_tabuleiro(tabuleiro)    
    while tabuleiro_celulas_vazias(tabuleiro):
        j=pede_jogada(tabuleiro)         
        if e_jogada(j):
            escreve_tabuleiro(tabuleiro_preenche_celula(tabuleiro,jogada_coordenada(j),jogada_valor(j)))
        else:
            print("Jogada invalida.")     
    if tabuleiro_completo(tabuleiro)==False:
        print("JOGO: O tabuleiro nao esta correto!")
        return False
    else:
        print("JOGO: Parabens, encontrou a solucao!")
        return True