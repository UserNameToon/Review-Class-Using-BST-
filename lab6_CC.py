"""*****************************************************************************
Name:    Chanchatri Chaichanathong
course:  CMPT 200 X03L
purpose: Review Class
ID:      3056450
*****************************************************************************"""
import string

'''
this is BST class that is used by main() to find the count of each words/ 
unique words within the text file. this class is a simulation of binary search tree.
the class will allow for search specific word returning information regard the searched
word.
the class contain a linked class - _Node in order to used node fuction of python

This class is base on BinarySearchTree.py by MacEwan's Computer Science department 
'''
class BST :
    class _Node :
        # Purpose: this method initialize node
        # Parameters:  left - left element, right - right element 
        # Return: none          
        def __init__(self, word, left = None, right = None) :
            self._value = word
            self._left = left
            self._right = right
            self._count = 1             #count of each words
            self._uCount = 0            #count of unique words
            
    # Purpose: this method initialize BST
    # Parameters: none
    # Return: none      
    def __init__(self) :
        self._root = None
    # Purpose: this method check for empty
    # Parameters: none
    # Return: Node          
    def isEmpty(self) :
        return self._root == None
    # Purpose: this method check for unique count
    # Parameters: none
    # Return: int - unique count     
    def uniquie(self):
        return self._root._uCount
    # Purpose: this method search for word
    # Parameters: value - inpput, total - total count
    # Return: found and not found     
    def search(self, value,total) :
        probe = self._root
        while (probe != None) :
            if value == probe._value :
                return 'word: ' + str(value) + ' count: ' + str(probe._count) +' percent: ' + '{0:2.1f}'.format((probe._count / total )* 100)+'%'
            if value <= probe._value :
                probe = probe._left
            else :
                probe = probe._right
        return 'No word found' 
    
    # Purpose: this method insert word in BST
    # Parameters: value - word
    # Return: none     
    def insert(self, value) :
        if self.isEmpty() :
            self._root = self._Node(value)
            return
        parent = None
        
        probe = self._root
        while (probe != None) :
            #if probe._count == 1:
            
               
            if value < probe._value :  
                parent = probe      
                probe = probe._left
            elif value > probe._value:                     
                parent = probe     
                probe = probe._right
            else:
                probe._count += 1
                return   
        
        if (value <= parent._value) :   
            parent._left = self._Node(value)
        else :                          
            parent._right = self._Node(value)
            
    # Purpose: this method display word in order
    # Parameters: none
    # Return: None      
    def inOrder(self) :
        self.recInOrder(self._root)

    # Purpose: this method print word in order
    # Parameters: Node
    # Return: Node          
    def recInOrder(self,node) :
        if node == None : return
        self.recInOrder(node._left)
        print('word: ',node._value,' count: ', node._count)
        self.recInOrder(node._right) 
# Purpose: this method start program
# Parameters: None
# Return: Node           
def main():
    #file input
    mazeFile = []
    while True:
        try:
            userInput = input('Enter file name: ')
            if userInput == '':
                userInput = 'sample.txt'
            mazeFile = open_file(userInput)
            break
         #alert user if the input is invalid
        except:
            print('Invalid inpunt!') 
    #init bst
    t = BST() 
    for i in string.punctuation:
        if i not in ',-':
            mazeFile = mazeFile.replace(i,'')
    #pre for insertion
    listWord = mazeFile.split()
    total = 0
    for i in listWord:
        total += 1
        #insert word to bst
        t.insert(i.lower())
    #interactive menu
    print('Menu Interface: ')    
    while True:
        print('\na) Number of Unique words'+
              '\nb) all unidue words in alphabetic + frequency'+
              '\nc) specific word'+
              '\nd) Exit menu') 
        userInput = input("\nPlease choose one of the option: ")
        if userInput == 'a':
            print('number of unique words: ',t.uniquie())
        if userInput == 'b':
            t.inOrder()
        if userInput == 'c':
            userIn = input('\nEnter word: ')
            print(t.search(userIn,total))
        if userInput == 'd':
            print('\nExiting...')
            break  
# Purpose: this method open file
# Parameters: filename - userinput file name
# Return: text  
def open_file(fileName):
    listWord = []
    try:
        obj = open(fileName)
        listWord = obj.read()
        obj.close()        
    except:
        print('The file ' + userInput + ' does not exist or is not readable.')
    return listWord
main()