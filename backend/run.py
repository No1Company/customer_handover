#!/usr/bin/env python3
#Kod för att köra igång systemet.

from bot_backend import app
from bot_backend.databasemgmt import resetDB
import sys
import os

if __name__ == "__main__":

    port = "5020"
    host = "localhost"
    args = sys.argv

    resetDB()

    print(args)

    if "--port" in args:
        port = args[args.index("--port")+1]

    if "--host" in args:
        host = args[args.index("--host")+1]    

    app.run(port=port, host=host, debug=True)