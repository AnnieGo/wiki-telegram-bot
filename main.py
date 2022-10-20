#!/usr/bin/env python3
import wikipedia

wikipedia.set_lang("ru")

def wiki():
  while True:
    random_article = wikipedia.random()
    page = wikipedia.page(random_article)
    print(f"{random_article}")
    print(wikipedia.summary(random_article))
    print("Вы хотели бы прочитать эту статью? (да/нет). Чтобы закончить работу наберите стоп.")
    ans = input("").lower()
    if ans == "да":
        url = page.url
        print(url)
        break
    elif ans == "нет":
        print("Может быть другую?")
        continue
    elif ans == "стоп":
        print("Приходите еще!")
        continue
    else:
        print("Ошибка ввода")
        print("Вы хотели бы прочитать эту статью? (да/нет). Чтобы закончить работу наберите стоп.")
        ans = input("").lower()
        if ans == "да":
            url = page.url
            print(url)
            break

if __name__ == "__main__":
  try:
    wiki()
  except wikipedia.exceptions.DisambiguationError as e:
      print(e.options)
