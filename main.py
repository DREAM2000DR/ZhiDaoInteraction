import config
import user
import queue
import time
import random
import threading

usersPool = queue.Queue()

questionsPool = queue.Queue()

answersPool = queue.Queue()

running = True


def loginAll():
    i = 0
    while i < len(config.users):
        try:
            item = config.users[i]
            u = user.ZDUser(item[0], item[1])
            usersPool.put(u)
        except Exception as e:
            print(str(e))
            print('{} 登录失败，已被抛弃'.format(item[0]))
        else:
            print('{} 登录成功，加入到队列'.format(item[0]))
            i = i + 1
        time.sleep(1)


def publishQuestions():
    while running:
        if questionsPool.qsize() < config.MAX_LEN:
            u = usersPool.get()

            course = random.sample(config.courses, 1)[0]
            FAQIdx = random.randint(0, len(config.FQAs) - 1)
            try:
                questionId = u.saveQuesion(
                    course[2], course[1], config.FQAs[FAQIdx][0])
                questionsPool.put((questionId, FAQIdx, 0))
            except Exception:
                print('问题: {}, 用户: {}, 提问失败'.format(
                    config.FQAs[FAQIdx][0], u.realName))
            else:
                print('问题: {}, 用户: {}, 提问成功'.format(
                    config.FQAs[FAQIdx][0], u.realName))

            usersPool.put(u)
        time.sleep(2)


def publishAnswers():
    while running:
        if answersPool.qsize() < config.MAX_LEN:
            u = usersPool.get()
            question = questionsPool.get()
            ans = random.sample(
                config.FQAs[question[1]][1], 1)[0]

            try:
                answerId = u.saveAnswer(question[0], ans)
                answersPool.put((answerId, 0))
            except Exception:
                print('问题: {}, 答案: {}, 用户: {}, 回答失败'.format(
                    config.FQAs[question[1]][0], ans, u.realName))
                questionsPool.put(question)
            else:
                print('问题: {}, 答案: {}, 用户: {}, 回答成功'.format(
                    config.FQAs[question[1]][0], ans, u.realName))
                if question[2] < 3:
                    questionsPool.put(
                        (question[0], question[1], question[2]+1))

            usersPool.put(u)
        time.sleep(3)


def commitLike():
    while running:
        u = usersPool.get()
        answer = answersPool.get()

        try:
            u.updateOperationToLike(answer[0])
        except Exception:
            print('回答: {}, 用户: {}, 点赞失败'.format(
                answer[0], u.realName))
            answersPool.put(answer)
        else:
            print('回答: {}, 用户: {}, 点赞成功'.format(
                answer[0], u.realName))
            if answer[1] < 3:
                answersPool.put((answer[0], answer[1]+1))

        usersPool.put(u)
        time.sleep(1)


if __name__ == "__main__":
    loginAll()
    threading.Thread(target=publishQuestions).start()
    time.sleep(random.randint(1, 2))
    threading.Thread(target=publishAnswers).start()
    time.sleep(random.randint(1, 2))
    threading.Thread(target=publishAnswers).start()
    time.sleep(random.randint(1, 2))
    threading.Thread(target=commitLike).start()
