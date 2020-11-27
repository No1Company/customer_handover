#!/usr/bin/env python3
#Kod för att köra igång systemet.

from bot_backend import app

if __name__ == "__main__":
    app.run(port="5020", debug = True)