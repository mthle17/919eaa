from matplotlib import pyplot as plt
import requests
import random

while(answer := input("Load comic? [y|n]: ") == "y"):
    url = f"https://xkcd.com/{random.randint(1,2000)}/info.0.json"
    response = requests.get(url)
    data = response.json()

    print(f"{data['title']}, {data['year']}")

    img = requests.get(data['img'])
    name = f"strip.{data['img'].split('.')[-1]}"
    with open(f"{name}", "wb") as f:
        f.write(img.content)

    i = plt.imread(name)
    plt.imshow(i)
    plt.show()
