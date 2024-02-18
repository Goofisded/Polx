
import os
import requests
import threading

def print_banner():
    banner = """
    [38;2;255;165;0m  
██████╗  ██████╗ ██╗     ██╗  ██╗
██╔══██╗██╔═══██╗██║     ╚██╗██╔╝
██████╔╝██║   ██║██║      ╚███╔╝ 
██╔═══╝ ██║   ██║██║      ██╔██╗ 
██║     ╚██████╔╝███████╗██╔╝ ██╗
╚═╝      ╚═════╝ ╚══════╝╚═╝  ╚═╝
                                 
       
    """
    made_by = "[38;2;255;165;0m                      Made by Goof"
    print(f"{banner.center(120)}\n{made_by.center(120)}\n")
    input("[38;2;255;165;0mPress Enter to start...")
    os.system('cls' if os.name == 'nt' else 'clear')  

def check_subdomains(url, subdomains_file):
    try:
        with open(subdomains_file, 'r') as file:
            subdomains = file.read().splitlines()

        found_links = []

        def check_subdomain(subdomain):
            full_url = f"http://{subdomain}.{url}"
            try:
                response = requests.get(full_url)
                if response.status_code == 200:
                    found_links.append(full_url)
                    print(full_url, "[Found]")
            except requests.ConnectionError:
                pass 

        for subdomain in subdomains:
            thread = threading.Thread(target=check_subdomain, args=(subdomain,))
            thread.start()

        for thread in threading.enumerate():
            if thread is threading.main_thread():
                continue
            thread.join()

        with open(f"{url}_Subdomains.txt", 'w') as output_file:
            for found_link in found_links:
                output_file.write(f"{found_link}\n")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print_banner()
    url = input("Enter the base URL (usage example.com): ")
    subdomains_file = "subdomains.txt"
    check_subdomains(url, subdomains_file)
