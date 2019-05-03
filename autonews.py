import time
import markov
import newspaper
import random
def title():
    print("         .8.       8 8888      88 8888888 8888888888 ,o888888o.               b.             8 8 8888888888 `8.`888b                 ,8' d888888o.  ")
    time.sleep(.5)
    print("        .888.      8 8888      88       8 8888    . 8888     `88.             888o.          8 8 8888        `8.`888b               ,8'.`8888:' `88.")
    time.sleep(.5)
    print("       :88888.     8 8888      88       8 8888   ,8 8888       `8b            Y88888o.       8 8 8888         `8.`888b             ,8' 8.`8888.   Y8")
    time.sleep(.5)
    print("      . `88888.    8 8888      88       8 8888   88 8888        `8b           .`Y888888o.    8 8 8888          `8.`888b     .b    ,8'  `8.`8888.    ")
    time.sleep(.5)
    print("     .8. `88888.   8 8888      88       8 8888   88 8888         88           8o. `Y888888o. 8 8 888888888888   `8.`888b    88b  ,8'    `8.`8888.   ")
    time.sleep(.5)
    print("    .8`8. `88888.  8 8888      88       8 8888   88 8888         88           8`Y8o. `Y88888o8 8 8888            `8.`888b .`888b,8'      `8.`8888.  ")
    time.sleep(.5)
    print("   .8' `8. `88888. 8 8888      88       8 8888   88 8888        ,8P           8   `Y8o. `Y8888 8 8888             `8.`888b8.`8888'        `8.`8888. ")
    time.sleep(.5)
    print("  .8'   `8. `88888.` 8888     ,8P       8 8888   `8 8888       ,8P            8      `Y8o. `Y8 8 8888              `8.`888`8.`88'     8b   `8.`8888.")
    time.sleep(.5)
    print(" .888888888. `88888. 8888   ,d8P        8 8888    ` 8888     ,88'             8         `Y8o.` 8 8888               `8.`8' `8,`'      `8b.  ;8.`8888")
    time.sleep(.5)
    print(".8'       `8. `88888. `Y88888P'         8 8888       `8888888P'               8            `Yo 8 888888888888        `8.`   `8'        `Y8888P ,88P'")
    time.sleep(.5)
    print()
    print('All your news in 150-300 words!')
def interface():
    title()
    print()
    choices={'1':('local.txt','https://kristv.com/'),'2':('r_estate.txt','https://realestate.usnews.com'),'3':('money.txt','https://money.usnews.com'),'4':('science.txt','https://www.sciencenews.org/'),'5':('sports.txt','http://www.espn.com/espn/latestnews'),'6':('health.txt','https://www.healthline.com'),'7':('obituaries.txt','https://www.nytimes.com/section/obituaries')}
    while True:
        print('What news would you like?')
        print('1. Local News')
        print('2. Real Estate')
        print('3. Money')
        print('4. Science')
        print('5. Sports')
        print('6. Health')
        print('7. Obituaries')
        print('X. Quit')
        choice=input('> ')
        if choice.lower()=='x':
                print()
                print('Thank you for using Auto-News')
                break
        elif choice in choices:
                create_article(choices[choice])
        else:
                print()
                print('Invalid choice, please try again')
                print()

def create_article(inputa):
        paper=newspaper.build(inputa[1],memoize_articles=False)
        text=''
        check=''
        title=''
        papers=[]
        i=0
        if inputa[0]=='sports.txt':
                while True:
                        choices=('nhl','nba','nfl','mlb')
                        print('Would you like NHL, NBA, NFL, or MLB news?')
                        choice=input('> ')
                        if choice.lower() in choices:
                                check=choice
                                break
                        else:
                                print()
                                print('Invalid input, please try again.')
                                print()
        if inputa[0]=='obituaries.txt':
                check='obituaries'
        print('Loading, please wait...')

        while len(papers)<=25:
                try:
                        if check in paper.articles[i].url:
                                paper.articles[i].download()
                                paper.articles[i].parse()
                                text+=paper.articles[i].text+' '
                                title+=paper.articles[i].title+' '
                                papers+=[paper.articles[i]]
                except Exception:
                        break
                i+=1
        with open('titles.txt',"w") as file:
                file.write(title)
        markov.markov('titles.txt','titles1.txt',random.randint(8,22))
        print()
        with open(inputa[0],"w",encoding='utf-8',errors='replace') as file:
                file.write(text.encode('utf-8','replace').decode('utf-8','replace'))
        markov.markov(inputa[0],inputa[0],random.randint(150,300))
        print()
        print(f'Continued on page {random.randint(1,1000000000)}')
        print()
        time.sleep(3)
interface()