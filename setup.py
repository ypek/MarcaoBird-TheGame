import cx_Freeze
executables = [cx_Freeze.Executable(
    script="flappy_update.py", icon="assets/marcaoIcon.ico")]

cx_Freeze.setup(
    name="MarcãoBird-TheGame",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": ["assets","sound","04B_19.ttf"]
                           }},
    executables=executables
)
