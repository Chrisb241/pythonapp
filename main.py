import requests

def main():
    response = requests.get("https://api.github.com")
    print("Status code:", response.status_code)
    print("Headers:", response.headers["content-type"])

if __name__ == "__main__":
    main()