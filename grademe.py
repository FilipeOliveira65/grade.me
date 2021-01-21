from time import sleep
from datetime import datetime

# funções e variáveis para serem acionadas posteriormente
def error_message():
    print('\033[1;31mOOPS, opção inválida.\033[m')
    
def no_note():
    print('\033[1;31mA nota média tem que ser maior que 0!\033[m')
    
def login():
    name = str(input('Digite seu nome: '))
    key = int(input('Digite sua senha de login: '))
    
def var_alunos():
    soma = 0
    nota = 0
    ND = 0
    ED = 0
    D = 0
    menções = list()
    matérias = list()
    task = list()
    
    
hora_atual = datetime.now()
hora = hora_atual.strftime('%H')
hora_int = hora_atual.strftime('%H:%M')
# iníio da aplicação
função = str(input('''\033[36m=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
VOCÊ É: A- aluno | P- Professor(a): \033[m''')).upper()

if função not in "AaPp" or função == ' ':
    while True:
        print()
        função = str(input('\033[1;31mOpção inválida.\033[m \033[36mVOCÊ É: A- aluno | P- Professor(a):\033[m ')).upper()
        if função in "Aa" or função in "Pp":
            break

if função == 'A':
    # sistema do aluno
    var_alunos()

    
    #cabeçalho com opções
    print()
    print("\033[31m           !!!ATENÇÃO!!!\033[m")
    print('''\033[33mESTE PROGRAMA É PARA VOCÊ TER UMA BASE
DE QUAIS SERÃO AS NOTAS QUE ESTARÃO NO
SEU BOLETIM E, BASEADO NELAS, SE VOCÊ
IRÁ PASSAR DE ANO OU NÃO.\033[m''')
    print()
    if hora < '12':
        print('\033[33mBOM DIA!!!\033[m')
        print(f'AGORA SÃO: {hora_int}')
        print('\033[32mEspero que seu dia tenha começado bem!\033[m')
        print()
    elif hora >= '12' and hora < '18':
        print('\033[34mBOA TARDE!!!\033[m')
        print(f'AGORA SÃO: {hora_int}')
        print('\033[32mEspero que seu dia esteja ótimo!\033[m')
    elif hora >= '18':
        print('\033[35mBOA NOITE!!!\033[m')
        print(f'AGORA SÃO: {hora_int}')
        print('\033[32mSei que tudo pode estar tão difícil, mas tente se acalmar e descansar um pouco!\033[m')
        print('\033[33mAmanhã será um dia muito produtivo.\033[m')
        
    print()    
    sleep(7)
    continuar = input('\033[34mAperte QUALQUER tecla para continuar\33[m')
    print()
    
    print('\033[35mPreencha algumas informações para melhor experiência!\033[m')
    
    print()
    continuar = input('\033[34mAperte QUALQUER tecla para continuar\033[m')
    # sistema de avaliação
    print()
    
    print('''\033[32m=-=-=-=Sistema de avaliação=-=-=-=
[T]- Tarefas                   
[A]- Atividades                
=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=\033[m''')
    print()
    sistem = str(input('\033[32mSISTEMA DE AVALIAÇÃO:\033[m ')).upper()
    print()
    if sistem not in "TtAa":
        while True:
            error_message()
            sistem = str(input('\033[32mSISTEMA DE AVALIAÇÃO:\033[m ')).upper()
            if sistem in "TtAa":
                break
    print()
    # sistema de notas
    print('''\033[32m=-=Selecione o sistema de notas de sua escola=-=
[M]- Menções: ND, ED ou D                      
[N]- Notas de 0 a 10 (ou de 0 a 20)          
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\033[m''')
    print()
    notas = str(input('\033[32mSISTEMA DE NOTAS:\033[m ')).upper()
    print()
    if notas not in "MmNn":
        while True:
            error_message()
            notas = str(input('\033[32mSISTEMA DE NOTAS:\033[m ')).upper()
            if notas in "MmNn":
                break

    if notas == 'N':
        media = float(input('\033[36mDIGITE A NOTA MÉDIA:\033[m '))
        while not média > 0:
            no_note()
            media = float(input('\033[36mDIGITE A NOTA MÉDIA:\033[m '))
            if media > 0:
                break

    # se na escola é matéria ou área
    print('''\033[32m=-=-=-Onde você estuda o aprendizado é por=-=-=
[M]- Matéria                                 
[A]- Área                                   
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\033[m''')
    print()
    aprend = str(input('\033[32mAPRENDIZADO POR:\033[m ')).upper()
    print()
    if aprend not in "MmAa":
        while True:
            error_message()
            aprend = str(input('\033[32mAPRENDIZADO POR:\033[m ')).upper()
            if aprend in "MmAa":
                break
        
    # qual serviço o usuário selecionará
    print(f'''\033[32m=-=-=-=-=-=-Selecione uma das opções abaixo:-=-=-=-=-=-=-=-=        
[U] - Cálculo das {"notas" if notas in 'Nn' else "menções"} de uma {"matéria" if aprend in 'Mm' else "área"} específica       
[V] - Cálculo das {"notas" if notas in 'Nn' else "menções"} em mais de uma {"matéria" if aprend in 'Mm' else "área"}         
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\033[m''')
    print()
    opcao = str(input('\033[36mSUA OPÇÃO:\033[m  '))
    while opcao not in 'UuVv':
        error_message()
        opcao = str(input('\033[36mSUA OPÇÃO:\033[m  '))

    print()
    # essa parte aparecerá independente das escolhas do usuário, pois é o que vai ajudar na hora de calcular a média 
    if opcao in "Uu":
        print('=-' * 9)
        print()
        materia = str(input(f'\033[36mNOME DA {"ÁREA" if aprend in "Aa" else "MATÉRIA"}: '))
        print()
        tarefas = int(input(f'DIGITE QUANTAS {"TAREFAS" if sistem in "Tt" else "ATIVIDADES"} FORAM APLICADAS:\033[m '))
        
        
    # parte responsável por funcionar caso a escola do usuário avalie por Notas
        if notas in 'Nn':
            for c in range(1, tarefas + 1):
                print()
                ativi = str(input(f'\033[35mTÍTULO DA {c}ª {"TAREFA" if sistem in "Tt" else "ATIVIDADE"}: '))
                task.append(ativi)
                notaf = float(input(f'SUA NOTA NA {ativi}:\033[m '))
                print()
                nota += notaf
                divi = nota / tarefas
                
            if divi < media and notas == 'N':
                print()
                print('\033[31msua nota final em {} foi {:.1f}. Infelizmente tu não passou...\033[m'.format(materia, divi))
                
            else:
                print()
                print('\033[31mSua nota final em {} foi {:.1f}. Parabéns! Tu conseguiu passar!\033[m'.format(materia, divi))
                
#parte responsável por funcionar caso a escola da usuário avalie por Menções 
        if notas == 'M':
            for c in range(1, tarefas + 1):
                print()
                ativi = str(input(f'\033[35mTÍTULO DA {c}ª {"TAREFA" if sistem in "Tt" else "ATIVIDADE"}: '))
                task.append(ativi)
                menção = str(input(f'\033[35mSUA MENÇÃO NA {ativi}:\033[m ')).upper()
                menções.append(menção)
                print()
                if menção == 'ND':
                    ND += 1
                elif menção == 'ED':
                    ED += 1
                elif menção == 'D':
                    D += 1
            if tarefas == 2 and menções[0] != menções[1]:
                    print()
                    print(f'''\033[33mPOR TEREM SIDO APLICADAS APENAS 2 {"TAREFAS" if sistem == "T" else "ATIVIDAES"} NÃO FOI POSSIÍVEL CERTIFICAR QUAL FOI SUA {"MENÇÃO" if notas == "M" else "NOTA"} FINAL.\033[m''')
                    print(f'\033[32mAGUARDE ATÉ O FINAL DO BIMESTRE PARA TER MAIS {"MENÇÕES" if notas == "M" else "NOTAS"} ACUMULADAS!\033[m')   
                               
            elif ND > ED and ND > D:
                print()
                print(f'\033[31mSua menção final em {materia} foi ND. Calma, tu consegue fazer melhor!\033[m')
                
            elif ED > ND and ED > D:
                print()
                print(f'\033[33mSua menção final em {materia} foi ED. É isso aí, tu está quase lá!\033[m')
                
            elif D > ND and D > ED:
                print()
                print(f'\033[32mSua menção final em {materia} foi D. Parabéns, mas não deixe de estudar!.\033[m')
                
# essa parte só funcionará se o usuário seleciona quiser saber a média das matérias unificadas
    if opcao in "Vv":
        print()
        quantidade = int(input(f'\033[36mDIGITE O TANTO DE {"MATÉRIAS" if aprend in "Mm" else "ÁREAS"} PARA CÁLCULO DA {"MÉDIA" if notas in "Nn" else "MENÇÃO FINAL"}: '))
        print()

        for c in range(1, quantidade + 1):
            materia = str(input(f'\033[36mDIGITE A {c}ª {"MATÉRIA" if aprend in "Mm" else "ÁREA"}: ')).upper()
            matérias.append(materia)
            
            if notas == 'N':
                nota = input(f'DIGITE SUA NOTA EM {materia}: ')
                soma += nota
                calculo = soma / quantidade
                print()
                
                if calculo < media:
                    print()
                    print('\033[31mSua média final foi {:.1f}. Infelizmente você NÃO PASSOU.\033[m'.format(calculo))
                    print('\033[31mEstude mais um pouco! Certeza que da próxima TU CONSEGUE!\033[m')
                    
                else:
                    print()
                    print('\033[32mSua média final foi {:.1f}. VOCÊ PASSOU!\033[m'.format(calculo))
                    print('\033[36mCONTINUE ESTUDANDO para melhorar cada vez mais!\033[m')
                    
            elif notas == 'M':
                menção = input(f'DIGITE SUA MENÇÃO EM {materia}:\033[m').upper()
                menções.append(menção)
                
                if menção == 'ND':
                    ND += 1
                elif menção == 'ED':
                    ED += 1
                elif menção == 'D':
                    D += 1
                    
                if quantidade == 2 and menções[0] != menções[1]:
                    print()
                    print(f'''\033[33mPOR TEREM SIDO APLICADAS APENAS 2 {"TAREFAS" if sistem == "T" else "ATIVIDAES"} NÃO FOI POSSIÍVEL CERTIFICAR QUAL FOI SUA {"MENÇÃO" if notas == "M" else "NOTA"} FINAL.\033[m''')
                    print(f'\033[32mAGUARDE ATÉ O FINAL DO BIMESTRE PARA TER MAIS {"MENÇÕES" if notas == "M" else "NOTAS"} ACUMULADAS!\033[m')
                      
                elif ND > ED and ND > D:
                    print()
                    print(f'\033[31mA menção predominante foi ND. Infelizmente nesse bimestre tu não foi nada bem :(\033[m')
                    print(f'\033[32mNão desista, é errando que se aprende!!!\033[m')
                    
                elif ED > ND and ED > D:
                    print()
                    print(f'\033[33m A menção predominante foi ED. É isso aí, tu está quase lá!\033[m')
                    print('\033[34mSó mais um pouco de esforço e certeza que tu consegue.\033[m')
                    
                elif D > ND and D > ED:
                    print()
                    print(f'\033[32mA menção predominante foi D. Parabéns, mas não deixe de estudar!.\033[m')
                    print('\033[36mContinue assim e tu vai se da muito bem!\033[m')        
                
    print()
    print('\033[34mDeseja ver seu boletim? ')
    desej = int(input('0 - Sim | 1 - Não:\033[m '))
    
    if desej == 0:
        print()
        print('''\033[33mESTE RECURSO AINDA ESTÁ EM DESENVOLVIMENTO. EM BREVE ELE SERÁ APRIMORADO.\033[m''')
        print()
        print('==' * 31)
        print(f'\033[7;36m{"BOLETIM":^62}\033[m')
        print('==' * 31)
        print(f'\033[7;33m{"MATÉRIA" if aprend == "M" else "ÁREA":<30}\033[m {"|":^1} \033[7;34m{"NOTA" if notas == "N" else "MENÇÃO":>29}\033[m')
        print('--' * 31)
        
        for pos in range(0, len(task)):
            print(f'\033[33m\n{task[pos]:<30}\033[m {"|":^1} \033[34m{menções[pos]:>29}\033[m')
            print('--' * 31)
            
if função == 'P':
    
    User = 'Professor'
    password = 7895688
    
    print()
    print('\033[31m                                               ATENÇÃO!!!\033[m')
    print('\033[33m                      ESTA ÁREA É PRIVADA AOS PROFESSORES E GESTORES DA ESCOLA.')
    print('SE VOCÊ SE ENQUADRA NOS CARGOS ACIMA CITADOS, POR FAVOR,\033[m \033[36mDIGITE A SEGUIR SEU NOME DE USUÁRIO e SENHA DE LOGIN.\033[m')
    print()
    
    name = str(input('\033[36mDigite seu nome: '))
    key = int(input('Digite sua senha de login:\033[m '))
    
    if name == User and password == key:
        print()
        print('\033[32mOlá!!!\033[m')
    elif name != User and password == key:
        print()
        print('\033[31mNome de usuário incorreto!\033[m')
        print('\033[33mTente novamente!\033[m')
    elif name == User and password != key:
        print()
        print("\033[31mSenha de login incorreta!\033[m")
        print('\033[33mTente novamente!\033[m')
    elif name != User and password != key:
        print()
        print("\033[31mUsuário não encontrado...")
        print('Acione a equipe gestora da escola!\033[m')
    
    