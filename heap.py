class Heap :
    def __init__ ( self , arr ) : self.heap = arr
    
    def heapify ( self , n , i ) :
        largest , l , r = i , 2 * i + 1 , 2 * i + 2
        if l < n and self.heap [i] < self.heap [l] : largest = l
        if r < n and self.heap [largest] < self.heap [r] : largest = r
        if largest != i :
            self.heap [i] , self.heap [largest] = self.heap [largest] , self.heap [i]
            self.heapify ( n , largest )
        return self.heap

    def heapPush ( self , n ) :
        self.heap.append ( n )
        self.heapSort ()
        return self.heap

    def heapPop ( self ) :
        key = self.heap [0]
        self.heap.remove ( key )
        print ( "New heap :" , self.heap )
        return key

    def heapReplace ( self , key ) :
        index = self.heap.index ( min ( self.heap ) )
        self.heap [ index ] = key
        self.heapSort ()
        return self.heap

    def heapSort ( self ) :
        n = len ( self.heap )
        for i in range ( n , -1 , -1 ) : self.heapify ( n , i )
        for i in range ( n-1 , 0 , -1 ) :
            self.heap [i] , self.heap [0] = self.heap [0] , self.heap [i]
            self.heapify ( i , 0 )
        return self.heap
      
Obj = Heap ( [ 2 , 5 , 3 , 8 , 6 , 5 , 4 , 7 ] )
print ( "Sorted array is :" , Obj.heapSort () )
print ( "Replaced array is :" , Obj.heapReplace ( 1 ) )
print ( "Array with added element is :" , Obj.heapPush ( 9 ) )
print ( "Removed element :" , Obj.heapPop () )
