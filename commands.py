import os
from aiogram import types
from config import USER_ID, GITHUB_REPO
from strings import COMMANDS
import subprocess
import requests


async def restart(message: types.Message):
    if message.from_user.id == USER_ID:
        await message.answer("📢 Cihaz yeniden başlatılıyor...")
        os.system("sudo reboot")

async def shutdown(message: types.Message):
    if message.from_user.id == USER_ID:
        await message.answer("⚠ Cihaz kapanıyor...")
        os.system("sudo shutdown -h now")

async def status(message: types.Message):
    await message.answer("✅ Raspberry Pi aktif ve çalışıyor!")

async def check_update(message: types.Message):
    """GitHub'daki son commit ile mevcut kodun commit ID'sini karşılaştırır"""
    try:

        local_commit = subprocess.check_output(["git", "rev-parse", "HEAD"]).decode("utf-8").strip()

        url = f"https://api.github.com/repos/{GITHUB_REPO}/commits/main"
        response = requests.get(url)
        latest_commit = response.json()["sha"]

        if local_commit == latest_commit:
            await message.answer("✅ Botunuz güncel!")
        else:
            await message.answer("⚠️ Güncelleme mevcut! Yeni sürümü çekmek için `/update` komutunu kullanın.")

    except Exception as e:
        await message.answer(f"❌ Güncelleme kontrol edilirken hata oluştu: {str(e)}")

async def update_code(message: types.Message):
    """Kodları GitHub'dan güncelleyip botu yeniden başlatır"""
    try:
        await message.answer("🚀 Güncelleme indiriliyor...")
        
        subprocess.run(["git", "pull"], check=True)
        
        await message.answer("✅ Güncelleme tamamlandı! Raspberry Pi yeniden başlatılıyor...")
        
        subprocess.run(["sudo", "reboot"])
    
    except Exception as e:
        await message.answer(f"❌ Güncelleme sırasında hata oluştu: {str(e)}")

async def get_cpu_temp(message: types.Message):
    """Raspberry Pi'nin CPU sıcaklığını döndürür"""
    try:

        temp_output = subprocess.check_output(["vcgencmd", "measure_temp"]).decode("utf-8")
        temp = temp_output.replace("temp=", "🌡 CPU Sıcaklığı: ").strip()

        await message.answer(temp)

    except Exception as e:
        await message.answer(f"❌ Sıcaklık okunamadı: {str(e)}")