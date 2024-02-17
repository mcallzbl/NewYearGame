# -*- mode: python ; coding: utf-8 -*-

import os

current_dir = os.getcwd()
block_cipher = None


a = Analysis(
    ['main.py'],
    pathex=[current_dir],
    binaries=[],
    datas=[('Resource/bgm', 'Resource/'), ('Resource/font1', 'Resource/'), ('Resource/font2', 'Resource/'),('scene.py','.'),('Resource/icon),'Resource/'],
    hiddenimports=['Controller'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='旅途乐章：春节版',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    onfile=True
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main',
)