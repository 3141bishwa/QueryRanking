import wikipedia
import nltk

class Queue:
    "A container with a first-in-first-out (FIFO) queuing policy."
    def __init__(self):
        self.list = []

    def push(self,item):
        "Enqueue the 'item' into the queue"
        self.list.insert(0,item)

    def pop(self):
        """
          Dequeue the earliest enqueued item still in the queue. This
          operation removes the item from the queue.
        """
        return self.list.pop()

    def isEmpty(self):
        "Returns true if the queue is empty"
        return len(self.list) == 0

queue = Queue()

def getNouns(sentence, exclude_words):
    nouns = []
    for word,pos in nltk.pos_tag(nltk.word_tokenize(sentence)):
        if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS') and word not in exclude_words:
            nouns.append(word)
    return nouns

corpus = []

def wikipedia_stuff(word):

    level = 1
    counter = 0

    result = wikipedia.search(word)[0]
    queue.push(result)

    while not queue.isEmpty() and counter < level:
        search = queue.pop()

        print search
        page = wikipedia.page(search)

        nouns = getNouns(page.content, [])
        for noun in nouns:
            print noun
        corpus.extend(nouns)

        for link in page.links:
            queue.push(link)

    count += 1
    return corpus

print wikipedia_stuff("jewellry")
