from tqdm import tqdm
from time import sleep
import dns.resolver
import pyfiglet
from termcolor2 import colored
def myDNS(domainName, myType='A'):
    try:
        result = dns.resolver.resolve(domainName, myType)
        print(f"DNS {myType} records for {domainName}:")
        for res in result:
            print(res.to_text())
    except dns.resolver.NoAnswer:
        print(f"No {myType} record found for {domainName}.")
    except dns.resolver.NXDOMAIN:
        print(f"The domain {domainName} doesn't exist.")
    except Exception as e:
        print(f"You have an error: {e}")
def print_art(color, message):
    ascii_art = pyfiglet.figlet_format(message)
    ascii_art = colored(ascii_art, color=color)
    print(ascii_art)
print_art('magenta', 'DNS viewer')
domain_name=input("Please enter your domain: ")
while True:
    if domain_name=='exit':
        print_art('red', 'See you later!')
        break
    else:
        for i in tqdm(range(100)):
                sleep(0.02)
        if __name__ == "__main__":
            domainName = domain_name
            myDNS(domainName, 'A') 
            myDNS(domainName, 'MX')
            myDNS(domainName, 'NS')
        domain_name=input("Please enter your domain: ")