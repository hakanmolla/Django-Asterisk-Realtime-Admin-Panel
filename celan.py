import sys
import mariadb
import socket
import re
# Kullanıcı Tanımları Start :
SERVER_IP = "192.168.0.244"
AMI_HOST = "192.168.0.244"
DB_USER = "molla"
DB_NAME = "asterisk"
DB_PORT= 3306
DB_PASSWORD = "molla-neyapiyorsun-123456"
AMI_PORT= 5038
AMI_USER='molla'
AMI_PASSWORD='molla-123'
table_name = "CustemCdrTables"  # tablo adı değişkeni
# Kullanıcı Tanımları End :
# MariaDB Bağlantı Bloğu Start 
try:
    con = mariadb.connect(
        user = DB_USER,
        password = DB_PASSWORD,
        host = SERVER_IP,
        port = DB_PORT,
        database= DB_NAME
    )
except mariadb.Error as ex:
    print(f"MariaDB'ye bağlanırken bir hata oluştu: {ex}")
    sys.exit(1) 
# DB Bağlantı Bloğu End
# Cursor nesnesi tanımlanması
cursor = con.cursor()
print("Bağlanılan veritabanı: ", con.database)
# AMI'ye bağlantı Bloğu Start
event_filter = re.compile('^(Cdr)') 
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((AMI_HOST, AMI_PORT))
    print("Asterisk Amiye Bağlandı ")
except Exception as e:
    print("Bağlantı hatası:", e)
# AMI'ye bağlantı Bloğu End
# Login işlemini yapın
try:
    login_data = f"Action: Login\r\nUsername: {AMI_USER}\r\nSecret: {AMI_PASSWORD}\r\n\r\n"
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
# Veritabanı adını görüntüleme
print("Eventleri işleme döngüs: ")
#***************************************************************************************
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
                        try:
                            event_name = event_dict['Event']  # event_name değerini al
                            event_data = str(event_dict)  # event_data değerini al
                             # Sütun isimlerini ve yer tutucuları dinamik olarak oluştur
                            column_names = ', '.join([f"`{column}`" for column in event_dict.keys()])
                            placeholders = ', '.join(['%s'] * len(event_dict))
                            cursor.execute(
                            f"INSERT INTO {table_name} ({column_names}) VALUES ({placeholders})",
                            tuple(event_dict.values())  # event_dict değerlerini tuple olarak gönder
                                )
                            con.commit()
                        except Exception as e:
                            print("Event yazma hatası:", e)
                response = ''
    except Exception as e:
        print(f'Event processing error: {e}')
        s.close()


# Bağlantıyı kapatma
con.close()

print("Bağlantı kapatıldı.")