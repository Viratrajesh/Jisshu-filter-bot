import os

class script(object):
    START_TXT = """<b>Hey {},\n\nI am a powerful AutoFilter Bot. You can use me in your group—I will provide movies or series in your group and PM!! 😍\n<blockquote>🌿 Maintained by: <a href="https://t.me/Askmovies">Askmovies</a></blockquote></b>"""

    TELE_TXT = """<b>/telegraph - Send me a picture or video (under 5 MB)\n\nNote: This command works in both groups and bot PM.</b>"""

    FSUB_TXT = """<b>• Add me to your group and make me an admin 😗
• Make me admin in your target force-subscribe channel or group 😉
• Send /fsub your_target_chat_id
  Example: <code>/fsub -1001234567890</code>

Now it's set. I will compel users to join your channel/group before providing files.

To disable fsub in your group, send <code>/del_fsub</code>.
To check fsub status, send <code>/show_fsub</code>.</b>"""

    FORCESUB_TEXT = """<b>In order to get the requested movie:
You must join our official channel.

First, click on the "Join Update Channel" button, then click on the "Request to Join" button.
After that, try accessing the movie again, then click "Try Again".</b>"""

    TTS_TXT = """<b>• Send /tts to use this feature</b>"""

    DISCLAIMER_TXT = """<b>THIS IS AN OPEN SOURCE PROJECT.
All files in this bot are freely available on the internet or posted by others. This bot only indexes publicly available files. We respect copyright laws and comply with DMCA & EUCD. If any content here infringes on your rights, please contact me for removal. The bot does not own any content—only indexes files from Telegram.
<blockquote>🌿 Maintained by: <a href='https://t.me/Master_xkid'>Askmovies</a></blockquote></b>"""

    ABOUT_TEXT = """<blockquote><b>‣ My Name: Masterx\n‣ Creator: <a href='https://t.me/Rajesh18'>MR. Rajesh</a></b></blockquote>"""

    SUPPORT_GRP_MOVIE_TEXT = """<b>Hey {},\n\nI found {} results 🎁, but I can't send here 🤞🏻\nPlease join our requests group to get them ✨</b>"""

    CHANNELS = """<u>Our All Groups and Channels:</u>\n
▫ All latest and old movies & series.
▫ All languages supported.
▫ Always admin support.
▫ 24×7 service available."""

    LOGO = """\nBOT WORKING PROPERLY 🔥"""

    RESTART_TXT = """<b>Bot Restarted!\n> {}\n📅 Date: <code>{}</code>\n⏰ Time: <code>{}</code>\n🌐 Timezone: <code>Asia/Kolkata</code>\n🛠️ Build Status: <code>v4.2 [Stable]</code>\n\nBy Creator</b>"""

    STATUS_TXT = """<b><u>🗃 Database 1</u>\n» Total users: <code>{}</code>\n» Total groups: <code>{}</code>\n» Used storage: <code>{} / {}</code>\n\n<u>🗳 Database 2</u>\n» Total files: <code>{}</code>\n» Used storage: <code>{} / {}</code>\n\n<u>🤖 Bot Details</u>\n» Uptime: <code>{}</code>\n» RAM: <code>{}%</code>\n» CPU: <code>{}%</code></b>"""

    NEW_USER_TXT = """<b>#New_User {}\n\nID: <code>{}</code>\nName: {}</b>"""

    NEW_GROUP_TXT = """<b>#New_Group {}\nGroup name: {}\nID: <code>{}</code>\nGroup username: @{}\nGroup link: {}\nTotal members: <code>{}</code>\nAdded by: {}</b>"""

    REQUEST_TXT = """<b>📜 User: {}\n📇 ID: <code>{}</code>\n🎁 Request msg: <code>{}</code></b>"""

    IMDB_TEMPLATE_TXT = """<b>Hey {message.from_user.mention}, here are the results for your query: {search}.\n\n🍿 Title: {title}\n🎃 Genres: {genres}\n📆 Year: {release_date}\n⭐ Rating: {rating}/10</b>"""

    FILE_CAPTION = """<b>{file_name}\n\nJoin ➥ <a href="https://t.me/Jisshu_Originals">Jisshu Originals</a></b>"""

    ALRT_TXT = "Jaldi yaha se hato!"

    OLD_ALRT_TXT = "You're using old messages—send a new request."

    NO_RESULT_TXT = """<b>This message is not released or added in my database 🙄</b>"""

    I_CUDNT = """<b>Hello {},\n\nI couldn't find any movie or series with that name.. 😐</b>"""

    I_CUD_NT = """<b>Hello {},\n\nI couldn't find anything related to that 😞… please check your spelling.</b>"""

    CUDNT_FND = """<b>Hello {},\n\nI couldn't find anything related to that—did you mean one of these? 👇</b>"""

    FONT_TXT = """<b>You can change your font style by using the /font command:\n
<code>/font hi how are you</code></b>"""

    PLAN_TEXT = """<b>We offer premium plans at very low prices:\n\n1 Rupee/day 👻\n29 Rupees/1 month 😚\n55 Rupees/2 months 😗\n\nClick below to continue buying.</b>"""

    VERIFICATION_TEXT = """<b>Hey {} {},\n\n📌 You are not verified today—click "Verify" to get unlimited access until next verification.\n\n#Verification: 1/3 ✓\n\nTo bypass verification, send /plan to buy bot subscription.</b>"""

    VERIFY_COMPLETE_TEXT = """<b>Hey {},\n\nYou have completed the 1st verification ✓\n\nNow you have unlimited access until next {}</b>"""

    SECOND_VERIFICATION_TEXT = """<b>Hey {} {},\n\n📌 You are not verified—tap the Verify link to get access until next verification.\n
#Verification: 2/3\nTo bypass, send /plan.</b>"""

    SECOND_VERIFY_COMPLETE_TEXT = """<b>Hey {},\n\nYou completed the 2nd verification ✓\n\nNow you have access until next {}</b>"""

    THIRDT_VERIFICATION_TEXT = """<b>Hey {},\n\n📌 You are not verified today—tap the Verify link to get full-day access.\n#Verification: 3/3\nTo bypass again, buy premium.</b>"""

    THIRDT_VERIFY_COMPLETE_TEXT = """<b>Hey {},\n\nYou completed the 3rd verification ✓\n\nNow you have unlimited access until next full day.</b>"""

    VERIFIED_LOG_TEXT = """<b><u>☄ User Verified Successfully ☄</u>\n\n⚡ Name: {} [<code>{}</code>]\n📆 Date: <code>{}</code>\n\n#verified_{}_completed</b>"""

    MOVIES_UPDATE_TXT = """<b>#New_File_Added ✅\n🍿 Title: {title}\n🎃 Genres: {genres}\n📆 Year: {year}\n⭐ Rating: {rating}/10</b>"""

    PREPLANS_TXT = """<b>Hey {},\n\n🎁 Premium feature benefits:\n❏ No need to open links\n❏ Get direct files\n❏ Ad-free experience\n❏ Unlimited movies & series\n❏ Full admin support\n❏ Requests fulfilled in 1h (if available)\n\n⛽ Check your active plan: /myplan</b>"""

    OTHER_TXT = """<b>Hey {},\n\n🎁 Other Plans\n⏰ Custom days according to your needs\n🏆 Want a different plan? Contact the owner via /plan</b>"""

    FREE_TXT = """<b>Hey {},\n\n🎖️ Available premium plans:\n015₹ – 1 week\n039₹ – 1 month\n... etc.\n\n⛽ Check active plan: /myplan\n🏷️ <a href='https://t.me/jisshu_Premium_proof'>Premium Proof</a>\n‼️ Send screenshot after payment.\n‼️ We'll add you shortly.</b>"""

    ADMIN_CMD_TXT = """<b><blockquote>
--- User Premium ---
➩ /add_premium {user ID} {Times} – Add premium user
➩ /remove_premium {user ID} – Remove premium user
➩ /add_redeem – Generate redeem code
➩ /premium_users – List premium users
➩ /refresh – Refresh free trial
--- Update Channel ---
➩ /set_muc {channel ID} – Set movies update channel
--- PM Search ---
➩ /pm_search_on – Enable PM search
➩ /pm_search_off – Disable PM search
--- Verify ID ---
➩ /verify_id – Generate verification ID
--- Set Ads ---
➩ /set_ads {ads name}#{Times}#{photo URL} – Explain
➩ /del_ads – Delete ads
--- Top Trending ---
➩ /setlist {list} – Explain
➩ /clearlist – Clear all lists
</blockquote></b>"""

    ADMIN_CMD_TXT2 = """<b><blockquote>
--- Index File ---
➩ /index – Index all files
--- Leave Link ---
➩ /leave {group ID} – Leave group
--- Send Message ---
➩ /send {username} – Reply to message to send
--- Ban User ---
➩ /ban {username} – Ban user
➩ /unban {username} – Unban user
--- Broadcast ---
➩ /broadcast – All users
➩ /grp_broadcast – Connected groups
</blockquote></b>"""

    GROUP_TEXT = """<b><blockquote>
--- Set Verify ---
/set_verify {link} {api}
/set_verify_2 {link} {api}
/set_verify_3 {link} {api}
--- Set Verify Time ---
/set_time_2 {seconds} – Set 2nd verification time
/set_time_3 {seconds} – Set 3rd verification time
--- On/Off Verification ---
/verifyoff {code} – Turn off (contact admin)
/verifyon – Turn on
--- Set File Caption ---
/set_caption – Set custom file caption
--- Set IMDb Template ---
/set_template – Set IMDb template
--- Set Tutorial ---
/set_tutorial – Set verification tutorial
--- Set Log Channel ---
/set_log {log channel ID}
Use /details to check settings.
Add me as admin to use features."""
  
    SOURCE_TXT = """<b>NOTE:\n- Source code: <a href="https://t.me/Master_xkid</a>\nDeveloper: MasterX</b>"""

    GROUP_C_TEXT = """<b><blockquote>
--- Set Verify ---
... same as above ...
</blockquote>\nIf you have any doubts, contact my admin.</b>"""
