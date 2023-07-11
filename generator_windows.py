
# this is a program that generates random practice problems from HW and textbook

# need this
import random
import subprocess
import os
from os.path import expanduser

home = expanduser('~')
os.chdir(os.path.join(home, 'Desktop', 'PracticeExam'))

def prompt():

    exam_1 ='x'
    exam_2 ='x'
    exam_3 ='x'
    exam_4 ='x'
    ns ='x'

    while (exam_1 != 'y') and (exam_1 != 'n'):
        exam_1 = input('Would you like to include material from exam 1? (y/n) (then press enter)')

    while (exam_2 != 'y') and (exam_2 != 'n'):
        exam_2 = input('Would you like to include material from exam 2? (y/n) (then press enter)')

    while (exam_3 != 'y') and (exam_3 != 'n'):
        exam_3 = input('Would you like to include material from exam 3? (y/n) (then press enter)')

    while (exam_4 != 'y') and (exam_4 != 'n'):
        exam_4 = input('Would you like to include material from exam 4? (y/n) (then press enter)')

    while (ns != 'y') and (ns != 'n'):
        ns = input('Would you like to include new material, or "new stuff"? (y/n) (then press enter)')

    reviewList = list()

    def makeReviewlist():
        if (exam_1 == 'y'):
            reviewList.append('exam 1')
        if (exam_2 == 'y'):
            reviewList.append('exam 2')
        if (exam_3 == 'y'):
         reviewList.append('exam 3')
        if (exam_4 == 'y'):
            reviewList.append('exam 4')
        if (ns == 'y'):
            reviewList.append('new stuff')
    
    makeReviewlist()
    return reviewList

this = prompt()

promptAgain = 'x'

while (promptAgain != 'y'):
    print('You chose to review,', this,'.\n')
    promptAgain = input('Is this correct? (y/n) (then press enter)')
    if (promptAgain == 'y'):
        break
    this = prompt()

print('When you are ready for a question, press enter.\n When you are ready to see the solution, press enter again.\n When you are done with the review, press "q" to quit\n')

def makelist(sectlist):
    sects = list()
    if 'exam 1' in sectlist:
        sects.append(1)
    if 'exam 2' in sectlist:
        sects.append(2)
    if 'exam 3' in sectlist:
        sects.append(3)
    if 'exam 4' in sectlist:
        sects.append(4)
    if 'new stuff' in sectlist:
        sects.append(5)
    return sects

def outputquestion(l):
    quitornah = str()

    while quitornah != 'q':
        e1_length = 28
        e2_length = 15
        e3_length = 14
        e4_length = 14
        ns_length = 14

        chapter = random.choice(l)

        if chapter == 1:
            choice = str(random.randint(1,e1_length))

            p = ['e1_p', choice, '.png']
            p = ''.join(p)
            p = os.path.join('exam1', 'exam1Problems', p)

            s = ['e1_s', choice, '.png']
            s = ''.join(s)
            s = os.path.join('exam1', 'exam1Solutions', s)

            with open(p) as q:
                q = subprocess.Popen(["mspaint.exe", p], shell=True)
                input('press enter to continue')
                q.terminate()
                q.kill()

            with open(s) as q:
                q = subprocess.Popen(["mspaint.exe", s], shell=True)
                input('press enter to continue')
                q.terminate()
                q.kill()

        if chapter == 2:
            choice = str(random.randint(1,e2_length))
            p = ['e2_p', choice, '.png']
            p = ''.join(p)
            p = os.path.join('exam2', 'exam2Problems', p)

            s = ['e2_s', choice, '.png']
            s = ''.join(s)
            s = os.path.join('exam2', 'exam2Solutions', s)

            with open(p) as q:
                q = subprocess.Popen(["mspaint.exe", p], shell=True)
                input('press enter to continue')
                q.terminate()
                q.kill()

            with open(s) as q:
                q = subprocess.Popen(["mspaint.exe", s], shell=True)
                input('press enter to continue')
                q.terminate()
                q.kill()

        if chapter == 3:
            choice = str(random.randint(1,e3_length))
            p = ['e3_p', choice, '.png']
            p = ''.join(p)
            p = os.path.join('exam3', 'exam3Problems', p)

            s = ['e3_s', choice, '.png']
            s = ''.join(s)
            s = os.path.join('exam3', 'exam3Solutions', s)

            with open(p) as q:
                q = subprocess.Popen(["mspaint.exe", p], shell=True)
                input('press enter to continue')
                q.terminate()
                q.kill()

            with open(s) as q:
                q = subprocess.Popen(["mspaint.exe", s], shell=True)
                input('press enter to continue')
                q.terminate()
                q.kill()

        if chapter == 4:
            choice = str(random.randint(1,e4_length))
            p = ['e4_p', choice, '.png']
            p = ''.join(p)
            p = os.path.join('exam4', 'exam4Problems', p)

            s = ['e4_s', choice, '.png']
            s = ''.join(s)
            s = os.path.join('exam4', 'exam4Solutions', s)

            with open(p) as q:
                q = subprocess.Popen(["mspaint.exe", p], shell=True)
                input('press enter to continue')
                q.terminate()
                q.kill()

            with open(s) as q:
                q = subprocess.Popen(["mspaint.exe", s], shell=True)
                input('press enter to continue')
                q.terminate()
                q.kill()

        if chapter == 5:
            choice = str(random.randint(1,ns_length))
            p = ['ns_p', choice, '.png']
            p = ''.join(p)
            p = os.path.join('newstuff', 'newstuffProblems', p)

            s = ['ns_s', choice, '.png']
            s = ''.join(s)
            s = os.path.join('newstuff', 'newstuffSolutions', s)

            with open(p) as q:
                q = subprocess.Popen(["mspaint.exe", p], shell=True)
                input('press enter to continue')
                q.terminate()
                q.kill()

            with open(s) as q:
                q = subprocess.Popen(["mspaint.exe", s], shell=True)
                input('press enter to continue')
                q.terminate()
                q.kill()

        quitornah = input('press q then enter to quit, or just enter to continue')    

outputquestion(makelist(this))
