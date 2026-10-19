class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #key is the sorted word, and value is the array of unsorted words
        appeared_words = {}
        result =[]
        for word in strs:
            sorted_word = sorted(word)
            sorted_word = ''.join(sorted_word)
            appeared_words[sorted_word] =      appeared_words.get(sorted_word,[])
            appeared_words[sorted_word].append(word)
        for val in appeared_words.values():
            result.append(val)
        return result