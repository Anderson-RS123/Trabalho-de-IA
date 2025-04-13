# Trabalho-de-IA
Trabalho 1 


# Descrição #

  Essa atividade foi desenvolvida para o Trabalho 1 da cadeira de Inteligência Artificial 1, da Antonio Meneghatti Faculdade.
  Para esse trabalho, ouve algumas partes obigatórias que deveria estar no desenvolvimento do trabalho, como: 
     - Reconhecimento de Imagens
     - Utilização de arquivos
     - Utilização de um modelo de IA
     - Promp do usuário
  Foi utilizada a linguagem python para o desenvolvimento do código desse trabalho.

  
# Tema da Atividade #

  O contexto utilizado para o desenvolvimento do trabalho, foi a distração de motoristas no trânsito brasileiro.
  Com esse problema, foi criado esse pequeno sistema para identificar qual a atividade atual do motorista, para podermos gerar uma análise de dados 
  dos registros realizados, para conseguirmos ter um direcionamento de qual ação realizar.


# Lógica de funcionamento do Código #

  O funcionamento do código utilizado é o seguinte:
     - Pasta "img": esta pasta contem as fotos registradas dos motoristas.
     - arquivo "keras_model.h5": esse arquivo contém a lógica necessária para que o código consiga realizar o reconhecimento de imagens.
     - arquivo "labels.txt": esse arquivo contém as classificações que cada foto pode ter.
     - arquivo "registros.txt": esse arquivo armazena a data e horário da realização de registros realizados, além de qual classificação a respectiva imagem pertence.
     - arquivo "teachable.py": esse código foi gerado pelo programa "Google Teachable", após treinamento do modelo. Foi necessário adicionar um Hack para configurar a biblioteca 'Keras' e fazer o código funcionar.
     - arquivo "save_events.py": esse código armazena os registros no arquivo "registros.txt". Ele também faz a contagem de cada item da classificação das imagens.
     - arquivo "respostaIA": esse código se conecta com o Gemini, e faz requisições por API para obter a análise dos dados e as perguntas posteriores do usuário.


# Para utilizar esse código #
  Baixe os arquivos: "keras_model.h5", "labels.txt", "tachable.py", save_events.py", "respostaIA.py".
  Crie uma pasta "img", e coloque algumas imagens relacionadas ao tema da Atividade, e nomeie iniciando em "teste1.jpg". A Cada foto, altere o número para ser consecutivo.
  Crie um ambiente virtual no arquivo "teachable.py" no VSCode. 
         - execute no terminal: python -m venv venv
  Ative o ambiente virtual:
         - .\venv\Scripts\Activate.ps1
  Execute os seguinte comandos para baixar as dependências:
        - pip install tensorflow keras pillow h5py
  Você precisa colocar na variável "api_Key", dentro das àspas duplas, no arquivo "respostaIA", a chave API do google. Para conseguir a   
  chave API do Gemini, vá nesse caminho: https://aistudio.google.com/apikey , faça login com sua conta google, e copie a chave API 
  localizada no campo "Chave de API".
  Execute o arquivo "teachable.py"
      
# Ferramentas Utilizadas #
   - Google Teachable
   - VSCode Studio
   - Google Generative AI (Gemini)
