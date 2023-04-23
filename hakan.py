import socket
import re
# AMI'ye bağlanmak için gerekli bilgileri tanımlayın
ami_host = '192.168.0.244'
ami_port = 5038
ami_username = 'molla'
ami_password = 'molla-123'
event_filter = re.compile('^(Cdr)')
#event_filter = re.compile('^(CEL)')
# event_filter = re.compile('^(ContactStatus)')
# event_filter = re.compile('^(QueueCallerAbandon)') 
#event_filter = re.compile('^(QueueCallerJoin)')


try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ami_host, ami_port))
except Exception as e:
    print("Bağlantı hatası:", e)
# Login işlemini yapın
try:
    login_data = f"Action: Login\r\nUsername: {ami_username}\r\nSecret: {ami_password}\r\n\r\n"
    s.send(login_data.encode())
    response = s.recv(1024).decode()
except Exception as e:
    print("Login hatası:", e)

# Response'ları işleyin
while True:
    try:
        response = s.recv(1024).decode()
        if not response:
            break
        events = response.strip().split('\r\n\r\n')

        for event in events:
            event_dict = {}
            for line in event.split('\r\n'):
                parts = line.split(': ', 1)
                if len(parts) == 2:
                    event_dict[parts[0]] = parts[1]
            if 'Event' in event_dict and event_filter.match(event_dict['Event']):
                print(event_dict)
    except Exception as e:
        print(f'Event processing error: {e}')
        s.close()
# while True:
#     try:
#         response = s.recv(1024).decode()
#         if not response:
#             break
#         events = response.strip().split('\r\n\r\n')

#         for event in events:
#             event_dict = {}
#             for line in event.split('\r\n'):
#                 parts = line.split(': ', 1)
#                 if len(parts) == 2:
#                     event_dict[parts[0]] = parts[1]
#             print(event_dict)
#     except Exception as e:
#         print(f'Event processing error: {e}')
#         s.close()