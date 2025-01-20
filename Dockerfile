# Esta imagem Docker tem como objetivo servir de base para o desenvolvimento 
# do projeto `DERCosimul`.
#
# O projeto DERCosimul tem como objetivo aplicar conceitos de co-simulação
# no estudo das interações dos ditos Distributed Energy Resources (DER) 
# com a rede elétrica.
#
#   O que esta imagem Docker faz?
# 
#   - utiliza a imagem lucassmelo/python-base-image:0.2 como base, padrao
#     dos projetos que utilizam Python no GREI.
#   - Configura o diretorio de trabalho /app.
#   - Clona o respositorio do projeto para a pasta /app do container.
#   - Cria o ambiente virtual anaconda `mosaik-env` com python 3.8.
#   - Inicializa o anaconda no terminal e executa comando de instalacao
#     dos prerrequisitos do projeto.
#   - Configura o ambiente virtual anaconda `mosaik-env` para ser utilizado
#     como ambiente padrao do container.
#   - Libera a porta 8000 para ser exposta pelo container.
#   - Configura o comando `/bin/bash` como padrao na inicializacao do container.
#
# Para criar um container Docker de desenvolvimento a partir da imagem descrita nesse
# arquivo Dockerfile, primeiro é preciso construir a imagem Docker usando o seguinte comando:
# ```
# docker image build --build-arg GITHUB_TOKEN=your_personal_access_token -t your_image_name .
# ```
#
# Em seguida, é necessário criar um container a partir da imagem construida anteriormente:
# ```
# docker container run -it --name your_container_name -p 8000:8000 your_image_name
# ``` 
#
#

# Use uma imagem base do Ubuntu
FROM lucassmelo/python-base-image:0.2

# Configurar o diretório de trabalho
WORKDIR /app

# Defina o token de acesso pessoal como uma variável de ambiente
ARG GITHUB_TOKEN
ENV GITHUB_TOKEN=${GITHUB_TOKEN}

RUN git clone https://${GITHUB_TOKEN}@github.com/grei-ufc/DER-cosimul.git

WORKDIR /app/DER-cosimul

# Criar um ambiente virtual chamado "mosaik-env" e instalar o pacote mosaik
RUN conda create -y -n mosaik-env python=3.8
RUN conda init
RUN conda run -v -n mosaik-env pip install -r requirements.txt

# Ativar o ambiente por padrão no container
RUN echo "conda activate mosaik-env" >> ~/.bashrc

# Expor portas, caso necessário (por exemplo, para APIs ou servidores)
EXPOSE 8000

# Entrar no shell com o ambiente ativado por padrão
CMD ["/bin/bash"]
