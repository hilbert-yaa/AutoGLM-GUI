"""CLI entry point for AutoGLM-GUI."""

import argparse


def main() -> None:
    """Start the AutoGLM-GUI server."""
    parser = argparse.ArgumentParser(
        description="AutoGLM-GUI - Web GUI for AutoGLM Phone Agent"
    )
    parser.add_argument(
        "--host",
        default="0.0.0.0",
        help="Host to bind the server to (default: 0.0.0.0)",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="Port to bind the server to (default: 8000)",
    )
    parser.add_argument(
        "--reload",
        action="store_true",
        help="Enable auto-reload for development",
    )

    args = parser.parse_args()

    import uvicorn

    from AutoGL_GUI.server import app

    print(f"Starting AutoGLM-GUI server at http://{args.host}:{args.port}")
    print("Press Ctrl+C to stop")

    uvicorn.run(
        app if not args.reload else "AutoGL_GUI.server:app",
        host=args.host,
        port=args.port,
        reload=args.reload,
    )


if __name__ == "__main__":
    main()
