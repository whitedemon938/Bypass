from asyncio import  sleep as asleep
from aiohttp import ClientSession
from os import environ
from logging import error as logerror
from Bypass import BASE_URL, PORT

if PORT is not None:
    async with ClientSession() as session:
        while True:
            try:
                res = await session.get(BASE_URL)
                if res.status == 200:
                    print(f"Server's Up. Status Code: {res.status}")
                    await asleep(600)
                else:
                    print(f"Server Returned Status Code: {res.status}")
            except Exception as e:
                logerror(f"alive.py: {e}")
                await asleep(600)
                continue
