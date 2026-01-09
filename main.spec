# -*- mode: python ; coding: utf-8 -*-

py_files = [
    'config\\Config.py',
    'config\\RuntimeContext.py',
    'constant\\CommonConstants.py',
    'constant\\ConfigConstants.py',
    'constant\\DuelConstants.py',
    'constant\\YuGiOhSeries.py',
    'duel_module\\BaseDuel.py',
    'duel_module\\PasserDuel.py',
    'duel_module\\PortalDuel.py',
    'duel_module\\SpecialEventDuel.py',
    'gui\\YuGiOhGUI.py',
    'service\\EventDispatcherService.py',
    'util\\ClickUtils.py',
    'util\\CommonUtils.py',
    'util\\DuelUtils.py',
    'util\\EventUtils.py',
    'main.py'
]

a = Analysis(
    py_files,
    pathex=['K:\\DevProjects\\python workspace\\yugioh_auto_duel\\yugioh_auto_duel'],
    binaries=[],
    datas=None,
    hiddenimports=[],
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
    name='DL决斗助手',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
