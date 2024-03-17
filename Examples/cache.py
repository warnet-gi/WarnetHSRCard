import asyncio
import starrailcard

async def main():
    async with starrailcard.Card(cache = {"maxsize": 500, "ttl": 60}) as card:
        print(card)

    #OR

    async with starrailcard.Card(cache = {"maxsize": 500}) as card:
        print(card)

    #OR

    async with starrailcard.Card(cache = {"ttl": 60}) as card:
        print(card)
        
asyncio.run(main())
