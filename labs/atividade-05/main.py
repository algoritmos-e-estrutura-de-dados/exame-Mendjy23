def maximizar_troca_de_figurinhas(figurinhas_da_maria, figurinhas_do_joao):
  i = 0
   
  if len(figurinhas_da_maria) < len(figurinhas_do_joao):
    for i in range(len(figurinhas_da_maria)):
      for z in range(len(figurinhas_do_joao)):
        if figurinhas_da_maria[i] == figurinhas_do_joao[z]:
          i += 1
          name = len(figurinhas_da_maria) - i

  elif len(figurinhas_do_joao) < len(figurinhas_da_maria):
      for i in range(len(figurinhas_do_joao)):
        for z in range(len(figurinhas_da_maria)):
          if figurinhas_do_joao[i] == figurinhas_da_maria[z]:
            i += 1
      name = len(figurinhas_do_joao) - i

      return name





if __name__ == '__main__':
  A, B = input().split(' ')
  figurinhas_da_maria = input().split(' ')
  figurinhas_da_joao = input().split(' ')
  maximizar_troca_de_figurinhas(figurinhas_da_maria, figurinhas_da_joao)
