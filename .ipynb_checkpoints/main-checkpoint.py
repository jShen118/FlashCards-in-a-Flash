import quizletbot as qb
import model as m
from image_to_txt import screenshot_to_string as sts
import gui


#Hackathon123!
def main():
    gui.rungui()
    sts.main()
    
    #first user copy pastes into input.txt
    m.execute()
    cards = open('output.txt', 'r', encoding ='utf8').read()
    bot = qb.QuizletBot(cards)
    bot.login()
    bot.createFlashcards()

if __name__ == "__main__":
    main()









