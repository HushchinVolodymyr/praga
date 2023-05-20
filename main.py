#import logging
import inline_markup

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InputMediaPhoto, InputFile
from token1 import TOKEN

#logging.basicConfig(level = logging.INFO)

bot = Bot(token = TOKEN)
dp = Dispatcher(bot)

##########################################################################################

@dp.callback_query_handler(text = "main_info")
async def main_info_func(message: types.Message):
    info_praga = [InputMediaPhoto(open('images/praga.jpg', 'rb'), "Пра́га (чеськ. Praha) — столиця та найбільше місто Чехії, адміністративний центр Середньочеського краю, а також двох його районів Прага-Захід та Прага-Схід. Прага розташована в західній частині Чехії, в історичній області Богемія.")]
    await bot.send_media_group(message.from_user.id, info_praga)

@dp.callback_query_handler(text = "go_home")
async def go_home_func(message: types.Message):
    go_home_link = "https://www.google.com/maps/dir//P%C5%99%C3%ADstavn%C3%AD+340%2F2,+170+00+Praha+7-Hole%C5%A1ovice,+%D0%A7%D0%B5%D1%85%D0%B8%D1%8F/@50.1038117,14.4477079,19.25z/data=!4m9!4m8!1m0!1m5!1m1!1s0x470b94b3e31081e9:0x7d416f7850e00f93!2m2!1d14.4474404!2d50.1040427!3e3"
    await bot.send_message(message.from_user.id, f"Ходімо до дому:\n {go_home_link}")

@dp.callback_query_handler(text = "metro")
async def metro_map_func(message: types.Message):
    metro_praga = [InputMediaPhoto(open('images/metromap.png', 'rb'), "Карта Пражського метро")]
    await bot.send_media_group(message.from_user.id, metro_praga)

@dp.callback_query_handler(text = "all_places")
async def all_places_func(message: types.Message):
    await bot.send_message(message.from_user.id, "Тут зібрані усі цікаві місця Праги, оберіть місце яке вас зацікавило!", reply_markup = inline_markup.places_keyboard)

#########################################################################################

@dp.callback_query_handler(text = "grad")
async def grad_func(message: types.Message):
    grad_info = [InputMediaPhoto(open('images/Places/grad.jpg','rb'), "Празький град (чеськ. Pražský hrad) — празька фортеця, традиційна резиденція чеських володарів, деяких імператорів Священної Римської імперії, з 1918 року резиденція президента республіки, спочатку Чехословацької, а з 1993 Чеської.\nПерша відома історії фортеця виникла на місці Празького граду в IX ст. Надалі град розширявся й добудовувався, доки не став одним із найбільших замкових комплексів у світі. Згідно з Книгою рекордів Гіннеса, маючи довжину 570 м і ширину 130 м, він є найбільшим замком у світі. Частиною комплексу є собор святого Віта — головний кафедральний собор Праги, в якому поховано багато видатних правителів Чехії, а також є гробниця святого Яна Непомуцького.")]
    await bot.send_media_group(message.from_user.id, grad_info)
    await bot.send_message(message.from_user.id, "Відправитись!", reply_markup = inline_markup.MenuGradLink)

@dp.callback_query_handler(text = "gradLink")
async def gradLink_func(message: types.Message):
    grad_link = "https://www.google.com/maps/dir//%D0%9F%D1%80%D0%B0%D0%B6%D1%81%D0%BA%D0%B8%D0%B9+%D0%93%D1%80%D0%B0%D0%B4,+Hrad%C4%8Dany,+119+08+Praha+1,+%D0%A7%D0%B5%D1%85%D0%B8%D1%8F/@49.9525145,17.1663309,6z/data=!3m1!4b1!4m10!4m9!1m1!4e1!1m5!1m1!1s0x470b951e6c24b7c3:0x2acf3c88af12259f!2m2!1d14.4016165!2d50.0910966!3e3"
    await bot.send_message(message.from_user.id, f"Ось дорога до Пражского града!\n {grad_link}")


@dp.callback_query_handler(text = "StareMisto")
async def StareMisto_func(message: types.Message):
    StareMisto_info = [InputMediaPhoto(open('images/Places/Stare-mesto.jpg','rb'), "Празьке Старе місто було відокремлено від решти поселення напівкруговим ровом і муром, з'єднаним із Влтавою на обох його кінцях. У теперішній час на місці рову пролягають вулиці (перераховуються з півночі на південний захід): Револучні (Revoluční), На Пршикопі (na Příkopě), та Національна (Národni), яка власне є офіційною межею кадастрового району Старе Мєсто. Зараз він розташований у міському районі Прага 1.\nПісля того, як Прага була розширена в XIV столітті за правління короля Карла IV, а са́ме — було засноване Нове Мєсто, невдовзі рів та мури Старого Мєста були демонтовані.\nВідомі місця празького Старого міста — Староміська площа з її Староміською ратушею й Празькими курантами, а також празьке гетто Йозефов (чеськ. Josefov) зі Староновою синагогою. Уздовж Влтави у Старому місті розташована Мала Страна (чеськ. Malá Strana). Ці дві частини поєднує Карлів міст. Йозефов розташований у північно-західній частині Старого міста (поблизу, але не доходячи до Влтави).")]
    await bot.send_media_group(message.from_user.id, StareMisto_info)
    await bot.send_message(message.from_user.id, "Відправитись!", reply_markup = inline_markup.MenuStareMistoLink)

@dp.callback_query_handler(text = "StareMistoLink")
async def StareMistoLink_func(message: types.Message):
    StareMisto_link = "https://www.google.com/maps/dir//%D0%A1%D1%82%D0%B0%D1%80%D0%B5-%D0%9C%D0%B5%D1%81%D1%82%D0%BE,+110+00+%D0%9F%D1%80%D0%B0%D0%B3%D0%B0+1,+%D0%A7%D0%B5%D1%85%D0%B8%D1%8F/@49.8919479,17.1810884,6z/data=!3m1!4b1!4m10!4m9!1m1!4e1!1m5!1m1!1s0x470b94e919e5d5e9:0x2600af105c20fb51!2m2!1d14.4211484!2d50.0876983!3e3"
    await bot.send_message(message.from_user.id, f"Ось дорога до Старого міста!\n {StareMisto_link}")


@dp.callback_query_handler(text = "Ratonda")
async def Ratonda_func(message: types.Message):
    Ratonda_info = [InputMediaPhoto(open('images/Places/Sobor-vita.jpg','rb'), "Собо́р свято́го Ві́та (чеськ. Katedrála svatého Víta, до 1997 року; повна сучасна офіційна назва: Катедра святого Віта, Вацлава і Войтеха / чеськ. Katedrála svatého Víta, Václava a Vojtěcha) — католицький храм, кафедральний собор, присвячений святому Віту, у столиці Чехії місті Празі; шедевр готичної та неоготичної архітектури, з яким тісно пов'язана історія міста та країни. Усипальниця королів Богемії, сховище коронаційних регалій.\nПразький собор святого Віта — це один з найвідоміших соборів у світі, видатний взірець культового будування, як за технічними характеристиками, так і за художнім рівнем, один із символів Праги.\nСобор розташований у Празькому Граді, є його невід'ємною складовою.")]
    await bot.send_media_group(message.from_user.id, Ratonda_info)
    await bot.send_message(message.from_user.id, "Відправитись!", reply_markup = inline_markup.MenuRatondaLink)

@dp.callback_query_handler(text = "RatondaLink")
async def RatondaLink_func(message: types.Message):
    Ratonda_link = "https://www.google.com/maps/dir//%D0%A0%D0%BE%D1%82%D0%BE%D0%BD%D0%B4%D0%B0+%D1%81%D0%B2%D1%8F%D1%82%D0%BE%D0%B3%D0%BE+%D0%92%D0%B8%D1%82%D0%B0,+III.+n%C3%A1dvo%C5%99%C3%AD+48%2F2,+119+01+Praha+1-Hrad%C4%8Dany,+%D0%A7%D0%B5%D1%85%D0%B8%D1%8F/@49.8919479,17.1678689,6z/data=!3m1!4b1!4m10!4m9!1m1!4e1!1m5!1m1!1s0x470b951e38024f5b:0x69ad3850f2d989a2!2m2!1d14.4005114!2d50.0908918!3e3"
    await bot.send_message(message.from_user.id, f"Ось дорога до Ротонди святого Віта!\n {Ratonda_link}")


@dp.callback_query_handler(text = "MalaStrana")
async def MalaStrana_func(message: types.Message):
    MalaStrana_info = [InputMediaPhoto(open('images/Places/Mala_strana.jpg','rb'), "Ма́ла Стра́на (чеськ. Malá Strana) — історичний район столиці Чехії міста Праги, це Празький малий град перед великим градом. Кадастровий район Мала Страна (адміністративно належить до Праги 1) розташований на лівому березі Влтави нижче Градчан, просто навпроти Старого Міста, з яким поєднаний Карловим мостом.\nВузькі середньовічні вулиці, площі й сади Малої Страни розташовані біля підніжжя двох пагорбів: пагорб, на якому стоїть Празький град, є природною північною межею району, з півдня такою границею є порослий деревами Петршин.\nНа Малій Страні розташовані площі — Малостранська (чеськ. Malostranské náměstí), Мальтійська (чеськ. Maltézské náměstí), Дражицького (чеськ. Dražického náměstí), Вальдштейна (чеськ. Valdštejnské náměstí), Велкопршеворська (чеськ. Velkopřevorské náměstí), місцини Кампа (чеськ. Kampa) і Кларов (чеськ. Klárov).\nПлоща Малої Страни становить 1,37 км², населення (станом на 16 жовтня 2006 року) — 6 445 осіб.")]
    await bot.send_media_group(message.from_user.id, MalaStrana_info)
    await bot.send_message(message.from_user.id, "Відправитись!", reply_markup = inline_markup.MenuMalaStranaLink)

@dp.callback_query_handler(text = "MalaStranaLink")
async def MalaStranaLink_func(message: types.Message):
    MalaStrana_link = "https://www.google.com/maps/dir//%D0%9C%D0%B0%D0%BB%D0%B0-%D0%A1%D1%82%D1%80%D0%B0%D0%BD%D0%B0,+%D0%9F%D1%80%D0%B0%D0%B3%D0%B0+1,+%D0%A7%D0%B5%D1%85%D0%B8%D1%8F/@49.8919479,17.1707446,6z/data=!3m1!4b1!4m10!4m9!1m1!4e1!1m5!1m1!1s0x470b94e3e8a99aff:0xc8f2b21d66118b88!2m2!1d14.4038934!2d50.0877053!3e3"
    await bot.send_message(message.from_user.id, f"Ось дорога до Мала страна!\n {MalaStrana_link}")


@dp.callback_query_handler(text = "Kvartal")
async def Kvartal_func(message: types.Message):
    Kvartal_info = [InputMediaPhoto(open('images/Places/Kvartal.jpg','rb'), "Йозефов (також Єврейський квартал; нім. Josefstadt) — міський квартал і найменша кадастрова територія Праги, Чехія, колишнє єврейське гетто міста. Він оточений Старим містом. Квартал часто представлений прапором єврейської громади Праги[en], жовтим Маґен Давидом (зіркою Давида) на червоному полі.")]
    await bot.send_media_group(message.from_user.id, Kvartal_info)
    await bot.send_message(message.from_user.id, "Відправитись!", reply_markup = inline_markup.MenuKvartalLink)

@dp.callback_query_handler(text = "KvartalLink")
async def KvartalLink_func(message: types.Message):
    Kvartal_link = "https://www.google.com/maps/dir//%D0%95%D0%B2%D1%80%D0%B5%D0%B9%D1%81%D0%BA%D0%B8%D0%B9+%D0%BA%D0%B2%D0%B0%D1%80%D1%82%D0%B0%D0%BB,+U+Star%C3%A9+%C5%A1koly,+110+00+Star%C3%A9+M%C4%9Bsto,+%D0%A7%D0%B5%D1%85%D0%B8%D1%8F/@49.8843445,17.1658023,6z/data=!3m1!4b1!4m10!4m9!1m1!4e1!1m5!1m1!1s0x470b94e9cbbce729:0x44008f074af9a449!2m2!1d14.4192259!2d50.0907915!3e3"
    await bot.send_message(message.from_user.id, f"Ось дорога до Єврейського кварталу!\n {Kvartal_link}")


@dp.callback_query_handler(text = "Dim")
async def Dim_func(message: types.Message):
    Dim_info = [InputMediaPhoto(open('images/Places/Dim.jpg','rb'), "«Танцюючий дім» (чеськ. Tančící dům) — деконструктивістська оригінальна адміністративно-офісна споруда неподалік на північній межі середмістя чеської столиці Праги, зведена Владо Милуничем і Френком Гері у 1992—96 роках.")]
    await bot.send_media_group(message.from_user.id, Dim_info)
    await bot.send_message(message.from_user.id, "Відправитись!", reply_markup = inline_markup.MenuDimLink)

@dp.callback_query_handler(text = "DimLink")
async def DimLink_func(message: types.Message):
    Dim_link = "https://www.google.com/maps/dir//%D0%A2%D0%B0%D0%BD%D1%86%D1%83%D1%8E%D1%89%D0%B8%D0%B9+%D0%B4%D0%BE%D0%BC,+Jir%C3%A1skovo+n%C3%A1m.+1981%2F6,+120+00+Nov%C3%A9+M%C4%9Bsto,+%D0%A7%D0%B5%D1%85%D0%B8%D1%8F/@49.8843445,17.1645627,6z/data=!3m1!4b1!4m10!4m9!1m1!4e1!1m5!1m1!1s0x470b94f6c2373f17:0x93016537050b3344!2m2!1d14.4140653!2d50.0754002!3e3"
    await bot.send_message(message.from_user.id, f"Ось дорога до Танцюючого дому!\n {Dim_link}")


@dp.callback_query_handler(text = "Vesha")
async def Vesha_func(message: types.Message):
    Vesha_info = [InputMediaPhoto(open('images/Places/Porohova.jpg','rb'), "Порохова́ Бра́ма (чеськ. Prašná brána) — вежа з брамою колишніх міських укріплень Праги, столиці Чехії, одна з найвідоміших празьких архітектурних пам'яток епохи пізньої готики. Знаходиться поблизу від площі Республіки. Заввишки 65 м, нагору ведуть кам'яні гвинтові сходи зі 186 сходинками. З її вершини відкривається чудовий вигляд на історичний центр Праги. Всередині вежі працює невелика музейна експозиція")]
    await bot.send_media_group(message.from_user.id, Vesha_info)
    await bot.send_message(message.from_user.id, "Відправитись!", reply_markup = inline_markup.MenuVeshaLink)

@dp.callback_query_handler(text = "VeshaLink")
async def VeshaLink_func(message: types.Message):
    Vesha_link = "https://www.google.com/maps/dir//%D0%9F%D0%BE%D1%80%D0%BE%D1%85%D0%BE%D0%B2%D0%B0%D1%8F+%D0%B1%D0%B0%D1%88%D0%BD%D1%8F,+N%C3%A1m.+Republiky+5,+110+00+Star%C3%A9+M%C4%9Bsto,+%D0%A7%D0%B5%D1%85%D0%B8%D1%8F/@49.8843445,17.1731736,6z/data=!3m1!4b1!4m10!4m9!1m1!4e1!1m5!1m1!1s0x470b94eb050ff205:0x9349b85fec4613a6!2m2!1d14.4278039!2d50.0873015!3e3"
    await bot.send_message(message.from_user.id, f"Ось дорога до Порохова вежа!\n {Vesha_link}")


@dp.callback_query_handler(text = "StarmPlosha")
async def StarmPlosha_func(message: types.Message):
    StarmPlosha_info = [InputMediaPhoto(open('images/Places/Star-plosha.jpg','rb'), "Староміська́ пло́ща або Ста́ромєстська пло́ща (чеськ. Staroměstské náměstí) — старовинна площа в середмісті столиці Чехії Празі — Старому Місті, багата на історико-архітектурні пам'ятки XIV—XIX століть. Загальна площа майдану становить близько 15 тисяч м².\nПлощу творять культові, громадські й житлові споруди XIV—XIX століть, архітектурні стилі яких варіюються від готики до бароко, ренесансу й рококо (останній — в окремих деталях будинкових фасадів та інтер'єрах), що робить вигляд майдану неповторним і легко впізнаваним.\nСтароміська площа оточена або від неї відходять такі празькі вулиці й майдани: Целетна вулиця (Celetná ulice), Паризький проспект (Pařížská třída), Довгий проспект (Dlouhá třída, Длугий проспект), Тинська вулиця (Týnská ulice), Мала площа (Malé náměstí), Залізна вулиця (Železná ulice), площа Франца Кафки (Náměstí Franze Kafky).\nНа Староміській площі — бруківка.\n")]
    await bot.send_media_group(message.from_user.id, StarmPlosha_info)
    await bot.send_message(message.from_user.id, "Відправитись!", reply_markup = inline_markup.MenuStarmPloshaLink)

@dp.callback_query_handler(text = "StarmPloshaLink")
async def StarmPloshaLink_func(message: types.Message):
    StarmPlosha_link = "https://www.google.com/maps/dir//%D0%A1%D1%82%D0%B0%D1%80%D0%BE%D0%BC%D0%B5%D1%81%D1%82%D1%81%D0%BA%D0%B0%D1%8F+%D0%BF%D0%BB%D0%BE%D1%89%D0%B0%D0%B4%D1%8C,+Starom%C4%9Bstsk%C3%A9+n%C3%A1m.,+110+00+Josefov,+%D0%A7%D0%B5%D1%85%D0%B8%D1%8F/@49.8843445,17.1698731,6z/data=!3m1!4b1!4m10!4m9!1m1!4e1!1m5!1m1!1s0x470b94e93451fa21:0x97ef2407c21e72c4!2m2!1d14.4211875!2d50.0875692!3e3"
    await bot.send_message(message.from_user.id, f"Ось дорога до Староміська площа!\n {StarmPlosha_link}")


@dp.callback_query_handler(text = "KarlovMist")
async def KarlovMist_func(message: types.Message):
    KarlovMist_info = [InputMediaPhoto(open('images/Places/Mist.jpg','rb'), "Карлів міст (чеськ. Karlův most) є найстарішим мостом через річку Влтаву в столиці Чехії місті Празі і другим за давниною мостом у країні. У Чехії, він був історично четвертим зведеним кам'яним мостом.\nКарлів міст побудований з плит пісковика, його довжина — 520 м, а  ширина — 10 м. За понад шість століть свого існування міст був декілька разів суттєво ушкоджений повенями — у 1432, 1496, 1784 та 1890 роках.")]
    await bot.send_media_group(message.from_user.id, KarlovMist_info)
    await bot.send_message(message.from_user.id, "Відправитись!", reply_markup = inline_markup.MenuKarlovMistLink)

@dp.callback_query_handler(text = "KarlovMistLink")
async def KarlovMistLink_func(message: types.Message):
    KarlovMist_link = "https://www.google.com/maps/dir//%D0%9A%D0%B0%D1%80%D0%BB%D0%BE%D0%B2+%D0%BC%D0%BE%D1%81%D1%82,+Karl%C5%AFv+most,+110+00+Praha+1,+%D0%A7%D0%B5%D1%85%D0%B8%D1%8F/@50.0047691,22.4488104,6z/data=!3m1!4b1!4m10!4m9!1m1!4e1!1m5!1m1!1s0x470b94e5e58eb59f:0x75209738d1d3b126!2m2!1d14.4114366!2d50.0864771!3e3"
    await bot.send_message(message.from_user.id, f"Ось дорога до Карлов міст!\n {KarlovMist_link}")


@dp.callback_query_handler(text = "Loreta")
async def Loreta_func(message: types.Message):
    Loreta_info = [InputMediaPhoto(open('images/Places/Loreta.jpg','rb'), "Празька Лорета, або просто Лорета (чеськ. Pražská Loreta) — римо-католицький комплекс у Празі, центром якого є костел Різдва Господнього (чеськ. Kostel Narození Páně) і Лоретанська хата Діви Марії. Комплекс розташовується на східному боці Лоретанської площі, у празькому історичному районі Градчани.\nНазвана на честь італійського міста Лорето, куди за легендою, у ХІІІ ст., небесними силами була перенесена з Палестини хата Діви Марії, для порятунку її від сарацинів. Подібні комплекси, що мали назву «лоретанських», з відтворенням цієї хати, виникають згодом у різних містах католицької Європи. У XVII ст. Лоретанський комплекс виник і в Празі.")]
    await bot.send_media_group(message.from_user.id, Loreta_info)
    await bot.send_message(message.from_user.id, "Відправитись!", reply_markup = inline_markup.MenuLoretaLink)

@dp.callback_query_handler(text = "LoretaLink")
async def LoretaLink_func(message: types.Message):
    Loreta_link = "https://www.google.com/maps/dir//%D0%9F%D1%80%D0%B0%D0%B6%D1%81%D0%BA%D0%B0%D1%8F+%D0%9B%D0%BE%D1%80%D0%B5%D1%82%D0%B0,+Loret%C3%A1nsk%C3%A9+n%C3%A1m.+7,+118+00+Praha+1-Hrad%C4%8Dany,+%D0%A7%D0%B5%D1%85%D0%B8%D1%8F/@50.0047691,22.4386167,6z/data=!3m1!4b1!4m10!4m9!1m1!4e1!1m5!1m1!1s0x470b951bd1d89c0b:0x8222d4bd084a0951!2m2!1d14.39151!2d50.089239!3e3"
    await bot.send_message(message.from_user.id, f"Ось дорога до Празька Лорета!\n {Loreta_link}")


@dp.callback_query_handler(text = "VatslavPlosha")
async def VatslavPlosha_func(message: types.Message):
    VatslavPlosha_info = [InputMediaPhoto(open('images/Places/Vaclavska.jpg','rb'), "Ва́цлавська пло́ща (чеськ.Václavské náměstíфайл, площа святого Вацлава; розмовна вживана назва Вацлавак/чеськ. Václavák) — один із найвідоміших і найбільших міських майданів у світі, головний центр Нового Міста в Празі.\nВацлавська площа — місце багатьох історичних подій, традиційний майданчик для проведення демонстрацій, зборів та іншого виявлення громадянської позиції пражан і чехів, святкувань і народних гулянь тощо. Це торговельний і бізнесовий центр Праги (і Чехії), де розташовані офіси міжнародних компаній (наприклад, Škoda Holding), великі готелі, численні крамниці, ресторани та кав'ярні.\nПлоща названа на честь Святого Вацлава, князя Чеського, небесного заступника країни.")]
    await bot.send_media_group(message.from_user.id, VatslavPlosha_info)
    await bot.send_message(message.from_user.id, "Відправитись!", reply_markup = inline_markup.MenuVatslavPloshaLink)

@dp.callback_query_handler(text = "VatslavPloshaLink")
async def VatslavPloshaLink_func(message: types.Message):
    VatslavPlosha_link = "https://www.google.com/maps/dir//%D0%92%D0%B0%D1%86%D0%BB%D0%B0%D0%B2%D1%81%D0%BA%D0%B0%D1%8F+%D0%BF%D0%BB%D0%BE%D1%89%D0%B0%D0%B4%D1%8C,+%D0%9F%D1%80%D0%B0%D0%B3%D0%B0+1,+%D0%A7%D0%B5%D1%85%D0%B8%D1%8F/@50.0796893,14.4182997,14.5z/data=!4m10!4m9!1m1!4e1!1m5!1m1!1s0x470b94ed30d58c83:0x31bac9b91ab53afb!2m2!1d14.4279917!2d50.0810226!3e3"
    await bot.send_message(message.from_user.id, f"Ось дорога до Вацлавська площа!\n {VatslavPlosha_link}")


@dp.callback_query_handler(text = "NatsTeatr")
async def NatsTeatr_func(message: types.Message):
    NatsTeatr_info = [InputMediaPhoto(open('images/Places/Teatr.jpg','rb'), "Національний театр (чеськ. Národní divadlo) — головний театр Праги та Чехії, має у своєму складі чотири театральні сцени: власна сцена Національного театру, Державна опера, Становий театр та Нова сцена. Сучасна будівля театру з 1958 року має статус національної пам'ятки архітектури.")]
    await bot.send_media_group(message.from_user.id, NatsTeatr_info)
    await bot.send_message(message.from_user.id, "Відправитись!", reply_markup = inline_markup.MenuNatsTeatrLink)

@dp.callback_query_handler(text = "NatsTeatrLink")
async def NatsTeatrLink_func(message: types.Message):
    NatsTeatr_link = "https://www.google.com/maps/dir//%D0%9D%D0%B0%D1%86%D0%B8%D0%BE%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9+%D1%82%D0%B5%D0%B0%D1%82%D1%80,+N%C3%A1rodn%C3%AD+2,+110+00+Nov%C3%A9+M%C4%9Bsto,+%D0%A7%D0%B5%D1%85%D0%B8%D1%8F/@50.0807497,14.4116003,17.25z/data=!4m10!4m9!1m1!4e1!1m5!1m1!1s0x470b94e8bf53ab29:0x9df10604144e9bfe!2m2!1d14.4135196!2d50.081309!3e3"
    await bot.send_message(message.from_user.id, f"Ось дорога до Національний театр!\n {NatsTeatr_link}")


@dp.callback_query_handler(text = "StragMonast")
async def StragMonast_func(message: types.Message):
    StragMonast_info = [InputMediaPhoto(open('images/Places/Monastr.jpg','rb'), "Страговський монастир (чеськ. Královská kanonie premonstrátů na Strahově) — абатство католицького премонстрантського ордену на Страговському надвір'ї у празькому районі Градчани, неподалік від празького Граду.\nЗаснований у ХІІ ст. Сучасний, бароковий вигляд набув у XVII-XVIII ст. Назва монастиря пов'язана зі словом «сторожа» (варта). Страговський монастир відомий своєю бібліотекою і броварнями (Броварня Страговського монастиря). Монастирським пивом пригощають і зараз у декількох шинках біля монастирських мурів.")]
    await bot.send_media_group(message.from_user.id, StragMonast_info)
    await bot.send_message(message.from_user.id, "Відправитись!", reply_markup = inline_markup.MenuStragMonastLink)

@dp.callback_query_handler(text = "StragMonastLink")
async def StragMonastLink_func(message: types.Message):
    StragMonast_link = "https://www.google.com/maps/dir//%D0%A1%D1%82%D1%80%D0%B0%D0%B3%D0%BE%D0%B2%D1%81%D0%BA%D0%B8%D0%B9+%D0%BC%D0%BE%D0%BD%D0%B0%D1%81%D1%82%D1%8B%D1%80%D1%8C,+Strahovsk%C3%A9+n%C3%A1dvo%C5%99%C3%AD+1%2F132,+118+00+Praha+1-Strahov,+%D0%A7%D0%B5%D1%85%D0%B8%D1%8F/@50.0047691,22.4375896,6z/data=!3m1!4b1!4m10!4m9!1m1!4e1!1m5!1m1!1s0x470b936721e269bb:0xcf35623df3761af0!2m2!1d14.3892515!2d50.0861478!3e3"
    await bot.send_message(message.from_user.id, f"Ось дорога до Страгівський монастир!\n {StragMonast_link}")


@dp.callback_query_handler(text = "KorSad")
async def KorSad_func(message: types.Message):
    KorSad_info = [InputMediaPhoto(open('images/Places/Sad.jpg','rb'), "Королівський сад – сад біля Празького Граду у Градчанах у Празі. Площа 3,6 га. Відокремлений від Града Оленою яром. Заснований королем Фердинандом I у стилі ренесанс у 1534 році на місці середньовічних виноградників.\nСад призначався для розведення дерев, не типових Середньої Європи. Так у Празі з'явився каштан, клен, ліщина.")]
    await bot.send_media_group(message.from_user.id, KorSad_info)
    await bot.send_message(message.from_user.id, "Відправитись!", reply_markup = inline_markup.MenuKorSadLink)

@dp.callback_query_handler(text = "KorSadLink")
async def KorSadLink_func(message: types.Message):
    KorSad_link = "https://www.google.com/maps/dir//%D0%9A%D0%BE%D1%80%D0%BE%D0%BB%D0%B5%D0%B2%D1%81%D0%BA%D0%B8%D0%B9+%D1%81%D0%B0%D0%B4,+%D0%93%D1%80%D0%B0%D0%B4%D1%87%D0%B0%D0%BD%D1%8B,+%D0%9F%D1%80%D0%B0%D0%B3%D0%B0+1,+%D0%A7%D0%B5%D1%85%D0%B8%D1%8F/@50.0917237,14.3963385,15.75z/data=!4m10!4m9!1m1!4e1!1m5!1m1!1s0x470b951fedad1399:0x8184fc3e3e3b244!2m2!1d14.4019696!2d50.0932563!3e3"
    await bot.send_message(message.from_user.id, f"Ось дорога до Королівський сад!\n {KorSad_link}")


@dp.callback_query_handler(text = "NatsMuseum")
async def NatsMuseum_func(message: types.Message):
    NatsMuseum_info = [InputMediaPhoto(open('images/Places/museam.jpg','rb'), "Національний музей (чеськ. Národní muzeum) — найбільший і найстаріший державний музей у столиці Чехії місті Празі, головне й найбільше зібрання матеріалів з історії та культури Чехії.\nФактично Національний музей у Празі є об'єднанням низки музейних закладів, бібліотек, замків, окремих експозицій та виставок, а також приписаних до музеїв пам'ятників видатним чеським персоналіям, до того ж не тільки в Празі. Однак центральне місце в комплексі посідає головний корпус Національного музею — на Вацлавській площі.")]
    await bot.send_media_group(message.from_user.id, NatsMuseum_info)
    await bot.send_message(message.from_user.id, "Відправитись!", reply_markup = inline_markup.MenuNatsMuseumLink)

@dp.callback_query_handler(text = "NatsMuseumLink")
async def NatsMuseumLink_func(message: types.Message):
    NatsMuseum_link = "https://www.google.com/maps/dir//%D0%9D%D0%B0%D1%86%D0%B8%D0%BE%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9+%D0%BC%D1%83%D0%B7%D0%B5%D0%B9,+V%C3%A1clavsk%C3%A9+n%C3%A1m.+68,+110+00+Nov%C3%A9+M%C4%9Bsto,+%D0%A7%D0%B5%D1%85%D0%B8%D1%8F/@50.0047691,22.4635887,6z/data=!3m1!4b1!4m10!4m9!1m1!4e1!1m5!1m1!1s0x470b948d824eafb9:0x428e5a03743d49a6!2m2!1d14.4309369!2d50.0789704!3e3"
    await bot.send_message(message.from_user.id, f"Ось дорога до Національний музей!\n {NatsMuseum_link}")


@dp.callback_query_handler(text = "Runok")
async def Runok_func(message: types.Message):
    Runok_info = [InputMediaPhoto(open('images/Places/Rynok.jpg','rb'), "Вузька Гавельская вулиця, що веде від Староміської площі до Вацлавської, називається так, тому що впирається в костел Св. Галла або Гавлена. З 13 століття тут розташовується міський ринок, куди празькі домогосподарки регулярно навідувалися за продуктами для приготування шедеврів чеської кухні. Так склалося, що інші середньовічні міські ринки поступово закрилися, а цей уцілів.\nСьогодні асортимент товарів дещо інший. Як і раніше багато натуральних продуктів з фермерських господарств, але у вихідні дні переважають прилавки з богемським склом, шкіряними виробами ручної роботи, старовинними речами та сувенірами.")]
    await bot.send_media_group(message.from_user.id, Runok_info)
    await bot.send_message(message.from_user.id, "Відправитись!", reply_markup = inline_markup.MenuRunokLink)

@dp.callback_query_handler(text = "RunokLink")
async def RunokLink_func(message: types.Message):
    Runok_link = "https://www.google.com/maps/dir//Havelsk%C3%A9+tr%C5%BEi%C5%A1t%C4%9B,+Havelsk%C3%A1+13,+110+00+Star%C3%A9+M%C4%9Bsto,+%D0%A7%D0%B5%D1%85%D0%B8%D1%8F/@50.0842942,14.419977,18.5z/data=!4m10!4m9!1m1!4e1!1m5!1m1!1s0x470b94ee9047d2a7:0x611c95a9156c477c!2m2!1d14.4206386!2d50.0845528!3e3"
    await bot.send_message(message.from_user.id, f"Ось дорога до Гавельський ринок!\n {Runok_link}")


@dp.callback_query_handler(text = "Kuranti")
async def Kuranti_func(message: types.Message):
    Kuranti_info = [InputMediaPhoto(open('images/Places/Kuranti.jpg','rb'), "Пра́зькі кура́нти або Ста́роміський асторономічний годинник (чеськ. Staroměstský orloj) — астрономічний годинник у Празі, Чехія. Один із символів чеської столиці, одна з головних туристичних принад міста. Встановлений 1410 року в Старому Місті, на південному фасаді міської ратуші на Староміській площі.\nАстрономічний циферблат годинника є однією з форм механічної астролябії, пристрою, що використовується в середньовічній астрономії. Годинник показує роки, місяці, дні та години, час сходу і заходу Сонця, час сходу і заходу Місяця, а також положення знаків зодіаку.")]
    await bot.send_media_group(message.from_user.id, Kuranti_info)
    await bot.send_message(message.from_user.id, "Відправитись!", reply_markup = inline_markup.MenuKurantiLink)

@dp.callback_query_handler(text = "KurantiLink")
async def KurantiLink_func(message: types.Message):
    Kuranti_link = "https://www.google.com/maps/dir//%D0%9F%D1%80%D0%B0%D0%B6%D1%81%D0%BA%D0%B8%D0%B5+%D0%BA%D1%83%D1%80%D0%B0%D0%BD%D1%82%D1%8B,+Starom%C4%9Bstsk%C3%A9+n%C3%A1m.+1,+110+00+Josefov,+%D0%A7%D0%B5%D1%85%D0%B8%D1%8F/@50.0047691,22.4588432,6z/data=!3m1!4b1!4m10!4m9!1m1!4e1!1m5!1m1!1s0x470b94e939c02f49:0xf17b44b25aa20696!2m2!1d14.4207269!2d50.0869955!3e3"
    await bot.send_message(message.from_user.id, f"Ось дорога до Празькі куранти!\n {Kuranti_link}")
#########################################################################################

@dp.callback_query_handler(text = "first_day")
async def first_day_func(message: types.Message):
    first_day_info = [InputMediaPhoto(open('images/First_day/PraagGrad.jpg','rb'), "Перший день туру!1️⃣")]
    username = message.from_user.username
    await bot.send_media_group(message.from_user.id, first_day_info)
    await bot.send_message(message.from_user.id, f"Добрий день, {username}, сьогодні я пропоную відвідати такі місця!", reply_markup = inline_markup.MenuFirstDay)

@dp.callback_query_handler(text = "second_day")
async def second_day_func(message: types.Message):
    second_day_info = [InputMediaPhoto(open('images/Second_day/stare_misto.jpg','rb'), "Другий день туру!2️⃣")]
    username = message.from_user.username
    await bot.send_media_group(message.from_user.id, second_day_info)
    await bot.send_message(message.from_user.id, f"Добрий день, {username}, сьогодні я пропоную відвідати такі місця!", reply_markup = inline_markup.MenuSecondDay)


@dp.callback_query_handler(text = "third_day")
async def third_day_func(message: types.Message):
    third_day_info = [InputMediaPhoto(open('images/Third_day/Vltava_river.jpg','rb'), "Третій день туру!3️⃣")]
    username = message.from_user.username
    await bot.send_media_group(message.from_user.id, third_day_info)
    await bot.send_message(message.from_user.id, f"Добрий день, {username}, сьогодні я пропоную відвідати такі місця!", reply_markup = inline_markup.MenuThirdDay)

#########################################################################################
@dp.message_handler()
async def echo_answer(message: types.Message):
    username = message.from_user.username
    await message.answer(f"Привіт {username}, я спорбую допомогти вам у вашій подорожі по Празі)", reply_markup = inline_markup.main_menu)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)