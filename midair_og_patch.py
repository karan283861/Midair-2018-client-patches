# Midair-OG client patcher
# For use with latest publically available Midair client via steam

import pymem
from pymem import Pymem

class Patch:
    def __init__(self, offset : int, instructions : list, size : int):
        self.offset = offset
        self.instructions = instructions
        self.bytes = bytes(instructions)
        self.size = size

class Process:
    def __init__(self, name : str):
        self.name = name
        self.pymem_instance = Pymem(name)
        self.id = self.pymem_instance.process_id
        self.base_address = pymem.process.base_module(self.pymem_instance.process_handle).lpBaseOfDll

    def PerformPatch(self, patch : Patch):
        print("Patching offset {0:x} with {1} ({2} bytes)".format(
            patch.offset, [hex(instruction) for instruction in patch.instructions], patch.size
            )
        )
        target_address = self.base_address + patch.offset
        self.pymem_instance.write_bytes(target_address, patch.bytes, len(patch.bytes))
        if patch.size > len(patch.bytes):
            nops = [OPCODE_NOP] * (patch.size - len(patch.bytes))
            self.pymem_instance.write_bytes(target_address + len(patch.bytes), bytes(nops), len(nops))

PROCESS_NAME = 'Midair-Win64-Test.exe'
GAME_PROCESS = Process(PROCESS_NAME)
OPCODE_NOP = 0x90

def PatchPredictCommand():
    # When predict is set to 0, players are drawn closest to their server position.
    # However, projectiles are now drawn when the server confirms them, thus causing them
    # to be drawn delayed.
    # The following patches allow using predict 0 AND having (Fake)projectiles drawn immediately,
    # with no syncing with the server projectile.

    print("Patching for PatchPredictCommand")

    patches = [
        Patch(0x026839e, [OPCODE_NOP], 2),
        Patch(0x2683a0, [OPCODE_NOP], 5),
        Patch(0x34014b, [OPCODE_NOP], 4),
        Patch(0x033e0d3, [OPCODE_NOP], 6),
        Patch(0x033e0d9, [OPCODE_NOP], 7),
        Patch(0x33e0ea, [OPCODE_NOP], 6),
        Patch(0x33e0fa, [OPCODE_NOP], 6),
        Patch(0x33e165, [0xEB, 0xA2], 7)
        ]

    for patch in patches:
        GAME_PROCESS.PerformPatch(patch)

    unstable_patches = [
        Patch(0x3400ba, [0x00], 1),
        Patch(0x342637, [OPCODE_NOP], 6)
        ]

    for patch in unstable_patches:
        GAME_PROCESS.PerformPatch(patch)

    print("Completed patching for PatchPredictCommand")

def __main__():
    PatchPredictCommand()

__main__()