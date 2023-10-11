import uvicorn
import os
import argparse
import uvicorn.config
from dotenv import load_dotenv
from coloredlogs import ColoredFormatter
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

load_dotenv()


def main():
    parser = argparse.ArgumentParser(description="Run the UVicorn server.")
    parser.add_argument('--host', type=str, default='0.0.0.0', help='Host IP address to bind to.')
    parser.add_argument('--port', type=int, default=os.getenv("PORT"), help='Port number to listen on.')
    parser.add_argument('--reload', action='store_true', help='Enable auto-reload.')
    parser.add_argument('--access-log', action='store_false', help='Enable access log.')
    parser.add_argument('--log-level', type=str, default='debug', help='Log level for UVicorn.')
    parser.add_argument('--log-config', type=str, default='./log_config.yaml',
                        help='Path to log configuration file.')
    parser.add_argument('--use-colors', action='store_false', help='Enable log colors.')
    args = parser.parse_args()
    path = "./logs"
    is_exist = os.path.exists(path)
    if not is_exist:
        os.makedirs(path)

    uvicorn.run(
        'main:app',
        host=args.host,
        port=args.port,
        reload=args.reload,
        access_log=args.access_log,
        log_level=args.log_level,
        log_config=args.log_config,
        use_colors=args.use_colors,
    )


if __name__ == '__main__':
    main()
