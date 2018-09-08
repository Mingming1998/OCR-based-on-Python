from PyInstaller.__main__ import run
if __name__ == '__main__':
    opts = [r'C:\Users\123\PycharmProjects\untitled\imgRec.py',\
            '-D',r'--distpath=C:\Users\123\PycharmProjects\untitled',\
            r'--workpath=C:\Users\123\PycharmProjects\untitled',\
            r'--specpath=C:\Users\123\PycharmProjects\untitled',\
            r'--upx-dir','upx393w']
    run(opts)
