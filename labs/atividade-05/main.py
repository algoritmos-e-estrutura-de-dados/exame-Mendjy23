def maximizar_troca_de_figurinhas(figurinhas_da_maria, figurinhas_do_joao):
  c = Node
  while c != 0:
    figurinhas_da_maria = figurinhas_do_joao
    figurinhas_do_joao = c
    return figurinhas_do_joao
    
   
  





if __name__ == '__main__':
  A, B = input().split(' ')
  figurinhas_da_maria = input().split(' ')
  figurinhas_da_joao = input().split(' ')
  maximizar_troca_de_figurinhas(figurinhas_da_maria, 
 figurinhas_da_joao)
