from pyfrotz.ovos import FrotzSkill
from pyfrotz.parsers import zork0_intro_parser


class Zork0Skill(FrotzSkill):
    def __init__(self, *args, **kwargs):
        # game is english only, apply bidirectional translation
        super().__init__(*args,
                         game_id="zork_0",
                         game_lang="en-us",
                         game_data=f'{self.root_dir}/res/{self.game_id}.z5',
                         intro_parser=zork0_intro_parser,
                         **kwargs)
