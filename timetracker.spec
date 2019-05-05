# -*- mode: python -*-

block_cipher = None


a = Analysis(['timetracker/__main__.py'],
             pathex=['/home/travis/PycharmProjects/timetracker'],
             binaries=[],
             datas=[],
             hiddenimports=[
                'sqlalchemy',
                'flask',
                'flask_table',
                'psycopg2-binary',
                'pymysql',
                'mysqlclient',
                'pymssql'
             ],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='timetracker',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True)
