import eospy.cleos
import pytz
import datetime as dt

# Example Only - Key should be secured
key = "5KAunQfsUCTrfy3cCdNyW5mMNnMSkH5EMP45oEjF2B6xKacoC3x"

ce = eospy.cleos.Cleos(url='https://jungle2.cryptolions.io')

arguments_xfer = {
            "from": "gyftieuser11",  # sender
            "to": "gftorderboo1",  # receiver
            "quantity": '1.00000000 GFT',  
            "memo": "memo",
        }

arguments_placeorder = {
            "buyer": "gyftieuser11",  
            "price_per_gft": "2.5000 EOS", 
            "gft_amount": '1.00000000 GFT'}

payload_xfer = {
        "account": "gyftietoke11",
        "name": "transfer",
        "authorization": [{
            "actor": "gyftieuser11",
            "permission": "active",
        }],
    }

payload_placeorder = {
        "account": "gftorderboo1",
        "name": "limitbuygft",
        "authorization": [{
            "actor": "gyftieuser11",
            "permission": "active",
        }],
    }

data_xfer=ce.abi_json_to_bin(payload_xfer['account'],payload_xfer['name'],arguments_xfer)
payload_xfer['data']=data_xfer['binargs']

data_placeorder=ce.abi_json_to_bin(payload_placeorder['account'],payload_placeorder['name'],arguments_placeorder)
payload_placeorder['data']=data_placeorder['binargs']

trx = {"actions": [payload_xfer,payload_placeorder]}
trx['expiration'] = str((dt.datetime.utcnow() + dt.timedelta(seconds=60)).replace(tzinfo=pytz.UTC))

resp = ce.push_transaction(trx, key, broadcast=True)
print('------------------------------------------------')
print(resp)
print('------------------------------------------------')
