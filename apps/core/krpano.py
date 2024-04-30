import os
import shlex
import subprocess
import shutil
import logging

from django.conf import settings
from config.settings import env


KRPANO_BASE_DIR = settings.BASE_DIR / "krpano_tool"

KRPANO_SOURCE = env("KRPANO_SOURCE", default="/Users/elshod/Desktop/krpano-1.21.2/")

KRPANO_CUBE_CONFIG = os.path.join(KRPANO_SOURCE, "templates/vtour-multires.config")

KRPANO_TOOL = os.path.join(KRPANO_SOURCE, "krpanotools")

logger = logging.getLogger('krpano')


def _remove_folder(tile_path):
    shutil.rmtree(tile_path)


def _remove_file(image_path):
    os.remove(image_path)


def _call_subprocess(command):
    try:
        subprocess.run(command, check=True, timeout=60)
    except FileNotFoundError as exc:
        logger.exception(
            f"Command {command} failed because the process "
            f"could not be found.\n{exc}"
        )
    except subprocess.CalledProcessError as exc:
        logger.exception(
            f"Command {command} failed because the process "
            f"did not return a successful return code.\n{exc}"
        )
    except subprocess.TimeoutExpired as exc:
        logger.exception(f"Command {command} timed out.\n {exc}")


def make_pano(path, image):
    logger.debug("tiling cube")
    cube_command = "%s makepano -config=%s -panotype=sphere %s" % (KRPANO_TOOL, KRPANO_CUBE_CONFIG, image)
    _call_subprocess(shlex.split(cube_command))


def move_tiles(orig_path, des_path):
    shutil.move(orig_path, des_path)


def tile_full(image_path: str, old_image_path: str = None) -> None:
    image_path = str(settings.BASE_DIR) + image_path
    working_dir, orig_img_filename = os.path.split(image_path)
    pano_dir = working_dir + "/vtour/panos/" + orig_img_filename.split(".")[0] + ".tiles"
    vtour_dir = working_dir + "/vtour"
    try:
        make_pano(working_dir, image_path)
        move_tiles(pano_dir, working_dir)
    except Exception:
        logger.exception("tile caused exception")
        raise
    finally:
        try:
            _remove_folder(vtour_dir)
            if old_image_path:
                old_image_path = str(settings.BASE_DIR) + old_image_path
                old_image_tiles_dir = old_image_path.split(".")[0] + ".tiles"
                _remove_folder(old_image_tiles_dir)
                _remove_file(old_image_tiles_dir)
        except Exception:
            if os.path.isdir(vtour_dir):
                logging.exception("clean up work dir '%s' failed",
                                  vtour_dir)
