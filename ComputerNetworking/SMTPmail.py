## SMTP Email

from socket import *

# Mensagem a ser enviada
msg = '\r\nRedes de Computadores e fixe!'
endmsg = '\r\n.\r\n'

# Servidor de email
mailserver = 'smtp.ualg.pt'
portnumber = 25

# Criacao de socket e estabelecimento de conexao TCP com mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, portnumber))

# Analise da primeira resposta do servidor
serveranswer = clientSocket.recv(1024)
if (serveranswer[:3] != '220'):
    print "Error on first answer from sérver."
    clientSocket.close() 

# Envio do comando HELO para servidor
clientSocket.send("HELO ualg\r\n")
serveranswer = clientSocket.recv(1024)
if (serveranswer[:3] != '250'):
    print "Error on first answer from server."
    clientSocket.close() 

# Envio do comando MAIL FROM para servidor
clientSocket.send("MAIL FROM: <a34693@ualg.pt>\r\n")
serveranswer = clientSocket.recv(1024)
if (serveranswer[:3] != '250'):
    print "Error on first answer from server."
    clientSocket.close() 

# Envio do comando RCPT TO para servidor
clientSocket.send("RCPT TO: <aXXXXX@ualg.pt>\r\n")
serveranswer = clientSocket.recv(1024)
if (serveranswer[:3] != '250'):
    print "Error on first answer from server."
    clientSocket.close() 

# Envio do comando DATA para servidor
clientSocket.send("DATA\r\n")
serveranswer = clientSocket.recv(1024)
if (serveranswer[:3] != '354'):
    print "Error on first answer from server."
    clientSocket.close() 

# Envio da mensagem para servidor
clientSocket.send("from: Patricia <aXXXXX@ualg.pt>\r\n")
clientSocket.send("to: <aXXXXX@ualg.pt>\r\n")
clientSocket.send("SUBJECT: Ola Ion!\r\n")
clientSocket.send(msg)
clientSocket.send(endmsg)
serveranswer = clientSocket.recv(1024)
if (serveranswer[:3] != '250'):
    print "Error sending message."
    clientSocket.close() 

# Envio do comando QUIT para servidor
clientSocket.send("QUIT\r\n")
serveranswer = clientSocket.recv(1024)
if (serveranswer[:3] != '221'):
    print "Error exiting."
    clientSocket.close()
    
# Fim do programa
