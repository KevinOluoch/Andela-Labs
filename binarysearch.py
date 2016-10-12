class BinarySearch( list ):
    """ This is a BinarySearch class, that inherits from the list class
     the  __init__() takes two integers as parameters, a and b. a is the length of the
 list to be created and b is the step or difference between consecutive values.
 It initialize an instance variablelength`, that returns the number of elements
  in the array
    """


    def __init__(self, a, b):
        list.__init__(self,[ x*b for x in range( 1, a + 1)])
        self.length = len(self)

    def search( self, item ):
        """This method takes just one argument which is the value to find.
         it returns a dictionary object, which contains. count, the number of
         times the function iterated to find the index of the number in question index,
         the index of the number in question.
          It implements the binary search algorithm,
          """
        first_num = 0
        last_num = len(self)-1
        searching = True
        count = 0
        while ((first_num <= last_num) and searching) and (count<100):
            count += 1
            midpoint = (first_num + last_num)//2
            print count, midpoint
            if self[midpoint] == item:
                searching = False
            else:
	            if item < self[midpoint]:
	                last_num = midpoint-1
	            else:
	                first_num = midpoint+1


        if not self[midpoint] == item: return { "count": count, "index": -1 }
        return { "count": count, "index":midpoint }



