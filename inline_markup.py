from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

#####################################################################################
main_menu = InlineKeyboardMarkup()

btnInfo = InlineKeyboardButton(text = "Прага🏙️@", callback_data = "main_info")
btnMetro = InlineKeyboardButton(text = "Метро🚇", callback_data = "metro")

main_menu.row(btnInfo, btnMetro)

btn1Day = InlineKeyboardButton(text = "1 день", callback_data = "first_day")
main_menu.row(btn1Day)

btn2Day = InlineKeyboardButton(text = "2 день", callback_data = "second_day")
main_menu.row(btn2Day)

btn3Day = InlineKeyboardButton(text = "3 день", callback_data = "third_day")
main_menu.row(btn3Day)

btnHome = InlineKeyboardButton(text = "Додому🏠", callback_data = "go_home")
main_menu.row(btnHome)

btnPlaces = InlineKeyboardMarkup(text = "Усі місця⛪🏰🏞️", callback_data = "all_places")
main_menu.row(btnPlaces)
#####################################################################################

places_keyboard = InlineKeyboardMarkup()

###########################################################################################

btnGrad = InlineKeyboardMarkup(text = "Пражський град", callback_data = "grad")
places_keyboard.row(btnGrad)

MenuGradLink = InlineKeyboardMarkup()
btnGradLink = InlineKeyboardButton(text = "В дорогу!", callback_data = "gradLink")
MenuGradLink.row(btnGradLink)

###########################################################################################

btnStareMisto = InlineKeyboardMarkup(text = "Старе місто", callback_data = "StareMisto")
places_keyboard.row(btnStareMisto)

MenuStareMistoLink = InlineKeyboardMarkup()
btnStareMistoLink = InlineKeyboardButton(text = "В дорогу!", callback_data = "StareMistoLink")
MenuStareMistoLink.row(btnStareMistoLink)

###########################################################################################

btnRatonda = InlineKeyboardMarkup(text = "Ротонда святого Вита", callback_data = "Ratonda")
places_keyboard.row(btnRatonda)

MenuRatondaLink = InlineKeyboardMarkup()
btnRatondaLink = InlineKeyboardButton(text = "В дорогу!", callback_data = "RatondaLink")
MenuRatondaLink.row(btnRatondaLink)

###########################################################################################

btnMalaStrana = InlineKeyboardMarkup(text = "Мала-Страна", callback_data = "MalaStrana")
places_keyboard.row(btnMalaStrana)

MenuMalaStranaLink = InlineKeyboardMarkup()
btnMalaStranaLink = InlineKeyboardButton(text = "В дорогу!", callback_data = "MalaStranaLink")
MenuMalaStranaLink.row(btnMalaStranaLink)

###########################################################################################

btnKvartal = InlineKeyboardMarkup(text = "Єврейський квартал", callback_data = "Kvartal")
places_keyboard.row(btnKvartal)

MenuKvartalLink = InlineKeyboardMarkup()
btnKvartalLink = InlineKeyboardButton(text = "В дорогу!", callback_data = "KvartalLink")
MenuKvartalLink.row(btnKvartalLink)

###########################################################################################

btnDim = InlineKeyboardMarkup(text = "Танцюючий дім", callback_data = "Dim")
places_keyboard.row(btnDim)

MenuDimLink = InlineKeyboardMarkup()
btnDimLink = InlineKeyboardButton(text = "В дорогу!", callback_data = "DimLink")
MenuDimLink.row(btnDimLink)

###########################################################################################

btnVesha = InlineKeyboardMarkup(text = "Порохова вежа", callback_data = "Vesha")
places_keyboard.row(btnVesha)

MenuVeshaLink = InlineKeyboardMarkup()
btnVeshaLink = InlineKeyboardButton(text = "В дорогу!", callback_data = "VeshaLink")
MenuVeshaLink.row(btnVeshaLink)

###########################################################################################

btnStarmPlosha = InlineKeyboardMarkup(text = "Староміська площа", callback_data = "StarmPlosha")
places_keyboard.row(btnStarmPlosha)

MenuStarmPloshaLink = InlineKeyboardMarkup()
btnStarmPloshaLink = InlineKeyboardButton(text = "В дорогу!", callback_data = "StarmPloshaLink")
MenuStarmPloshaLink.row(btnStarmPloshaLink)

###########################################################################################

btnKarlovMist = InlineKeyboardMarkup(text = "Карлов міст", callback_data = "KarlovMist")
places_keyboard.row(btnKarlovMist)

MenuKarlovMistLink = InlineKeyboardMarkup()
btnKarlovMistLink = InlineKeyboardButton(text = "В дорогу!", callback_data = "KarlovMistLink")
MenuKarlovMistLink.row(btnKarlovMistLink)

###########################################################################################

btnLoreta = InlineKeyboardMarkup(text = "Празька Лорета", callback_data = "Loreta")
places_keyboard.row(btnLoreta)

MenuLoretaLink = InlineKeyboardMarkup()
btnLoretaLink = InlineKeyboardButton(text = "В дорогу!", callback_data = "LoretaLink")
MenuLoretaLink.row(btnLoretaLink)

###########################################################################################

btnVatslavPlosha = InlineKeyboardMarkup(text = "Вацлавська площа", callback_data = "VatslavPlosha")
places_keyboard.row(btnVatslavPlosha)

MenuVatslavPloshaLink = InlineKeyboardMarkup()
btnVatslavPloshaLink = InlineKeyboardButton(text = "В дорогу!", callback_data = "VatslavPloshaLink")
MenuVatslavPloshaLink.row(btnVatslavPloshaLink)

###########################################################################################

btnNatsTeatr = InlineKeyboardMarkup(text = "Національний театр", callback_data = "NatsTeatr")
places_keyboard.row(btnNatsTeatr)

MenuNatsTeatrLink = InlineKeyboardMarkup()
btnNatsTeatrLink = InlineKeyboardButton(text = "В дорогу!", callback_data = "NatsTeatrLink")
MenuNatsTeatrLink.row(btnNatsTeatrLink)

###########################################################################################

btnStragMonast = InlineKeyboardMarkup(text = "Страгівський монастир", callback_data = "StragMonast")
places_keyboard.row(btnStragMonast)

MenuStragMonastLink = InlineKeyboardMarkup()
btnStragMonastLink = InlineKeyboardButton(text = "В дорогу!", callback_data = "StragMonastLink")
MenuStragMonastLink.row(btnStragMonastLink)

###########################################################################################

btnKorSad = InlineKeyboardMarkup(text = "Королівський сад", callback_data = "KorSad")
places_keyboard.row(btnKorSad)

MenuKorSadLink = InlineKeyboardMarkup()
btnKorSadLink = InlineKeyboardButton(text = "В дорогу!", callback_data = "KorSadLink")
MenuKorSadLink.row(btnKorSadLink)

###########################################################################################

btnNatsMuseum = InlineKeyboardMarkup(text = "Національний музей", callback_data = "NatsMuseum")
places_keyboard.row(btnNatsMuseum)

MenuNatsMuseumLink = InlineKeyboardMarkup()
btnNatsMuseumLink = InlineKeyboardButton(text = "В дорогу!", callback_data = "NatsMuseumLink")
MenuNatsMuseumLink.row(btnNatsMuseumLink)

###########################################################################################

btnRunok = InlineKeyboardMarkup(text = "Гавельський ринок", callback_data = "Runok")
places_keyboard.row(btnRunok)

MenuRunokLink = InlineKeyboardMarkup()
btnRunokLink = InlineKeyboardButton(text = "В дорогу!", callback_data = "RunokLink")
MenuRunokLink.row(btnRunokLink)

###########################################################################################

btnKuranti = InlineKeyboardMarkup(text = "Празькі куранти", callback_data = "Kuranti")
places_keyboard.row(btnKuranti)

MenuKurantiLink = InlineKeyboardMarkup()
btnKurantiLink = InlineKeyboardButton(text = "В дорогу!", callback_data = "KurantiLink")
MenuKurantiLink.row(btnKurantiLink)

###########################################################################################

MenuFirstDay = InlineKeyboardMarkup()
MenuFirstDay.row(btnKorSad)
MenuFirstDay.row(btnGrad)
MenuFirstDay.row(btnRatonda)
MenuFirstDay.row(btnLoreta)
MenuFirstDay.row(btnStragMonast)

MenuSecondDay = InlineKeyboardMarkup()
MenuSecondDay.row(btnKvartal)
MenuSecondDay.row(btnStareMisto)
MenuSecondDay.row(btnStarmPlosha)
MenuSecondDay.row(btnKuranti)
MenuSecondDay.row(btnRunok)
MenuSecondDay.row(btnVesha)

MenuThirdDay = InlineKeyboardMarkup()
MenuThirdDay.row(btnNatsMuseum)
MenuThirdDay.row(btnVatslavPlosha)
MenuThirdDay.row(btnDim)
MenuThirdDay.row(btnNatsTeatr)
MenuThirdDay.row(btnKarlovMist)
MenuThirdDay.row(btnMalaStrana)





