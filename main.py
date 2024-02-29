import requests
import random

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# from urllib import request

# Function to read user agents from file and get a random user agent
def get_random_user_agent():
    with open('user-agents.txt', 'r') as file:
        user_agents = file.read().splitlines()

    return random.choice(user_agents)

# Function to read proxy list from file and get a random proxy
def get_random_proxy():
    with open('proxy.txt', 'r') as file:
        proxies = file.read().splitlines()

    return random.choice(proxies)

# Function to make a request with a random user agent and proxy
def make_request(url, iteration):
    user_agent = get_random_user_agent()
    proxy = get_random_proxy()

    headers = {
        'User-Agent': user_agent
    }
    
    try:
        response = requests.get(
            url, 
            headers=headers, 
            proxies={'http': proxy, 'https': proxy}, 
            timeout=10
        )
        # Process the response here
        print(f"+=============================================================")
        print(f"+ Iteration {iteration} working with PROXY: {proxy}")
        print(f"+ User Agent: {user_agent}")
        print(f"+ Request successful. Status code: {response.status_code}")
        print(f"+=============================================================\n")
        
        # Open Chrome and visit the website every 10 iterations
        if iteration % 2 == 0:
            open_browser(url, user_agent, proxy)
    except Exception as e:
        print(f"Iteration {iteration} failed with PROXY: {proxy}")
        print(f"Error making request: {e}\n")

# Function to open Firefox and visit a website
def open_browser(url, user_agents, proxy):
    options = Options()
    options.add_argument(f"--user-agent={user_agents}")
    options.add_argument(f'--proxy-server={proxy}')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get(url)

    # Scrill Down
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Scroll up
    driver.execute_script("window.scrollTo(0, 0);")
    
    sleep(10)
    driver.close()

# Take user input for the URL to crawl
# url_to_crawl = input("Enter the URL to crawl: ")
url_to_crawl = "https://tabibdigital.com/"

# Take user input for the number of requests to make
# num_requests = int(input("Enter the number of requests to make: "))
num_requests = 100

# Make multiple requests
for iteration in range(1, num_requests + 1):
    make_request(url_to_crawl, iteration)
