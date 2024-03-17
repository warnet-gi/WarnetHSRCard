<p align="center">
 <img src="./documentation/StarRailCardM.png" alt="Баннер"/>
</p>

____

## StarRailCard

Module for generating Honkai Star Rail character cards

* Ability to generate with or without background.<br>
* Ability to set a custom image.<br>
* Flexible map settings.

## Api
>
> You can use the API to generate cards if you are using a different programming language.
[Documentation](https://github.com/DEViantUA/StarRailCard/wiki/StarRailCard-API)

## Installation

```
pip install starrailcard
```

## Launch

``` python
from starrailcard import honkaicard 
import asyncio

async def mains():
    async with honkaicard.MiHoMoCard(template=1) as hmhm:
        r = await hmhm.creat(700649319)
        print(r)

asyncio.run(mains())
```

<details>
<summary>Add image author</summary>

``` python
from starrailcard import honkaicard 
import asyncio

async def mains():
    async with honkaicard.MiHoMoCard(template=1) as hmhm:
        r = await hmhm.creat(700649319)
        for key in r.card:
            cards = await hmhm.add_author(link= "https://www.deviantart.com/dezzso", card= key.card)
            #cards.save(f"{key.id}.png") #A function to save an image with the author's stamp added.
        print(r)

asyncio.run(mains())
```

</details>

<details>
<summary>Create a profile card.</summary>

``` python
from starrailcard import honkaicard 
import asyncio

async def mains():
    async with honkaicard.MiHoMoCard(template=1) as hmhm:
        r = await hmhm.get_profile(700649319,  card = True)
        print(r)

asyncio.run(mains())
```

</details>

## Languages Supported

| Languege    |  Code   | Languege    |  Code   | Languege    |  Code   |
|-------------|---------|-------------|---------|-------------|---------|
|  English    |     en  |  русский    |     ru  |  Chinese    |    chs  |
|  Tiếng Việt |     vi  |  ไทย        |     th  | Taiwan     |    cht  |
|  português  |     pt  | 한국어      |     kr  | deutsch    |     de  |
|  日本語      |     jp  | 中文        |     zh  | español    |     es  |
|  中文        |     zh  | Indonesian |     id  | français   |     fr  |

<details>
<summary>Sample 1 template</summary>

[![Adaptation][3]][3]

[3]: ./documentation/a-18.png
  
</details>

<details>
<summary>Sample 2 template</summary>

[![Adaptation][4]][4]

[4]: ./documentation/a-27.png

</details>

<details>
<summary>Sample 3 template</summary>

[![Adaptation][2]][2]

[2]: ./documentation/a-21.png

</details>

<details>
<summary>Sample 4 template</summary>

[![Adaptation][5]][5]

[5]: ./documentation/a-25.png

</details>

<details>
<summary>Sample 5 template</summary>

[![Adaptation][6]][6]

[6]: ./documentation/a-26.png

</details>

<details>
<summary>Sample profile template</summary>

[![Adaptation][1]][1]

[1]: ./documentation/a-22.png

</details>

# Thank the author for the code

* **Patreon**: <https://www.patreon.com/deviantapi>
