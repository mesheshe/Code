# Course: CS261 - Data Structures
# Student Name: Elias Meshesha 
# Assignment: 5
# Description: Impelements a min heap


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.heap.length() == 0

    def add(self, node: object) -> None:
        """
        Adds the given node to the heap. It does this by adding the node to the 
        end of the heap list and then percolating it upward by constantly swapping 
        the parent node with the child node, if the parent node's value is greater 
        than the child node's value
        """
        self.heap.append(node)
        i = self.heap.length() - 1
        j = (i - 1)//2
        while (j >= 0 and self.heap.get_at_index(j) > self.heap.get_at_index(i)):
            self.heap.swap(j,i)
            i = j
            j = (i - 1)//2

    def get_min(self) -> object:
        """
        Returns the minimum value stored in the heap, which is stored in the root 
        of the tree, or otherwise known as index 0.
        """
        if self.is_empty():
            raise MinHeapException
        return self.heap.get_at_index(0)

    def remove_min(self) -> object:
        """
        Removes and returns the minimum value. It does so by first saving the minmum
        value, and then swapping the root with last element leaf child, and then popping
        off the last element. With the new root, it is percolated down the tree, by
        checking to see if the child's value is lower than the parent
        """
        if self.is_empty():
            raise MinHeapException
        elif self.heap.length() == 1:
            return self.heap.pop()
        self.heap.swap(0, self.heap.length() - 1)
        returnVal = self.heap.pop()
        i, leftVal, rightVal, compareVal = 0, None, None, self.heap.get_at_index(0) 
        L, R = 2*i + 1, 2*i + 2
        while L < self.heap.length() or R < self.heap.length():
            if L < self.heap.length():
                leftVal = self.heap.get_at_index(L)
            else:
                leftVal = None
            if R < self.heap.length():
                rightVal = self.heap.get_at_index(R)
            else:
                rightVal = None

            if (leftVal is not None) and (rightVal is None or leftVal <= rightVal) and (compareVal >= leftVal):
                self.heap.swap(L, i)
                i = L
            elif (rightVal is not None) and (compareVal > rightVal) and (rightVal < leftVal):
                self.heap.swap(R, i)
                i = R
            else:
                i = L
            L, R = 2*i + 1, 2*i + 2
        return returnVal

    
    def build_heap(self, da: DynamicArray) -> None:
        """
        From an unsorted array, this function builds a heap. It does so in O(N) time.
        It first starts with the leaves nodes, it assumes each of them are all valid 
        sub heaps, then it goes up a level, and makes sure that is a valid subheap, and
        it does so for each level of the tree. Until it finally ends with a valid min heap 
        overall 
        """
        self.heap = DynamicArray()
        len =  da.length()
        for i in range(len):
            self.heap.append(da.get_at_index(i))
        
        for i in range(len//2-1, -1, -1):        
            k, L, R = i, 2*i + 1, 2*i + 2
            compareVal = self.heap.get_at_index(i)
            x = False
            if (L < len and self.heap.get_at_index(L) < compareVal) or (R < len and self.heap.get_at_index(R) < compareVal):
                x = True 
            while i < len//2 and x:
                if L < len:
                    leftVal = self.heap.get_at_index(L)
                else:
                    leftVal = None
                if R < len:
                    rightVal = self.heap.get_at_index(R)
                else:
                    rightVal = None

                if (leftVal is not None) and (rightVal is None or leftVal <= rightVal) and (compareVal > leftVal):
                    self.heap.swap(L, k)
                    k = L
                elif (rightVal is not None) and (compareVal > rightVal):
                    self.heap.swap(R, k)
                    k = R
                else:
                    x = False
                L, R = 2*k + 1, 2*k + 2 
            

# BASIC TESTING
if __name__ == '__main__':
    
    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)
    
    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)
    

    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())


    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty():
        print(h, end=' ')
        print(h.remove_min())

    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)
    da.set_at_index(0, 500)
    print(da)
    print(h)
    h = MinHeap([1])
    h.build_heap(DynamicArray([-956, -632, -297, -561, 631, 507, -660, -538, -294, -5, 70, -1, 136, -75, 839, 244, 968, 476, -843, 105, -541, -221, -387, -704, -697, -810, -373, 39, 159, 352, -940, 408, 63, 712, -551, 682, 362, 687, 445, 288, -466, 598, 54, -233, -335, 489, 396, -233, 144, 380, -402, -321, -627, -859, -383, 625, 383, 74, -977, 558, 868, 78, 126, -514, 526, -330, -973, 537, -453, 792, -507, 260, -315, 818, 979, 500, 179, 449, -570, 464, -71, -227, 673, -417, -273, -284, 27, 568, -453, 859, 738, 581, 327, -392, 963, 272, 607, 687, 419, -97, 967, 50, 767, 210, -190, 23, -898, 575, 477, 205, 223, 205, 215, -56, 279, 112, -50, -564, 109, -620, -976, 555, -199, 207, 280, -982, 368, 563, -403, 697, 198, 782, -801, 913, -710, 902, 380, 583, 866, -887, -558, 879, -884, 588, -277, 37, 402, 638, -135, 298, 513, 284, 970, 996, 757, 218, 794, -975, 761, -319, -195, -764, 258, -502, -247, -735, 744, -397, -716, -875, -570, -205, -722, -254, 75, 42, 85, -594, -492, 315, -952, -40, -662, 468, -66, 876, 899, -323, 132, 578, 685, -242, 286, 466, 736, 383, -335, -383, 59, 422, -455, -135, 384, 656, 430, 264, -371, -557, 45, -924, -57, 803, -223, 125, -202, -843, 750, -94, 976, -501, -473, 447, 14, -217, 585, -145, 81, -892, -291, 792, 969, 728, 714, -921, 192, -402, 294, 348, -237, -849, 383, 281, 768, 536, 340, 488, -410, -717, -6, 134, 376, -546, 142, 400, -22, 408, -396, -595, 808, -915, -523, -557, -739, -993, 813, -650, -535, 924, -791, -838, 770, 491, 970, -960, 405, 882, 522, -735, -334, 537, 417, -306, 357, 727, -833, -264, -902, -120, 144, 730, 318, 917, 294, 58, -422, 372, -495, -588, -806, 334, 70, -61, -730, -238, -198, -360, -541, -775, 563, 870, -271, -337, 293, 628, 463, 970, -638, -361, -81, -79, -353, -105, -235, 95, 196, 342, 614, -142, -938, -376, -111, -390, 976, 914, -419, 442, 953, 750, 107, -471, -683, 952, -250, 153, -182, 323, -215, 601, 190, 773, -279, -330, -875, 71, 738, -798, -180, 464, -638, 217, 517, 168, 579, -660, 623, -476, -718, -659, -648, 487, -500, 169, -275, 141, -320, 565, 86, 219, 269, -655, 359, 541, 380, 992, 952, -784, 204, -917, -683, -213, -739, -597, 529, -20, 750, -576, -752, -391, 195, -393, 21, -217, -548, 289, -305, -192, -243, -760, -743, 467, -526, -898, -135, -561, 218, 268, 283, 456, -502, -847, 390, 682, -9, 769, -485, 18, -796, 42, -853, -821, 474, 319, -528, -868, 484, -959, 227, 257, -85, -232, 146, -38, 939, -834, -848, 906, -614, -95, -533, -301, 828, 200, -735, -695, 320, -229, 373, 101, 126, -764, -171, 387, 202, -546, -18, 283, 720, -472, 141, 355, -976, 380, -25, -265, -418, 666, -848, -68, 369, 89, 387, -580, 503, 536, -88, -563, 577, 953, -197, 116, 521, 67, -549, -870, -278, 169, 803, 942, 528, 294, 83, -44, 674, -263, 25, 692, -45, 727, 487, -331, 995, 995, -745, -365, 544, -63, -499, -8, -883, -763, -851, -956, -472, 320, -617, -670, 701, 283, 316, 150, -241, 329, -136, 331, 657, -201, -722, -210, -982, -316, 311, 411, 950, -810, -451, -409, 17, 383, -118, -788, 432, -902, -869, 559, -338, -798, -972, 594, 589, -16, -396, 712, -864, -55, -631, 216, -214, 191, -415, -387, -329, 448, -749, -509, -509, 9, 734, 506, -266, -323, 235, -938, -73, -719, -820, 617, -91, 113, -129, 325, 860, 725, 354, 693, -465, -784, 309, 169, 464, 262, -103, 594, 614, -36, 346, 112, 392, 507, 635, 609, -877, 333, 204, 658, 982, 237, 587, 458, -848, -739, -279, 662, -345, 712, 726, 975, -204, -411, -988, -388, -59, 946, -347, 749, 633, 715, 744, -666, -615, 345, 426, 891, -958, -160, -425, 894, -997, -722, -12, 478, -789, 220, 632, 753, -511, 695, -445, -686, 563, 653, 26, -782, -384, 176, 38, 513, -377, -418, 220, 200, -909, 86, -824, 590, -104, 951, 638, -271, 281, -230, 153, 222, 567, 774, -767, 178, 166, 930, 572, 944, -24, -751, 423, -575, 700, -87, -817, 91, 478, 356, 807, 513, 161, -805, -278, 369, 520, -981, -710, -876, -863, -183, -706, 836, -731, -352, -90, -412]))
    b = DynamicArray([-997, -993, -982, -988, -981, -959, -977, -982, -975, -958, -952, -917, -924, -976, -976, -973, -972, -938, -956, -938, -875, -876, -659, -784, -898, -898, -868, -892, -921, -870, -940, -956, -838, -960, -902, -820, -806, -877, -843, -789, -909, -824, -817, -875, -718, -648, -655, -739, -752, -548, -760, -847, -853, -859, -848, -735, -764, -546, -848, -849, -660, -717, -546, -883, -915, -801, -791, -810, -902, -887, -884, -323, -719, -784, -730, -541, -848, -411, -666, -425, -764, -782, -735, -716, -767, -751, -279, -863, -798, -335, -662, -500, -320, -392, 359, -704, -683, -597, -576, -455, -305, -743, -561, -557, -810, -796, -821, -843, -94, -501, -834, -533, -695, -291, -171, -297, -472, -564, -237, -620, -563, -197, -549, -6, -44, -263, -331, -745, -595, -851, -739, -330, -650, -722, -710, -451, -788, -869, -798, -864, -631, -833, -749, -266, -277, -315, -422, -495, -588, -103, -61, -238, -360, -775, -739, -337, -388, -638, -615, -353, -235, -722, -511, -686, -466, -390, -419, -417, -541, -683, -570, -205, -722, -254, 54, -805, -710, -731, -638, 217, 168, -660, -476, 468, -387, -275, 141, -323, 132, 396, 380, -242, 204, -1, -233, 383, -335, -383, -391, -393, -217, -135, -243, -697, -526, -135, -402, 210, -502, -321, -57, -485, -223, -627, -202, -528, 484, 136, -85, -232, -473, -383, -614, -217, -301, -145, 81, -229, 101, 39, 202, -18, 283, -75, -50, -402, -418, 109, -68, 89, -580, -88, 558, 536, 116, 67, -410, 169, 78, 83, 280, 25, -45, 400, -22, 408, -396, -514, -403, -763, -523, -617, -670, 283, -241, -136, -535, -561, -210, -538, 411, 491, -409, -118, 405, 583, -338, -735, -334, -396, 417, -558, -214, -415, -387, -551, -509, -120, 144, 235, -73, 37, -91, -129, 325, 354, -465, 309, -135, 262, 70, -36, 112, 500, -198, 204, 658, 179, 458, -279, -345, 218, -204, 449, -59, -347, -570, -361, -294, -79, -319, -160, -195, -12, -71, 220, 258, -445, -502, -376, -384, 38, -377, -418, 200, -397, -104, 638, -271, -471, -273, 598, -250, 153, -182, -284, -575, -87, 91, 356, 75, -330, 42, -632, -233, -706, -453, -352, -492, 315, 517, 859, 579, -40, 623, 70, 738, 489, 581, 487, -66, 169, 876, 327, 899, 565, 86, 219, 269, 578, 963, 541, 685, 992, 952, 286, 272, 466, 607, -213, 736, 687, 529, -20, 750, 419, 144, 59, 195, 422, 21, 380, -97, 289, 967, -192, 384, 656, 50, 467, 430, 264, 767, -371, 218, 268, 283, 456, 45, -190, 390, 682, -9, 769, 803, 18, 23, 42, 125, 507, 474, 319, -373, 750, 575, 477, 227, 257, 976, 205, 146, -38, 939, 223, 447, 906, 14, -95, 205, 585, 828, 200, 215, 625, 320, -56, 373, 383, 126, 792, 279, 387, 969, 728, 112, 714, 720, 74, 141, 355, 192, 380, -25, -265, 294, 666, 348, 159, 369, 352, 387, 383, 503, 536, 281, 768, 577, 953, 555, 340, 521, 868, 488, -199, -278, 207, 803, 942, 528, 294, 134, 376, 674, 126, 839, 692, 142, 727, 487, 368, 995, 995, 563, -365, 544, -63, -499, -8, 808, 408, 526, 697, -472, 320, -557, 198, 701, 782, 316, 150, 813, 329, 63, 331, 657, -201, 924, 244, 913, -316, 311, 770, 950, 968, 902, 970, 17, 383, 380, 537, 432, 882, 712, 559, 522, 866, -453, 594, 589, -16, 537, 712, 792, -55, -306, 216, 357, 191, 727, 879, -329, 448, -264, -507, -509, 9, 734, 506, 588, 730, 260, 318, 682, 476, 917, 617, 294, 113, 58, 402, 860, 725, 372, 693, 638, 818, 362, 169, 464, 298, 334, 594, 614, 979, 346, 513, 392, 507, 635, 609, 284, 333, 687, 970, 982, 237, 587, 996, 563, 870, 757, 662, -271, 712, 726, 975, 293, 794, 628, 463, 445, 946, 970, 749, 633, 715, 744, -81, 761, 345, 426, 891, 288, 464, -105, 894, 105, 95, -5, 478, 196, 342, 632, 753, 614, 695, -142, -227, 563, 653, 26, -111, -247, 176, 631, 513, 976, 914, 220, 673, 744, 86, 442, 590, 953, 951, 750, 107, 281, -230, 153, 222, 567, 774, 952, 178, 166, 930, 572, 944, -24, 323, 423, -215, 700, 27, 601, 190, 478, 773, 807, 513, 161, -221, -278, 369, 520, 71, 85, 738, 568, -183, -594, 836, -180, 464, -90, -412])
    c = DynamicArray([-100, -100, -98, -97, -99, -96, -97, -87, -96, -98, -98, -84, -89, -90, -95, -85, -76, -91, -96, -95, -89, -95, -96, -76, -75, -81, -60, -76, -83, -87, -61, -67, -75, -73, -70, -73, -76, -75, -68, -87, -82, -89, -87, -89, -93, -75, -81, -47, -37, -64, -25, -69, -35, -39, -48, -36, -54, -72, -81, -74, -84, 23, -35, 0, -62, -54, -22, -71, -50, -55, -33, -66, -64, -66, -56, -35, -66, -57, -65, -74, -51, -55, -80, -78, -87, -82, -77, -87, -82, -51, -87, -64, -68, -52, -73, -94, -30, -22, 2, -57, 3, -3, -9, -65, -66, 11, -9, -13, -34, 36, -35, 35, -2, -41, -53, -19, 26, 15, -74, 14, -14, -12, -83, 35, 39, 6, -2, 35, 7, -52, -26, 4, 0, 16, -2, -55, -31, -37, -21, -26, -31, -6, -33, -62, -54, -21, -59, -60, 5, -1, 9, 9, -25, -65, -37, -47, -43, 16, -32, -67, -3, -26, -19, 6, 37, -46, 49, -25, 7, -31, -15, -58, -32, -42, -61, -67, -44, -47, -17, -42, -17, 27, -4, -63, -57, 2, -29, -16, -20, 1, -38, -3, 58, 88, 8, 86, -21, 83, 32, 66, -20, 22, 49, 75, 76, 1, 73, 4, -47, 56, 47, 53, 35, 66, 18, 58, 84, 6, 45, 78, 82, -1, 33, 53, 48, 73, 4, 11, 6, 67, 12, 8, 78, 38, 73, 60, 44, -8, 76, 25, 69, 32, 26, 94, 37, 12, 74, 71, 94, 44, 65, 7, 58, 47, 52, 80, 49, 13, 25, 9, 96, 47, 55, 32, 69, 59, 98, 48, 57, 41, 37, -27, 96, 15, 42, 46, 10, 50, 88, 89, 81, 31, -3, 25, 5, 33, 73, -50, 70, 93, -28, 65, 42, 82, 5, 53, 59, 48, 55, 71, 22, 99, 19, 41, 19, 91, 70, 99, 25, 76, 14, 67, 12, -36, 7, 27, 96, 32, -9, -28, -3, 49, 3, 20, 1, 98, 0, 50, 13, 80, 74, 73, 26, 96, 51, 91, 49, 81, 27, 83, 34, 32, 43, 16, 48, 18, 28, -8, 76, 10, 69, 27, -48, -33, 47, 72, -47, 52, 47, 54, 15, -10, 90, 49, 67, 70, 7, 13, 2, 36, 11, 60, 14, 55, 14, 43, 61, 71, 74, 59, 37, -24, 5, 12])
    print(h.heap == b)
    for num in range(b.length()):
        if h.heap.get_at_index(num) != b.get_at_index(num):
            print("index =", num, "a[i] =", h.heap.get_at_index(num), "b[i] =", b.get_at_index(num))