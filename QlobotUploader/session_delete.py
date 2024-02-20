import httpx, time, random
from .model import Account

class SessionDel:
    def __init__(self, target: str, delay_beetween: list[int]) -> None:
        self.url_delete = 'http://localhost:9918/api/tool/delete_product/action/run'
        self.headers = {
            'Connection':'keep-alive',
            'Content-Type':'application/json;charset=UTF-8'
        }
        self.timeout = 10
        self.client = httpx.Client()
        self.list_ids = []
        self.log = create_logger()
        self.target = target
        self.delay_start = delay_beetween[0]
        self.delay_end = delay_beetween[1]
        
    def run_delete(self, data: Account, num: int, lenght: int):
        payload = {"delay_start":0,"delay_end":5,"target":self.target,"items":[{"username":data.username,"password":data.password,"keyword":"","data_count":1}]}
        r = self.client.post(self.url_delete, headers=self.headers, json=payload, timeout=self.timeout)
        r.raise_for_status()
        r = r.json()
        if r['success']:
            self.log.info(f'{data.username}: Success ( {num} / {lenght} )')
        else:
            self.log.error(f'{data.username}: Error ( {num} / {lenght} )')
            
    def run(self, path_to_account: str):
        with open(path_to_account, "r") as f:
            accounts_data = f.readlines()
            accounts = [tuple(acc.strip().split('|')) for acc in accounts_data if acc]
            account_instances = [Account(username=username, password=password, start=int(start), end=int(end), colect=int(colect))
                                    for username, password, start, end, colect in accounts]

        for num, acc in enumerate(account_instances, start=1):
            self.run_delete(acc, num, len(account_instances))
            time.sleep(random.randint(self.delay_start, self.delay_end))
        
from .logger import create_logger