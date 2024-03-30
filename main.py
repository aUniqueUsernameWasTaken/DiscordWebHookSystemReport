import asyncio
import aiohttp
import discord
import gatherInfo
from discord import Webhook
url = "https://discord.com/api/webhooks/1223585404255604817/Nmw01vX5RYuwTxcrihO2XoF6kUXtwGSkyrzozygePi-t5e6bjL_irwQt-ch29ci3nWVc"


async def send_webhook(url):
    async with aiohttp.ClientSession() as session:            
        webhook = Webhook.from_url(url, session=session)
        embed = discord.Embed(title="Syster", description="\n".join(gatherInfo.getUsage()), color=0x2e3440)
        await webhook.send(embed=embed, username="Syster")

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(send_webhook(url))
    loop.close()