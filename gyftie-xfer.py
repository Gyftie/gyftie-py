import eospy.cleos
import pytz
import datetime as dt

# Example Only - Key should be secured
key = "5KAunQfsUCTrfy3cCdNyW5mMNnMSkH5EMP45oEjF2B6xKacoC3x"

ce = eospy.cleos.Cleos(url='https://jungle2.cryptolions.io')

arguments = {
            "from": "gyftieuser11",  # sender
            "to": "gftorderboo1",  # receiver
            "quantity": '2.5000 EOS',  
            "memo": "memo",
        }
payload = {
        "account": "eosio.token",
        "name": "transfer",
        "authorization": [{
            "actor": "gyftieuser11",
            "permission": "active",
        }],
    }

data=ce.abi_json_to_bin(payload['account'],payload['name'],arguments)
payload['data']=data['binargs']

trx = {"actions": [payload]}
trx['expiration'] = str((dt.datetime.utcnow() + dt.timedelta(seconds=60)).replace(tzinfo=pytz.UTC))

resp = ce.push_transaction(trx, key, broadcast=True)
print('------------------------------------------------')
print(resp)
print('------------------------------------------------')
