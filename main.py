import time, validators, os, pandas as pd
import file.run as rn
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

if not os.path.exists("data") :
    os.mkdir("data")
if not os.path.exists("file/items.csv") :
    df = pd.DataFrame({"item":[], "url":[], "date":[]})
    df.to_csv("file/items.csv", index=False)


while True : 
    time.sleep(0.5)
    print("What do you want to do : \n1. Add Item\n2. Check current price\n3. Delete an Item\n4. Exit")
    choice = int(input("Enter number of your choice : "))
    if choice == 1 : 
        while True : 
            time.sleep(0.5)
            url = input("Enter link : ")
            if validators.url(url) and url.startswith("https://www.amazon.in/") : 
                df = pd.read_csv("file/items.csv")
                if url in list(df.url) : 
                    print("Item is already present with this link!")
                    time.sleep(0.5)
                else : 
                    break
            else : 
                print("Invalid Link provided :(")

        while True : 
            name = input("By what name it should be called (spaces will be  removed) : ")
            name = name.replace(" ", "")
            df = pd.read_csv("file/items.csv")
            if input("Confirm? (y/n) : ").lower() == "y" :
                if not os.path.exists(f"data/{name}.csv") :
                    df = pd.DataFrame({"price":[], "time":[], })
                    df.to_csv(f"data/{name}.csv", index=False)
                    newdf = pd.DataFrame({"item":[name], "url":[url], "date":[time.strftime("%d-%b-%Y")]})
                    df = pd.read_csv("file/items.csv")
                    df = pd.concat([newdf, df])
                    df.to_csv("file/items.csv", index=False)
                    rn.run()
                    time.sleep(0.5)
                    break
                else : 
                    print("Item with the following item name is already present! Kindly choose a new name.")
                    time.sleep(0.5)

    elif choice == 2 :
        df = pd.read_csv("file/items.csv")
        if len(df.index) != 0 :
            rn.run()
            while True :
                time.sleep(0.5)
                print("Which item you would like to see?")
                time.sleep(0.5)
                for i in range(len(df.index)) :
                    itemname = df.loc[i, "item"]
                    print(f"{i+1} = {itemname}")
                choice = int(input("Enter number of your choice : "))
                choice -= 1
                if choice > len(df.index) or choice < 0 :
                    print("Not a correct number :(")
                    time.sleep(0.5)
                else :
                    df2 = pd.read_csv(f"data/{df.loc[choice, "item"]}.csv")
                    print(f"Current Price = ₹{df2.loc[len(df.index)-1, "price"]}")
                    time.sleep(1)
                    break
        else : 
            print("No item is there to show :(")
            time.sleep(0.5)

    elif choice == 3 : 
        while True :
            df = pd.read_csv("file/items.csv")
            time.sleep(0.5)
            if len(df.index) != 0 :
                print("Which item you would like to delete?")
                time.sleep(0.5)
                for i in range(len(df.index)) :
                    itemname = df.loc[i, "item"]
                    print(f"{i+1} = {itemname}")
                choice = int(input("Enter number of your choice : "))
                choice -= 1
                if choice > len(df.index) or choice < 0 :
                    print("Not a correct number :(")
                    time.sleep(0.5)
                else :
                    df2 = pd.read_csv(f"data/{df.loc[choice, "item"]}.csv")
                    if input("WARNING : THIS ITEM WILL NO LONGER EXIST IN ANY OF THE CSV    FILES!\nType CONFIRM to confirm : ").upper() == "CONFIRM" :
                        fileloc = f"data/{df.loc[choice, "item"]}.csv"
                        os.remove(fileloc)
                        df.drop(choice, axis=0, inplace=True)
                        df.to_csv("file/items.csv", index=False)
                        print("Confirmed!")
                        time.sleep(1)
                    else :
                        print("No confirmation")
                    break
            else : 
                print("No item has been added yet.")
                break

    elif choice == 4 :
        print("Exiting the program!")
        time.sleep(1)
        break
    else : 
        print("Wrong Input!!")
        time.sleep(0.5)

