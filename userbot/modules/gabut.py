# Coded by Koala
# Recode by @Bomansyah

import time
from datetime import datetime
from platform import uname
from time import sleep

from userbot import ALIVE_NAME, StartTime
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["Dtk", "Mnt", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@register(outgoing=True, pattern=r"^\.keping$")
async def pingme(pong):
    """For .ping command, ping the userbot from any chat."""
    await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("**『𝙉𝙂𝙀𝙉𝙏𝙊𝙏』**")
    await pong.edit("**𝙆𝙊𝙉𝙏𝙊𝙇**")
    await pong.edit("**𝙋𝙀𝘾𝘼𝙃 𝘽𝙄𝙅𝙄 𝙇𝙊 𝘼𝙅𝙂**")
    await pong.edit("**𝙎𝙄𝘼𝙋 𝙎𝙄𝘼𝙋 𝙂𝙐𝘼 𝙋𝙐𝙆𝙐𝙇 𝙉𝙄𝙃 𝘽𝙄𝙅𝙄 𝙇𝙊**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(
        f"✲ 𝘿𝙐𝘼𝙍 𝙈𝙀𝙈𝙀𝙆 "
        f"\n ⫸ ᴷᵒⁿᵗᵒˡ `%sms` \n"
        f"✲ 𝘿𝙐𝘼𝙍 𝙆𝙊𝙉𝙏𝙊𝙇 "
        f"\n ⫸ 𝙏𝙐𝘼𝙉『`{ALIVE_NAME}`』 \n" % (duration)
    )


@register(outgoing=True, pattern=r"^\.kping$")
async def pingme(pong):
    """For .ping command, ping the userbot from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("8✊===D")
    await pong.edit("8=✊==D")
    await pong.edit("8==✊=D")
    await pong.edit("8===✊D")
    await pong.edit("8==✊=D")
    await pong.edit("8=✊==D")
    await pong.edit("8✊===D")
    await pong.edit("8=✊==D")
    await pong.edit("8==✊=D")
    await pong.edit("8===✊D")
    await pong.edit("8==✊=D")
    await pong.edit("8=✊==D")
    await pong.edit("8✊===D")
    await pong.edit("8=✊==D")
    await pong.edit("8==✊=D")
    await pong.edit("8===✊D")
    await pong.edit("8===✊D💦")
    await pong.edit("8====D💦💦")
    await pong.edit("**CROOTTTT PINGGGG!**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(
        f"**NGENTOT!! 🐨**\n**KAMPANG** : %sms\n**Bot Uptime** : {uptime}🕛" % (duration)
    )


@register(outgoing=True, pattern=r"^\.a(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Halo Saya {DEFAULTUSER}**")
    sleep(2)
    await typew.edit("**Assalamualaikum**")


# Owner @Si_Dian


@register(outgoing=True, pattern=r"^\.j(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**JAKA SEMBUNG BAWA GOLOK**")
    sleep(3)
    await typew.edit("**GAK NYAMBUNG GOBLOKK!!!🖕**")


# Owner @Si_Dian


@register(outgoing=True, pattern=r"^\.k(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Hallo KIMAAKK SAYA {DEFAULTUSER}**")
    sleep(2)
    await typew.edit("**LU SEMUA NGENTOT 🔥**")


# Owner @Si_Dian


@register(outgoing=True, pattern=r"^\.ass(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Salam Dulu Biar Sopan**")
    sleep(2)
    await typew.edit("**السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ**")


# Owner @mixiologist


@register(outgoing=True, pattern="^.usange(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Getting Information...`")
    sleep(1)
    await typew.edit(
        "**Informasi Dyno ★**:\n\n╭━━━━━━━━━━━━━━━━━━━━╮\n"
        f"-> `Penggunaan Dyno` **{ALIVE_NAME}**:\n"
        f" ❉ **10 Jam - "
        f"51 Menit - 0%**"
        "\n ◐━─━─━─━─━──━─━─━─━─━◐\n"
        "-> `Sisa Dyno Bulan Ini`:\n"
        f" ❉ **9989 Jam - 9948 Menit "
        f"- 99%**\n"
        "╰━━━━━━━━━━━━━━━━━━━━╯"
    )


# @mixiologist

