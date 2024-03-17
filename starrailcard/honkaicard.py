# Copyright 2023 DEViantUa <t.me/deviant_ua>
# All rights reserved.

from .src.tools import translation, pill, modal, openFile
from .src.generators import one, two, tree,four,five, author, profile, relics,two_new
from honkairail import starrailapi
import asyncio,re,os,datetime

def process_input(characterImgs, characterName,characterBackground):
    if characterImgs:
        if isinstance(characterImgs, dict):
            characterImgs = {key.lower(): value for key, value in characterImgs.items()}
        else:
            raise TypeError("The charterImg parameter must be a dictionary, where the key is the name of the character, and the parameter is an image.\nExample: charterImg = {'Himeko': 'img.png'} or {'Himeko': 'img.png', 'Seele': 'img2.jpg', ...}")

    if characterBackground:
        if isinstance(characterBackground, dict):
            characterBackground = {key.lower(): value for key, value in characterBackground.items()}
        else:
            raise TypeError("The characterBackground parameter must be a dictionary, where the key is the name of the character, and the parameter is an image.\nExample: charterImg = {'Himeko': 'img.png'} or {'Himeko': 'img.png', 'Seele': 'img2.jpg', ...}")

    
    if characterName:
        if isinstance(characterName, str):
            characterName = [name.strip().lower() for name in characterName.split(",")]
        else:
            raise TypeError("The name parameter must be a string, to pass multiple names, list them separated by commas.\nExample: name = 'Himeko' or name = 'Himeko, Seele',..")
    
    return characterImgs, characterName,characterBackground


def remove_html_tags(text):
    clean_text = re.sub('<.*?>', '', text)
    return clean_text


async def saveBanner(uid, res, name):
    data = datetime.datetime.now().strftime("%d_%m_%Y %H_%M")
    path = os.path.join(os.getcwd(), "RailCard", str(uid))
    os.makedirs(path, exist_ok=True)
    file_path = os.path.join(path, f"{name}_{data}.png")
    res.save(file_path)

class MiHoMoCard():
    def __init__(self,lang = "en", characterImgs = None, characterName = None, characterBackground = None, backgroundBlur = False, hide = False, save = False, background = True, template = 3, seeleland = False, font = None):

        """
        :param lang: str, What language to receive information supported:  en, ru, vi, th, pt, kr, jp, zh, id, fr, es, de, chs, cht.
        :param characterImgs: dict, Dictionary: {"Name_charter_1": "image link","Name_charter_2": "image link",...}.
        :param characterName: str, If we want to get certain characters: "Name_charter_1,Name_charter_1,Name_charter_1" Character names must be in the same language as in the lang parameter.
        :param hide: bool, Display UID.
        :param save: bool, Save images or not.
        :param background: bool, Generate image with or without background.
        :param seeleland: bool, Get information from the site: seeleland.com (Only for 3 patterns).
        :param font: str, Name or path to the font file to replace.

        """        
        self.font = font
        self.template = template
        self.backgroundBlur = backgroundBlur
        
        
        if not int(template) in [1,2,3,4,5]:
            self.template = 3

        if not lang in translation.supportLang:
            self.lang = "en"
        else:
            self.lang = lang
        
        self.translateLang = translation.Translator(lang)
        self.background = background
        
        try:
            self.characterImgs, self.characterName,self.characterBackground = process_input(characterImgs, characterName,characterBackground)
        except Exception as e:
            print(e.message)
            return

        self.API = starrailapi.StarRailApi(lang, v = 2)
        self.save = save
        self.hide = hide
        self.img = None
        self.characterBackgroundimg = None
        self.b = None
        self.seeleland = seeleland

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        pass
    
    async def get_characterBackgroundImg(self,name,ids):
        if name in self.characterBackground:
            self.characterBackgroundimg = await pill.get_user_image(self.characterBackground[name])
        else:
            self.characterBackgroundimg = None
        
        if ids in self.characterBackground:
            self.characterBackgroundimg = await pill.get_user_image(self.characterBackground[ids])
        
    async def characterImg(self,name,ids):
        if name in self.characterImgs:
            self.img = await pill.get_user_image(self.characterImgs[name])
        else:
            self.img = None
        
        if ids in self.characterImgs:
            self.img = await pill.get_user_image(self.characterImgs[ids])
    
    async def creat(self, uid):
        if self.font is None:
            if self.template == 4:
                await openFile.change_font(self.lang, genshin_font = True)
            elif self.template == 2:
                await openFile.change_font(self.lang, comf = True)
            else:
                await openFile.change_font(self.lang)
        else:
            await openFile.change_font(self.lang, font_path = self.font)
        task = []
        data = await self.API.get_full_data(uid)
        user = {
            "settings": {
                "uid": int(uid),
                "lang": self.lang,
                "hide": self.hide,
                "save": self.save,
                "background": self.background
            },
            "player": data.player,
            "card": [],
            "cards": None,
            "name": "",
            "id": "",
        }

        
        for key in data.characters:
            
            user["name"] += f"{key.name}, "
            user["id"] += f"{key.id}, "
            
            if self.characterName:
                if not key.name.lower() in self.characterName and not str(key.id) in self.characterName:
                    continue       

            if self.characterImgs:
                await self.characterImg(key.name.lower(), str(key.id))
            if self.characterBackground:
                await self.get_characterBackgroundImg(key.name.lower(), str(key.id))
            if self.template == 1:
                task.append(one.Creat(key, self.translateLang,self.img,self.hide,int(uid),remove_html_tags(data.player.nickname),self.background).start())
            elif self.template == 3:
                task.append(tree.Creat(key, self.translateLang,self.img,self.hide,int(uid),self.seeleland,self.characterBackgroundimg,self.backgroundBlur).start())
            elif self.template == 4:
                task.append(four.Creat(key, self.translateLang,self.img,self.hide,int(uid),self.seeleland).start())
            elif self.template == 5:
                task.append(five.Creat(key, self.translateLang, self.img).start())
            else:
                task.append(two_new.Creat(key, self.translateLang,self.img,self.hide,int(uid), self.seeleland).start())

        user["card"] = await asyncio.gather(*task)

        if self.template == 5:
            user["cards"] = await five.get_bg(self.background,user["card"])

        if self.save:
            if self.template == 5:
                await saveBanner(uid,user["cards"], "total")
            for keys in user["card"]:
                await saveBanner(uid,keys["card"], keys["name"])

        return modal.HSRCard(**user)
    
    async def get_profile(self, uid, banner = None, card = False):
        data = await self.API.get_full_data(uid)
        if not self.font is None:
            await openFile.change_font(self.lang, font_path = self.font)
            
        user = {
            "settings": {
                "uid": int(uid),
                "lang": self.lang,
                "hide": self.hide,
                "save": self.save,
                "background": self.background
            },
            "player": data.player,
            "card": None,
            "name": "",
            "id": "",
        }
        for key in data.characters:
            user["name"] += f"{key.name}, "
            user["id"] += f"{key.id}, "

        if card:
            if not banner is None:
                banner = await pill.get_user_image(banner)
            user["card"] = await profile.Creat(data, self.translateLang, banner, self.hide).start()
            

        return modal.HSRCard(**user)

    async def get_relic(self,uid,charter_id, position = None):
        """
        :param position: int, Relic position from 1 to 6.
        :param charter_id: int, The character ID of the relic to get.
        """
        if not position is None:
            if position < 1 and position > 6:
                raise TypeError("Argument: position expects a number between 1 and 6")

        await openFile.change_font(self.lang, genshin_font = True)

        result = {
            "uid": uid,
            "card": None,
            "charter_id": charter_id,
            "relic": [],
        }

        data = await self.API.get_full_data(uid)
        for character in data.characters:
            if int(character.id) == int(charter_id):
                if not position is None:
                    for z in character.relics:
                        if z.id[-1:] == str(position):
                            result["relic"] = [await relics.creat(z,character.id,position,name_charter= character.name)]
                else:
                    relic_tasks = [relics.creat(key,character.id,key.id[-1:], name_charter= character.name) for key in character.relics]
                    result["relic"] = await asyncio.gather(*relic_tasks)

        if not position is None:
            result["card"] = result["relic"][0].card
        else:
            positione = [
                (40,40),(593,40),
                (40,401),(593,401),
                (1146,40),(1146,401),
            ]

            card_bg = openFile.ImageCache().relic_total_bg.convert("RGBA")

            for key in result["relic"]:
                card_bg.alpha_composite(key.card, positione[key.position-1])
            
            result["card"] = card_bg

        return modal.StarRailRelic(**result)


    async def add_author(self, card, link = "", name = "", profile = False):
        """
        :param card: PILL.IMAGE, Generated card using the create function
        :param link: str, Specify the author through the link
        :param name: str, Specify the author through the text
        :param profile: bool, Is the card a profile card.
        """
        types = 0
        if link != "":
            try:
                _, text = await author.get_site_info(link)
                icon = await author.get_site_icon(link)
            except:
                url = link
                text = link
                icon = openFile.ImageCache().icon
                types = 1
        else:
            if name != "":
                text = name
                icon = openFile.ImageCache().icon
                types = 1
            else:
                raise TypeError("Specify one of the parameters: lang or name")

        author_icon = await author.start(text,icon,types)

        if profile:
            position = (510,0)
        else:
            if self.template == 1:
                position = (278,447)
            elif self.template == 2:
                position = (36,56)
            else:
                position = (1356,609)

        card.alpha_composite(author_icon,position)
        
        return card
            

class StarRaillScore:
    def __init__(self, chart_id, relic) -> None:
        """
        :param chart_id: int, Character id
        :param relic: class, the object you get from the method: get_relic()
        """
        
        if relic == []:
            raise TypeError("Doesn't accept lists. Only 1 relic")
        
        if not relic.position:
            raise TypeError("Pass an object of the RelicData class, you can get it using the method: get_relic()")
        
        self.relic = relic
        self.chart_id = chart_id

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        pass

    async def calculate(self):
        return await relics.creat(self.relic.relic,self.chart_id,self.relic.position)
