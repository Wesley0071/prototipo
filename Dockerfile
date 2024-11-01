# nao esqueca que voce esta subindo um container com a imagem do python
FROM python:3.9

# aqui cria a pasta /code dentro do container
WORKDIR /code

# aqui ele copia o arquivo requirements.txt para um novo arquivo requirements.txt dentro de code
COPY ./requirements.txt /code/requirements.txt

# instala as dependencias dentro do container
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# copia todo o projeto de /src para dentro de /src que sera criado dentro de /code
COPY ./src /code/src

# comando para o container executar
# CMD python3 src/main.py
CMD ["python3", "src/main.py"]
