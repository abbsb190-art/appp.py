from telethon import TelegramClient, errors
import asyncio
import random

# ========= بياناتك ========= #
api_id = 36285371
api_hash = "cc13c78a223d855c0def54a3de7658d3"

# ========= المجموعة والرسالة ========= #
GROUP = "https://t.me/+1dQIce3w7L1hNTNi"

MESSAGE = """🔥 متوفر حسابات PayPal جديدة فارغة

أوكرانيا
كمبوديا
إثيوبيا
إندونيسيا

🎮 تنفع لدفع السوني ونتفلكس.

📩 راسلني للشراء."""

async def main():
    client = TelegramClient("session", api_id, api_hash)
    await client.start()
    print("🚀 بدء النشر المستمر (كل دقيقة ونصف)...")
    
    message_count = 0
    
    while True:
        try:
            await client.send_message(GROUP, MESSAGE)
            message_count += 1
            print(f"✅ [{message_count}] تم الإرسال بنجاح")
            
            # انتظار دقيقة ونصف (90 ثانية)
            print(f"⏳ انتظار دقيقة ونصف حتى الإرسال التالي...")
            await asyncio.sleep(90)
            
        except errors.FloodWaitError as e:
            print(f"⛔ تم الحظر المؤقت: {e.seconds} ثانية")
            print("⏳ جاري الانتظار حتى انتهاء الحظر...")
            await asyncio.sleep(e.seconds + 30)
            
        except Exception as e:
            print(f"❌ حدث خطأ: {e}")
            print("🔄 إعادة المحاولة بعد دقيقة ونصف...")
            await asyncio.sleep(90)

# ========= تشغيل السكربت ========= #
if __name__ == "__main__":
    asyncio.run(main())