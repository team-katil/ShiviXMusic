from os import path

from yt_dlp import YoutubeDL

from ShiviXMusic import BOT_NAME

ytdl = YoutubeDL(
    {
        "outtmpl": "downloads/%(id)s.%(ext)s",
        "format": "bestaudio/best",
        "geo_bypass": True,
        "nocheckcertificate": True,
        "quiet": True,
        "no_warnings": True,
    }
)


def download(videoid: str, mystic, title) -> str:
    flex = {}
    url = f"https://www.youtube.com/watch?v={videoid}"

    def my_hook(d):
        if d["status"] == "downloading":
            percentage = d["_percent_str"]
            per = (str(percentage)).replace(".", "", 1).replace("%", "", 1)
            per = int(per)
            eta = d["eta"]
            speed = d["_speed_str"]
            size = d["_total_bytes_str"]
            bytesx = d["total_bytes"]
            if str(bytesx) in flex:
                pass
            else:
                flex[str(bytesx)] = 1
            if flex[str(bytesx)] == 1:
                flex[str(bytesx)] += 1
                try:
                    if eta > 2:
                        mystic.edit(
                            f"**» {BOT_NAME} 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳𝙴𝚁**\n\n**𝚃𝙸𝚃𝙻𝙴 :** {title}\n**𝚂𝙸𝚉𝙴 :** {size}\n\n**<u>𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳𝙴𝙳 :</u>**\n**𝚂𝙿𝙴𝙴𝙳 :** {speed}\n**𝙴𝚃𝙰 :** {eta} 𝚂𝙴𝙲𝙾𝙽𝙳𝚂\n\n\n{percentage} ─────────── 100%"
                        )
                except Exception as e:
                    pass
            if per > 250:
                if flex[str(bytesx)] == 2:
                    flex[str(bytesx)] += 1
                    if eta > 2:
                        mystic.edit(
                            f"**» {BOT_NAME} 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳𝙴𝚁**\n\n**𝚃𝙸𝚃𝙻𝙴 :** {title}\n**𝚂𝙸𝚉𝙴 :** {size}\n\n**<u>𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳𝙴𝙳 :</u>**\n**𝚂𝙿𝙴𝙴𝙳 :** {speed}\n**𝙴𝚃𝙰 :** {eta} 𝚂𝙴𝙲𝙾𝙽𝙳𝚂\n\n\n{percentage} ■■■───────── 100%"
                        )
            if per > 500:
                if flex[str(bytesx)] == 3:
                    flex[str(bytesx)] += 1
                    if eta > 2:
                        mystic.edit(
                            f"**» {BOT_NAME} 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳𝙴𝚁**\n\n**𝚃𝙸𝚃𝙻𝙴 :** {title}\n**𝚂𝙸𝚉𝙴 :** {size}\n\n**<u>𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳𝙴𝙳 :</u>**\n**𝚂𝙿𝙴𝙴𝙳 :** {speed}\n**𝙴𝚃𝙰 :** {eta} 𝚂𝙴𝙲𝙾𝙽𝙳𝚂\n\n\n{percentage} ■■■■■■────── 100%"
                        )
            if per > 800:
                if flex[str(bytesx)] == 4:
                    flex[str(bytesx)] += 1
                    if eta > 2:
                        mystic.edit(
                            f"**» {BOT_NAME} 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳𝙴𝚁**\n\n**𝚃𝙸𝚃𝙻𝙴 :** {title}\n**𝚂𝙸𝚉𝙴 :** {size}\n\n**<u>𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳𝙴𝙳 :</u>**\n**𝚂𝙿𝙴𝙴𝙳 :** {speed}\n**𝙴𝚃𝙰 :** {eta} 𝚂𝙴𝙲𝙾𝙽𝙳𝚂\n\n\n{percentage} ■■■■■■■■■■── 100%"
                        )
        if d["status"] == "finished":
            try:
                taken = d["_elapsed_str"]
            except Exception as e:
                taken = "00:00"
            size = d["_total_bytes_str"]
            mystic.edit(
                f"**» {BOT_NAME} 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳𝙴𝚁**\n\n**𝚃𝙸𝚃𝙻𝙴 :** {title}\n\n100% ■■■■■■■■■■■■ 100%\n\n**𝙲𝙾𝙽𝚅𝙴𝚁𝚃𝙸𝙽𝙶 𝙰𝚄𝙳𝙸𝙾 [𝙵𝙵𝙼𝙿𝙴𝙶 𝙿𝚁𝙾𝙲𝙴𝚂𝚂]**"
            )

    ydl_optssx = {
        "format": "bestaudio/best",
        "outtmpl": "downloads/%(id)s.%(ext)s",
        "geo_bypass": True,
        "nocheckcertificate": True,
        "quiet": True,
        "no_warnings": True,
    }
    try:
        x = YoutubeDL(ydl_optssx)
        x.add_progress_hook(my_hook)
        dloader = x.download([url])
    except Exception as y_e:
        return print(y_e)
    else:
        dloader
    info = x.extract_info(url, False)
    xyz = path.join("downloads", f"{info['id']}.{info['ext']}")
    return xyz
