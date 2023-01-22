import random 

class Vertex:
    def __init__(self, value):
        self.value = value 
        self.children = {}
    
    def add_child(self, vertex):
        if vertex.value in self.children:
            self.children[vertex.value] += 1
        else:
            self.children[vertex.value] = 1

    def __repr__(self) -> str:
        output_string = f"{self.value} --> "
        for child in self.children:
            output_string += f"({child}, {self.children[child]}), "
         
        return output_string


def multinomial(weights, num_samples=1):
    """
    Sample multiple elements from a list of weights.
    """
    # Normalize the weights
    weights = [float(w) / sum(weights) for w in weights]
    sample_indices = []
    for _ in range(num_samples):
        # Choose a random sample between 0 and 1
        r = random.random()
        # Subtract the weight of each element from the random sample
        # until it is less than or equal to zero
        for i, w in enumerate(weights):
            r -= w
            if r <= 0:
                sample_indices.append(i)
                break
    return sample_indices



class Graph:
    def __init__(self, words):
        self.vertices = {}
        prev_word = words[0]
        self.vertices[prev_word] = Vertex(prev_word)
        for word in words[1:]:
            if not word in self.vertices:
                self.vertices[word] = Vertex(word)
            self.vertices[prev_word].add_child(self.vertices[word])
            prev_word = word

    def __repr__(self):
        output_string = ""
        
        for vertex in self.vertices:
            output_string += f"{vertex} --> "
            for child in self.vertices[vertex].children:
                output_string += f"({child}, {self.vertices[vertex].children[child]}), \n"
        return output_string
    
    def get_next_word(self, word):
        """
        Returns the next word in the sentence
        """
        if word in self.vertices:
            if len(list(self.vertices[word].children)) > 0:
                index = multinomial(self.vertices[word].children.values())[0]
            
                
                return list(self.vertices[word].children.keys())[index]
            else: 
                return None
                
        else:
            return None
    
    def generate_sentence(self, seed_word=None, length=10):
        if seed_word == None:
            seed_word = random.choice(list(self.vertices.keys()))
        sentence = [seed_word]
        for i in range(length):
            word = sentence[-1]
            next_word = self.get_next_word(word)
            if next_word is None:
                break
            sentence.append(next_word)
        return " ".join(sentence)