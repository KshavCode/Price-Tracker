from bs4 import BeautifulSoup
import requests, pandas as pd, time, os, warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

def run(location="file/items.csv") :
    df = pd.read_csv(location)
    dir_path = os.path.dirname(os.path.realpath(__file__))[:-4].replace("\\", "/")
    for obj in range(len(df.index)) : 
        url = df.loc[obj, "url"]
        df2 = pd.read_csv(f"{dir_path}/data/{df.loc[obj, "item"]}.csv")
        content = requests.get(url, headers={"User-Agent":"Defined"}).text
        try : 
            soup = BeautifulSoup(content, "html.parser")
            price = soup.find(class_="a-price-whole").text
            if "," in str(price) :
                price = price.replace(",", "")
            price = float(price)
            newdf = pd.DataFrame({"price":[price], "date":[time.strftime("%d-%b-%Y")], "time":[time.strftime("%H:%M:%S")]})
            df2 = pd.concat([df2, newdf])
            df2.to_csv(f"{dir_path}/data/{df.loc[obj, "item"]}.csv", index=False)
        except Exception as e :
            print(e)
            with open("file/log.txt", "a") as f :
                f.write(f"{e}\n\n")
            time.sleep(0.5)


if __name__ == "__main__" :
    run()