#Projecto 1
#Miguel Amaral 78694
#Luis Ferreira 83500


# Funcao que vai devolver o indice do elemento maior da lista Hond. 
# Vai servir para substituir na lista Hond o elemento correto, assim como atribuir o divisor correto.
def get_maior(Hond, nr_votos):
       maior=Hond[0]
       i=0
       size=len(Hond)
       for j in range(size):
              if Hond[j] == maior:
                     #no caso de haver duas entradas iguais na lista Hond, vai usar o maior que tem menor numero total de votos
                     if nr_votos[j] < nr_votos[i]:
                            i = j              
              if Hond[j] > maior:
                     maior = Hond[j]
                     i = j
       return i
      

# Funcao que cria os divisores iniciais, uma lista com todas as entradas a 1 (com o mesmo numero de entradas que o numero de entradas do tuplo nr_votos) 
def make_divisores(nr_votos): 
       size=len(nr_votos)
       lista=[1]
       a=1
       while a<size:
              lista += [1]
              a += 1 
       return lista


#funcao que vai transformar a lista de divisores no tuplo de mandatos, subtraindo todas as entradas por 1 
def transform(div): 
       size=len(div)
       for i in range(size):
              div[i] -= 1
       return tuple(div)
       

#Esta funcao chama a transform, a make_divisores e a get_maior, e aplica o metodo de Hond para distribuir os mandatos       
def mandatos(nr_mandatos,nr_votos):
       Hond=list(nr_votos)
       divisor=make_divisores(nr_votos) 
       while nr_mandatos != 0:
              i=get_maior(Hond,nr_votos)
              divisor[i] = divisor[i] + 1              
              Hond[i]= nr_votos[i]/divisor[i] 
              nr_mandatos = nr_mandatos - 1
       mandatos=transform(divisor)
       return mandatos
              
# Sabendo o numero de mandatos a atribuir em cada circulo (lista deputados), vai aplicar o metodo de hond nesse circulo para distribuir os deputados pelos partidos. 
#No final devolve um tuplo com o numero total de deputados que um partido tem, somando os deputados que esse partido tem em cada circulo
def assembleia(votacoes):
       assembleia=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
       #deputados a atribuir em cada circulo
       deputados=[16,3,19,3,4,9,3,9,4,10,47,2,39,9,18,6,5,9,5,6,2,2] 
       for k in range(22):
              n_mandatos=deputados[k]
              n_votos=votacoes[k]
              #devolve um tuplo com o numero de deputados em cada partido num determinado(k) circulo
              man_part_circ=mandatos(n_mandatos,n_votos)
              for w in range(15):
                     assembleia[w]=assembleia[w]+man_part_circ[w] 
       return tuple(assembleia)
       

#funcao que retorna, para o maior numero de mandatos atribuidos, o partido/coligacao correspondente
def max_mandatos(votacoes):
       partidos_list=['PDR\tPartido Democratico Republicano','PCP-PEV\tCDU - Coligacao Democratica Unitaria','PPD/PSD-CDS/PP\tPortugal a Frente','MPT\tPartido da Terra','L/TDA\tLIVRE/Tempo de Avancar','PAN\tPessoas-Animais-Natureza','PTP-MAS\tAgir','JPP\tJuntos pelo Povo','PNR\tPartido Nacional Renovador','PPM\tPartido Popular Monarquico','NC\tNos, Cidadaos!','PCTP/MRPP\tPartido Comunista dos Trabalhadores Portugueses','PS\tPartido Socialista','B.E.\tBloco de Esquerda','PURP\tPartido Unido dos Reformados e Pensionistas']
       assembl=assembleia(votacoes)
       maior=0
       c=0
       #ve o maior (ignora o empate)
       for i in range(15):
              if assembl[i]>maior:
                     maior=assembl[i]
                     c=i
       #ve se ha "dois maiores"
       for i in range(15):
              if assembl[i]==maior:
                     if i!=c:                  
                            return 'Empate tecnico'
              else:
                     partido=partidos_list[c]
       return str(partido)
