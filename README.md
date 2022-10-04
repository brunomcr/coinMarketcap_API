# 📘 Consuming CoinMarketCap API
Consumes the CoinMarketCap API, acquiring the price data and change of the day in %, of the first hundred cryptocurrency in the list.

<br>

### 📑 Main technologies:
```
Poetry 1.0.0
Python 3.9
Requests 2.28.1
```

<br>

### ⚙️Requirements.
Create a free account in: https://coinmarketcap.com/api/

**varenv.py**
* Copy the API Key of your account from: https://pro.coinmarketcap.com/account
    
    ```shell
    # Private API KEY
    # https://pro.coinmarketcap.com/account
    
    API_KEY = "YOUR PRIVATE API KEY"
    ```

<br>

### 💻 How to use:

- Clone the repository:
```shell
$ git clone https://github.com/brunomcr/consuming-coinMarketcap-API.git
$ cd consuming-coinMarketcap-API/
```

- Install dependencies:
```shell
$ poetry install
```

- Run main code and saving the data in .csv:
```shell
$ poetry run python main.py
```

<br>

✅ With the main code executed, you can view the data in **coinMarketCap.csv**!

**coinMarketCap.csv**

<table>
  <tr>
    <th>Name</th>
    <th>Symbol</th>
    <th>Price</th>
    <th>% 24h</th>
  </tr>
  <tr>
    <td>Bitcoin</td>
    <td>BTC</td>
    <td>19984.58</td>
    <td>3.74</td>
  </tr>
  <tr>
    <td>Ethereum</td>
    <td>ETH</td>
    <td>1352.45</td>
    <td>3.56</td>
  </tr>
  <tr>
    <td>Tether</td>
    <td>USDT</td>
    <td>1.0</td>
    <td>0.01</td>
  </tr>
  <tr>
    <td>BNB</td>
    <td>BNB</td>
    <td>293.94</td>
    <td>2.7</td>
  </tr>
  <tr>
    <td>USD Coin</td>
    <td>USDC</td>
    <td>1.0</td>
    <td>0.0</td>
  </tr>
</table>
