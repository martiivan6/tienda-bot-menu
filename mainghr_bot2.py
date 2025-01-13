import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackContext, CallbackQueryHandler, MessageHandler, filters
from aiohttp import web

# Obtén los tokens y la URL base de las variables de entorno
BOT2_TOKEN = os.getenv("BOT2_TOKEN")
WEBHOOK_URL_BASE = os.getenv("WEBHOOK_URL_BASE", "https://placeholder.onrender.com")

# Configura el segundo bot
def setup_bot2():
    async def start(update: Update, context: CallbackContext) -> None:
        keyboard = [
            [InlineKeyboardButton("HACER PEDIDO", url='https://t.me/alh_1997')],
            [InlineKeyboardButton("VER ESTADO DEL PEDIDO", callback_data='ver_estado_del_pedido')],
            [InlineKeyboardButton("VER CATALOGO", callback_data='ver_catalogo')],
            [InlineKeyboardButton("GUIA DE TALLAS", callback_data='guia_de_tallas')],
            [InlineKeyboardButton("PRECIOS", callback_data='precios')],
            [InlineKeyboardButton("PROMOS", callback_data='promos')],
            [InlineKeyboardButton("REDES SOCIALES", callback_data='redes_sociales')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Hola, aquí tienes el menú de la tienda Uniquejerseyghr. Elige lo que necesites:",
            reply_markup=reply_markup
        )

    async def handle_callback(update: Update, context: CallbackContext) -> None:
        query = update.callback_query
        await query.answer()

        # Menú de retorno al menú principal
        back_to_main_menu_keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("⬅️ Volver al menú principal", callback_data='main_menu')]
        ])

        if query.data == 'ver_estado_del_pedido':
            await query.edit_message_text(
                "Aquí puedes ver el estado de tu pedido: http://123.207.20.21:8082/en/trackIndex.htm",
                reply_markup=back_to_main_menu_keyboard
            )
        elif query.data == 'ver_catalogo':
            keyboard = [
                [InlineKeyboardButton("CAMISETAS DE FÚTBOL", callback_data='catalogo_futbol')],
                [InlineKeyboardButton("CAMISETAS NBA", callback_data='catalogo_nba')],
                [InlineKeyboardButton("CAMISETAS NFL", callback_data='catalogo_nfl')],
                [InlineKeyboardButton("CAMISETAS F1", callback_data='catalogo_f1')],
                [InlineKeyboardButton("CHÁNDALS", callback_data='catalogo_chandals')],
                [InlineKeyboardButton("⬅️ Volver al menú principal", callback_data='main_menu')]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            await query.edit_message_text(
                text="Elige una categoría del catálogo:",
                reply_markup=reply_markup
            )
        elif query.data == 'catalogo_futbol':
            keyboard = [
                [InlineKeyboardButton("⬅️ Volver al catálogo", callback_data='ver_catalogo')]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            await query.edit_message_text(
                "Has seleccionado CAMISETAS DE FÚTBOL: https://drive.google.com/drive/folders/1lxyq6EjtylR8RlLGzB25OBBWEWt2wn6P.",
                reply_markup=reply_markup
            )
        elif query.data == 'catalogo_nba':
            keyboard = [
                [InlineKeyboardButton("⬅️ Volver al catálogo", callback_data='ver_catalogo')]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            await query.edit_message_text(
                "Has seleccionado CAMISETAS NBA: https://drive.google.com/drive/folders/1mpKAE3QWi5DDCd2J8Qb3I0_XcYZvqZLE.",
                reply_markup=reply_markup
            )
        elif query.data == 'catalogo_nfl':
            keyboard = [
                [InlineKeyboardButton("⬅️ Volver al catálogo", callback_data='ver_catalogo')]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            await query.edit_message_text(
                "Has seleccionado CAMISETAS NFL: https://drive.google.com/drive/folders/1ha9theGvBhUPs9RwziaXHhBo9kQUZq6u.",
                reply_markup=reply_markup
            )
        elif query.data == 'catalogo_f1':
            keyboard = [
                [InlineKeyboardButton("⬅️ Volver al catálogo", callback_data='ver_catalogo')]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            await query.edit_message_text(
                "Has seleccionado CAMISETAS F1: https://drive.google.com/drive/folders/1_ExfzaOTepN4jc73cotQDRfOh4OzMMgg.",
                reply_markup=reply_markup
            )
        elif query.data == 'catalogo_chandals':
            keyboard = [
                [InlineKeyboardButton("⬅️ Volver al catálogo", callback_data='ver_catalogo')]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            await query.edit_message_text(
                "Has seleccionado CHÁNDALS: https://drive.google.com/drive/folders/1emxdyQOqin7li4TENe4qhgZWx9laM2t1.",
                reply_markup=reply_markup
            )
        elif query.data == 'precios':
            precios = """
🛒 Lista de Precios:

⚽ Camisetas de Fútbol Actuales: 24,99€
👕 Camisetas Retro: 27,99€
🏀 Camisetas NBA: 29,99€
🏈 Camisetas NFL: 34,99€
🏎️ Camisetas F1: 30€
🎽 Chándales: 55€

➕ Personalización:
🔢 Dorsal: +2€
🩹 Parches: +1€
"""
            await query.edit_message_text(
                precios,
                reply_markup=back_to_main_menu_keyboard
            )
        elif query.data == 'guia_de_tallas':
            await query.edit_message_text(
                "Aquí tienes la GUÍA DE TALLAS: https://drive.google.com/uc?export=view&id=1x6aW1N4WMCKc7hrFvdqFv3DqrRLk-7IJ.",
                reply_markup=back_to_main_menu_keyboard
            )
        elif query.data == 'promos':
            await query.edit_message_text(
                "🎉 PROMOS:\n- Compra 4 y lleva 1 GRATIS.\n- 15% de descuento en invierno.",
                reply_markup=back_to_main_menu_keyboard
            )
        elif query.data == 'redes_sociales':
            keyboard = [
                [InlineKeyboardButton("INSTAGRAM", url="https://www.instagram.com/uniquejerseysghr/")],
                [InlineKeyboardButton("TIKTOK", url="https://www.tiktok.com/@uniquejerseysghr")],
                [InlineKeyboardButton("⬅️ Volver al menú principal", callback_data='main_menu')]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            await query.edit_message_text(
                text="Nuestras redes sociales:",
                reply_markup=reply_markup
            )
        elif query.data == 'main_menu':
            await start(update, context)

    async def handle_message(update: Update, context: CallbackContext) -> None:
        if update.message.chat.type == "private":
            await start(update, context)

    application = Application.builder().token(BOT2_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(handle_callback))
    application.add_handler(MessageHandler(filters.ChatType.PRIVATE & filters.TEXT, handle_message))

    return application

# Inicializa el bot
bot2 = setup_bot2()

# Configura el webhook para el bot 2
async def set_webhook(application, path):
    url = f"{WEBHOOK_URL_BASE}{path}"
    await application.bot.set_webhook(url=url)

async def setup_webhooks():
    await set_webhook(bot2, "/bot2")

# Crea la aplicación web para manejar los webhooks
app = web.Application()
app.add_routes([
    web.post("/bot2", bot2.update_queue.put),  # Cambiado a update_queue.put
])

# Inicia el servidor web
if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(setup_webhooks())
    web.run_app(app, host="0.0.0.0", port=int(os.getenv("PORT", 8443)))
