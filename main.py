import os

def clear():
    """Cross-platform clear screen function"""
    os.system('cls' if os.name == 'nt' else 'clear')

# Game data for all three stages
stages = [
    {
        "word": "MOTOCICLETA",
        "entrada": ["___________", "M__________", "M_________A", "M__O______A", "M__OC____TA", "MOTOCICLETA"],
        "vocabulario": ["MOTOR", "RODAS", "MOTOQUEIRO", "ENTREGA", "MOTO"],
        "gender": "feminino",
        "definition": "Veículo com {0} e duas {1}, para transporte do {2} e mais uma pessoa, habitualmente utilizado para {3} de coisas. Ver {4}.",
        "syllables": "mo-to-ci-cle-ta",
        "syllables_hidden": "__-__-__-___-__"
    },
    {
        "word": "ÔNIBUS",
        "entrada": ["______", "Ô_____", "Ô____S", "ÔN___S", "ÔNI__S", "ÔNIBUS"],
        "vocabulario": ["MOTORIZADO", "RODAS", "PASSAGEIROS", "PROFISSIONAL", "PASSAGEM"],
        "gender": "masculino",
        "definition": "Meio de transporte {0}, com 4 ou mais {1}, apresenta linhas de circulação e trajetos pré-definidos e quantidade de ocupação maior do que 42 {2}. É operado por um {3} qualificado e seu uso é mediante o pagamento de uma {4} ou uso de passes cadastrados.",
        "syllables": "ô-ni-bus",
        "syllables_hidden": "_-__-___"
    },
    {
        "word": "MICRO-ÔNIBUS",
        "entrada": ["____________", "M___________", "M__________S", "MI_________S", "MIC________S", "MICRO-ÔNIBUS"],
        "vocabulario": ["MOTOR", "PORTAS", "RODAS", "PESSOAS", "ÔNIBUS"],
        "gender": "masculino",
        "definition": "Veículo com {0}, duas {1} e quatro {2}, capacidade máxima de 20 {3}. Semelhante ao {4}, com capacidade reduzida.",
        "syllables": "mi-cro--ô-ni-bus",
        "syllables_hidden": "__-___--__-__-___"
    }
]

current_stage = 0
respostas = ["*", "*", "*", "*", "*"]
round = 0
vidas = 5
acertos = 0
unfinished = True

while unfinished:
    stage = stages[current_stage]

    if vidas == 0:
        print("\nVocê perdeu!")
        print(f"A palavra era: {stage['word']}")

        # Ask if player wants to try again
        try_again = input("\nDeseja tentar novamente esta fase? (qualquer tecla/n): ").lower()
        if try_again in ['n', 'no', 'não', 'nao']:
            unfinished = False
            break
        else:
            # Reset current stage variables
            respostas = ["*", "*", "*", "*", "*"]
            round = 0
            vidas = 5
            acertos = 0
            continue

    elif acertos == 5:
        print(f"\nPARABÉNS! Você completou a palavra: {stage['word']}")
        print(f"\nsubstantivo feminino/masculino {stage['syllables']}")

        # Create colored definition
        colored_words = [respostas[i] for i in range(5)]
        print(stage['definition'].format(*colored_words))

        # Check if this was the last stage
        if current_stage == 2:
            print("\n🎉 PARABÉNS! Você completou todas as três palavras! 🎉")
            try_again = input("\nDeseja jogar novamente desde o início? (qualquer tecla/n): ").lower()
            if try_again in ['n', 'no', 'não', 'nao']:
                break
            else:
                # Reset to first stage
                current_stage = 0
                respostas = ["*", "*", "*", "*", "*"]
                round = 0
                vidas = 5
                acertos = 0
                continue
        else:
            # Move to next stage
            input("\nPressione Enter para continuar para a próxima palavra...")
            current_stage += 1
            respostas = ["*", "*", "*", "*", "*"]
            round = 0
            vidas = 5
            acertos = 0
            continue

    entrada = stage['entrada'][acertos]
    clear()
    print("Atividade de Lexicologia - Glossário do Trânsito")
    print(f"Palavra {current_stage + 1}/3")
    print(f"\nVidas: {vidas}")
    print(f"Palavra-entrada: {entrada}")

    # Create colored version of the definition
    colored_answers = []
    for i in range(5):
        colored_answers.append(respostas[i])

    print(f"\nsubstantivo {stage['gender']} {stage['syllables_hidden']}")
    print(f"\n{stage['definition'].format(*colored_answers)}")

    chute = input("\nComplete o verbete: ")

    if chute.upper() not in stage['vocabulario']:
        vidas -= 1
        print("Resposta incorreta! Você perdeu uma vida.")
        input("Pressione Enter para continuar...")
    else:
        # Check if this word hasn't been guessed already
        word_index = stage['vocabulario'].index(chute.upper())
        if respostas[word_index] == "*":
            respostas[word_index] = chute.upper()
            acertos += 1

    round += 1