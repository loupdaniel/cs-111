"""
Purpose: Solution for project 5 (Processing DNA)
Author: Chanhui Lee, Brian Wang
Date: October 31st, 2024
CS 111, Fall 2024
"""

def readingFrames(dna, frameNum):
    """A function that returns all the codons based on specific reading frame in the order that the codons appear

    Parameters:
        dna: a DNA string
        frameNum: the number 0, 1, or 2 counting the number of nucleotides ignore
        before starting to group nucleotides into codons for a reading frame.
        
    Returns:
        codons: a list of length-3 strings representing all the codons
        of the chosen reading frame in the order that the codons appear
    """
    
    if len(str(dna)) == 0:
        return "DNA string is empty!"
    
    
    codons= []
    numCodons= (len(dna)-frameNum)//3
    
    x=frameNum
    for i in range(numCodons):
        
        codon = dna [x:x+3]
        codons.append(codon.lower())
        
        x=x+3
        
    return codons



def nextORF(dna):
    """A function that returns the index of the “a” in the start codon and
    the index of the nucleotide just after the stop codon to find the complete open reading frame

    Parameters:
        dna: a DNA string

    Returns:
        x: The index of the “a” in the start codon. Returns None if no ORFs are found.
        y: The index of the nucleotide just after the stop codon. Returns None if no ORFs are found.
    """
    
    if len(str(dna)) == 0:
        return "DNA string is empty!"
    
    
    temp = []
    startCodon = "atg"
    stopCodon = ["taa", "tag", "tga"]

    
    for i in range(3):
        temp = readingFrames(dna, i)

        index = 0
        
        xList = []
        yList = []
        
        while index < len(temp):
            if temp[index] == startCodon:
                xList.append((index * 3) + i)
                
                for index2 in range(index + 1, len(temp)):
                    if temp[index2] in stopCodon:
                        yList.append((index2 * 3) + i + 3)
                        
                        #return xList[0], yList[0]
                
                if len(yList) != 0:
                    return xList[0], yList[0]
                else:
                    break
            
            index += 1
            
    return None, None


def potentialGenes(dna, size):
    """A function that returns the total amount of ORFs of at least the specified size contained in the DNA.

    Parameters:
        dna: a DNA string
        size: the minimum number of codons to consider in an ORF (including start and stop codons).

    Returns:
        count:  an integer counting the number of ORFs of at least that size contained in the DNA,
        where size is counted by the number of codons (not nucleotides).
    """
    
    if len(str(dna)) == 0:
        return "DNA string is empty!"
    
    
    if size > len(str(dna))//3:
        return "The minimum number of codons to consider in an ORF is bigger than the number of codons in the given DNA string!"
    
    count = 0
    isNone = False
    originalDna = dna
    x = 0
    y = 0
    
    while not isNone:
        x, y = nextORF(originalDna)
        
        if x == None or y == None:
            # isNone = True
            break
        
        if ((y-x)//3) >= size:
            count += 1

        originalDna = originalDna[y:]
        #print("@@@")
        
        if len(originalDna) == 0:
            isNone = True
    
    return count



def longestMatch(dna1, dna2):
    """A function that returns the longest DNA sequence that is common to both dna1 and dna2.
    If more than one shared sequence is of the longest length, then the function returns the one
    that occurs earliest in the argument dna1.

    Parameters:
        dna1: a DNA string
        dna2: a DNA string

    Returns:
        longestDna: a string representing the longest DNA sequence that is common to both dna1 and dna2. 
    """

    result = []
    longestDna = ""
    
    
    if len(dna1) == 0 or len(dna2) == 0:
        return "One or both DNA strings are not given!"

    
    if len(dna1) > len(dna2):
        if len(dna2) == 1:
            if dna2 in dna1:
                return dna2.lower()
            else:
                return "Common match not found!"

        for i in range(len(dna1)):
        
            for lenSub in range(1, len(dna1) + 1):
                dna1Sub = dna1[i:i + lenSub]

                if dna1Sub in dna2:
                    result.append(dna1Sub)
                    
            
        for index in range(1, len(result)):
            if len(result[index]) > len(result[index-1]) and len(longestDna) < len(result[index]):
                longestDna = result[index]
            elif len(result[index]) < len(result[index-1]) and len(longestDna) < len(result[index-1]):
                longestDna = result[index-1]
            elif len(result[index]) == len(result[index-1]) and len(longestDna) < len(result[index]):
                longestDna = result[index-1]
                
        return longestDna.lower()
        
        
    elif len(dna1) < len(dna2):
        if len(dna1) == 1:
            if dna1 in dna2:
                return dna1.lower()
            else:
                return "Common match not found!"
        
        for i in range(len(dna1)):
        
            for lenSub in range(1, len(dna1) + 1):
                dna1Sub = dna1[i:i + lenSub]

                if dna1Sub in dna2:
                    result.append(dna1Sub)
                    
            
        for index in range(1, len(result)):
            if len(result[index]) > len(result[index-1]) and len(longestDna) < len(result[index]):
                longestDna = result[index]
            elif len(result[index]) < len(result[index-1]) and len(longestDna) < len(result[index-1]):
                longestDna = result[index-1]
            elif len(result[index]) == len(result[index-1]) and len(longestDna) < len(result[index]):
                longestDna = result[index-1]
                
        return longestDna.lower()

    else:
        if len(dna1) == 1 and len(dna2) == 1:
            if dna1 in dna2:
                return dna1.lower()
            else:
                return "Common match not found!"
        
        for i in range(len(dna1)):
        
            for lenSub in range(1, len(dna1) + 1):
                dna1Sub = dna1[i:i + lenSub]

                if dna1Sub in dna2:
                    result.append(dna1Sub)
                    
            
        for index in range(1, len(result)):
            if len(result[index]) > len(result[index-1]) and len(longestDna) < len(result[index]):
                longestDna = result[index]
            elif len(result[index]) < len(result[index-1]) and len(longestDna) < len(result[index-1]):
                longestDna = result[index-1]
            elif len(result[index]) == len(result[index-1]) and len(longestDna) < len(result[index]):
                longestDna = result[index-1]
                
        return longestDna.lower()



def readingFrames_test():
    
    # Common cases
    assert readingFrames("aatcgtagctt", 0) == ["aat", "cgt", "agc"], "Error occurred! The result should be " + str(["aat", "cgt", "agc"])
    assert readingFrames("aatcgtagctt", 1) == ["atc", "gta", "gct"], "Error occurred! The result should be " + str(["atc", "gta", "gct"])
    assert readingFrames("aatcgtagctt", 2) == ["tcg", "tag", "ctt"], "Error occurred! The result should be " + str(["tcg", "tag", "ctt"])
    
    
    # Edge cases
    assert readingFrames("", 0) == "DNA string is empty!", "Error occurred! DNA string is empty!"
    
    assert readingFrames("a", 0) == [], "Error occurred! The list that was returned should contain nothing!"
    assert readingFrames("aa", 0) == [], "Error occurred! The list that was returned should contain nothing!"
    assert readingFrames("aag", 1) == [], "Error occurred! The list that was returned should contain nothing!"
    assert readingFrames("aagt", 2) == [], "Error occurred! The list that was returned should contain nothing!"
    
    
    print("readingFrames passes all tests.")



def nextORF_test():
    
    # Common cases
    assert nextORF("atgaatcgtagctt") == (None, None), "Error occurred! The result should be (None, None)"    
    assert nextORF("cccatggcccggtgagatga") == (3, 15), "Error occurred! The result should be (3, 15)"
    assert nextORF("acccatggcccggtgagatga") == (4, 16), "Error occurred! The result should be (4, 16)"
    assert nextORF("aacccatggcccggtgagactgattt") == (5, 17), "Error occurred! The result should be (5, 17)"
    
    # Edge cases
    assert nextORF("") == "DNA string is empty!", "Error occurred! DNA string is empty!"
    assert nextORF("a") == (None, None), "Error occurred! The result should be (None, None)"
    
    assert nextORF("atg") == (None, None), "Error occurred! The result should be (None, None)"
    
    assert nextORF("taa") == (None, None), "Error occurred! The result should be (None, None)"
    assert nextORF("tag") == (None, None), "Error occurred! The result should be (None, None)"
    assert nextORF("tga") == (None, None), "Error occurred! The result should be (None, None)"
    
    print("nextORF passes all tests.")



def potentialGenes_test():
    
    # Common cases
    assert potentialGenes("cccatggcccggtgagactgattt", 2) == 1, "Error occurred! The result should be 1"
    assert potentialGenes("cccatggcccggtgagatga", 2) == 1, "Error occurred! The result should be 1"
    assert potentialGenes("atgaatcgtagctt", 2) == 0, "Error occurred! The result should be 0"
    assert potentialGenes("atgtaacccatgtaaccc", 2) == 2, "Error occurred! The result should be 2"
    assert potentialGenes("cccatgtaacccatgtaacccatgccctga", 2) == 3, "Error occurred! The result should be 3"
    
    # Edge cases
    assert potentialGenes("", 3) == "DNA string is empty!", "Error occurred! DNA string is empty!"
    assert potentialGenes("a", 1) == "The minimum number of codons to consider in an ORF is bigger than the number of codons in the given DNA string!", "Error occurred! The minimum number of codons to consider in an ORF is bigger than the number of codons in the given DNA string!"
    assert potentialGenes("atgta", 3) == "The minimum number of codons to consider in an ORF is bigger than the number of codons in the given DNA string!", "Error occurred! The minimum number of codons to consider in an ORF is bigger than the number of codons in the given DNA string!"

    assert potentialGenes("atgtaacccatgtaa", 3) == 0, "Error occurred! The result should be 0"
    
    print("potentialGenes passes all tests.")


def longestMatch_test():
    
    # Common cases
    assert longestMatch("attattagccgc", "attattccgccgcc") == "attatt", "Error occurred! The result should be attatt"    
    assert longestMatch("attattccgccgcc", "attattagccgc") == "attatt", "Error occurred! The result should be attatt"
    assert longestMatch("attatt", "att") == "att", "Error occurred! The result should be att"
    assert longestMatch("attattgccgcc", "gccgccattatt") == "attatt", "Error occurred! The result should be attatt"
    assert longestMatch("gctataa", "tagcaa") == "gc", "Error occurred! The result should be gc"
    assert longestMatch("tagcaa", "gctataa") == "ta", "Error occurred! The result should be ta"
    assert longestMatch("gctaaa", "tagcaa") == "gc", "Error occurred! The result should be gc"
    
    
    # Edge cases
    assert longestMatch("", "a") == "One or both DNA strings are not given!", "Error occurred! One or both DNA strings are not given!"
    assert longestMatch("a", "") == "One or both DNA strings are not given!", "Error occurred! One or both DNA strings are not given!"
    assert longestMatch("", "") == "One or both DNA strings are not given!", "Error occurred! One or both DNA strings are not given!"
    
    assert longestMatch("", "a") == "One or both DNA strings are not given!", "Error occurred! One or both DNA strings are not given!"
    assert longestMatch("a", "") == "One or both DNA strings are not given!", "Error occurred! One or both DNA strings are not given!"
    assert longestMatch("", "") == "One or both DNA strings are not given!", "Error occurred! One or both DNA strings are not given!"
    
    assert longestMatch("a", "a") == "a", "Error occurred! The result should be a"
    assert longestMatch("a", "aa") == "a", "Error occurred! The result should be a"
    assert longestMatch("aa", "a") == "a", "Error occurred! The result should be a"
    
    assert longestMatch("g", "c") == "Common match not found!", "Error occurred! The common match is not found!"
    assert longestMatch("ga", "c") == "Common match not found!", "Error occurred! The common match is not found!"
    assert longestMatch("c", "ga") == "Common match not found!", "Error occurred! The common match is not found!"
    
    
    print("longestMatch passes all tests.")


if __name__ == "__main__":
  readingFrames_test()
  nextORF_test()
  potentialGenes_test()
  longestMatch_test()
