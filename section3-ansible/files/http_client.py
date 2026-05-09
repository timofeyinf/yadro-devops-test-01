import requests


def send_request(url):
    try:
        response = requests.get(url, timeout=5, allow_redirects=False)
        status = response.status_code
        body = response.text if response.text else "<empty>"

        if 100 <= status < 400:
            print(f"[INFO] Status: {status}")
            print(f"[INFO] Body: {body[:100]}")
        else:
            raise Exception(f"HTTP error: {status}, Body: {body[:100]}")

    except requests.exceptions.RequestException as e:
        print(f"[NETWORK ERROR] {e}")

    except Exception as e:
        print(f"[APPLICATION ERROR] {e}")


def main():
    status_codes = [101, 200, 301, 400, 500]
    base_url = "https://httpbin.org/status/"

    for code in status_codes:
        url = f"{base_url}{code}"
        print(f"\n[REQUEST] Sending request to {url}")
        send_request(url)


if __name__ == "__main__":
    main()
