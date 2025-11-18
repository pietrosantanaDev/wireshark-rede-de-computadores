# Importa o módulo socket
from socket import *
import sys  # Necessário para encerrar o programa

# Cria o socket TCP (orientado à conexão)
serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepara o socket do servidor
# #Fill in start
serverPort = 6789
serverSocket.bind(("", serverPort))  # Associa o socket ao endereço local e porta
serverSocket.listen(1)  # Começa a escutar conexões TCP (1 conexão na fila)
# #Fill in end

print(f"Servidor pronto na porta {serverPort}...")

while True:
    # Estabelece a conexão
    print("Aguardando novas requisicoes...")
    # #Fill in start
    connectionSocket, addr = serverSocket.accept()  # Aceita a conexão do cliente
    # #Fill in end

    try:
        # Recebe a mensagem do cliente (requisição HTTP)
        # #Fill in start
        message = connectionSocket.recv(
            1024
        ).decode()  # Recebe bytes e decodifica para string
        # #Fill in end

        # Se a mensagem estiver vazia, volta para o início do loop (evita erros aleatórios)
        if not message:
            continue

        filename = message.split()[1]
        f = open(
            filename[1:]
        )  # Pula a barra "/" do nome do arquivo (ex: /index.html -> index.html)

        # #Fill in start
        outputdata = f.read()  # Lê todo o conteúdo do arquivo html
        # #Fill in end

        # Envia a linha de status do cabeçalho HTTP
        # #Fill in start
        # Header padrão 200 OK. O \r\n\r\n indica o fim do cabeçalho.
        header = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
        connectionSocket.send(header.encode())
        # #Fill in end

        # Envia o conteúdo do arquivo ao cliente
        # Nota: O código original sugere um loop char por char, o que é lento,
        # mas mantive para seguir seu esqueleto.
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        # Fecha a conexão com o cliente
        connectionSocket.close()

    except IOError:
        # Envia mensagem de erro 404 se o arquivo não for encontrado
        # #Fill in start
        header_404 = "HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n"
        response_404 = "<html><head></head><body><h1>404 Not Found</h1><p>Arquivo nao encontrado no servidor.</p></body></html>"

        connectionSocket.send(header_404.encode())
        connectionSocket.send(response_404.encode())
        # #Fill in end

        # Fecha o socket do cliente
        # #Fill in start
        connectionSocket.close()
        # #Fill in end

# Estas linhas nunca serão alcançadas devido ao while True, mas fazem parte do esqueleto
serverSocket.close()
sys.exit()  # Encerra o programa
