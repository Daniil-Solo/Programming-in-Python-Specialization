from engine import ObservableEngine
from observer import ShortNotificationPrinter, FullNotificationPrinter


if __name__ == "__main__":
    # Создание наблюдаемого движка и наблюдателей
    obs_engine = ObservableEngine()
    short1 = ShortNotificationPrinter()
    short2 = ShortNotificationPrinter()
    full1 = FullNotificationPrinter()
    full2 = FullNotificationPrinter()

    # Подписывание наблюдателей на уведомления от движка
    observers = [short1, short2, full1, full2]
    for observer in observers:
        obs_engine.subscribe(observer)

    # Посылаем уведомление
    print(1)
    achievement = {
        "title": "Покоритель",
        "text": "Дается при выполнении всех заданий в игре"
    }
    obs_engine.notify(achievement)

    # Отписываем некоторых наблюдателей
    obs_engine.unsubscribe(short1)
    obs_engine.unsubscribe(full1)

    # Посылаем уведомление
    print(2)
    achievement = {
        "title": "Наблюдатель",
        "text": "Дается при наблюдении за движком"
    }
    obs_engine.notify(achievement)

    # Смотрим содержимое
    print("all")
    for observer in observers:
        print(observer.achievements)
