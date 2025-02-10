# -*- mode: python -*-

local_stub_flasher_path = "./.venv/Lib/site-packages/esptool/targets/stub_flasher"

added_files = [
    ("{}/1".format(local_stub_flasher_path), "./esptool/targets/stub_flasher/1"),
    ("{}/2".format(local_stub_flasher_path), "./esptool/targets/stub_flasher/2"),
    ("images", "images")
    ]

a = Analysis(['DIYFB-Firmware-Flasher.py'],
    binaries=[],
    datas=added_files,
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False
    )
pyz = PYZ(a.pure)
exe = EXE(pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='DIYFB-Firmware-Flasher',
    version='windows-version-info.txt',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    icon='images\\icon-256.ico',
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    )
