# Raspberry Pi Telegram Bot 🤖

Bu proje, **Raspberry Pi** üzerinde çalışan bir **Telegram botudur**.  
Bot, Raspberry Pi açıldığında otomatik olarak bir Telegram grubuna mesaj atabilir ve komutlarla yönetilebilir (örneğin, `reboot` ve `shutdown`).

## 🚀 Kurulum ve Çalıştırma

### 1️⃣ Gerekli Bağımlılıkları Yükleme

Önce **virtual environment** oluşturup bağımlılıkları yükleyelim:

```bash
# Sanal ortam oluştur
python3 -m venv venv

# Sanal ortamı etkinleştir
source venv/bin/activate

# Bağımlılıkları yükle
pip install -r requirements.txt
```

### 2️⃣ config.py Dosyasını Düzenleme

Projede çalışabilmesi için `config.py` dosyasını oluşturup aşağıdaki gibi doldurun:

```python
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"  # Telegram Bot Token
USER_ID = "XXXXXXXXXX"  # User ID
```

### 3️⃣ Botu Çalıştırma

Botu çalıştırmak için:

```bash
python3 run.py
```

## 📌 Notlar

- Bu bot Aiogram 2.25.1 sürümünü kullanmaktadır.
- Eğer bot gruba mesaj atamıyorsa, config.py içindeki GROUP_ID'yi kontrol edin.
- Raspberry Pi'nin terminalinde çalıştırılmalıdır.
