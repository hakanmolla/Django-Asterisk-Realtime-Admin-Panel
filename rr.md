# Python Django için Sanal Ortam Kurulumu

Python Django projelerinizde sanal ortam kullanmak, projenizin bağımlılıklarını ve gereksinimlerini izole etmek için iyi bir uygulamadır. İşte Python Django için bir sanal ortam oluşturmanız gerektiğinde izleyebileceğiniz adımlar:

## Adım 1: Python Kurulumu

Öncelikle, Python'ın sisteminizde yüklü olduğundan emin olun. Python'ın en son sürümünü [Python resmi web sitesi](https://www.python.org/downloads/) üzerinden indirebilir ve kurabilirsiniz. Kurulumu tamamladıktan sonra, Python komut satırında veya terminalde kullanılabilir hale gelecektir.

## Adım 2: pip Kurulumu
pip, Python paketlerini yönetmek için kullanılan bir paket yöneticisidir ve Django'nun da kurulumu için kullanılır. Eğer sisteminizde pip zaten yüklü değilse, aşağıdaki komutu kullanarak pip'i kurabilirsiniz:

Windows:

```bash
python get-pip.py
```

macOS/Linux:

```bash
curl https://bootstrap.pypa.io/get-pip.py | python3
```


## Adım 3: Virtualenv Kurulumu

Django projelerinizde sanal ortam kullanabilmek için `virtualenv` adlı Python paketini kurmanız gerekmektedir. Komut satırına veya terminalinize aşağıdaki komutu girerek `virtualenv` paketini kurabilirsiniz:

```bash
pip install virtualenv

```

## Adım 4: Sanal Ortam Oluşturma
Sanal ortam oluşturmak için projenizin ana dizininde bir klasör oluşturun. Bu klasör, sanal ortamınızın kök dizini olacaktır. Ardından, aşağıdaki komutu girerek sanal ortamı oluşturabilirsiniz:

Windows:
```bash
python -m venv project-name

```
macOS/Linux:

```bash
python3 -m venv project-name

```

Burada **project-name**, oluşturmak istediğiniz sanal ortamın adıdır. İsterseniz başka bir isim de seçebilirsiniz.

## Adım 5: Sanal Ortamı Aktif Etme
Sanal ortamı etkinleştirmek için aşağıdaki komutları kullanabilirsiniz:

Windows:
```bash

project-name\Scripts\activate

```

Unix veya Linux:
```bash
source myenv/bin/activate

```


## Adım 6: Django Kurulumu
Sanal ortamınız etkinleştirildiğinde, projenizin kök dizininde bulunan pip paket yöneticisini kullanarak Django paketini yükleyebilirsiniz:

```bash
pip install django

```

## Adım 7: Colorama Eklentisi (isteğe bağlı)
Colorama, Python dilinde terminal üzerinde renkli yazılar yazmak için kullanılan bir pakettir.

py -m pip install colorama

## Adım 8: Django Projesi Oluşturma
Django paketini başarıyla yükledikten sonra, sanal ortamınızda bir Django projesi oluşturabilirsiniz. Aşağıdaki komutu kullanarak Django projesi oluşturabilirsiniz:

```bash
django-admin startproject myproject

```
<span style="color:red"> Not!: Benim tavsiyem **config** olarak oluşturmanız ve sonuna . koymanız olacaktır. </span>

```bash
django-admin startproject config .

```

Burada myproject, oluşturmak istediğiniz Django projesinin adıdır. İsterseniz başka bir isim de seçebilirsiniz.

## Adım 9: Django Projeyi Çalıştırma
Django projesini çalıştırmak için projenizin
```bash


```



