# Copyright (C) 2020 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.

from covid import Covid

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^\.covid (.*)")
async def corona(event):
    await event.edit("`Processing...`")
    country = event.pattern_match.group(1)
    covid = Covid(source="worldometers")
    country_data = covid.get_status_by_country_name(country)
    if country_data:
        output_text = f"`⚠️ᴄᴏɴғɪʀᴍᴇᴅ   : {country_data['confirmed']} (+{country_data['new_cases']})`\n"
        output_text += f"`☢️ᴀᴄᴛɪᴠᴇ      : {country_data['active']}`\n"
        output_text += f"`🤕ᴄʀɪᴛɪᴄᴀʟ    : {country_data['critical']}`\n"
        output_text += f"`😟ɴᴇᴡ ᴅᴇᴀᴛʜs  : {country_data['new_deaths']}`\n\n"
        output_text += f"`⚰️ᴅᴇᴀᴛʜs      : {country_data['deaths']} (+{country_data['new_deaths']})`\n"
        output_text += f"`😔ɴᴇᴡ ᴄᴀsᴇs   : {country_data['new_cases']}`\n"
        output_text += f"`😇ʀᴇᴄᴏᴠᴇʀᴇᴅ   : {country_data['recovered']}`\n"
        output_text += f"`🧪ᴛᴏᴛᴀʟ ᴛᴇsᴛ : {country_data['total_tests']}`\n\n"
        output_text += f"**ᴅᴀᴛᴀ ᴘʀᴏᴠɪᴅᴇᴅ ʙʏ [ᴡᴏʀʟᴅᴏᴍᴇᴛᴇʀ]**(https://www.worldometers.info/coronavirus/country/{country})"
    else:
        output_text = "No information yet about this country!"

    await event.edit(f"**ᴄᴏʀᴏɴᴀ ᴠɪʀᴜs ɪɴғᴏ ɪɴ {country}:**\n\n{output_text}")


@register(outgoing=True, pattern="^.covid$")
async def corona(event):
    await event.edit("`Processing...`")
    country = "World"
    covid = Covid(source="worldometers")
    country_data = covid.get_status_by_country_name(country)
    if country_data:
        output_text = f"`⚠️ᴄᴏɴғɪʀᴍᴇᴅ   : {country_data['confirmed']} (+{country_data['new_cases']})`\n"
        output_text += f"`☢️ᴀᴄᴛɪᴠᴇ      : {country_data['active']}`\n"
        output_text += f"`🤕ᴄʀɪᴛɪᴄᴀʟ    : {country_data['critical']}`\n"
        output_text += f"`😟ɴᴇᴡ ᴅᴇᴀᴛʜs  : {country_data['new_deaths']}`\n\n"
        output_text += f"`⚰️ᴅᴇᴀᴛʜs      : {country_data['deaths']} (+{country_data['new_deaths']})`\n"
        output_text += f"`😔ɴᴇᴡ ᴄᴀsᴇs   : {country_data['new_cases']}`\n"
        output_text += f"`😇ʀᴇᴄᴏᴠᴇʀᴇᴅ   : {country_data['recovered']}`\n"
        output_text += "`🧪ᴛᴏᴛᴀʟ ᴛᴇsᴛ : N/A`\n\n"
        output_text += f"**ᴅᴀᴛᴀ ᴘʀᴏᴠɪᴅᴇᴅ ʙʏ **[ᴡᴏʀʟᴅᴏᴍᴇᴛᴇʀ](https://www.worldometers.info/coronavirus/country/{country})"
    else:
        output_text = "No information yet about this country!"

    await event.edit(f"**ᴄᴏʀᴏɴᴀ ᴠɪʀᴜs ɪɴғᴏ ɪɴ {country}:**\n\n{output_text}")


CMD_HELP.update(
    {
        "covid": "**Plugin : **`covid`\
        \n\n  •  **Syntax :** `.covid`\
        \n  •  **Function : **Memberikan Informasi semua data COVID-19 dari semua negara.\
        \n\n  •  **Syntax :** `.covid` <nama negara>\
        \n  •  **Function : **Memberikan Informasi tentang data COVID-19 dari negara.\
    "
    }
)
