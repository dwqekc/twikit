import asyncio
import httpx

from twikit import Client,TwoCaptcher

###########################################

# Enter your account information,proxy,2captcha token
COOKIES = ...
PROXY = ...
API_KEY = ...



async def main():
    captcha_solver = TwoCaptcher(api_key=API_KEY)
    transport = httpx.AsyncHTTPTransport(
        proxy=PROXY
    )
    http = httpx.AsyncClient(transport=transport,follow_redirects=True,timeout=httpx.Timeout(60.0))

    client = Client(captcha_solver=captcha_solver,http=http)

    # Asynchronous client methods are coroutines and
    # must be called using `await`.
    client.set_cookies(cookies=COOKIES)
    article_id = await client.create_article(title='Example title',text='Example text',users=['@elonmusk'],media='...')
    print(article_id)



asyncio.run(main())
