api_Key = "" 
           

import google.generativeai as genai
genai.configure(api_key=api_Key)

model = genai.GenerativeModel('gemini-2.0-flash')
chat = model.start_chat(history=[]) 
def chama_api():
    arquivo = "registros.txt"

    # leitura do arquivo:
    with open(arquivo, "r", encoding="utf-8") as ler_arquivo:
        arquivo_lido = ler_arquivo.read()
    

    # Inicializa o histórico da conversa
    conversation_history = f"""Você é dono de uma empresa de transportes, especialista em segurança de trânsito, e está monitorando as ocorrências de distração dos seus motoristas no Brasil," 
                                como por exemplo:  Normaly: o motorista está conduzindo o veículo com segurança; Usando Celular: o motorista está utilizando o telefone celular enquanto está dirigindo;
                                Com sono: o motorista está com sono enquanto dirige o veículo; Looking Around: o motorista está distraído ao invés de prestar atenção no trânsito; Not Found: o motorista não está no banco enquanto o caminhão está andando.
                                Com base nisso, tenho os seguintes registros e o horário de ocorrências: {arquivo_lido}. Essas ocorrencias são o que o motorista está fazendo no momento do registro, analise cada registro e faça uma análise de dados em cima desses registros. Sempre me dê resposte de no máximo 2000 caracteres. """

    primeira_interacao = True
    while True:
        if primeira_interacao == True:
            # Solicita uma pergunta ao usuário
            user_input = conversation_history
            primeira_interacao = False
        else: 
            user_input = input("Usuário: ")
        
        def generate_prompt(prompt):
            return f"{prompt}"

        # Envia e recebe a resposta da IA
        response = chat.send_message(generate_prompt(user_input), stream=True)
        for s in response:
            if s.text:
                print(s.text, end='', flush=True)