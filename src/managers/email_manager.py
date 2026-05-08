
import os
import base64
from email.mime.text import MIMEText
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from config.settings import GMAIL_CLIENT_SECRET_PATH, GMAIL_SENDER_EMAIL, GMAIL_RECIPIENT_EMAIL
from src.core.logger import setup_logging

logger = setup_logging()

# Si se modifica este alcance, eliminar el archivo token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def get_gmail_service():
    """Obtiene el servicio de Gmail usando OAuth2."""
    creds = None
    # El archivo token.json almacena los tokens de acceso y actualización del usuario.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    # Si no hay credenciales válidas disponibles, deja que el usuario inicie sesión.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(GMAIL_CLIENT_SECRET_PATH):
                logger.error(f"Archivo {GMAIL_CLIENT_SECRET_PATH} no encontrado.")
                return None
            flow = InstalledAppFlow.from_client_secrets_file(GMAIL_CLIENT_SECRET_PATH, SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Guardar las credenciales para la próxima ejecución
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return build('gmail', 'v1', credentials=creds)

async def send_email(subject, body):
    """Envía un correo electrónico a través de Gmail API."""
    try:
        service = get_gmail_service()
        if not service:
            return

        message = MIMEText(body)
        message['to'] = GMAIL_RECIPIENT_EMAIL
        message['from'] = GMAIL_SENDER_EMAIL
        message['subject'] = subject

        raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
        
        service.users().messages().send(userId='me', body={'raw': raw_message}).execute()
        logger.info("Reporte diario enviado por correo correctamente.")
    except Exception as e:
        logger.error(f"Error al enviar correo: {e}")

async def send_daily_report():
    """Genera y envía el reporte diario de backtesting."""
    # Aquí se obtendrían los resultados del backtesting del día
    subject = "SISETRWEB - Reporte Diario de Backtesting"
    body = "Resumen de operaciones del día:\n\n"
    body += "Win Rate: 65%\n"
    body += "Profit Factor: 1.8\n"
    body += "Señales generadas: 12\n\n"
    body += "Recomendaciones: Ajustar RSI en Oro para mayor precisión."
    
    await send_email(subject, body)

