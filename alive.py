
from asyncio import sleep as asleep, run
from aiohttp import ClientSession
import logging
from bot import BASE_URL, PORT

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("alive.log"),
        logging.StreamHandler()
    ]
)

async def check_server():
    if PORT is not None:
        async with ClientSession() as session:
            while True:
                try:
                    res = await session.get(BASE_URL)
                    if res.status == 200:
                        logging.info(f"Server's Up. Status Code: {res.status}")
                    else:
                        logging.warning(f"Server Returned Status Code: {res.status}")
                except Exception as e:
                    logging.error(f"alive.py Exception: {e}")
                await asleep(600)

if __name__ == "__main__":
    run(check_server())
