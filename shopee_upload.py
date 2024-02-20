from QlobotUploader.upload import Upload
from QlobotUploader.utils import create_require

def main():
    create_require()
    up = Upload()
    up.run_upload('data/shopee_payload.json', 'akun.txt')
    
if __name__ == '__main__':
    main()