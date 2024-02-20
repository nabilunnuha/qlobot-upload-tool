import httpx, time, json, random
from .model import Account

class Upload:
    def __init__(self) -> None:
        self.url_collection = 'http://localhost:9918/api/collections/'
        self.url_direct = 'http://localhost:9918/api/tool/products_grabber_uploader/action/direct_upload'
        self.url_mapping = 'http://localhost:9918/api/tool/products_grabber_uploader/action/setmapping'
        self.headers = {
            'Connection':'keep-alive',
            'Content-Type':'application/json;charset=UTF-8'
        }
        self.timeout = 10
        self.client = httpx.Client()
        self.list_ids = []
        self.log = create_logger()
        
    def init_product(self) -> list:
        r = self.client.get(self.url_collection, headers=self.headers, timeout=self.timeout)
        r.raise_for_status()
        r = r.json()
        for col in r['data']:
            col_id = col['id']
            self.list_ids.append(col_id)
            r = self.client.get(self.url_collection + f'{col_id}', headers=self.headers, timeout=self.timeout)
            r = self.client.get(self.url_collection + f'getdata/{col_id}', headers=self.headers, timeout=self.timeout)
            r = self.client.get(self.url_mapping + f'?id={col_id}', headers=self.headers, timeout=self.timeout)
            time.sleep(3)
    
    def direct_upload(self, data: Account, payload: dict, num: int, lenght: int):
        try:
            if data.colect not in self.list_ids:
                raise ValueError('collection id not found')
            payload['collection_id'] = data.colect
            payload['data_upload_start'] = data.start
            payload['data_upload_end'] = data.end
            payload['accounts'][0]['username'] = data.username
            payload['accounts'][0]['password'] = data.password
            if 'random_delay_per_akun' in payload:
                del payload['random_delay_per_akun']
            dumps_payload = json.dumps(payload)
            r =  self.client.post(self.url_direct, headers=self.headers, data=dumps_payload).json()
            if r['success']:
                self.log.info(f'{data.username}: Success ( {num} / {lenght} )')
            else:
                status = r['message']
                self.log.error(f'{data.username}: {status} ( {num} / {lenght} )')
        except Exception as err:
            self.log.error(err)
    
    def run_upload(self, path_to_payload: str, path_to_account: str):
        with open(path_to_payload,'r') as f:
            payload: dict = json.load(f)
        start_delay = payload['random_delay_per_akun'][0]
        end_delay = payload['random_delay_per_akun'][1]
        with open(path_to_account, "r") as f:
            accounts_data = f.readlines()
            accounts = [tuple(acc.strip().split('|')) for acc in accounts_data if acc]
            account_instances = [Account(username=username, password=password, start=int(start), end=int(end), colect=int(colect))
                                    for username, password, start, end, colect in accounts]

        self.init_product()
        for start, account in enumerate(account_instances, start=1):
            self.direct_upload(account, payload, start, len(account_instances))
            time.sleep(random.randint(start_delay, end_delay))
    
from .logger import create_logger