import socket
import re
import sys
import mariadb

# MySQL veritabanı bağlantı bilgileri
db_host = '192.168.0.244'
db_port = 3306
db_user = 'root'
db_password = 'password'
db_name = 'mydb'  # Veritabanı adını değiştirin
event_filter = re.compile('^(Cdr)')


try:
    # MariaDB veritabanına bağlanma
    con = mariadb.connect(
        user="molla",
        password="molla-neyapiyorsun-123456",
        host="192.168.0.244",
        port=3306,
        database="asterisk"
    )
except mariadb.Error as ex:
    print(f"MariaDB'ye bağlanırken bir hata oluştu: {ex}")
    sys.exit(1)

# Veritabanı adını görüntüleme
print("Bağlanılan veritabanı: ", con.database)

# Bağlantıyı kapatma
con.close()

print("Bağlantı kapatıldı.")


# AMI'ye bağlanmak için gerekli bilgileri tanımlayın
ami_host = '192.168.0.244'
ami_port = 5038
ami_username = 'molla'
ami_password = 'molla-123'
event_filter = re.compile('^(Cdr)') 

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
response = s.recv(1024).decode()

try:
    event_data = "Action: Events\r\nEventMask: on\r\n\r\n"
    s.send(event_data.encode())
except Exception as e:
    print("Event izleme hatası:", e)

#Eventleri işleme döngüsü
while True:
    try:
        response = ''
        while True:
            data = s.recv(1024).decode()
            if not data:
                break
            response += data
            if '\r\n\r\n' in response:
                events = response.strip().split('\r\n\r\n')
                for event in events:
                    event_dict = {}
                    for line in event.split('\r\n'):
                        parts = line.split(': ', 1)
                        if len(parts) == 2:
                            event_dict[parts[0]] = parts[1]
                    if 'Event' in event_dict and event_filter.match(event_dict['Event']):
                        print(event_dict)

                        # Eventleri MySQL veritabanına yazma
                        try:
                            cursor.execute(
                                "INSERT INTO events (event_name, event_data) VALUES (%s, %s)",
                                (event_dict['Event'], str(event_dict))
                            )
                            db.commit()
                        except Exception as e:
                            print("Event yazma hatası:", e)
                response = ''
    except Exception as e:
        print(f'Event processing error: {e}')
        s.close()