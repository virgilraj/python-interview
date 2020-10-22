import poplib 
import email 
import socket


 
server = poplib.POP3('pop.gmail.com') 
socket.getaddrinfo('pop.gmail.com', 995)
server.user('analytics@softcrylic.com') 
server.pass_('SoftPass123$') 
 
# get amount of new mails and get the emails for them 
messages = [server.retr(n+1) for n in range(len(server.list()[1]))] 
 
# for every message get the second item (the message itself) and convert it to a string with \n; then create python email with the strings 
emails = [email.message_from_string('\n'.join(message[1])) for message in messages] 
 
for mail in emails: 
    # check for attachment; 
    print(mail)
    for part in mail.walk(): 
        if not mail.is_multipart(): 
            continue 
        if mail.get('Content-Disposition'): 
            continue 
        file_name = part.get_filename() 
        # check if email park has filename --> attachment part 
        if file_name: 
            file = open(file_name,'w+') 
            file.write(part.get_payload(decode=True)) 
            file.close() 