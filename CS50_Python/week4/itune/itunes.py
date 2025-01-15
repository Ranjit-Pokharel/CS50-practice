import requests
import sys

def main()-> None:
    if len(sys.argv) != 2:
        sys.exit("usage: itune.py <song name>.")
    
    limit:int = 10

    url:str = f"https://itunes.apple.com/search?entity=song&limit={limit}&term={sys.argv[1]}"

    response:requests.Response = requests.get(url=url)
    datas = response.json()

    for data in datas["results"]:
        print(data["trackName"])


if __name__ == "__main__":
    main()

