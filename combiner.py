class Combine:

    def sides(self, sides):
        """Join all the sides together into one single string.

        :param sides: dictionary with all the sides
        :returns: string
        """
        combined = ''
        for face in 'FRUBLD':
            combined += ''.join(sides[face])
        
        return combined

combine = Combine()
