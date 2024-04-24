# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['borderless_window.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
a.datas += [
	('nicolexd.png','C:\\Users\\jvgon\\Documents\\Programming\\Python\\borderless_window\\nicolexd.png', 'DATA'),
	('FACELESSGAMES.COM.BR_ACELERADO_BLZ.mp3','C:\\Users\\jvgon\\Documents\\Programming\\Python\\borderless_window\\FACELESSGAMES.COM.BR_ACELERADO_BLZ.mp3', 'DATA')]

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='borderless_window',
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
    icon=['mara.ico'],
)
