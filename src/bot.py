import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
import os

from scraping.scraper_factory import ScraperFactory

load_dotenv()
api_token = os.getenv('API_TOKEN')

SUPERMARKETS = ["jumbo", "atomo", "carrefour", "changomas", "coto", "vea"]

# Configuración logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

user_states = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "¡Hola! Soy un bot de Mendoza para buscar precios de productos en los distintos supermercados.\n"
        "Primero, escribí el nombre del supermercado donde deseas buscar. Los supermercados disponibles son: Jumbo, Atomo, Vea, Carrefour, Changomas y Coto.\n"
    )

# Manejar mensajes de texto
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    user_input = update.message.text.strip().lower()

    if user_id not in user_states or "supermarket" not in user_states[user_id]:
        # El usuario está seleccionando el supermercado
        if user_input in SUPERMARKETS:
            user_states[user_id] = {"supermarket": user_input}
            await update.message.reply_text(
                f"Seleccionaste el supermercado '{user_input.title()}'. "
                "Ahora escribí el nombre del producto que quéres buscar."
            )
        else:
            await update.message.reply_text(
                "El supermercado ingresado no es válido. Los disponibles son:\n"
                f"{', '.join(SUPERMARKETS).title()}.\n"
                "Por favor, ingresá uno correcto."
            )
    else:
        supermarket = user_states[user_id]["supermarket"]
        product = update.message.text.strip()

        await update.message.reply_text(
            f"Buscando '{product}' en el {supermarket.title()}..."
        )

        try:
            scraper = ScraperFactory.get_scraper(supermarket)
            results = scraper.scrape(product)

            if results:
                # División de resultados en lotes para evitar error por mensajes largos
                batch_size = 5 
                for i in range(0, len(results), batch_size):
                    batch = results[i:i + batch_size]
                    message_text = f"*Resultados del {supermarket.title()} para '{product}':*\n\n"
                    for item in batch:
                        name = item.get("name", "Sin nombre")
                        price = item.get("price", "Sin precio")
                        product_url = item.get("product_url", "#")
                        message_text += f"- {name}: {price} ([Ver producto]({product_url}))\n"
                    await update.message.reply_text(message_text, parse_mode="Markdown")

            else:
                await update.message.reply_text(f"No se encontraron resultados para el producto '{product}' en {supermarket.title()}.")
        except Exception as e:
            logger.error(f"Error durante el scraping: {e}")
            await update.message.reply_text("Ocurrió un error al buscar el producto.")

        # Restablecer el estado del usuario para una nueva búsqueda
        user_states[user_id] = {}

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    logger.error(f"Update {update} causó un error {context.error}")

def main():
    # Crear bot
    app = ApplicationBuilder().token(api_token).build()

    # Handlers para comandos y mensajes
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Manejo de errores
    app.add_error_handler(error_handler)

    # Iniciar el bot
    logger.info("Bot iniciado...")
    app.run_polling()

if __name__ == "__main__":
    main()
