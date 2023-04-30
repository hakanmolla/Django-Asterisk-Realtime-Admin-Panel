
## Kuyruk Ekleme Parametrelerin acıklması : 

-   **name:** Kuyruk adı
-   **musiconhold:** Müzik tutma (Music on Hold) sınıfı
-   **announce:** Kuyruğa yeni bir çağrı eklendiğinde hangi kaydın çalınacağı
-   **context:** Kuyruk içindeki çağrıların yönlendirileceği bağlam (context)
-   **timeout:** Kuyruktaki bir üyenin yanıt vermesi için geçen süre
-   **ringinuse:** Meşgul olan üyelerin aranıp aranmayacağı
-   **setinterfacevar:** Arama yapılan arayüz (interface) için özel değişkenler tanımlar
-   **setqueuevar:** Kuyruk için özel değişkenler tanımlar
-   **setqueueentryvar:** Kuyruğa yeni bir çağrı eklendiğinde çağrı için özel değişkenler tanımlar
-   **monitor_format:** Kuyrukta yapılan çağrıların kaydedileceği dosya formatı
-   **membermacro:** Kuyruktaki üyelerin, çağrılarını cevaplarken çalışacak makrolar
-   **membergosub:** Kuyruktaki üyelerin, çağrılarını cevaplarken çalışacak Subroutine'lar
-   **queue_youarenext:** Sıradaki çağrıyı cevaplayacak üyeye söylenen mesaj
-   **queue_thereare:** Kuyrukta kaç adet çağrı olduğunu söyleyen mesaj
-   **queue_callswaiting:** Kuyrukta kaç çağrının beklediğini söyleyen mesaj
-   **queue_quantity1:** Kuyruktaki bir çağrı için kullanılacak mesaj
-   **queue_quantity2:** Kuyrukta birden fazla çağrı için kullanılacak mesaj
-   **queue_holdtime:** Kuyrukta bekleyen çağrıların beklemeleri için yapılan duyuru
-   **queue_minutes:** Kuyrukta bekleyen çağrıların beklemeleri için dakika cinsinden yapılan duyuru
-   **queue_minute:** Kuyrukta bekleyen çağrıların beklemeleri için dakika cinsinden yapılan kısa bir duyuru
-   **queue_seconds:** Kuyrukta bekleyen çağrıların beklemeleri için saniye cinsinden yapılan duyuru
-   **queue_thankyou:** Kuyrukta bekleyen bir çağrının kuyruktan çıkması durumunda söylenen mesaj
-   **queue_callerannounce:** Kuyrukta bekleyen bir çağrının, beklerken duyacağı mesaj
-   **queue_reporthold:** Kuyrukta bekleyen çağrıların bekleme sürelerini raporlama
-   **announce_frequency:** Çağrı bekleme sürelerinin duyurulma sıklığı
-   **announce_to_first_user:** Çağrı bekleme süresinin ilk üyeye duyurulup duyurulmayacağı
-   **min_announce_frequency:** Çağrı bekleme süresi için minimum duyuru sıklığı
-   **announce_round_seconds:** Duyuruda kullanılacak sürenin en yakın tam sayıya yuvarlanması
-   **announce_holdtime:** Bekleme süresinin duyurulması için kullanılacak kayıt
-   **announce_position:** Kuyruktaki çağrının pozisyonunun duyurulması için kullanılacak kayıt
-   **announce_position_limit:** Kuyruktaki çağrıların pozisyonu için bir üst sınır
-   **periodic_announce:** Belirli aralıklarla yapılan duyuruların açılıp kapatılması
-   **periodic_announce_frequency:** Belirli aralıklarla yapılan duyuruların sıklığı
-   **relative_periodic_announce:** Belirli aralıklarla yapılan duyuruların çağrıyı cevaplayacak üyeye göre yapılması
-   **random_periodic_announce:** Belirli aralıklarla yapılan duyuruların rastgele seçilmesi
-   **retry:** Bir çağrıyı kaç kez tekrar deneyeceği
-   **wrapuptime:** Kuyruktan çıkan bir çağrının ardından bir sonraki çağrının işleme girmesi için geçmesi gereken süre
-   **penaltymemberslimit:** Üyelerin penaltıya tabi olacağı maksimum sayı
-   **autofill:** Kuyruğa yeni bir çağrı geldiğinde, penaltıya tabi üyelerin otomatik olarak eklenip eklenmeyeceği
-   **monitor_type:** Kuyruktaki çağrıların nasıl kaydedileceği
-   **autopause:** Kuyruktaki üyelerin çağrılardan önce otomatik olarak duraklatılıp duraklatılmayacağı
-   **autopausedelay:** Üyelerin duraklatılması için geçmesi gereken süre
-   **autopausebusy:** Kuyruktaki üyelerin meşgul olması durumunda otomatik olarak duraklatılıp duraklatılmayacağı
-   **autopauseunavail:** Kuyruktaki üyelerin kullanılamaz durumda olması durumunda otomatik olarak duraklatılıp duraklatılmayacağı
-   **maxlen:** Kuyruktaki maksimum çağrı sayısı
-   **servicelevel:** Kuyruktaki çağrıların hizmet seviyesi
-   **strategy:** Kuyruk stratejisi

    +   **'Ring All':** Bu stratejide, tüm kuyruk üyeleri eşit bir şekilde çağrı alır. Bu strateji, her bir üyenin çağrıya yanıt verme şansının eşit olduğu durumlarda kullanılabilir.
    +   **'Least Recent':** Bu stratejide, en son çağrıya en az yanıt veren üye çağrı alır. Bu strateji, kuyruktaki üyelerin yanıt verme sürelerinin farklı olduğu durumlarda kullanılabilir.
    +   **'Fewest Calls':** Bu stratejide, en az çağrıya sahip olan üye çağrı alır. Bu strateji, kuyruktaki üyelerin farklı yoğunlukta çağrı aldığı durumlarda kullanılabilir.
    +   **'Random':** Bu stratejide, rastgele bir üye çağrı alır. Bu strateji, kuyrukta eşit şekilde yoğunluk olmadığı durumlarda kullanılabilir.
    +   **'Round Robin':** Bu stratejide, üyeler sırayla çağrı alırlar. Bu strateji, tüm üyelerin eşit şekilde yoğunluk aldığı durumlarda kullanılabilir.
    +   **'Round Robin Memory':** Bu stratejide, en son çağrıya en az yanıt veren üye çağrı alır. Ancak, her üye kuyrukta eşit miktarda çağrı aldığında, tüm üyeler eşit şekilde çağrı alır.
    +   **'Linear':** Bu stratejide, çağrılar belirli bir sırayla sıralanır ve her üye sırayla çağrı alır. Bu strateji, kuyruktaki üyelerin farklı yoğunlukta çağrı aldığı durumlarda kullanılabilir.
    +   **'Weighted Random':** Bu stratejide, üyelerin belirli bir ağırlıklandırma faktörüne sahip olduğu düşünülür ve rastgele bir üye çağrı alır. Bu strateji, kuyruktaki üyelerin farklı yoğunlukta çağrı aldığı durumlarda kullanılabilir.
    +   **'Round Robin Ordered':** Bu stratejide, üyeler belirli bir sırayla çağrı alır. Ancak, bir üye çağrıya yanıt vermediği durumlarda, sıradaki diğer üye çağrı alır. Bu strateji, kuyruktaki üyelerin yanıt verme sürelerinin farklı olduğu durumlarda kullanılabilir.

-   **joinempty:** Kuyrukta hiç çağrı olmadığında üyelerin kuyruğa katılıp katılmayacağı
-   **leavewhenempty:** Kuyrukta hiç çağrı olmadığında üyelerin kuyruktan ayrılıp ayrılmayacağı
-   **reportholdtime:** Kuyrukta bekleyen çağrıların bekleme süresinin raporlanıp raporlanmayacağı
-   **memberdelay:** Üyeler arasında çağrıların dağıtımı için geçmesi gereken süre
-   **weight:** Kuyruktaki üyelerin öncelik seviyesi
-   **timeoutrestart:** Bir çağrının tekrar denemesi için beklenmesi gereken süre
-   **defaultrule:** Kuyruktaki çağrıların hangi kurala uyması gerektiğini belirleyen varsayılan kural
-   **timeoutpriority:** Kuyruktaki çağrıların zaman aşımı önceliği seviyesi.


## Kuyruğa Dahili Ekleme Parametreleri : 

-   **queue_name:** Kuyruk ismi.
-   **interface:** Kuyruğa dahil edilecek olan kullanıcının bağlandığı arayüz. Örneğin "SIP/100".
-   **membername:** Kuyruğa dahil edilecek olan kullanıcının ismi.
-   **state_interface:** Kuyruktaki kullanıcının durumunu (çevrimiçi, çevrimdışı, meşgul vb.) takip etmek için kullanılan arayüz.
-   **penalty:** Kuyruğa dahil edilen kullanıcının öncelik durumu. Daha yüksek bir değer, daha düşük öncelik anlamına gelir.
-   **paused:** Kuyruktaki kullanıcının duraklatılıp duraklatılmayacağına karar veren bir değerdir. "1" duraklatılmış, "0" ise duraklatılmamış anlamına gelir.
-   **uniqueid:** Kuyruk üyesinin eşsiz kimliği.
-   **wrapuptime:** Kuyruktan çıktıktan sonra, bir sonraki çağrı almadan önce geçmesi gereken süre.
-   **ringinuse:** Kuyruktaki kullanıcı meşgulse, çağrıyı diğer kullanıcılara yönlendirmek için kullanılan bir değerdir. "yes" veya "no" olabilir.


## Kuyruk Logları 


-   **time:** olayın gerçekleştiği tarih ve zaman
-   **data5:** olayla ilgili 5. bilgi
-   **data4:** olayla ilgili 4. bilgi
-   **data3:** olayla ilgili 3. bilgi
-   **data2:** olayla ilgili 2. bilgi
-   **data1:** olayla ilgili 1. bilgi
-   **event:** kuyruktaki olay türü (örn. JOIN, LEAVE, ABANDON)
-   **agent:** olayla ilgili ajanın kimliği (isteğe bağlı)
-   **queuename:** kuyruğun adı
-   **callid:** çağrı kimliği (isteğe bağlı)




## Event List

Sıra günlük olay tipleri
Aşağıdaki olaylar (ve bunlarla ilişkili bilgiler), sıra günlüğündeki olaylardır:

**ABANDON (pozisyon | origposition | bekleme süresi)** - Arayan, sıradaki konumunu terk etti. Pozisyon, arayanın sıradaki pozisyonu, kapattıklarında; origposition, arayanın ilk girdiğindeki orijinal pozisyonu; ve bekleme süresi, koparma anındaki bekleme süresidir.
**ADDMEMBER** - Bir üye sıraya eklendi. Köprülenmiş kanal adı, sıraya eklenen kanalın adı ile doldurulacaktır.
**AGENTDUMP** - Ajan, sıra duyurusunu dinlerken arayanı boşalttı.
**AGENTLOGIN (kanal)** - Ajan giriş yaptı. Kanal kaydedildi.
**AGENTCALLBACKLOGIN (exten@context)** - Geri arama ajanı giriş yaptı. Giriş uzantısı ve bağlam kaydedildi.
**AGENTLOGOFF (kanal | giriş saati)** - Ajan çıkış yaptı. Kanal kaydedildi ve ajanın giriş yaptığı toplam süre de kaydedildi.
**AGENTCALLBACKLOGOFF (exten@context | giriş saati | neden)** - Geri arama ajanı çıkış yaptı. Son giriş uzantısı ve bağlam kaydedildi, ajanın giriş yaptığı toplam süre de kaydedildi ve çıkışın nedeni normal bir çıkış değilse (Örn: Otomatik çıkış, Kanal müsait değil)
**ATTENDEDTRANSFER (yöntem | yöntem verisi | bekletme süresi | arama süresi | origposition)** - (12'de eklendi) Bu mesaj, katılımlı aktarımın nasıl tamamlandığını gösterecektir: Bir köprüleme birleşimi için BRIDGE, bir köprü veya kanalda bir uygulama çalıştırmak için APP veya iki köprüyü yerel kanallarla birleştirmek için LINK.
**BLINDTRANSFER (dahili | bağlam | bekletme süresi | arama süresi | origposition)** - (12'de eklendi) Kör aktarma, hedef bağlam ve dahili numara ile BLINDTRANSFER mesajına neden olacaktır.
**COMPLETEAGENT (bekleme süresi | arama süresi | origposition)** - Arayan bir ajanla bağlandı ve arama ajan tarafından normal olarak sonlandırıldı. Arayanın bekleme süresi ve aramanın uzunluğu da kaydedilir. Arayanın orijinal sıradaki pozisyonu origposition olarak kaydedilir.
**COMPLETECALLER (bekleme süresi | arama süresi | origposition)** - Arayan bir ajanla bağlandı ve arama arayan tarafından normal olarak sonlandırıldı. Arayanın bekle

**COMPLETECALLER(holdtime|calltime|origposition)** - Arayan bir ajanla bağlantı kurdu ve arama normal olarak arayan tarafından sonlandırıldı. Arayanın bekleme süresi ve aramanın süresi kaydedilir. Arayanın sıradaki orijinal pozisyonu origposition'da kaydedilir.

**CONFIGRELOAD** - Yapılandırma yeniden yüklendi (örneğin asterisk -rx reload ile).

**CONNECT(holdtime|bridgedchanneluniqueid|ringtime)** - Arayan bir ajanla bağlantı kurdu. Bekleme süresi, arayanın bekletildiği süreyi temsil eder. Bridged channel unique ID, aramayı alan sıra üyesi kanalının benzersiz kimliğini içerir. Bu, kayıt dosya adlarını sıradaki belirli bir çağrıya bağlamaya çalışırken yararlıdır. Ringtime, sıra üyesinin telefonunun cevaplanmadan önce çaldığı süreyi temsil eder.

**ENTERQUEUE(url|callerid)** - Bir çağrı sıraya girdi. URL (belirtilmişse) ve Caller*ID kaydedilir.

**EXITEMPTY(position|origposition|waittime)** - Sıra, ulaşılabilir üyesi olmadığında arayanı zorla sıradan çıkardı ve arayanın pozisyonu, arayanın sıraya girdiği orijinal pozisyonu ve bağlantının kesildiği sırada aramanın sırada beklediği süre kaydedilir.

**EXITWITHKEY(key|position|origposition|waittime)** - Arayan, sıradan çıkmak için bir menü tuşunu kullanmayı seçti. Tuş ve arayanın sıradaki pozisyonu kaydedilir. Arayanın giriş pozisyonu ve bekleyen süre de kaydedilir.

**EXITWITHTIMEOUT(position|origposition|waittime)** - Arayan çok uzun süre bekletildi ve zaman aşımı süresi doldu. Zaman aşımı gerçekleştiğinde sırada pozisyon, giriş pozisyonu ve beklenen süre kaydedilir.

**QUEUESTART** - Sıra sistemi bu oturum için ilk kez başlatıldı.

**REMOVEMEMBER** - Bir sıra üyesi sıradan çıkarıldı. Bridge channel alanı, sıradan çıkarılan üyenin adını içerecektir.

**RINGNOANSWER(ringtime)** - Mevcut sıra üyesine bağlanmak için ringtime ms denedikten sonra, üye çağrıyı açmadan bağlantı denemesi sona erdi. Kötü sıra üyesi!

**RINGCANCELED** - Bir arayan, bir sıra üyesini arıyor, ancak üye yanıt vermeden veya zaman aşımı yapmadan önce arama sonlandırıyor.

**RINGNOANSWER (ringtime)** - Mevcut kuyruk üyesine bağlanmak için ringtime ms denemeden sonra, üye aramayı cevaplamadan deneme sona erdi. Kötü kuyruk üyesi!

**RINGCANCELED** - Bir arayan, bir kuyruk üyesini ararken, üye cevaplamadan önce veya zaman aşımına uğramadan önce aramayı sonlandırır.

**SYSCOMPAT** - Bir çağrı, bir ajans tarafından cevaplandı, ancak kanallar uyumlu olmadığından çağrı düştü.

**TRANSFER(extension|context|holdtime|calltime|origposition)** - Arayan farklı bir dahili numaraya aktarıldı. Bağlam ve dahili numara kaydedilir. Arayanın bekleme süresi ve çağrının süresi kaydedilir, aynı zamanda aktarma anındaki arayanın giriş pozisyonu da kaydedilir. Lütfen unutmayın, SIP UA'ların yeniden daveti yoluyla gerçekleştirdiği aktarmaların Asterisk tarafından her zaman yakalanamayacağı ve bu olayı tetiklemeyebileceği. Kuyruk üyesi tarafından gerçekleştirilen bir aktarımın bu etkinliği tetikleyeceğinden %100 emin olmanın tek yolu, Asterisk'in yerleşik aktarım işlevselliğini kullanmaktır.