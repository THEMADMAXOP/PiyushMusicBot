#
# Copyright (C) 2023-2024 by CoderXPiyush@Github, < https://github.com/CoderXPiyush >.
#
# This file is part of < https://github.com/CoderXPiyush/PiyushMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/CoderXPiyush/PiyushMusicBot/blob/master/LICENSE >
#
# All rights reserved.
#
#

import glob
from os.path import dirname, isfile


def __list_all_modules():
    work_dir = dirname(__file__)
    mod_paths = glob.glob(work_dir + "/*/*.py")

    all_modules = [
        (((f.replace(work_dir, "")).replace("/", "."))[:-3])
        for f in mod_paths
        if isfile(f)
        and f.endswith(".py")
        and not f.endswith("__init__.py")
    ]

    return all_modules


ALL_MODULES = sorted(__list_all_modules())
__all__ = ALL_MODULES + ["ALL_MODULES"]
