import requests

def convert_curr():
    init_currency = input("Enter the initial currency: ")
    target_currency = input("Enter the target currency: ")

    while True:
        try:
            amount = float(input("Enter the amount: "))
        except:
            print("The amount must be a number")
            continue

        if not amount>0:
            print("The amount needs to be greater than 0")
            continue
        else:
            break

    url = "https://api.apilayer.com/fixer/convert?to={target_currency}&from={init_currency}&amount={amount}"

    payload = {}
    headers= {
       "apikey": "OLZg86YdQw0EWvoLqpapysqCISs3qdpR"
    }

    response = requests.request("GET", url, headers=headers, data = payload)
    status_code = response.status_code

    if status_code !=200:
        result = response.json()
        print('Error response:'+str(result))
        quit()

    result = response.json()
    print('Conversion result:'+str(result))

if __name__=='__main__':
    convert_curr()