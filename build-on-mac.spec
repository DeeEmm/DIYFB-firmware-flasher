# -*- mode: python -*-

block_cipher = None

a = Analysis(['DIYFB-Firmware-Flasher.py'],
             binaries=None,
             datas=[("images", "images")],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='DIYFB-Firmware-Flasher',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='images/icon-256.icns')
app = BUNDLE(exe,
             name='DIYFB-Firmware-Flasher.app',
             version='0.0.1',
             icon='./images/icon-256.icns',
             bundle_identifier='com.frightanic.DIYFB-Firmware-Flasher')
