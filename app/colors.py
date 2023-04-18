from termcolor import colored

def success():
    return colored("[+] ", 'green')

def info():
    return colored("[i] ", 'blue')

def warning():
    return colored("[!] ", 'yellow')

def error():
    return colored("[x]", 'red')