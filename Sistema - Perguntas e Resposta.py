perguntas = {
    'Pergunta 1':{  # Pergunta mãe, são as primeiras chaves.
        'pergunta': 'Quanto é 2+2? ',  # Pergunta subnivel são as perguntas dentro da primeira chave.
        'resposta': {'a': '1', 'b': '4', 'c': '22',},
        'resposta_certa': 'b'
    },
    'Pergunta 2':{
        'pergunta': 'Quem roeu a roupa do rei de roma? ',
        'resposta': {'a': 'gato', 'b': 'cachorro', 'c': 'rato',},
        'resposta_certa': 'c'
    },
    'Pergunta 3':{
        'pergunta': 'Qual a data do dia da independência do Brasil? ',
        'resposta': {'a': '7 de setembro', 'b': '25 de dezembro', 'c': '1 de janeiro',},
        'resposta_certa': 'a'
    },
}

for perg_mae, perg_subnivel in perguntas.items():
    print(f'{perg_mae}: {perg_subnivel["pergunta"]}')
    print('Escolha uma alternativa abaixo')
    for abc, valabc in perg_subnivel['resposta'].items():
        print(f'[{abc}]: {valabc}')

    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == perg_subnivel['resposta_certa']:
        print('Aeee, parabêns a resposta está correta!')
    else:
        print('Hmm, você precisa estudar mais.')
    print()
