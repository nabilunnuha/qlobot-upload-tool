from QlobotUploader.session_delete import SessionDel
import traceback
from QlobotUploader.utils import create_require

def main():
    try:
        create_require()
        target_input = str(input('target? shopee ( s / t ) tokopedia: ')).strip().lower()
        target = 'tokopedia' if target_input == 't' else 'shopee'
        s = SessionDel(target, [4, 7])
        s.run('akun.txt')
    except:
        traceback.print_exc()

if __name__ == '__main__':
    main()