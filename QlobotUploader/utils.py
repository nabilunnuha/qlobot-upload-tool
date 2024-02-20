import os, json

def create_require():
    if not os.path.exists('data'):
        os.mkdir('data')
    if not os.path.exists('log'):
        os.mkdir('log')
    if not os.path.exists('akun.txt'):
        with open('akun.txt', 'w') as f:
            f.write('username|password|data_upload_start|data_upload_end|collection_id')
    if not os.path.exists('data/shopee_payload.json'):
        shopee = {"random_delay_per_akun":[15,25],"collection_id":None,"direct_upload_target":"shopee","data_upload":"selected","data_upload_start":None,"data_upload_end":None,"upload_mode":"human","browser_mode":"request","delay_start":120,"delay_end":210,"data_upload_checked":[],"watermark_thumbnail":False,"json_file":"","failed_pause":False,"skip_empty_stock":True,"direct_mode":"default","categories":[],"category_attributes":[],"use_category_mapping":True,"use_category_recomendation":True,"autofill_category_fields":True,"stock_start":10,"stock_end":20,"days_to_ship":2,"accounts":[{"username":None,"password":None}]}
        with open('data/shopee_payload.json','w') as f:
            json.dump(shopee, f, indent=2)
    if not os.path.exists('data/tokopedia_payload.json'):
        tokopedia = {"random_delay_per_akun":[15,25],"collection_id":None,"direct_upload_target":"tokopedia","data_upload":"selected","data_upload_start":None,"data_upload_end":None,"upload_mode":"human","browser_mode":"request","delay_start":120,"delay_end":210,"data_upload_checked":[],"watermark_thumbnail":False,"json_file":"","failed_pause":False,"skip_empty_stock":True,"direct_mode":"default","categories":[],"etalase_name":{},"etalase":"","use_category_mapping":True,"use_category_recomendation":True,"tersedia":1,"min_order":1,"stock_start":10,"stock_end":20,"min_order_follow":True,"wajib_asuransi":False,"preorder":False,"preorder_days":7,"mass_variant":False,"accounts":[{"username":None,"password":None}]}
        with open('data/tokopedia_payload.json','w') as f:
            json.dump(tokopedia, f, indent=2)