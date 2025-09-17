def calcula_media(nota1, nota2, nota3, nota4):
    media = nota1 + nota2 + nota3 + nota4 
    media_do_aluno = media/4
    return media_do_aluno



def tabela_nota(nota):
    if nota > 5:
        return 'aprovado'
    
    elif nota >= 4:
        return 'recuperação'
    
    else:
        return 'reprovado'