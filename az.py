from telethon import TelegramClient, errors
from telethon.sessions import StringSession
import asyncio
import os

# ========= بياناتك ========= #
api_id = 36285371
api_hash = "cc13c78a223d855c0def54a3de7658d3"

# النص الذي استخرجته (String Session)
string_session = "1AZWarzMBu4Fhb0aWB-bjcsWMswqINpt52bO9t3MKcdRgfqoHH2X3aYP17Eky9kxPCXQxeFrsuqnPVt5wZyCDV6v0ScRQkMZ9gCLNKlsqwXk_Wo55niuD06Ol-XonUJ3odlVQSZ_qDch-pIUG5Ui5d8KP4i9EOWigO2P9gQfIwh6vB8i_j2Ur-IknIljvWhe0NSB6sQqqDJtXh3RtGymUdjcgyVx-acGobOlbBq-2-HT8hbnXHiQjX3hwWSCLOfWdrCkfDB9NjQmweYeeVyDzWu8JieF0xNLbJ8pnuaJH_vRtyYEiejOFY1MQbVSR4w9ItxlWwzHJAyfcJZSxnyMRDyZK_u6echU="

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
    # استخدام StringSession بدلاً من ملف session التقليدي
    client = TelegramClient(StringSession(string_session), api_id, api_hash)
    await client.start()
    print("🚀 بدء النشر المستمر (كل دقيقة ونصف)...")
    
    message_count = 0
    
    while True:
        try:
            await client.send_message(GROUP, MESSAGE)
            message_count += 1
            print(f"✅ [{message_count}] تم الإرسال بنجاح")
            
            # انتظار دقيقة ونصف
            await asyncio.sleep(90)
            
        except errors.FloodWaitError as e:
            print(f"⛔ تم الحظر المؤقت: {e.seconds} ثانية")
            await asyncio.sleep(e.seconds + 30)
            
        except Exception as e:
            print(f"❌ حدث خطأ: {e}")
            await asyncio.sleep(90)

# ========= تشغيل السكربت ========= #
if __name__ == "__main__":
    asyncio.run(main())
