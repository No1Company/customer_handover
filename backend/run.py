#!/usr/bin/env python3
#Kod för att köra igång systemet.

from bot_backend import app
import sys
import os

if __name__ == "__main__":

    port = "5020"
    host = "localhost"
    args = sys.argv

    print(args)
    
    if "--port" in args:
        port = args[args.index("--port")+1]

    if "--host" in args:
        host = args[args.index("--host")+1]    
    
    # Let gitlab provide password as token
    if "--ehrpassword" in args:
        password = args[args.index("--ehrpassword")+1]
        print('ehr length', password)

        with open(os.path.join("..","..",'login.txt'), 'w') as f:
            f.write("Basic " + password)
            print("login key saved")
            f.close()

    app.run(port=port, host=host, debug=True)