from telethon import TelegramClient, errors
import asyncio
import os
import sys

api_id = int(os.environ.get('API_ID', 36285371))
api_hash = os.environ.get('API_HASH', 'cc13c78a223d855c0def54a3de7658d3')

# استخدم None - لن يحفظ ملفاً
client = TelegramClient(None, api_id, api_hash)

async def main():
    print("🔄 جاري تسجيل الدخول...")
    
    # إذا كانت هذه أول مرة، سيدخل رمز التحقق
    await client.start()
    print("✅ تم تسجيل الدخول بنجاح!")
    
    GROUP = "https://t.me/+1dQIce3w7L1hNTNi"
    MESSAGE = """🔥 متوفر حسابات PayPal جديدة فارغة

أوكرانيا
كمبوديا
إثيوبيا
إندونيسيا

🎮 تنفع لدفع السوني ونتفلكس.

📩 راسلني للشراء."""
    
    count = 0
    while True:
        try:
            await client.send_message(GROUP, MESSAGE)
            count += 1
            print(f"✅ [{count}] تم الإرسال")
            await asyncio.sleep(90)
        except errors.FloodWaitError as e:
            print(f"⛔ حظر {e.seconds} ثانية")
            await asyncio.sleep(e.seconds + 30)
        except Exception as e:
            print(f"❌ خطأ: {e}")
            await asyncio.sleep(90)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"❌ فشل: {e}")
        sys.exit(1)
