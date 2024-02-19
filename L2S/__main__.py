import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from L2S import LOGGER, app, userbot
from L2S.core.call import TGN
from L2S.misc import sudo
from L2S.plugins import ALL_MODULES
from L2S.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await sudo()
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("L2S.plugins" + all_module)
    LOGGER("L2S.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await TGN.start()
    try:
        await TGN.stream_call("https://telegra.ph/file/69503142042c9f3b24c4c.mp4")
    except NoActiveGroupCall:
        LOGGER("L2S").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await TGN.decorators()
    LOGGER("L2S").info(
        "TGN Music Bot Started Successfully"
    )
    await idle()
    await app.stop()
    LOGGER("L2S").info("Stopping TGN Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
