import eospy.cleos
import pytz
import datetime as dt


# Example Only - Key should be secured
key = "5KAunQfsUCTrfy3cCdNyW5mMNnMSkH5EMP45oEjF2B6xKacoC3x"

ce = eospy.cleos.Cleos(url='https://jungle2.cryptolions.io')

arguments = {
            "buyer": "gyftieuser11",  
            "price_per_gft": "2.5000 EOS", 
            "gft_amount": '1.00000000 GFT', 
        }

payload = {
        "account": "gftorderboo1",
        "name": "limitbuygft",
        "authorization": [{
            "actor": "gyftieuser11",
            "permission": "active",
        }],
    }

#Converting payload to binary
data=ce.abi_json_to_bin(payload['account'],payload['name'],arguments)
payload['data']=data['binargs']
trx = {"actions": [payload]}
trx['expiration'] = str((dt.datetime.utcnow() + dt.timedelta(seconds=60)).replace(tzinfo=pytz.UTC))

resp = ce.push_transaction(trx, key, broadcast=True)
print('------------------------------------------------')
print(resp)
print('------------------------------------------------')
