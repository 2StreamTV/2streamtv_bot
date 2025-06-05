from telegram import Update, BotCommand
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters
)
import logging

# Set up logging to show status and errors in the console
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

BOT_TOKEN = '7823277651:AAHYu09x6Q_poBRVURNDFthj51FLTkynaIw'  # Replace with your actual token

# --- Command Handlers ---

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Welcome to 2StreamTV Support Bot! Type /help to see available commands.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📋 Available Commands:\n"
        "/account – Account issues\n"
        "/maintenance – Weekly maintenance steps\n"
        "/buffering – Fix buffering problems\n"
        "/youtube – Video tutorials\n"
        "/router – Router setup/help\n"
        "/vpn – VPN info\n"
        "/firestick – Firestick support\n"
        "/install – Installation guides"
    )

async def account(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📨 **Account Support**\n"
        "Forgot login or account questions?\n"
        "• Email: 2streamtv.adm@gmail.com\n"
        "• Use your original signup email\n"
        "• Support: Mon–Fri, 9am–5pm EST\n"
        "• Closed weekends/holidays"
    )

async def maintenance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛠️ **Weekly Maintenance Steps**\n"
        "1. On your device (stick or box), go to Settings > Apps. Select your app, then tap Force Stop and Clear Cache (do not select Clear Data).\n"
        "2. Power off your device.\n"
        "3. Unplug router/modem for 1–5 min.\n"
        "4. Plug in modem/router and power on device.\n"
        "5. Open 2StreamTV app."
    )

async def buffering(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "⚠️ **Buffering Fixes**\n"
        "1. Run speed test in 2StreamTV app\n"
        "   • 2StreamTV Smarters Tutorial: https://youtu.be/RyJDKqM8BOI\n"
        "   • 2StreamTV XCIPTV Tutorial: https://youtu.be/r_CpRrHYDJw\n"
        "2. If ping > 40ms, this may be contributing to the buffering issue. To reduce high ping, do the following:\n"
        "   • Switch to the 5.0 GHz band on your router for faster speeds and less interference.\n"
        "   • Ensure your streaming device is within a reasonable distance from the router.\n"
        "   • Reduce network congestion by disconnecting other devices and pausing downloads/uploads.\n"
        "   • If possible, connect your streaming device directly to the router via Ethernet.\n"
        "3. Additional Tips:\n"
        "   • Close unnecessary apps or browser tabs that may consume bandwidth.\n"
        "   • Restart your modem and router.\n"
        "   • Contact your ISP if issues persist.\n"
        "   • Additional tips: https://youtu.be/sFtgyJdyFjE"
    )

async def youtube(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "▶️ **YouTube Tutorials**\n"
        "• Move apps to front: https://youtu.be/pXGhLwixFgU?si=UJtQ3gf7oXRGk3FS\n"
        "• Background Apps & Process List + Force Stop/Clear Cache: https://youtu.be/nG92Ra3Jxqw?si=j6SDd3_TFX-8DL9w\n"
        "• Delete files off Downloader App: https://youtu.be/ZTodK4-YWSI?si=GYQ5X341LMkWeq1s\n\n"
        "(Other commands continue unchanged...)"
    )

async def router(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📡 **Router & ISP Solutions**\n"
        "(unchanged...)"
    )

async def vpn(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛡️ **VPN Setup**\n"
        "(unchanged...)"
    )

async def firestick(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 **Firestick Help**\n"
        "(unchanged...)"
    )

async def install(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📦 **Installation Help**\n"
        "(unchanged...)"
    )

async def welcome_new_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for member in update.message.new_chat_members:
        user_mention = f"[{member.full_name}](tg://user?id={member.id})"
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=(
                f"👋 Welcome {user_mention} to 2 StreamTV Customers Group!\n"
                "I am the 2StreamTV Support Bot here to assist with basic help.\n"
                "Type /help to see available commands."
            ),
            parse_mode='Markdown'
        )

async def keyword_responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if any(word in text for word in ["login issue", "can't login", "account help", "forgot password"]):
        await update.message.reply_text("🔐 For login/account issues, email 2streamtv.adm@gmail.com using the email tied to your account.")
    elif any(word in text for word in ["buffering", "lag", "slow"]):
        await update.message.reply_text("⚠️ Having buffering issues? Run a speed test and check /buffering for tips.")
    elif any(word in text for word in ["how to pay", "payment", "invoice"]):
        await update.message.reply_text("💳 You can pay your invoice using the link sent by email. Make sure your email is correct before submitting.")
    elif any(word in text for word in ["vpn", "connect", "blocked"]):
        await update.message.reply_text("🛡️ Using a VPN? Force stop and clear cache of the VPN and streaming apps. Log in again. Type /vpn for more help.")

async def set_bot_commands(app):
    commands = [
        BotCommand("start", "Welcome message"),
        BotCommand("help", "List available commands"),
        BotCommand("account", "Account recovery/help"),
        BotCommand("maintenance", "Weekly maintenance steps"),
        BotCommand("buffering", "Fix buffering issues"),
        BotCommand("youtube", "Video tutorials"),
        BotCommand("router", "Router/ISP fixes"),
        BotCommand("vpn", "VPN setup info"),
        BotCommand("firestick", "Firestick instructions"),
        BotCommand("install", "Installation guides"),
    ]
    await app.bot.set_my_commands(commands)

def main():
    logging.info("Starting the bot...")
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("account", account))
    app.add_handler(CommandHandler("maintenance", maintenance))
    app.add_handler(CommandHandler("buffering", buffering))
    app.add_handler(CommandHandler("youtube", youtube))
    app.add_handler(CommandHandler("router", router))
    app.add_handler(CommandHandler("vpn", vpn))
    app.add_handler(CommandHandler("firestick", firestick))
    app.add_handler(CommandHandler("install", install))
    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome_new_member))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), keyword_responder))

    app.post_init = set_bot_commands

    logging.info("✅ 2StreamTV Bot is running... (Press CTRL+C to stop)")
    app.run_polling()

if __name__ == "__main__":
    main()
