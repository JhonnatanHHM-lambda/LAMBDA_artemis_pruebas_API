from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from datetime import datetime
import platform

app = FastAPI(
    title="Artemis API",
    description="Servicio API para Artemis",
    version="1.0.0"
)


@app.get("/", response_class=HTMLResponse)
def home():
    return f"""
    <html>
        <head>
            <title>Artemis API</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #0f172a;
                    color: white;
                    text-align: center;
                    padding: 40px;
                }}
                .container {{
                    max-width: 700px;
                    margin: auto;
                    background: #1e293b;
                    padding: 30px;
                    border-radius: 10px;
                }}
                h1 {{
                    color: #38bdf8;
                }}
                .status {{
                    background: #16a34a;
                    padding: 10px;
                    border-radius: 6px;
                    display: inline-block;
                    margin-top: 10px;
                }}
                a {{
                    color: #38bdf8;
                    text-decoration: none;
                    font-weight: bold;
                }}
                .footer {{
                    margin-top: 30px;
                    font-size: 12px;
                    color: #94a3b8;
                }}
            </style>
        </head>

        <body>

            <div class="container">

                <h1>🚀 Artemis API</h1>

                <p>La API está funcionando correctamente.</p>

                <div class="status">
                    ❤️ Status: Online
                </div>

                <p style="margin-top:20px;">
                    📚 Documentación interactiva:
                    <br><br>
                    <a href="/docs">Swagger UI</a>
                    |
                    <a href="/redoc">ReDoc</a>
                </p>

                <hr style="margin:30px;">

                <p>
                    🖥 Servidor: {platform.system()}
                </p>

                <p>
                    ⏱ Hora del servidor: {datetime.utcnow()}
                </p>

                <div class="footer">
                    Artemis API v1.0.0
                </div>

            </div>

        </body>
    </html>
    """


@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "artemis-api",
        "version": "1.0.0"
    }


@app.get("/info")
def info():
    return {
        "service": "Artemis API",
        "version": "1.0.0",
        "environment": "production",
        "server_time": datetime.utcnow()
    }
