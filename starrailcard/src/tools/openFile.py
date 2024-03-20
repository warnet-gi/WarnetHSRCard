# Copyright 2023 DEViantUa <t.me/deviant_ua>
# All rights reserved.
from PIL import Image
import threading
from weakref import WeakValueDictionary
from pathlib import Path
import os


def determine_font_path_automatically(font_file='Times New Roman.ttf'):
    font_dirs = [
        '/usr/share/fonts',
        '/usr/local/share/fonts',
        '/Library/Fonts',
    ]

    for font_dir in font_dirs:
        font_path = os.path.join(font_dir, font_file)
        if os.path.isfile(font_path):
            return font_path

    return None


assets = Path(__file__).parent.parent / 'assets'
font = str(assets / 'font' / 'NotoSansKR-Bold.ttf')


async def change_font(x, genshin_font=False, comf=False, font_path=None):
    global font
    if font_path is None:
        if genshin_font:
            font = str(assets / 'font' / 'Genshin_Impact.ttf')
        elif comf:
            font = str(assets / 'font' / 'font_hsr.ttf')
        else:
            font = str(assets / 'font' / 'NotoSansKR-Bold.ttf')
    else:
        font_path = os.path.abspath(font_path)
        if os.path.isfile(font_path):
            font = font_path
        else:
            font_path = determine_font_path_automatically(font_path)
            if font_path is None:
                font = str(assets / 'font' / 'NotoSansKR-Bold.ttf')


mapping = {
    'total_bg': assets / 'bg' / 'bg.png',
    'bg_fire': assets / 'bg' / 'bg_fire.png',
    'bg_ice': assets / 'bg' / 'bg_ice.png',
    'bg_imaginary': assets / 'bg' / 'bg_imaginary.png',
    'bg_lightning': assets / 'bg' / 'bg_lightning.png',
    'bg_physical': assets / 'bg' / 'bg_physical.png',
    'bg_quantum': assets / 'bg' / 'bg_quantum.png',
    'bg_wind': assets / 'bg' / 'bg_wind.png',
    'bg_char_fire': assets / 'bg' / 'bg_char_fire.png',
    'bg_char_ice': assets / 'bg' / 'bg_char_ice.png',
    'bg_char_imaginary': assets / 'bg' / 'bg_char_imaginary.png',
    'bg_char_lightning': assets / 'bg' / 'bg_char_lightning.png',
    'bg_char_physical': assets / 'bg' / 'bg_char_physical.png',
    'bg_char_quantum': assets / 'bg' / 'bg_char_quantum.png',
    'bg_char_wind': assets / 'bg' / 'bg_char_wind.png',
    'frame_charters': assets / 'bg' / 'frame_charters.png',
    'mask_charters': assets / 'bg' / 'mask.png',
    'strs_1': assets / 'stars' / 'strs_1.png',
    'strs_2': assets / 'stars' / 'strs_2.png',
    'strs_3': assets / 'stars' / 'strs_3.png',
    'strs_4': assets / 'stars' / 'strs_4.png',
    'strs_5': assets / 'stars' / 'strs_5.png',
    'Closed': assets / 'const' / 'Closed.png',
    'Lock': assets / 'const' / 'Lock.png',
    'open': assets / 'const' / 'open.png',
    'bg_lc_total': assets / 'lc' / 'bg.png',
    'bg_lc': assets / 'lc' / 'bg_lc.png',
    'maska_lc': assets / 'lc' / 'maska.png',
    'logo': assets / 'LOGO.png',
    'uid': assets / 'UID.png',
    'STATS': assets / 'STATS.png',
    'ARTIFACT': assets / 'ARTIFACT.png',
    'bg_main': assets / 'Tallants' / 'bg_main.png',
    'bg_dop': assets / 'Tallants' / 'bg_dop.png',
    'bg_talants': assets / 'Tallants' / 'bg.png',
    'count_talants': assets / 'Tallants' / 'count.png',
    'dop_0': assets / 'Tallants' / 'dop_0.png',
    'dop_1': assets / 'Tallants' / 'dop_1.png',
    'dop_2': assets / 'Tallants' / 'dop_2.png',
    'dop_3': assets / 'Tallants' / 'dop_3.png',
    'sets_bg': assets / 'Sets' / 'bg.png',
    'sets_count': assets / 'Sets' / 'count.png',
    # TEAMPLE TWO
    "Knight": assets / 'teample_two_new' / 'path' / 'Knight.png',
    "Mage": assets / 'teample_two_new' / 'path' / 'Mage.png',
    "Priest": assets / 'teample_two_new' / 'path' / 'Priest.png',
    "Rogue": assets / 'teample_two_new' / 'path' / 'Rogue.png',
    "Shaman": assets / 'teample_two_new' / 'path' / 'Shaman.png',
    "Warlock": assets / 'teample_two_new' / 'path' / 'Warlock.png',
    "Warrior": assets / 'teample_two_new' / 'path' / 'Warrior.png',
    # TEAMPLE TREE
    "shadow_bg": assets / 'teample_tree' / 'bg' / 'shadow_bg.png',
    "splash_art": assets / 'teample_tree' / 'bg' / 'splash_art.png',
    "shadow_art": assets / 'teample_tree' / 'bg' / 'shadow_art.png',
    "art_frame": assets / 'teample_tree' / 'bg' / 'art_frame.png',
    "overlay": assets / 'teample_tree' / 'bg' / 'overlay.png',
    "lc_3_stars": assets / 'teample_tree' / 'lc' / '3_stars.png',
    "lc_4_stars": assets / 'teample_tree' / 'lc' / '4_stars.png',
    "lc_5_stars": assets / 'teample_tree' / 'lc' / '5_stars.png',
    "blink": assets / 'teample_tree' / 'lc' / 'blink.png',
    "lc_info": assets / 'teample_tree' / 'lc' / 'info.png',
    "closed_main": assets / 'teample_tree' / 'skills' / 'closed_main.png',
    "main_skills": assets / 'teample_tree' / 'skills' / 'main.png',
    "closed_trees": assets / 'teample_tree' / 'skills' / 'closed_trees.png',
    "count_tree": assets / 'teample_tree' / 'skills' / 'count_tree.png',
    "dop": assets / 'teample_tree' / 'skills' / 'dop.png',
    "open_trees": assets / 'teample_tree' / 'skills' / 'open_trees.png',
    "ON_const": assets / 'teample_tree' / 'const' / 'ON.png',
    "OFF_const": assets / 'teample_tree' / 'const' / 'OFF.png',
    "CLOSED_const": assets / 'teample_tree' / 'const' / 'CLOSED.png',
    "artifact_tree": assets / 'teample_tree' / 'artifact' / 'artifact.png',
    "sets_tree": assets / 'teample_tree' / 'artifact' / 'sets.png',
    "frame_art_1": assets / 'teample_tree' / 'artifact' / 'frame_art_1.png',
    "frame_art_2": assets / 'teample_tree' / 'artifact' / 'frame_art_2.png',
    "frame_art_3": assets / 'teample_tree' / 'artifact' / 'frame_art_3.png',
    "frame_art_4": assets / 'teample_tree' / 'artifact' / 'frame_art_4.png',
    "frame_art_5": assets / 'teample_tree' / 'artifact' / 'frame_art_5.png',
    "name_banners": assets / 'teample_tree' / 'name_banners.png',
    "stars_five": assets / 'teample_tree' / 'stars_five.png',
    "stars_four": assets / 'teample_tree' / 'stars_four.png',
    "icon": assets / "icon.png",
    "icon_maska": assets / "icon_maska.png",
    "seeleland": assets / "seeleland.png",
    "seeleland_v2": assets / "seeleland_v2.png",
    # TEAMPLE PROFILE
    "default_bg": assets / 'teample_profile' / "bg" / 'default_bg.png',
    "bg_shadow": assets / 'teample_profile' / "bg" / 'shadow.png',
    "name_frame": assets / 'teample_profile' / "bg" / 'name_frame.png',
    "total_bg_frame": assets / 'teample_profile' / "bg" / 'frame.png',
    "charter_icon_bg": assets / 'teample_profile' / "charters" / 'bg.png',
    "frame_stars_charters_4": assets / 'teample_profile' / "charters" / 'frame_stars_4.png',
    "frame_stars_charters_5": assets / 'teample_profile' / "charters" / 'frame_stars_5.png',
    "stats_frame_icon": assets / 'teample_profile' / "charters" / 'stats_frame_icon.png',
    "ups": assets / 'teample_profile' / "charters" / 'ups.png',
    "element_electro": assets / 'teample_profile' / "element" / 'electro.png',
    "element_fire": assets / 'teample_profile' / "element" / 'fire.png',
    "element_ice": assets / 'teample_profile' / "element" / 'ice.png',
    "element_IMAGINARY": assets / 'teample_profile' / "element" / 'IMAGINARY.png',
    "element_psyhical": assets / 'teample_profile' / "element" / 'psyhical.png',
    "element_quantom": assets / 'teample_profile' / "element" / 'quantom.png',
    "element_wind": assets / 'teample_profile' / "element" / 'wind.png',
    # TEAMPLE FOUR
    'ANEMO': assets / 'teample_enkcard' / 'background' / 'ANEMO2.png',
    'CRYO': assets / 'teample_enkcard' / 'background' / 'CRYO.png',
    'Electro': assets / 'teample_enkcard' / 'background' / 'Electro.png',
    'imaginary': assets / 'teample_enkcard' / 'background' / 'imaginary.png',
    'psyhical': assets / 'teample_enkcard' / 'background' / 'psyhical.png',
    'PYRO': assets / 'teample_enkcard' / 'background' / 'PYRO2.png',
    'quantom': assets / 'teample_enkcard' / 'background' / 'quantom.png',
    'CONST_CLOSED': assets / 'teample_enkcard' / 'const' / 'Closed.png',
    'CONST_CLOSED_LOCK': assets / 'teample_enkcard' / 'const' / 'Lock.png',
    'CONST_ANEMO': assets / 'teample_enkcard' / 'const' / 'const_wind.png',
    'CONST_CRYO': assets / 'teample_enkcard' / 'const' / 'const_ice.png',
    'CONST_Electro': assets / 'teample_enkcard' / 'const' / 'const_electro.png',
    'CONST_imaginary': assets / 'teample_enkcard' / 'const' / 'const_imaginary.png',
    'CONST_psyhical': assets / 'teample_enkcard' / 'const' / 'const_psyhical.png',
    'CONST_PYRO': assets / 'teample_enkcard' / 'const' / 'const_pyro.png',
    'CONST_quantom': assets / 'teample_enkcard' / 'const' / 'const_quantom.png',
    'maska_background': assets / 'teample_enkcard' / 'background' / 'maska.png',
    'shadow_enc': assets / 'teample_enkcard' / 'background' / 'shadow.png',
    'effect_soft': assets / 'teample_enkcard' / 'background' / 'soft.png',
    'effect_overlay': assets / 'teample_enkcard' / 'background' / 'overlay.png',
    'lc_frame': assets / 'teample_enkcard' / 'lc_frame.png',
    'strs_5_shadow': assets / 'teample_enkcard' / 'stars' / 'strs_5.png',
    'strs_4_shadow': assets / 'teample_enkcard' / 'stars' / 'strs_4.png',
    'strs_3_shadow': assets / 'teample_enkcard' / 'stars' / 'strs_3.png',
    'artifact_bg': assets / 'teample_enkcard' / 'artifact' / 'bg.png',
    'artifact_mask': assets / 'teample_enkcard' / 'artifact' / 'mask.png',
    'artifact_count': assets / 'teample_enkcard' / 'artifact' / 'count.png',
    'artifact_sets_count': assets / 'teample_enkcard' / 'artifact' / 'sets_count.png',
    'artifact_sets': assets / 'teample_enkcard' / 'artifact' / 'set.png',
    'talants_bg': assets / 'teample_enkcard' / 'talants' / 'bg.png',
    'talants_count': assets / 'teample_enkcard' / 'talants' / 'count.png',
    'dop_stats': assets / 'teample_enkcard' / 'talants' / 'dop_stats.png',
    'cryo_stats': assets / 'teample_enkcard' / 'talants' / 'cryo_stats.png',
    'electro_stats': assets / 'teample_enkcard' / 'talants' / 'electro_stats.png',
    'imaginari_stats': assets / 'teample_enkcard' / 'talants' / 'imaginari_stats.png',
    'psyhical_stats': assets / 'teample_enkcard' / 'talants' / 'psyhical_stats.png',
    'pyro_stats': assets / 'teample_enkcard' / 'talants' / 'pyro_stats.png',
    'quantom_stats': assets / 'teample_enkcard' / 'talants' / 'quantom_stats.png',
    'wind_stats': assets / 'teample_enkcard' / 'talants' / 'wind_stats.png',
    'stats_frame_enc': assets / 'teample_enkcard' / 'stats' / 'frame.png',
    'relic_total_bg': assets / 'relic' / 'total_bg.png',
    'relic_stats': assets / 'relic' / 'stats.png',
    'relic_1_stars': assets / 'relic' / '1_stars.png',
    'relic_2_stars': assets / 'relic' / '2_stars.png',
    'relic_3_stars': assets / 'relic' / '3_stars.png',
    'relic_4_stars': assets / 'relic' / '4_stars.png',
    'relic_5_stars': assets / 'relic' / '5_stars.png',
    # TEAMPLE FIVE
    'mask_bg_five': assets / 'teample_teams' / 'background' / 'mask.png',
    'shadow_bg_five': assets / 'teample_teams' / 'background' / 'shadow.png',
    'blink_bg_five': assets / 'teample_teams' / 'background' / 'blink.png',
    'stars_5_frame_up': assets / 'teample_teams' / 'background' / '5_stars_frame_up.png',
    'stars_5_frame': assets / 'teample_teams' / 'background' / '5_stars_frame.png',
    'stars_4_frame_up': assets / 'teample_teams' / 'background' / '4_stars_frame_up.png',
    'stars_4_frame': assets / 'teample_teams' / 'background' / '4_stars_frame.png',
    'total_cards_bg': assets / 'teample_teams' / 'background' / 'total_cards_bg.png',
    'shadow_3_lc': assets / 'teample_teams' / 'lk' / '3_shadow_lc.png',
    'star_3_frame': assets / 'teample_teams' / 'lk' / '3_star_frame.png',
    'star_3_frame_lc': assets / 'teample_teams' / 'lk' / '3_star_frame_lc.png',
    'shadow_4_lc': assets / 'teample_teams' / 'lk' / '4_shadow_lc.png',
    'star_4_frame': assets / 'teample_teams' / 'lk' / '4_star_frame.png',
    'star_4_frame_lc': assets / 'teample_teams' / 'lk' / '4_star_frame_lc.png',
    'shadow_5_lc': assets / 'teample_teams' / 'lk' / '5_shadow_lc.png',
    'star_5_frame': assets / 'teample_teams' / 'lk' / '5_star_frame.png',
    'star_5_frame_lc': assets / 'teample_teams' / 'lk' / '5_star_frame_lc.png',
    'blic_lc': assets / 'teample_teams' / 'lk' / 'blic.png',
    'frame_lc': assets / 'teample_teams' / 'lk' / 'frame_lc.png',
    'mask_lc_all': assets / 'teample_teams' / 'lk' / 'mask.png',
    'maska_lc_teams': assets / 'teample_teams' / 'lk' / 'maska_lc.png',
    'ranket': assets / 'teample_teams' / 'lk' / 'ranket.png',
    'stats_lc': assets / 'teample_teams' / 'lk' / 'stats.png',
    'def_bg': assets / 'teample_teams' / 'lk' / 'def_bg.png',
    'dark': assets / 'teample_teams' / 'lk' / 'dark.png',
    "stars_lc": assets / 'teample_teams' / 'lk' / 'stars.png',
    'const_five': assets / 'teample_teams' / 'const' / 'bg.png',
    'bg_dop_skills': assets / 'teample_teams' / 'skills' / 'bg_dop.png',
    'bg_dop_closed': assets / 'teample_teams' / 'skills' / 'closed.png',
    'stars_1_frame_relic': assets / 'teample_teams' / 'relic' / '1_stars.png',
    'stars_2_frame_relic': assets / 'teample_teams' / 'relic' / '2_stars.png',
    'stars_3_frame_relic': assets / 'teample_teams' / 'relic' / '3_stars.png',
    'stars_4_frame_relic': assets / 'teample_teams' / 'relic' / '4_stars.png',
    'stars_5_frame_relic': assets / 'teample_teams' / 'relic' / '5_stars.png',
    'shadow_frame_relic': assets / 'teample_teams' / 'relic' / 'shadow.png',
    'wind_five': assets / 'teample_teams' / 'background' / 'wind.png',
    'quantom_five': assets / 'teample_teams' / 'background' / 'quantom.png',
    'imaginary_five': assets / 'teample_teams' / 'background' / 'imaginary.png',
    'ice_five': assets / 'teample_teams' / 'background' / 'ice.png',
    'fire_five': assets / 'teample_teams' / 'background' / 'fire.png',
    'electro_five': assets / 'teample_teams' / 'background' / 'electro.png',
    'psyhical_five': assets / 'teample_teams' / 'background' / 'psyhical.png',
    'background_default': assets / 'teample_two_new' / 'background' / 'background_default.png',
    'background_line': assets / 'teample_two_new' / 'background' / 'line.png',
    'background_maska_art': assets / 'teample_two_new' / 'background' / 'maska_art.png',
    'background_maska_blur': assets / 'teample_two_new' / 'background' / 'maska_blur.png',
    'background_overlay': assets / 'teample_two_new' / 'background' / 'overlay.png',
    'background_shadow': assets / 'teample_two_new' / 'background' / 'shadow.png',
    'light_cone_frame': assets / 'teample_two_new' / 'light_cone' / 'frame.png',
    'light_cone_frame_five': assets / 'teample_two_new' / 'light_cone' / 'frame_five.png',
    'light_cone_frame_four': assets / 'teample_two_new' / 'light_cone' / 'frame_four.png',
    'light_cone_frame_three': assets / 'teample_two_new' / 'light_cone' / 'frame_three.png',
    'light_cone_stats': assets / 'teample_two_new' / 'light_cone' / 'stats.png',
    'light_cone_ups': assets / 'teample_two_new' / 'light_cone' / 'ups.png',
    'relic_backgroundl_score_line': assets
    / 'teample_two_new'
    / 'relic'
    / 'backgroundl_score_line.png',
    'relic_full_score_line': assets / 'teample_two_new' / 'relic' / 'full_score_line.png',
    'relic_count_sets': assets / 'teample_two_new' / 'relic' / 'count_sets.png',
    'relic_frame_line': assets / 'teample_two_new' / 'relic' / 'frame_line.png',
    'relic_line': assets / 'teample_two_new' / 'relic' / 'line.png',
    'relic_frame': assets / 'teample_two_new' / 'relic' / 'relic_frame.png',
    'relic_maska': assets / 'teample_two_new' / 'relic' / 'relic_maska.png',
    'relic_score_frame': assets / 'teample_two_new' / 'relic' / 'score_frame.png',
    'none_relic': assets / 'teample_two_new' / 'relic' / 'none_relic.png',
    'g_five': assets / 'teample_two_new' / 'stars' / 'g_five.png',
    'g_four': assets / 'teample_two_new' / 'stars' / 'g_four.png',
    'g_three': assets / 'teample_two_new' / 'stars' / 'g_three.png',
    'g_two': assets / 'teample_two_new' / 'stars' / 'g_two.png',
    'g_one': assets / 'teample_two_new' / 'stars' / 'g_one.png',
    'LOGO_WARNET': assets / 'teample_two_new' / 'LOGO.png',
    'path_count': assets / 'teample_two_new' / 'path' / 'count.png',
    'path_closed_main': assets / 'teample_two_new' / 'path' / 'closed_main.png',
    'path_closed_dop': assets / 'teample_two_new' / 'path' / 'closed_dop.png',
}


class ImageCache:
    def __init__(self):
        self.mapping = mapping
        self.cache = WeakValueDictionary()
        self.lock = threading.Lock()
        self.assets = assets

    def __dir__(self):
        return sorted(set([*globals(), *self.mapping]))

    def __getattr__(self, name):
        path = self.mapping.get(name)
        if not path:
            raise AttributeError(name)

        with self.lock:
            try:
                image = self.cache[name]
            except KeyError:
                self.cache[name] = image = Image.open(self.assets / path)

            return image
