import asyncio
import aiohttp
import secrets, string

async def test_this(emails):
    async def fetch(session, email):
        try:
            url = "https://100067.connect.garena.com/game/account_security/swap:send_otp"
            headers = {
                'Accept': 'application/json',
                'Accept-Encoding': 'gzip',
                'Content-Type': 'application/x-www-form-urlencoded',
                'User-Agent': "GarenaMSDK/4.0.39(PMT3748_3G ;Android 10;ko;KR;)",
            }
            data = {
                'app_id': 100067,
                'email': email,
            }

            async with session.post(url=url, headers=headers, data=data, timeout=5) as response:
                text = await response.text()
                print(f"{email} - {text}")
        except Exception as e:
            print(e)


    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, email) for email in emails]
        return await asyncio.gather(*tasks)

"""start the runtime"""
async def runner():


    def get_emails(amount):
        emails = []
        for _ in range(amount):
            password = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(20)) + "@gmail.com"
            emails.append(password)
        return emails

    try:
        emails = get_emails(100)
        await test_this(emails)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    asyncio.run(runner())
