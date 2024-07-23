import asyncio
import aiohttp
import json

async def fetch_data():
    # 여기에 아파트 데이터를 가져오는 로직을 구현합니다
    pass

async def main():
    while True:
        data = await fetch_data()
        # 데이터 처리 및 Home Assistant에 전송하는 로직
        await asyncio.sleep(60)  # 1분마다 실행

if __name__ == "__main__":
    asyncio.run(main())
