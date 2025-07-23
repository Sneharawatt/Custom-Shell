import os
import socket
import subprocess

# File Management
def ls(directory="."):
    """Lists files and directories in the current directory."""
    return os.popen(f"ls -l {directory}").read()

def cd(directory):
    """Changes the current working directory."""
    os.chdir(directory)
    return f"Changed directory to {os.getcwd()}"

def pwd():
    """Prints the full path of the current working directory."""
    return os.getcwd()

def mkdir(directory):
    """Creates a new directory."""
    return os.popen(f"mkdir {directory}").read()

def rm(path):
    """Removes files or directories."""
    return os.popen(f"rm -r {path}").read()

def cp(source, destination):
    """Copies files or directories."""
    return os.popen(f"cp -r {source} {destination}").read()

def mv(source, destination):
    """Moves or renames files or directories."""
    return os.popen(f"mv {source} {destination}").read()

def touch(filename):
    """Creates an empty file or updates the timestamp of an existing file."""
    return os.popen(f"touch {filename}").read()

# Text Processing
def cat(filename):
    """Concatenates and prints the contents of a file."""
    return os.popen(f"cat {filename}").read()

def grep(pattern, filename):
    """Searches for a pattern in a file."""
    return os.popen(f"grep '{pattern}' {filename}").read()

def sort(filename):
    """Sorts the lines of a text file."""
    return os.popen(f"sort {filename}").read()

def head(filename, n=10):
    """Displays the first few lines of a file."""
    return os.popen(f"head -n {n} {filename}").read()

def tail(filename, n=10):
    """Displays the last few lines of a file."""
    return os.popen(f"tail -n {n} {filename}").read()

# System Monitoring
def top():
    """Displays a dynamic view of the system's processes."""
    return os.popen("top -l 1").read()

def ps():
    """Lists the currently running processes."""
    return os.popen("ps aux").read()

def df():
    """Displays the disk space usage."""
    return os.popen("df -h").read()

# Permissions and Ownership
def chmod(path, permissions):
    """Changes the permissions of a file or directory."""
    return os.popen(f"chmod {permissions} {path}").read()

def chown(path, user, group=None):
    """Changes the owner of a file or directory."""
    cmd = f"chown {user}" 
    if group:
        cmd += f":{group}"
    cmd += f" {path}"
    return os.popen(cmd).read()

def chgrp(path, group):
    """Changes the group ownership of a file or directory."""
    return os.popen(f"chgrp {group} {path}").read()

# Networking
def ping(host):
    """Tests the connectivity to a network host."""
    return os.popen(f"ping -c 4 {host}").read()

def wget(url):
    """Downloads files from the web."""
    return os.popen(f"wget {url}").read()

def curl(url):
    """Transfers data with URLs."""
    return os.popen(f"curl {url}").read()

def ssh(user_host):
    """Securely connects to a remote server."""
    return os.popen(f"ssh {user_host}").read()

def scp(source, destination):
    """Securely copies files between servers."""
    return os.popen(f"scp {source} {destination}").read()

def ftp(host):
    """Uses the File Transfer Protocol."""
    return os.popen(f"ftp {host}").read()

# Other useful commands
def history():
    """Displays the command history."""
    return os.popen("history").read()

def sudo(command):
    """Executes a command with administrative privileges."""
    return os.popen(f"sudo {command}").read()

def man(command):
    """Displays the manual page for a command."""
    return os.popen(f"man {command}").read()

def help(command=None):
    """Provides information on a command."""
    if command:
        return os.popen(f"{command} --help").read()
    return "Type 'help <command>' for specific command help"

def exit():
    """Exits the shell."""
    return "Exiting shell..."

# macOS specific commands
def open_app(app_name):
    """Opens an application."""
    return os.popen(f"open -a '{app_name}'").read()

def brew(command, package=None):
    """Homebrew package manager commands."""
    if package:
        return os.popen(f"brew {command} {package}").read()
    return os.popen(f"brew {command}").read()

# Alias mappings for cross-platform compatibility
aliases = {
    'dir': ls,
    'ren': mv,
    'del': rm,
    'cls': lambda: os.system("clear"),
    'type': cat,
    'copy': cp,
    'move': mv,
    'md': mkdir,
    'rd': rm
}