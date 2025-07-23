import os
import socket
import subprocess
import platform

# File Management
def dir(directory="."):
    """Lists files and directories in the current directory."""
    return os.popen(f"dir {directory}").read()

def cd(directory):
    """Changes the current working directory."""
    try:
        os.chdir(directory)
        return f"Changed directory to {os.getcwd()}"
    except Exception as e:
        return str(e)

def pwd():
    """Prints the full path of the current working directory."""
    return os.getcwd()

def mkdir(directory):
    """Creates a new directory."""
    return os.popen(f"mkdir {directory}").read()

def del_file(path):
    """Removes files or directories."""
    return os.popen(f"del {path}").read()

def copy(source, destination):
    """Copies files or directories."""
    return os.popen(f"copy {source} {destination}").read()

def move(source, destination):
    """Moves or renames files or directories."""
    return os.popen(f"move {source} {destination}").read()

def type(filename):
    """Displays the contents of a file."""
    return os.popen(f"type {filename}").read()

# System Monitoring
def tasklist():
    """Lists the currently running processes."""
    return os.popen("tasklist").read()

def systeminfo():
    """Displays detailed system information."""
    return os.popen("systeminfo").read()

def df():
    """Displays the disk space usage."""
    return os.popen("wmic logicaldisk get size,freespace,caption").read()

# Networking
def ping(host):
    """Tests the connectivity to a network host."""
    return os.popen(f"ping {host}").read()

def curl(url):
    """Transfers data with URLs."""
    return os.popen(f"curl {url}").read()

def netstat():
    """Displays network statistics."""
    return os.popen("netstat -an").read()

# Other useful commands
def cls():
    """Clears the screen."""
    return os.system("cls")

def exit():
    """Exits the shell."""
    return "Exiting shell..."

def help(command=None):
    """Provides information on a command."""
    if command:
        return os.popen(f"help {command}").read()
    return "Type 'help <command>' for specific command help"

# Windows specific commands
def sfc():
    """System File Checker - Scans and repairs system files."""
    return os.popen("sfc /scannow").read()

def chkdsk(drive="C:"):
    """Check Disk - Scans and fixes disk errors."""
    return os.popen(f"chkdsk {drive}").read()

# Alias mappings for cross-platform compatibility
aliases = {
    'ls': dir,
    'rm': del_file,
    'cp': copy,
    'mv': move,
    'cat': type,
    'ps': tasklist,
    'clear': cls,
    'pwd': lambda: os.getcwd(),
    'touch': lambda f: os.popen(f"type nul > {f}").read(),
    'grep': lambda p, f: os.popen(f'findstr "{p}" {f}').read()
}