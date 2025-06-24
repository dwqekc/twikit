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
    media_id_header = await client.upload_media(...)
    media_id_1 = await client.upload_media(...)
    media_id_2 = await client.upload_media(...)
    media_id_3 = await client.upload_media(...)
    article_id = await client.create_article(title='Example title',users=['@elonmusk'],media_id_1=media_id_1,media_id_2=media_id_2,media_id_3=media_id_3,text_1='text_1',text_2='text_2',text_3='text_3',
                                             media_id_header=media_id_header,link='',link_spoof='')
    print(article_id)



asyncio.run(main())
