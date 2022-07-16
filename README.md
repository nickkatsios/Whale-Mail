# Whale-Mail.
Large blockchain tranasction monitoring script using [Whale Alert](https://whale-alert.io/) API.

Fetches all transactions larger than 500.000$ at a set `interval` time and notifies recipients from `recipients` list using e-mail with [smtp lib](https://docs.python.org/3/library/smtplib.html).

List of supported blockchains. 
- Bitcoin. 
- Ethereum.
- Stellar. 
- Ripple. 
- NEO. 
- Tron. 
- Tezos. 
- Binance Chain. 
- EOS. 
- Steem. 
- Icon.

## Notes.
1. Because transaction block confirmation varies between blockchains, some tranasctions on specific blockchains may come bundled at specific interval windows.
For example, **Bitcoin** blocks, containing all the most recent transactions, are added to the blockchain **every 10 minutes**. 
As a result , it is likely that the script will send multiple alerts about large tranactions on Bitcoin blockcahin every 10 minutes.
On the other hand , **Ethereum** tranactions take **15 seconds to 5 minutes** whereas **Tron** only takes about **3 seconds**.

2. The 500.000$ minimum threshold transaction value comes from the free API limitations and can be adjusted by changing the `threshold_value` variable. Due to calls/min limitation `interval` variable cannot be < 6secs ( i.e. 10 calls per min)  

# How to use.
To alert yourself ,or anyone you wish to, about large transactions , you need to do the following.

(All variables that need changing apear at the top of the script)
1. Get a whale alert API key by signing up [here](https://whale-alert.io/signup).
2. Get a gmail [app password](https://support.google.com/accounts/answer/185833?hl=en) for your account [here](https://myaccount.google.com/apppasswords).
3. Replace `key` variable with your API key. 
4. Replace `app_password` variable with your app password.
5. Replace `gmail_address` variable with your gmail address.
6. Add any recipients' e-mail addresses you want to send alerts to in the `recipients` list.
7. Choose an interval time in seconds between the API calls. (Recommended- Default: 2min = 120 secs) by changing the `interval` variable.

## Warning!
While testing any changes to commit to the script,
it is recommended that you use environment variables for your keys-passwords to avoid adding any sensitive information to your pull request.

[How to for Windows Machines.](https://youtu.be/IolxqkL7cD8)

[How to for Linux Machines.](https://youtu.be/5iWhQWVXosU)
