# -*- mode: python -*-

block_cipher = None

added_files = [
        ("images", "images"),
        ("{}/1".format(local_stub_flasher_path), "./esptool/targets/stub_flasher/1"),
        ("{}/2".format(local_stub_flasher_path), "./esptool/targets/stub_flasher/2")
   ]

imported_files = [
   ("wxpython.py"),
   ("pyserial")
]


a = Analysis(['DIYFB-Firmware-Flasher.py'],
             binaries=None,
             datas=added_files,
             hiddenimports=imported_files,
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
          debug=True,
          strip=False,
          upx=True,
          console=False , icon='images/icon-256.icns')
app = BUNDLE(exe,
             name='DIYFB-Firmware-Flasher.app',
             version='1.0.1',
             icon='./images/icon-256.icns',
             bundle_identifier='com.DeeEmm.DIYFB-Firmware-Flasher')
