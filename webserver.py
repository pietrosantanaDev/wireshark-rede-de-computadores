# Importa o módulo socket
from socket import *
import sys  # Necessário para encerrar o programa

# Cria o socket TCP (orientado à conexão)
serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepara o socket do servidor
# #Fill in start
serverPort = 6789
serverSocket.bind(("", serverPort))  
serverSocket.listen(1)  
# #Fill in end

print(f"Servidor pronto na porta {serverPort}...")

while True:
    # Estabelece a conexão
    print("Ready to serve...")
    # #Fill in start
    connectionSocket, addr = serverSocket.accept()  
    # #Fill in end

    try:
        # Recebe a mensagem do cliente (requisição HTTP)
        # #Fill in start
        message = connectionSocket.recv(
            1024
        ).decode()  
        # #Fill in end

        filename = message.split()[1]
        f = open(
            filename[1:]
        )  
        # #Fill in start
        outputdata = f.read()  # Lê todo o conteúdo do arquivo html
        # #Fill in end

        # Envia a linha de status do cabeçalho HTTP
        # #Fill in start
       
        header = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
        connectionSocket.send(header.encode())
        # #Fill in end

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

serverSocket.close()
sys.exit()  # Encerra o programa
