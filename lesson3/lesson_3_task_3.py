from address import Address
from mailing import Mailing

to_address = Address('192256', 'Санкт-Петербург', 'пр-кт Стачек', '67', '18')
from_address = Address('184209', 'Апатиты', 'ул. Ленина', '17', '15')
mailing = Mailing(to_address, from_address, 660, 'CA123456789UA')

print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")