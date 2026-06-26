import datetime
import getpass
import socket
import os
import colors
import requests

# Variable Init

command = ""
ctime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
user = getpass.getuser()
hostname = socket.gethostname()
cwd = os.getcwd()
version = "1.0"
response = ""

# Welcome User
def stats():
    ctime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    colors.green_print("Stats:")
    colors.bright_yellow_print(f"Time: {ctime}")
    colors.bright_cyan_print(f"Username: {user}")
    colors.red_print(f"Hostname: {hostname}")
    colors.blue_print(f"Working Directory: {cwd}")

def clear_screen():
    # 'nt' means Windows, 'posix' covers macOS and Linux
    os.system('cls' if os.name == 'nt' else 'clear')

def ls():
    os.system('dir' if os.name == 'nt' else 'ls')

import sys

def set_global_print_color(color_name: str):
    """
    Sets the terminal text color for all subsequent print statements.
    Accepts: 'red', 'green', 'blue', 'yellow', 'magenta', 'cyan', 'white', 'reset'
    """
    # Dictionary mapping color names to ANSI escape sequences
    ansi_colors = {
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m",
        "reset": "\033[0m"
    }
    
    # Normalize input to lowercase
    color_key = color_name.lower().strip()
    
    # Get the code or default to reset if color is not found
    code = ansi_colors.get(color_key, "\033[0m")
    
    # Write directly to stdout to change the terminal state immediately
    sys.stdout.write(code)
    sys.stdout.flush()

# Start Setup
clear_screen()
set_global_print_color("green")
stats()
set_global_print_color("green")

# Command Loop
while True:
    cmdinput = input(f"{user}@{hostname}:{cwd}$ ")
    parts = cmdinput.split(maxsplit=1)
    command = parts[0]
    argument = parts[1] if len(parts) > 1 else ""

    if command == "stats":
       stats()
    elif command == "help":
         colors.red_print("Work In Progress Feature...!")
    elif command == "echo":
         print(argument)
    elif command == "exit":
         exit()
    elif command == "whoami":
         colors.green_print(user)
    elif command == "pwd":
         colors.green_print(cwd)
    elif command == "version":
        colors.yellow_print(f"Version: {version}")
    elif command == "clear":
        clear_screen()
    elif command == "ls":
         ls()
    elif command == f"cat":
         filename = f"{argument}"
         try: 
            with open(f"{filename}", "r") as file:
                 content = file.read()
                 print(content)
         except FileNotFoundError:
                colors.red_print(f"File {filename} Not Found!")
    elif command == "date":
           date = datetime.datetime.now().strftime("%Y-%m-%d")
           print(date)
    elif command == "color":
         set_global_print_color(argument)
    elif command == "touch":
         if argument == "":
              colors.yellow_print("Invalid usage")
         else:
              with open(f"{argument}", "w") as file:
                   file.write("")
    elif command == "reload":
         clear_screen()
         stats()
         set_global_print_color("green")    
    elif command == "rm":
         
         if argument == "":
              colors.yellow_print("Invalid Usage")
         else:
              os.remove(argument)
    elif command == "write":
         if argument == "":
              colors.yellow_print("Invalid Usage")
         else:
              writef = input("Where To Write This Text To?: ") 
              if os.path.exists(argument):
                 with open(writef, "w") as file:
                      file.write(argument)
              else:
                   with open(writef, "w") as file:
                        file.write(argument)
    elif command == "download":
          if argument == "":
               print("Invalid Usage")
          else:
              fname = input("File Name To Save as: ")
              headers = {
                        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
              }         
              with requests.get(argument, stream=True, headers=headers) as response:
                       response.raise_for_status() # Check for HTTP errors
                       total_size = int(response.headers.get("content-length", 0))
                       downloaded = 0

                       with open(fname, "wb") as file:
                            # Write chunks of 8KB at a time
                            for chunk in response.iter_content(chunk_size=8192):
                                file.write(chunk)
                                downloaded += len(chunk)
                                percent = downloaded * 100 / total_size
                                bar_length = 30
                                filled = int(bar_length * downloaded / total_size)
                                bar = "█" * filled + " " * (bar_length - filled)
                                print(f"\r[{bar}] {percent:.1f}%", end="", flush=True)
                            colors.green_print(f"Downloaded {fname}")
    elif command == "os":
         colors.yellow_print(os.name)
    else:
         colors.red_print("Command Not Found!")