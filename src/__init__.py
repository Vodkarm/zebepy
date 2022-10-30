import requests, json

class Zebedee():
    class Wallet():
        def Details(key):
            r = requests.get("https://api.zebedee.io/v0/wallet", headers={"Content-Type": "application/json", "apikey": key})
            if "Invalid authentication credentials" in r.text:
                raise ValueError("(401) InvalidAuthenticationKey: Can't login to this wallet")
            else:
                return r.text

    class Charges():
        def Create(expi, am, desc, intid, cback, key):
            r = requests.post("https://api.zebedee.io/v0/charges", data=json.dumps({"expiresIn": int(expi), "amount": am, "description": desc, "internalId": intid, "callbackUrl": cback}), headers={"Content-Type": "application/json", "apikey": key})
            if "must be greater" in r.text:
                raise ValueError("(400) InvalidAmount: The amount (in millisatoshis) must be greater than 1 sat")
            elif "Charge expiration is" in r.text:
                raise ValueError("(400) InvalidExp: Expiration is limited, must be into 30 and 432000 seconds")
            elif "Error creating charge." in r.text:
                raise ValueError("(500) ChargeError: Can't create this charge")
            elif "Invalid authentication credentials" in r.text:
                raise ValueError("(401) InvalidAuthenticationKey: Can't login to this wallet")
            else:
                return r.text
        def GetAll(key):
            r = requests.get("https://api.zebedee.io/v0/charges", headers={"Content-Type": "application/json", "apikey": key})
            if "Invalid authentication credentials" in r.text:
                raise ValueError("(401) InvalidAuthenticationKey: Can't login to this wallet")
            else:
                return r.text
        def FromId(id, key):
            r = requests.get(f"https://api.zebedee.io/v0/charges/{id}", headers={"Content-Type": "application/json", "apikey": key})
            if "Invalid authentication credentials" in r.text:
                raise ValueError("(401) InvalidAuthenticationKey: Can't login to this wallet")
            elif "No Charge records" in r.text:
                raise ValueError("(404) ChargeNotFound: Cannot find any charge with the provided id")
            else:
                return r.text

    class Withdrawal():

        def Request(expi, am, desc, intid, cback, key):
            r = requests.post("https://api.zebedee.io/v0/withdrawal-requests", data=json.dumps({"expiresIn": int(expi), "amount": am, "description": desc, "internalId": intid, "callbackUrl": cback}), headers={"Content-Type": "application/json", "apikey": key})
            if "minimum Withdrawal amount supported" in r.text:
                raise ValueError("(400) InvalidAmount: The amount (in millisatoshis) must be greater than 10 sats")
            elif "Charge expiration is" in r.text:
                raise ValueError("(400) InvalidExp: Expiration is limited, must be into 30 and 432000 seconds")
            elif "Error creating charge." in r.text:
                raise ValueError("(500) WithdrawalError: Can't do that")
            elif "enough funds for" in r.text:
                raise ValueError("(400) LowBalance: You don't have enough funds for this transaction")
            elif "Invalid authentication credentials" in r.text:
                raise ValueError("(401) InvalidAuthenticationKey: Can't login to this wallet")
            else:
                return r.text
        def GetAll(key):
            r = requests.get("https://api.zebedee.io/v0/withdrawal-requests", headers={"Content-Type": "application/json", "apikey": key})
            if "Invalid authentication credentials" in r.text:
                raise ValueError("(401) InvalidAuthenticationKey: Can't login to this wallet")
            else:
                return r.text
        def FromId(id, key):
            r = requests.get(f"https://api.zebedee.io/v0/withdrawal-requests/{id}", headers={"Content-Type": "application/json", "apikey": key})
            if "Invalid authentication credentials" in r.text:
                raise ValueError("(401) InvalidAuthenticationKey: Can't login to this wallet")
            elif "No Charge records" in r.text:
                raise ValueError("(404) ChargeNotFound: Cannot find any withdrawal request with the provided id")
            else:
                return r.text

    class Payements():
        def Pay(desc, intid, inv, key):
            r = requests.post("https://api.zebedee.io/v0/payements", data=json.dumps({"description": desc, "internalId": intid, "invoice": inv}), headers={"Content-Type": "application/json", "apikey": key})
            if "enough funds for" in r.text:
                raise ValueError("(400) LowBalance: You don't have enough funds for this transaction")
            elif "Invalid authentication credentials" in r.text:
                raise ValueError("(401) InvalidAuthenticationKey: Can't login to this wallet")
            else:
                return r.text
        def GetAll(key):
            r = requests.get("https://api.zebedee.io/v0/payements", headers={"Content-Type": "application/json", "apikey": key})
            if "Invalid authentication credentials" in r.text:
                raise ValueError("(401) InvalidAuthenticationKey: Can't login to this wallet")
            else:
                return r.text
        def FromId(id, key):
            r = requests.get(f"https://api.zebedee.io/v0/payements/{id}", headers={"Content-Type": "application/json", "apikey": key})
            if "Invalid authentication credentials" in r.text:
                raise ValueError("(401) InvalidAuthenticationKey: Can't login to this wallet")
            elif "No Charge records" in r.text:
                raise ValueError("(404) ChargeNotFound: Cannot find any charge with the provided id")
            else:
                return r.text
                
    class Adress():
        def Send(adress, amount, comment, key):
            r = requests.post("https://api.zebedee.io/v0/ln-address/send-payment", data=json.dumps({"lnAdress": adress, "amount": amount, "comment": comment}), headers={"Content-Type": "application/json", "apikey": key})
            if "enough funds for" in r.text:
                raise ValueError("(400) LowBalance: You don't have enough funds for this transaction")
            elif "Invalid authentication credentials" in r.text:
                raise ValueError("(401) InvalidAuthenticationKey: Can't login to this wallet")
            elif "Could not generate invoice" in r.text:
                raise ValueError("(400) CouldNotGen: Could not generate invoice (The entered adress could be invalid)")
            else:
                return r.text
        def Fetch(adress, amount, comment, key):
            r = requests.post("https://api.zebedee.io/v0/ln-address/fetch-charge", data=json.dumps({"lnAdress": adress, "amount": amount, "comment": comment}), headers={"Content-Type": "application/json", "apikey": key})
            if "Missing parameters" in r.text:
                raise ValueError("(400) BadRequest: Missing paramters")
            elif "Min sendable" in r.text:
                raise ValueError("(400) InvalidAmount: Minimal is 10000 millisatoshis")
            elif "Could not generate" in r.text:
                raise ValueError("(400) InvalidArgs: Could not generate invoice")
            else:
                return r.text
        def Validate(adress, key):
            r = requests.get(f"https://api.zebedee.io/v0/ln-address/validate/{adress}", headers={"Content-Type": "application/json", "apikey": key})
            if "Invalid authentication credentials" in r.text:
                raise ValueError("(401) InvalidAuthenticationKey: Can't login to this wallet")
            else:
                return r.text

    class Gamertag():
        def Send(gamertag, amount, desc, key):
            r = requests.post("https://api.zebedee.io/v0/gamertag/send-payment", data=json.dumps({"gamertag": gamertag, "amount": amount, "description": desc}), headers={"Content-Type": "application/json", "apikey": key})
            if "enough funds for" in r.text:
                raise ValueError("(400) LowBalance: You don't have enough funds for this transaction")
            elif "Invalid authentication credentials" in r.text:
                raise ValueError("(401) InvalidAuthenticationKey: Can't login to this wallet")
            elif "Could not generate invoice" in r.text:
                raise ValueError("(400) CantSend: Could not send the payement")
            else:
                return r.text
        def FetchDetailsById(id, key):
            r = requests.get(f"https://api.zebedee.io/v0/gamertag/transaction/{id}", headers={"Content-Type": "application/json", "apikey": key})
            if "Invalid authentication credentials" in r.text:
                raise ValueError("(401) InvalidAuthenticationKey: Can't login to this wallet")
            else:
                return r.text
        def FetchById(id, key):
            r = requests.get(f"https://api.zebedee.io/v0/gamertag/user-id/{id}", headers={"Content-Type": "application/json", "apikey": key})
            if "Invalid authentication credentials" in r.text:
                raise ValueError("(401) InvalidAuthenticationKey: Can't login to this wallet")
            else:
                return r.text
        def FetchUserId(gamertag, key):
            r = requests.get(f"https://api.zebedee.io/v0/user-id/gamertag/{gamertag}", headers={"Content-Type": "application/json", "apikey": key})
            if "Invalid authentication credentials" in r.text:
                raise ValueError("(401) InvalidAuthenticationKey: Can't login to this wallet")
            else:
                return r.text
        def FetchCharge(gamertag, amount, desc, key):
            r = requests.post("https://api.zebedee.io/v0/gamertag/charges", data=json.dumps({"gamertag": gamertag, "amount": amount, "description": desc}), headers={"Content-Type": "application/json", "apikey": key})
            if "Invalid authentication credentials" in r.text:
                raise ValueError("(401) InvalidAuthenticationKey: Can't login to this wallet")
            else:
                return r.text

    class Utilities():
        def IsSupported(ip, key):
            r = requests.get(f"https://api.zebedee.io/v0/is-supported-region/{ip}", headers={"Content-Type": "application/json", "apikey": key})
            if "Invalid authentication credentials" in r.text:
                raise ValueError("(401) InvalidAuthenticationKey: Can't login to this wallet")
            else:
                return r.text
        def Prod(key):
            r = requests.get(f"https://api.zebedee.io/v0/prods-ip", headers={"Content-Type": "application/json", "apikey": key})
            if "Invalid authentication credentials" in r.text:
                raise ValueError("(401) InvalidAuthenticationKey: Can't login to this wallet")
            else:
                return r.text
        def ExchangeRate():
            r = requests.get(f"https://api.zebedee.io/v0/btcusd", headers={"Content-Type": "application/json"})
            return r.text
    # OAuth2 could be added soon.
    class Key():
        def Send(pubkey, amount, callback, key):
            r = requests.post("https://api.zebedee.io/v0/gamertag/send-payment", data=json.dumps({"amount": amount, "pubkey": pubkey, "tlv_records": [], "metadata": {}, "callbackUrl": callback}), headers={"Content-Type": "application/json", "apikey": key})
            if "enough funds for" in r.text:
                raise ValueError("(400) LowBalance: You don't have enough funds for this transaction")
            elif "Invalid authentication credentials" in r.text:
                raise ValueError("(401) InvalidAuthenticationKey: Can't login to this wallet")
            elif "Could not generate invoice" in r.text:
                raise ValueError("(400) CantSend: Could not send the payement")
            else:
                return r.text
