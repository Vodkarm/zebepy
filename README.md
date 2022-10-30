<img src="https://i.postimg.cc/2SgTN0rv/Zebepy.png">

# 📺 Zebepy

Hi! Welcome to the github of Zebepy
 Thanks you, and contributions are welcome.
 
 <img alt="Version" src="https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000" /> <img alt="Forks" src="https://img.shields.io/github/forks/vodkarm/zebepy?style=social"> <img alt="doc" src="https://img.shields.io/badge/Documentaion-yes-blue"> <img alt="maintened" src="https://img.shields.io/badge/maintened%3F-yes-blue"> ![GitHub Repo stars](https://img.shields.io/github/stars/vodkarm/zebepy?style=social) [![Downloads](https://pepy.tech/badge/zebepy)](https://pepy.tech/project/zebebpy)


 # ❓ What is it ?
Zebepy is the first python API WRAPPER (*Note: it's not the official*)
# 🌐 Is it open-source ?
Yes it is, under MIT License 
# 💥 How to use ?
```
pip install zebepy
```

## 🌹 Syntax Exemple
```py
from zebepy import Zebedee

print(Zebedee.Wallet.Details("my_api_key"))
```
# 💻 Documentation

*Feel free to translate it ;)*

## 🔥 Wallet

```py
from zebepy import Zebedee

print(Zebedee.Wallet.Details("my_api_key"))
```
Success response:
```
{"message":"Successfully retrieved Wallet.","data":{"unit":"msats","balance":"0"}}
```
## 🔥 Charges
### 🚀 Create charge
```py
from zebepy import Zebedee

print(Zebedee.Charges.Create("expirationInSeconds", "sats amount", "description", "internal id (to fetch this charge)", "callbackUrl (put any url if you don't have one)", "my_api_key"))
```
Success response:
```
{
    "message": "Successfully created Charge.",
    "data": {
        "unit": "msats",
        "amount": "10000",
        "confirmedAt": null,
        "status": "pending",
        "description": "My Charge Description",
        "createdAt": "2020-05-09T15:09:05.765Z",
        "expiresAt": "2020-05-09T15:14:05.618Z",
        "id": "1907b0fe-789b-4e25-b18a-0c4c0f5cced7",
        "internalId": "11af01d092444a317cb33faa6b8304b8",
        "callbackUrl": "https://your-website.com/callback",
        "invoice": {
            "request": "lnbc100n1p0td3u3pp5z2ed9yjfrz0rgu0fzuc5cdwfu8dtjlgrfztz5uga8hakkjy2yzgsdpzf4ujqsmgv9exwefqg3jhxcmjd9c8g6t0dccqzpgxqzfvsp5q8z5mkghmuzrnusxdwtmls7x8vuy63j25rt4z55gj3s7340dv72q9qy9qsqz02rlmlzcvew3vk90c6l0369ewk7tkr2tx0yrk3qa235v07w6d3qeksk99wm7y8f8ug7zqy6yjudu4cs2f4umpey43cw7msyj7uqj2qq8x03te",
            "uri": "lightning:lnbc100n1p0td3u3pp5z2ed9yjfrz0rgu0fzuc5cdwfu8dtjlgrfztz5uga8hakkjy2yzgsdpzf4ujqsmgv9exwefqg3jhxcmjd9c8g6t0dccqzpgxqzfvsp5q8z5mkghmuzrnusxdwtmls7x8vuy63j25rt4z55gj3s7340dv72q9qy9qsqz02rlmlzcvew3vk90c6l0369ewk7tkr2tx0yrk3qa235v07w6d3qeksk99wm7y8f8ug7zqy6yjudu4cs2f4umpey43cw7msyj7uqj2qq8x03te"
        }
    }
}
```
### 🚀 Fetch all charges
```py
from zebepy import Zebedee

print(Zebedee.Charges.GetAll("my_api_key"))
```
Success response:
```
{
    "message": "Successfully retrieved Charges.",
    "data": [
        {
            "unit": "msats",
            "amount": "10000",
            "confirmedAt": null,
            "status": "pending",
            "description": "My Charge Description",
            "createdAt": "2020-05-09T15:09:05.765Z",
            "expiresAt": "2020-05-09T15:14:05.618Z",
            "id": "1907b0fe-789b-4e25-b18a-0c4c0f5cced7",
            "internalId": "11af01d092444a317cb33faa6b8304b8",
            "callbackUrl": "https://your-website.com/callback",
            "invoice": {
                "request": "lnbc100n1p0td3u3pp5z2ed9yjfrz0rgu0fzuc5cdwfu8dtjlgrfztz5uga8hakkjy2yzgsdpzf4ujqsmgv9exwefqg3jhxcmjd9c8g6t0dccqzpgxqzfvsp5q8z5mkghmuzrnusxdwtmls7x8vuy63j25rt4z55gj3s7340dv72q9qy9qsqz02rlmlzcvew3vk90c6l0369ewk7tkr2tx0yrk3qa235v07w6d3qeksk99wm7y8f8ug7zqy6yjudu4cs2f4umpey43cw7msyj7uqj2qq8x03te",
                "uri": "lightning:lnbc100n1p0td3u3pp5z2ed9yjfrz0rgu0fzuc5cdwfu8dtjlgrfztz5uga8hakkjy2yzgsdpzf4ujqsmgv9exwefqg3jhxcmjd9c8g6t0dccqzpgxqzfvsp5q8z5mkghmuzrnusxdwtmls7x8vuy63j25rt4z55gj3s7340dv72q9qy9qsqz02rlmlzcvew3vk90c6l0369ewk7tkr2tx0yrk3qa235v07w6d3qeksk99wm7y8f8ug7zqy6yjudu4cs2f4umpey43cw7msyj7uqj2qq8x03te"
            }
        },
        {
            "unit": "msats",
            "amount": "10000",
            "confirmedAt": null,
            "status": "pending",
            "description": "My Charge Description",
            "createdAt": "2020-05-09T15:09:05.765Z",
            "expiresAt": "2020-05-09T15:14:05.618Z",
            "id": "1907b0fe-789b-4e25-b18a-0c4c0f5cced7",
            "internalId": "11af01d092444a317cb33faa6b8304b8",
            "callbackUrl": "https://your-website.com/callback",
            "invoice": {
                "request": "lnbc100n1p0td3u3pp5z2ed9yjfrz0rgu0fzuc5cdwfu8dtjlgrfztz5uga8hakkjy2yzgsdpzf4ujqsmgv9exwefqg3jhxcmjd9c8g6t0dccqzpgxqzfvsp5q8z5mkghmuzrnusxdwtmls7x8vuy63j25rt4z55gj3s7340dv72q9qy9qsqz02rlmlzcvew3vk90c6l0369ewk7tkr2tx0yrk3qa235v07w6d3qeksk99wm7y8f8ug7zqy6yjudu4cs2f4umpey43cw7msyj7uqj2qq8x03te",
                "uri": "lightning:lnbc100n1p0td3u3pp5z2ed9yjfrz0rgu0fzuc5cdwfu8dtjlgrfztz5uga8hakkjy2yzgsdpzf4ujqsmgv9exwefqg3jhxcmjd9c8g6t0dccqzpgxqzfvsp5q8z5mkghmuzrnusxdwtmls7x8vuy63j25rt4z55gj3s7340dv72q9qy9qsqz02rlmlzcvew3vk90c6l0369ewk7tkr2tx0yrk3qa235v07w6d3qeksk99wm7y8f8ug7zqy6yjudu4cs2f4umpey43cw7msyj7uqj2qq8x03te"
            }
        },
        { ... },
        { ... },
        { ... },
        { ... }
    ]
}
```
### 🚀 Fetch charge details
```py
from zebepy import Zebedee

print(Zebedee.Charges.FromId("internal charge id", "my_api_key"))
```
Success response:

```
{
    "message": "Successfully retrieved Charge.",
    "data": {
        "unit": "msats",
        "amount": "10000",
        "confirmedAt": null,
        "status": "pending",
        "description": "My Charge Description",
        "createdAt": "2020-05-09T15:09:05.765Z",
        "expiresAt": "2020-05-09T15:14:05.618Z",
        "id": "1907b0fe-789b-4e25-b18a-0c4c0f5cced7",
        "internalId": "11af01d092444a317cb33faa6b8304b8",
        "callbackUrl": "https://your-website.com/callback",
        "invoice": {
            "request": "lnbc100n1p0td3u3pp5z2ed9yjfrz0rgu0fzuc5cdwfu8dtjlgrfztz5uga8hakkjy2yzgsdpzf4ujqsmgv9exwefqg3jhxcmjd9c8g6t0dccqzpgxqzfvsp5q8z5mkghmuzrnusxdwtmls7x8vuy63j25rt4z55gj3s7340dv72q9qy9qsqz02rlmlzcvew3vk90c6l0369ewk7tkr2tx0yrk3qa235v07w6d3qeksk99wm7y8f8ug7zqy6yjudu4cs2f4umpey43cw7msyj7uqj2qq8x03te",
            "uri": "lightning:lnbc100n1p0td3u3pp5z2ed9yjfrz0rgu0fzuc5cdwfu8dtjlgrfztz5uga8hakkjy2yzgsdpzf4ujqsmgv9exwefqg3jhxcmjd9c8g6t0dccqzpgxqzfvsp5q8z5mkghmuzrnusxdwtmls7x8vuy63j25rt4z55gj3s7340dv72q9qy9qsqz02rlmlzcvew3vk90c6l0369ewk7tkr2tx0yrk3qa235v07w6d3qeksk99wm7y8f8ug7zqy6yjudu4cs2f4umpey43cw7msyj7uqj2qq8x03te"
        }
    },
}
```

## 🔥 Withdrawal Requests
### 🚀 Create Withdrawal Request
```py
from zebepy import Zebedee

print(Zebedee.Withdrawal.Request("expirationInSeconds", "sats amount", "description", "internal id (to fetch this withdrawal)", "callbackUrl (put any url if you don't have one)", "my_api_key")
```
Success reponse:
```
{
    "message": "Successfully created Withdrawal Request.",
    "data": {
        "unit": "msats",
        "amount": "12000",
        "status": "pending",
        "createdAt": "2020-05-09T15:15:30.222Z",
        "expiresAt": "2020-05-09T15:20:30.212Z",
        "description": "My Withdrawal Description",
        "id": "243ee7f6-a91b-4644-aa5f-ecc9c9fdd351",
        "internalId": "11af01d092444a317cb33faa6b8304b8",
        "callbackUrl": "https://your-website.com/callback",
        "invoice": {
            "request": "lnurl1dp68gurn8ghj7er9wch85etzv4jx2efwd9hj7a3s9acxz7tvdaskgtthd96xserjv9mkzmpdwfjhzat9wd6r7um9vdex2apaxfsnqvmz8pjx2ephxucnzdphxa3xzd3kvfjk2vnyxejnzdf3x93n2e3evesnsetyxsenzvesvdjrxdtrv9jxxdnzxaskxvm9vscrzeg58h24k",
            "fastRequest": "lnurl1dp68gurn8ghj7er9wch85etzv4jx2efwd9hj7a3s9acxz7tvdaskgtthd96xserjv9mkzmpdwfjhzat9wd6r7arpvu7hw6t5dpj8ycth2fjhzat9wd6zv6e385exzvpnvguxgetyxumnzvf5xumkycfkxe3x2efjvsmx2vf4xyckxdtx89nxzwr9vs6rxvfnxp3kgve4vdskgcekvgmkzcenv4jrqvt9yekkjmjhd96xserjv9mkzcnvv57nzv3sxqczvmtp0ptkjargv3exzampvfkx20f3xgcrqvpxv3jkvct4d36ygetnvdexjur5d9hku02d0ys9w6t5dpj8ycthv9kzq3r9wd3hy6tsw35k7m3xvdskcmrzv93kk0tgw368que69uhkgetk9eax2cn9v3jk2tnfduhhvvp0wpex7cm9wdej6amfw35xgunpwaskcttjv4ch2etnwsvtdjtq",
            "uri": "lightning:lnurl1dp68gurn8ghj7er9wch85etzv4jx2efwd9hj7a3s9acxz7tvdaskgtthd96xserjv9mkzmpdwfjhzat9wd6r7um9vdex2apaxfsnqvmz8pjx2ephxucnzdphxa3xzd3kvfjk2vnyxejnzdf3x93n2e3evesnsetyxsenzvesvdjrxdtrv9jxxdnzxaskxvm9vscrzeg58h24k",
            "fastUri": "lightning:lnurl1dp68gurn8ghj7er9wch85etzv4jx2efwd9hj7a3s9acxz7tvdaskgtthd96xserjv9mkzmpdwfjhzat9wd6r7arpvu7hw6t5dpj8ycth2fjhzat9wd6zv6e385exzvpnvguxgetyxumnzvf5xumkycfkxe3x2efjvsmx2vf4xyckxdtx89nxzwr9vs6rxvfnxp3kgve4vdskgcekvgmkzcenv4jrqvt9yekkjmjhd96xserjv9mkzcnvv57nzv3sxqczvmtp0ptkjargv3exzampvfkx20f3xgcrqvpxv3jkvct4d36ygetnvdexjur5d9hku02d0ys9w6t5dpj8ycthv9kzq3r9wd3hy6tsw35k7m3xvdskcmrzv93kk0tgw368que69uhkgetk9eax2cn9v3jk2tnfduhhvvp0wpex7cm9wdej6amfw35xgunpwaskcttjv4ch2etnwsvtdjtq"
        }
    }
}
```
### 🚀 Fetch All Withdrawal Requests
```py
from zebepy import Zebedee

print(Zebedee.Withdrawal.GetAll("my_api_key")
```
Success response:
```
{
    "message": "Successfully retrieved Withdrawal Requests.",
    "data": [
        "unit": "msats",
        "amount": "12000",
        "status": "pending",
        "createdAt": "2020-05-09T15:15:30.222Z",
        "expiresAt": "2020-05-09T15:20:30.212Z",
        "description": "My Withdrawal Description",
        "id": "243ee7f6-a91b-4644-aa5f-ecc9c9fdd351",
        "internalId": "11af01d092444a317cb33faa6b8304b8",
        "callbackUrl": "https://your-website.com/callback",
        "invoice": {
            "request": "lnurl1dp68gurn8ghj7er9wch85etzv4jx2efwd9hj7a3s9acxz7tvdaskgtthd96xserjv9mkzmpdwfjhzat9wd6r7um9vdex2apaxfsnqvmz8pjx2ephxucnzdphxa3xzd3kvfjk2vnyxejnzdf3x93n2e3evesnsetyxsenzvesvdjrxdtrv9jxxdnzxaskxvm9vscrzeg58h24k",
            "fastRequest": "lnurl1dp68gurn8ghj7er9wch85etzv4jx2efwd9hj7a3s9acxz7tvdaskgtthd96xserjv9mkzmpdwfjhzat9wd6r7arpvu7hw6t5dpj8ycth2fjhzat9wd6zv6e385exzvpnvguxgetyxumnzvf5xumkycfkxe3x2efjvsmx2vf4xyckxdtx89nxzwr9vs6rxvfnxp3kgve4vdskgcekvgmkzcenv4jrqvt9yekkjmjhd96xserjv9mkzcnvv57nzv3sxqczvmtp0ptkjargv3exzampvfkx20f3xgcrqvpxv3jkvct4d36ygetnvdexjur5d9hku02d0ys9w6t5dpj8ycthv9kzq3r9wd3hy6tsw35k7m3xvdskcmrzv93kk0tgw368que69uhkgetk9eax2cn9v3jk2tnfduhhvvp0wpex7cm9wdej6amfw35xgunpwaskcttjv4ch2etnwsvtdjtq",
            "uri": "lightning:lnurl1dp68gurn8ghj7er9wch85etzv4jx2efwd9hj7a3s9acxz7tvdaskgtthd96xserjv9mkzmpdwfjhzat9wd6r7um9vdex2apaxfsnqvmz8pjx2ephxucnzdphxa3xzd3kvfjk2vnyxejnzdf3x93n2e3evesnsetyxsenzvesvdjrxdtrv9jxxdnzxaskxvm9vscrzeg58h24k",
            "fastUri": "lightning:lnurl1dp68gurn8ghj7er9wch85etzv4jx2efwd9hj7a3s9acxz7tvdaskgtthd96xserjv9mkzmpdwfjhzat9wd6r7arpvu7hw6t5dpj8ycth2fjhzat9wd6zv6e385exzvpnvguxgetyxumnzvf5xumkycfkxe3x2efjvsmx2vf4xyckxdtx89nxzwr9vs6rxvfnxp3kgve4vdskgcekvgmkzcenv4jrqvt9yekkjmjhd96xserjv9mkzcnvv57nzv3sxqczvmtp0ptkjargv3exzampvfkx20f3xgcrqvpxv3jkvct4d36ygetnvdexjur5d9hku02d0ys9w6t5dpj8ycthv9kzq3r9wd3hy6tsw35k7m3xvdskcmrzv93kk0tgw368que69uhkgetk9eax2cn9v3jk2tnfduhhvvp0wpex7cm9wdej6amfw35xgunpwaskcttjv4ch2etnwsvtdjtq"
        },
        "unit": "msats",
        "amount": "12000",
        "status": "pending",
        "createdAt": "2020-05-09T15:15:30.222Z",
        "expiresAt": "2020-05-09T15:20:30.212Z",
        "description": "My Withdrawal Description",
        "id": "243ee7f6-a91b-4644-aa5f-ecc9c9fdd351",
        "internalId": "11af01d092444a317cb33faa6b8304b8",
        "callbackUrl": "https://your-website.com/callback",
        "invoice": {
            "request": "lnurl1dp68gurn8ghj7er9wch85etzv4jx2efwd9hj7a3s9acxz7tvdaskgtthd96xserjv9mkzmpdwfjhzat9wd6r7um9vdex2apaxfsnqvmz8pjx2ephxucnzdphxa3xzd3kvfjk2vnyxejnzdf3x93n2e3evesnsetyxsenzvesvdjrxdtrv9jxxdnzxaskxvm9vscrzeg58h24k",
            "fastRequest": "lnurl1dp68gurn8ghj7er9wch85etzv4jx2efwd9hj7a3s9acxz7tvdaskgtthd96xserjv9mkzmpdwfjhzat9wd6r7arpvu7hw6t5dpj8ycth2fjhzat9wd6zv6e385exzvpnvguxgetyxumnzvf5xumkycfkxe3x2efjvsmx2vf4xyckxdtx89nxzwr9vs6rxvfnxp3kgve4vdskgcekvgmkzcenv4jrqvt9yekkjmjhd96xserjv9mkzcnvv57nzv3sxqczvmtp0ptkjargv3exzampvfkx20f3xgcrqvpxv3jkvct4d36ygetnvdexjur5d9hku02d0ys9w6t5dpj8ycthv9kzq3r9wd3hy6tsw35k7m3xvdskcmrzv93kk0tgw368que69uhkgetk9eax2cn9v3jk2tnfduhhvvp0wpex7cm9wdej6amfw35xgunpwaskcttjv4ch2etnwsvtdjtq",
            "uri": "lightning:lnurl1dp68gurn8ghj7er9wch85etzv4jx2efwd9hj7a3s9acxz7tvdaskgtthd96xserjv9mkzmpdwfjhzat9wd6r7um9vdex2apaxfsnqvmz8pjx2ephxucnzdphxa3xzd3kvfjk2vnyxejnzdf3x93n2e3evesnsetyxsenzvesvdjrxdtrv9jxxdnzxaskxvm9vscrzeg58h24k",
            "fastUri": "lightning:lnurl1dp68gurn8ghj7er9wch85etzv4jx2efwd9hj7a3s9acxz7tvdaskgtthd96xserjv9mkzmpdwfjhzat9wd6r7arpvu7hw6t5dpj8ycth2fjhzat9wd6zv6e385exzvpnvguxgetyxumnzvf5xumkycfkxe3x2efjvsmx2vf4xyckxdtx89nxzwr9vs6rxvfnxp3kgve4vdskgcekvgmkzcenv4jrqvt9yekkjmjhd96xserjv9mkzcnvv57nzv3sxqczvmtp0ptkjargv3exzampvfkx20f3xgcrqvpxv3jkvct4d36ygetnvdexjur5d9hku02d0ys9w6t5dpj8ycthv9kzq3r9wd3hy6tsw35k7m3xvdskcmrzv93kk0tgw368que69uhkgetk9eax2cn9v3jk2tnfduhhvvp0wpex7cm9wdej6amfw35xgunpwaskcttjv4ch2etnwsvtdjtq"
        },
        { ... },
        { ... },
        { ... }
    ]
}
```

### 🚀 Fetch Withdrawal Details
```py
from zebepy import Zebedee

print(Zebedee.Withdrawal.FromId("internal withdrawal id", "my_api_key"))
```
Success reponse:
```
{
    "message": "Successfully retrieved Withdrawal Request.",
    "data": {
        "unit": "msats",
        "amount": "12000",
        "status": "pending",
        "createdAt": "2020-05-09T15:15:30.222Z",
        "expiresAt": "2020-05-09T15:20:30.212Z",
        "description": "My Withdrawal Description",
        "id": "243ee7f6-a91b-4644-aa5f-ecc9c9fdd351",
        "internalId": "11af01d092444a317cb33faa6b8304b8",
        "callbackUrl": "https://your-website.com/callback",
        "invoice": {
            "request": "lnurl1dp68gurn8ghj7er9wch85etzv4jx2efwd9hj7a3s9acxz7tvdaskgtthd96xserjv9mkzmpdwfjhzat9wd6r7um9vdex2apaxfsnqvmz8pjx2ephxucnzdphxa3xzd3kvfjk2vnyxejnzdf3x93n2e3evesnsetyxsenzvesvdjrxdtrv9jxxdnzxaskxvm9vscrzeg58h24k",
            "fastRequest": "lnurl1dp68gurn8ghj7er9wch85etzv4jx2efwd9hj7a3s9acxz7tvdaskgtthd96xserjv9mkzmpdwfjhzat9wd6r7arpvu7hw6t5dpj8ycth2fjhzat9wd6zv6e385exzvpnvguxgetyxumnzvf5xumkycfkxe3x2efjvsmx2vf4xyckxdtx89nxzwr9vs6rxvfnxp3kgve4vdskgcekvgmkzcenv4jrqvt9yekkjmjhd96xserjv9mkzcnvv57nzv3sxqczvmtp0ptkjargv3exzampvfkx20f3xgcrqvpxv3jkvct4d36ygetnvdexjur5d9hku02d0ys9w6t5dpj8ycthv9kzq3r9wd3hy6tsw35k7m3xvdskcmrzv93kk0tgw368que69uhkgetk9eax2cn9v3jk2tnfduhhvvp0wpex7cm9wdej6amfw35xgunpwaskcttjv4ch2etnwsvtdjtq",
            "uri": "lightning:lnurl1dp68gurn8ghj7er9wch85etzv4jx2efwd9hj7a3s9acxz7tvdaskgtthd96xserjv9mkzmpdwfjhzat9wd6r7um9vdex2apaxfsnqvmz8pjx2ephxucnzdphxa3xzd3kvfjk2vnyxejnzdf3x93n2e3evesnsetyxsenzvesvdjrxdtrv9jxxdnzxaskxvm9vscrzeg58h24k",
            "fastUri": "lightning:lnurl1dp68gurn8ghj7er9wch85etzv4jx2efwd9hj7a3s9acxz7tvdaskgtthd96xserjv9mkzmpdwfjhzat9wd6r7arpvu7hw6t5dpj8ycth2fjhzat9wd6zv6e385exzvpnvguxgetyxumnzvf5xumkycfkxe3x2efjvsmx2vf4xyckxdtx89nxzwr9vs6rxvfnxp3kgve4vdskgcekvgmkzcenv4jrqvt9yekkjmjhd96xserjv9mkzcnvv57nzv3sxqczvmtp0ptkjargv3exzampvfkx20f3xgcrqvpxv3jkvct4d36ygetnvdexjur5d9hku02d0ys9w6t5dpj8ycthv9kzq3r9wd3hy6tsw35k7m3xvdskcmrzv93kk0tgw368que69uhkgetk9eax2cn9v3jk2tnfduhhvvp0wpex7cm9wdej6amfw35xgunpwaskcttjv4ch2etnwsvtdjtq"
        }
    }
}
```
## 🔥 Payements
### 🚀 Pay Invoice
```py
from zebepy import Zebedee

print(Zebedee.Payements.Pay("description", "internal id to fetch transaction", "invoice to pay", "my_api_key"))
```
Success Response:
```
{
    "message": "Successfully made Payment.",
    "data": {
        "fee": "2000",
        "unit": "msats",
        "amount": "12000",
        "status": "completed",
        "processedAt": "2020-05-09T15:19:09.365Z",
        "id": "5d88b2e0-e491-40e1-a8a8-a81ae68f2297",
        "description": "My Custom Payment Description",
        "internalId": "11af01d092444a317cb33faa6b8304b8",
        "invoice": "lnbc120n1p0tdjwmpp5ycws0d788cjeqp9rn2wwxfymrekj9n80wy2yrk66tuu3ga5wukfsdzq2pshjmt9de6zqen0wgsrzv3qwp5hsetvwvsxzapqwdshgmmndp5hxtnsd3skxefwxqzjccqp2sp5vnsvmjlu6hrfegcdjs47njrga36g3x45wfmqjjjlerwgagj62yysrzjq2v4aw4gy7m93en32dcaplym056zezcljdjshyk8yakwtsp2h4yvcz9atuqqhtsqqqqqqqlgqqqqqqgqjq9qy9qsqhykfacrdy06cuyegvt4p50su53qwgrqn5jf6d83fd0upsa4frpxqnm2zl323zuvmz5ypv9gh9nr3jav6u2ccwkpd56h3n6l3ja5q7wgpxudlv4"
    }
}
```
### 🚀 Fetch All Payements
```py
from zebepy import Zebedee

print(Zebedee.Payements.GetAll("my_api_key"))
```
Response Exemple:
```
{
    "message": "Successfully retrieved Payment.",
    "data": [
        {
            "fee": "2000",
            "unit": "msats",
            "amount": "12000",
            "status": "completed",
            "processedAt": "2020-05-09T15:19:09.365Z",
            "id": "5d88b2e0-e491-40e1-a8a8-a81ae68f2297",
            "description": "My Custom Payment Description",
            "internalId": "11af01d092444a317cb33faa6b8304b8",
            "invoice": "lnbc120n1p0tdjwmpp5ycws0d788cjeqp9rn2wwxfymrekj9n80wy2yrk66tuu3ga5wukfsdzq2pshjmt9de6zqen0wgsrzv3qwp5hsetvwvsxzapqwdshgmmndp5hxtnsd3skxefwxqzjccqp2sp5vnsvmjlu6hrfegcdjs47njrga36g3x45wfmqjjjlerwgagj62yysrzjq2v4aw4gy7m93en32dcaplym056zezcljdjshyk8yakwtsp2h4yvcz9atuqqhtsqqqqqqqlgqqqqqqgqjq9qy9qsqhykfacrdy06cuyegvt4p50su53qwgrqn5jf6d83fd0upsa4frpxqnm2zl323zuvmz5ypv9gh9nr3jav6u2ccwkpd56h3n6l3ja5q7wgpxudlv4"
        },
        {
            "fee": "2000",
            "unit": "msats",
            "amount": "12000",
            "status": "completed",
            "processedAt": "2020-05-09T15:19:09.365Z",
            "id": "5d88b2e0-e491-40e1-a8a8-a81ae68f2297",
            "description": "My Custom Payment Description",
            "internalId": "11af01d092444a317cb33faa6b8304b8",
            "invoice": "lnbc120n1p0tdjwmpp5ycws0d788cjeqp9rn2wwxfymrekj9n80wy2yrk66tuu3ga5wukfsdzq2pshjmt9de6zqen0wgsrzv3qwp5hsetvwvsxzapqwdshgmmndp5hxtnsd3skxefwxqzjccqp2sp5vnsvmjlu6hrfegcdjs47njrga36g3x45wfmqjjjlerwgagj62yysrzjq2v4aw4gy7m93en32dcaplym056zezcljdjshyk8yakwtsp2h4yvcz9atuqqhtsqqqqqqqlgqqqqqqgqjq9qy9qsqhykfacrdy06cuyegvt4p50su53qwgrqn5jf6d83fd0upsa4frpxqnm2zl323zuvmz5ypv9gh9nr3jav6u2ccwkpd56h3n6l3ja5q7wgpxudlv4"
        },
        {...},
        {...},
        {...}
    ]
}
```
### 🚀 Fetch details from ID
```py
from zebepy import Zebedee

print(Zebedee.Payements.FromId("transaction id", "my_api_key"))
```
Response Exemple:
```
{
    "message": "Successfully retrieved Payment.",
    "data": {
        "fee": "2000",
        "unit": "msats",
        "amount": "12000",
        "status": "completed",
        "processedAt": "2020-05-09T15:19:09.365Z",
        "id": "5d88b2e0-e491-40e1-a8a8-a81ae68f2297",
        "description": "My Custom Payment Description",
        "internalId": "11af01d092444a317cb33faa6b8304b8",
        "invoice": "lnbc120n1p0tdjwmpp5ycws0d788cjeqp9rn2wwxfymrekj9n80wy2yrk66tuu3ga5wukfsdzq2pshjmt9de6zqen0wgsrzv3qwp5hsetvwvsxzapqwdshgmmndp5hxtnsd3skxefwxqzjccqp2sp5vnsvmjlu6hrfegcdjs47njrga36g3x45wfmqjjjlerwgagj62yysrzjq2v4aw4gy7m93en32dcaplym056zezcljdjshyk8yakwtsp2h4yvcz9atuqqhtsqqqqqqqlgqqqqqqgqjq9qy9qsqhykfacrdy06cuyegvt4p50su53qwgrqn5jf6d83fd0upsa4frpxqnm2zl323zuvmz5ypv9gh9nr3jav6u2ccwkpd56h3n6l3ja5q7wgpxudlv4"
    },
}
```
## 🔥 Lightning Address
### 🚀 Send Payment to Lightning Address
```py
from zebepy import Zebedee

print(Zebedee.Adress.Send("adress to send", "amount", "comment", "my_api_key"))
```
### 🚀 Fetch Charge from Lightning Address
```py
from zebepy import Zebedee

print(Zebedee.Adress.Fetch("adress to fetch", "amount", "comment", "my_api_key"))
```
### 🚀 Check if adress is valid
```py
from zebepy import Zebedee

print(Zebedee.Adress.Validate("adress to check", "my_api_key"))
```

## 🔥 Gamertag
### 🚀 Send to a gamertag
```py
from zebepy import Zebedee

print(Zebedee.Gamertag.Send("garmertag to send", "amount", "description", "my_api_key"))
```
Success Response:
```
{
    "success": true,
    "data": {
        "receiverId": "ec9b38d5-b126-4307-9d1e-8aa0dfab5d7e",
        "transactionId": "78fb6474-d791-47a1-bda1-a4b9023898c0",
        "amount": "1000",
        "comment": "Sending to Gamertag"
    },
    "message": "Payment done."
}
```
### 🚀 Fetch Gamertag Transaction Details By ID
```py
from zebepy import Zebedee

print(Zebedee.Gamertag.FetchDetailsById("id",  "my_api_key"))
```
Success Response:
```
{
    "success": true,
    "data": {
        "id": "78fb6474-d791-47a1-bda1-a4b9023898c0",
        "receiverId": "ec9b38d5-b126-4307-9d1e-8aa0dfab5d7e",
        "amount": "100000",
        "fee": "1000",
        "unit": "msats",
        "processedAt": "2022-08-12T15:11:07.358Z",
        "confirmedAt": "2022-08-12T15:11:07.351Z",
        "comment": "Sending to ZBD Gamertag",
        "status": "TRANSACTION_STATUS_COMPLETED"
    }
}
```
### 🚀 Fetch User ID By Gamertag
```py
from zebepy import Zebedee

print(Zebedee.Gamertag.FetchUserId("gamertag", "my_api_key"))
```
Success response:
```
{
  "success": true,
  "data": {
    "id": "0a59bf56-dba3-4888-8407-cbc02eba3a6e"
  }
}
```
### 🚀 Fetch Gamertag By User ID
```py
from zebepy import Zebedee

print(Zebedee.Gamertag.FetchById("id", "my_api_key")
```
Success Response:
```
{
    "success": true,
    "data": {
        "gamertag": "andre"
    },
    "message": "Fetched gamertag from uuid"
}
```
### 🚀 Fetch Charge from Gamertag
```py
from zebepy import Zebedee

print(Zebedee.Gamertag.FetchCharge("gamertag", "amount", "description", "my_api_key")
```
## 🔥 Utilities
### 🚀 Is Supported Region
```py
from zebepy import Zebedee

print(Zebedee.Utilities.IsSupported("ip adress to check", "my_api_key"))
```
### 🚀 API Production IPs
*Get list of zebedee's prods ips*
```py
from zebepy import Zebedee

print(Zebedee.Utilities.Prod("my_api_key"))
```
### 🚀 BTC USD Exchange Rate
```py
from zebepy import Zebedee

print(Zebedee.Utilities.ExchangeRate()) # API Key not requiered
```
Success response:
```
{
    "success": true,
    "data": {
        "btcUsdPrice": "20058.51",
        "btcUsdTimestamp": "1655665557"
    },
    "message": "Successfully retrieved BTC USD price ticker information."
}
```
## 🔥 Keysend
### 🚀 Send Keysend Payment
```py
from zebepy import Zebedee

print(Zebedee.Key.Send("public key that will receive sats", "amount", "callback url (put any url if you don't have one)", "my_api_key"))
```

# 💢 Note !

## 💲 Amount
*Every amount is in millisatoshis, exemple: 1 SAT = 1000 MILLISATS*
## 💯 Who?
*This package was did by vodkarm06, this package isn't the official*


# ✨ Dependencies
**Zebepy** has only 1 dependencies 🥳 !
It's only using **requests** !
## 👤 Author
👤 GitHub: [@**vodkarm**](https://github.com/vodkarm)
## 🤝 Contributing
Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/vodkarm/zebepy/issues).
## ❤ Show your support
Give a ⭐️ if this project helped you!
## 🤔 Creator message
Did in few hours, the code isn't perfect but it work ;)
