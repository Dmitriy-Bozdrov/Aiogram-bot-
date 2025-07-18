MESSAGES = {
    "greeting": {
        "ru": "👋 Привет! Пожалуйста, выберите язык:",
        "ua": "👋 Вітаю! Будь ласка, оберіть мову:",
        "en": "👋 Hello! Please select a language:"
    },
    "choose_language": {
        "ru": "Пожалуйста, выберите язык:",
        "ua": "Будь ласка, оберіть мову:",
        "en": "Please select a language:"
    },
    "choose_action": {
        "ru": "Выберите действие:",
        "ua": "Оберіть дію:",
        "en": "Choose an action:"
    },
    "choose_currency": {
        "ru": "Выберите валюту:",
        "ua": "Оберіть валюту:",
        "en": "Choose currency:"
    },
    "enter_amount": {
        "ru": "Введите сумму:",
        "ua": "Введіть суму:",
        "en": "Enter the amount:"
    },
    "choose_city_branch": {
        "ru": "Выберите город и отделение:",
        "ua": "Оберіть місто та відділення:",
        "en": "Choose city and branch:"
    },
    "choose_time": {
        "ru": "Выберите удобное время визита:",
        "ua": "Оберіть зручний час візиту:",
        "en": "Choose a convenient visit time:"
    },
    "enter_name": {
        "ru": "Введите имя:",
        "ua": "Введіть ім'я:",
        "en": "Enter your name:"
    },
    "enter_phone": {
        "ru": "Введите номер телефона:",
        "ua": "Введіть номер телефону:",
        "en": "Enter your phone number:"
    },
    "cash_request_summary": {
        "ru": "Новая заявка на внесение наличных:\nВалюта: {currency}\nСумма: {amount}\nГород: {city}\nОтделение: {branch}\nВремя визита: {time}\nИмя клиента: {name}\nТелефон: {phone}\nTelegram: @{username}",
        "ua": "Нова заявка на внесення готівки:\nВалюта: {currency}\nСума: {amount}\nМісто: {city}\nВідділення: {branch}\nЧас візиту: {time}\nІм'я клієнта: {name}\nТелефон: {phone}\nTelegram: @{username}",
        "en": "New cash deposit request:\nCurrency: {currency}\nAmount: {amount}\nCity: {city}\nBranch: {branch}\nVisit time: {time}\nClient name: {name}\nPhone: {phone}\nTelegram: @{username}"
    },
    "cash_request_success": {
        "ru": "Спасибо! Менеджер свяжется с вами в ближайшее время для подтверждения и уточнения деталей.",
        "ua": "Дякуємо! Менеджер зв'яжеться з вами найближчим часом для підтвердження та уточнення деталей.",
        "en": "Thank you! A manager will contact you soon to confirm and clarify the details."
    },
    "choose_network": {
        "ru": "Выберите сеть для USDT:",
        "ua": "Оберіть мережу для USDT:",
        "en": "Choose network for USDT:"
    },
    "send_to_address": {
        "ru": "💳 Отправьте USDT на следующий адрес:\n\n`{wallet_address}`\n\n🌐 Сеть: {network}\n⚠️ Убедитесь, что выбрали правильную сеть!",
        "ua": "💳 Надішліть USDT на наступну адресу:\n\n`{wallet_address}`\n\n🌐 Мережа: {network}\n⚠️ Переконайтеся, що обрали правильну мережу!",
        "en": "💳 Send USDT to the following address:\n\n`{wallet_address}`\n\n🌐 Network: {network}\n⚠️ Make sure you selected the correct network!"
    },
    "address_error": {
        "ru": "⚠️ Ошибка получения адреса кошелька. Пожалуйста, попробуйте позже.",
        "ua": "⚠️ Помилка отримання адреси гаманця. Будь ласка, спробуйте пізніше.",
        "en": "⚠️ Error getting wallet address. Please try again later."
    },
    "enter_tx_hash": {
        "ru": "🔍 После отправки криптовалюты, пожалуйста, введите хеш транзакции:\n\n💡 Хеш транзакции можно найти в вашем кошельке или на сайте блокчейн-эксплорера",
        "ua": "🔍 Після відправки криптовалюти, будь ласка, введіть хеш транзакції:\n\n💡 Хеш транзакції можна знайти у вашому гаманці або на сайті блокчейн-експлорера",
        "en": "🔍 After sending cryptocurrency, please enter the transaction hash:\n\n💡 The transaction hash can be found in your wallet or on the blockchain explorer website."
    },
    "invalid_tx_hash": {
        "ru": "❌ Введите корректный хеш или ссылку на транзакцию.",
        "ua": "❌ Введіть коректний хеш або посилання на транзакцію.",
        "en": "❌ Enter a valid hash or transaction link."
    },
    "checking_tx": {
        "ru": "🔍 Проверяю транзакцию...\n⏳ Это может занять несколько секунд.",
        "ua": "🔍 Перевіряю транзакцію...\n⏳ Це може зайняти декілька секунд.",
        "en": "🔍 Checking transaction...\n⏳ This may take a few seconds."
    },
    "invalid_tx_format": {
        "ru": "❌ Неверный формат хеша транзакции. Попробуйте еще раз.",
        "ua": "❌ Невірний формат хеша транзакції. Спробуйте ще раз.",
        "en": "❌ Invalid transaction hash format. Try again."
    },
    "tx_confirmed": {
        "ru": "✅ Транзакция подтверждена!\n\n📊 Сумма: {amount}\n👤 От: {from_addr}\n📅 Время: {timestamp}\n\nТеперь укажите ваш контакт для связи (номер телефона или Telegram).",
        "ua": "✅ Транзакція підтверджена!\n\n📊 Сума: {amount}\n👤 Від: {from_addr}\n📅 Час: {timestamp}\n\nТепер вкажіть ваш контакт для зв'язку (номер телефону або Telegram).",
        "en": "✅ Transaction confirmed!\n\n📊 Amount: {amount}\n👤 From: {from_addr}\n📅 Time: {timestamp}\n\nNow provide your contact for communication (phone number or Telegram)."
    },
    "tx_not_confirmed": {
        "ru": "❌ Транзакция не подтверждена!\n\n🔍 Ошибка: {error}\n\nВозможные причины:\n• Транзакция еще не прошла\n• Неверный хеш транзакции\n• Транзакция отправлена на другой адрес\n• Проблемы с сетью\n\nПопробуйте еще раз или обратитесь в поддержку.",
        "ua": "❌ Транзакція не підтверджена!\n\n🔍 Помилка: {error}\n\nМожливі причини:\n• Транзакція ще не пройшла\n• Невірний хеш транзакції\n• Транзакція відправлена на іншу адресу\n• Проблеми з мережею\n\nСпробуйте ще раз або зверніться в підтримку.",
        "en": "❌ Transaction not confirmed!\n\n🔍 Error: {error}\n\nPossible reasons:\n• Transaction not yet processed\n• Invalid transaction hash\n• Transaction sent to another address\n• Network issues\n\nTry again or contact support."
    },
    "crypto_request_summary": {
        "ru": "Новая заявка на обмен USDT:\nВалюта: USDT\nСумма: {amount}\nСеть: {network}\nАдрес кошелька: {wallet_address}\nХеш транзакции: {tx_hash}\nКонтакт: {contact}\nTelegram: @{username}",
        "ua": "Нова заявка на обмін USDT:\nВалюта: USDT\nСума: {amount}\nМережа: {network}\nАдреса гаманця: {wallet_address}\nХеш транзакції: {tx_hash}\nКонтакт: {contact}\nTelegram: @{username}",
        "en": "New USDT exchange request:\nCurrency: USDT\nAmount: {amount}\nNetwork: {network}\nWallet address: {wallet_address}\nTransaction hash: {tx_hash}\nContact: {contact}\nTelegram: @{username}"
    },
    "crypto_request_success": {
        "ru": "✅ Заявка на обмен принята!\n\n{summary}\n\n📞 Оператор свяжется с вами в ближайшее время.\n⏰ Обычно это занимает 5-15 минут.",
        "ua": "✅ Заявка на обмін прийнята!\n\n{summary}\n\n📞 Оператор зв'яжеться з вами найближчим часом.\n⏰ Зазвичай це займає 5-15 хвилин.",
        "en": "✅ Exchange request accepted!\n\n{summary}\n\n📞 The operator will contact you soon.\n⏰ Usually it takes 5-15 minutes."
    },
    "back": {
        "ru": "🔙 Назад",
        "ua": "🔙 Назад",
        "en": "🔙 Back"
    },
    "cash_exchange": {
        "ru": "💵 Обмен наличных",
        "ua": "💵 Обмін готівки",
        "en": "💵 Cash exchange"
    },
    "crypto_exchange": {
        "ru": "💸 Обмен крипты",
        "ua": "💸 Обмін крипти",
        "en": "💸 Crypto exchange"
    },
    "invalid_action": {
        "ru": "Пожалуйста, выберите действие с помощью кнопок.",
        "ua": "Будь ласка, оберіть дію за допомогою кнопок.",
        "en": "Please choose an action using the buttons."
    },
    "invalid_currency": {
        "ru": "Пожалуйста, выберите валюту с помощью кнопок.",
        "ua": "Будь ласка, оберіть валюту за допомогою кнопок.",
        "en": "Please choose a currency using the buttons."
    },
    "invalid_network": {
        "ru": "Пожалуйста, выберите сеть с помощью кнопок.",
        "ua": "Будь ласка, оберіть мережу за допомогою кнопок.",
        "en": "Please choose a network using the buttons."
    },
    "invalid_time": {
        "ru": "Пожалуйста, выберите время с помощью кнопок.",
        "ua": "Будь ласка, оберіть час за допомогою кнопок.",
        "en": "Please choose a time using the buttons."
    },
    "invalid_city": {
        "ru": "Пожалуйста, выберите город с помощью кнопок.",
        "ua": "Будь ласка, оберіть місто за допомогою кнопок.",
        "en": "Please choose a city using the buttons."
    },
    "invalid_branch": {
        "ru": "Пожалуйста, выберите отделение с помощью кнопок.",
        "ua": "Будь ласка, оберіть відділення за допомогою кнопок.",
        "en": "Please choose a branch using the buttons."
    },
    "currency_rates_error": {
        "ru": "❌ Ошибка загрузки курсов.",
        "ua": "❌ Помилка завантаження курсів.",
        "en": "❌ Error loading rates."
    },
    "amount_info": {
        "ru": "📊 Сумма: {amount}\n\n⚠️ Актуальный курс недоступен.\nПредположим, вы получите ~XXX USD за {amount} монет.\nТочный расчет будет сделан оператором обменника.",
        "ua": "📊 Сума: {amount}\n\n⚠️ Актуальний курс недоступний.\nПрипустимо, ви отримаєте ~XXX USD за {amount} монет.\nТочний розрахунок зробить оператор обмінника.",
        "en": "📊 Amount: {amount}\n\n⚠️ Current rate unavailable.\nAssume you will get ~XXX USD for {amount} coins.\nThe exact calculation will be made by the operator."
    },
    "qr_caption": {
        "ru": "💳 Адрес получателя:\n`{address}`",
        "ua": "💳 Адреса отримувача:\n`{address}`",
        "en": "💳 Recipient address:\n`{address}`"
    },
    "start": {
        "ru": "Старт",
        "en": "Start",
        "ua": "Старт"
},
}

def get_message(key, lang="ru", **kwargs):
    text = MESSAGES.get(key, {}).get(lang)
    if not text:
        text = MESSAGES.get(key, {}).get("ru", "")
    return text.format(**kwargs) if kwargs else text
