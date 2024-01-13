from typing import Callable, List, Set

import shell
import util
import wordsegUtil


############################################################
# Problem 1b: Solve the segmentation problem under a unigram model

class SegmentationProblem(util.SearchProblem):
    def __init__(self, query: str, unigramCost: Callable[[str], float]):
        self.query = query
        self.unigramCost = unigramCost

    def startState(self):
        # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
        return 0
        # END_YOUR_CODE

    def isEnd(self, state) -> bool:
        # BEGIN_YOUR_CODE (our solution is 2 lines of code, but don't worry if you deviate from this)
        return state == len(self.query)
        # END_YOUR_CODE

    def succAndCost(self, state):
        # BEGIN_YOUR_CODE (our solution is 7 lines of code, but don't worry if you deviate from this)
        results = []
        for i in range(state+1, len(self.query)+1):
            word = self.query[state:i]
            action = i - state
            new_state = i
            cost = self.unigramCost(word)
            results.append((action, new_state, cost))
        return results
        # END_YOUR_CODE


def segmentWords(query: str, unigramCost: Callable[[str], float]) -> str:
    if len(query) == 0:
        return ''

    ucs = util.UniformCostSearch(verbose=0)
    ucs.solve(SegmentationProblem(query, unigramCost))

    # BEGIN_YOUR_CODE (our solution is 3 lines of code, but don't worry if you deviate from this)
    actions = ucs.actions
    answer = ""
    for a in actions:
        answer += query[:a] + " "
        query = query[a:]
    return answer
    # END_YOUR_CODE


############################################################
# Problem 2b: Solve the vowel insertion problem under a bigram cost

class VowelInsertionProblem(util.SearchProblem):
    def __init__(self, queryWords: List[str], bigramCost: Callable[[str, str], float],
            possibleFills: Callable[[str], Set[str]]):
        self.queryWords = queryWords
        self.bigramCost = bigramCost
        self.possibleFills = possibleFills

    def startState(self):
        # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
        return (0, wordsegUtil.SENTENCE_BEGIN)
        # END_YOUR_CODE

    def isEnd(self, state) -> bool:
        # BEGIN_YOUR_CODE (our solution is 2 lines of code, but don't worry if you deviate from this)
        index, previous_word = state
        return len(self.queryWords) == index
        # END_YOUR_CODE

    def succAndCost(self, state):
        # BEGIN_YOUR_CODE (our solution is 8 lines of code, but don't worry if you deviate from this)
        index, previous_word = state
        results = []
        choices = self.possibleFills(self.queryWords[index])
        if len(choices) == 0:
            choices = set([self.queryWords[index]])
        for word in choices:
            action = word
            new_state = (index+1, word)
            cost = self.bigramCost(previous_word, word)
            results.append((action, new_state, cost))
        return results


        # END_YOUR_CODE


def insertVowels(queryWords: List[str], bigramCost: Callable[[str, str], float],
        possibleFills: Callable[[str], Set[str]]) -> str:
    # BEGIN_YOUR_CODE (our solution is 3 lines of code, but don't worry if you deviate from this)
    ucs = util.UniformCostSearch(verbose=0)
    ucs.solve(VowelInsertionProblem(queryWords, bigramCost, possibleFills))
    return " ".join(ucs.actions)
    # END_YOUR_CODE


############################################################
# Problem 3b: Solve the joint segmentation-and-insertion problem

class JointSegmentationInsertionProblem(util.SearchProblem):
    def __init__(self, query: str, bigramCost: Callable[[str, str], float],
            possibleFills: Callable[[str], Set[str]]):
        self.query = query
        self.bigramCost = bigramCost
        self.possibleFills = possibleFills

    def startState(self):
        # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
        return (0, wordsegUtil.SENTENCE_BEGIN)
        # END_YOUR_CODE

    def isEnd(self, state) -> bool:
        # BEGIN_YOUR_CODE (our solution is 2 lines of code, but don't worry if you deviate from this)
        index, previous_word = state
        return index == len(self.query)
        # END_YOUR_CODE

    def succAndCost(self, state):
        # BEGIN_YOUR_CODE (our solution is 14 lines of code, but don't worry if you deviate from this)
        index, previous_word = state
        results = []
        for i in range(index+1, len(self.query)+1):
            letters = self.query[index:i]
            new_state = i
            choices = self.possibleFills(letters)
            for word in choices:
                action = word
                new_state = (i, word)
                cost = self.bigramCost(previous_word, word)
                results.append((action, new_state, cost))
        return results

        # END_YOUR_CODE


def segmentAndInsert(query: str, bigramCost: Callable[[str, str], float],
        possibleFills: Callable[[str], Set[str]]) -> str:
    if len(query) == 0:
        return ''

    # BEGIN_YOUR_CODE (our solution is 4 lines of code, but don't worry if you deviate from this)
    ucs = util.UniformCostSearch(verbose=0)
    ucs.solve(JointSegmentationInsertionProblem(query, bigramCost, possibleFills))
    return " ".join(ucs.actions)

    # END_YOUR_CODE


############################################################

if __name__ == '__main__':
    shell.main()
