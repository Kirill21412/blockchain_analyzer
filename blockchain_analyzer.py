import requests

def get_block_data(block_number):
    url = f"https://api.blockchair.com/bitcoin/blocks/{block_number}"
    response = requests.get(url)
    data = response.json()
    return data

if __name__ == "__main__":
    block_number = input("Enter block number: ")
    block_data = get_block_data(block_number)
    print(block_data)
