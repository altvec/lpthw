# -*- coding: utf8 -*-
print "Ты вошел в темную комнату с двуму дверьми. Через какую дверь ты пройдешь?"
door = raw_input("> ")

if door == "1":
    print "За дверью стоит турникет, а рядом бородатый охранник. Что делать?"
    print "1. Приложить магнинтый пропуск к считывателю на турникете."
    print "2. Перепрыгнуть через турникет."
    print "3. Подождать, пока не появится кто-нибудь с пропуском и пройти вместе с ним."
    print "4. Развернуться и уйти."
    ans = raw_input("> ")

    if ans == "1":
        print "Ты прошел дальше и поднимаешься вверх по мокрой лестнице, подскальзываешься, падаешь вниз и ломаешь себе шею."
    elif ans == "2":
        print "Охранник ловит тебя, бьет дубинкой по голове и ты умираеешь."
    elif ans == "3":
        print "Охранник заметил твою попытку пройти без пропуска и отбил тебе почки. Ты умер мучительной смертью"
    elif ans == "4":
        print "Ты вышел на улицу, но неожиданно тебе на голову упал кирпич. Ты умер."
    else:
        print "Возможно %s было лучшим решением. Охранник пропустил тебя." % ans

elif door == "2":
    print "Происходит взрыв и ты умираешь."
