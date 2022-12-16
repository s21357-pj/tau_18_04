class Hamming:
    @staticmethod
    def distance(gen_a, gen_b):
        dist = 0
        if len(gen_a) == len(gen_b):
            for i in range(len(gen_a)):
                if gen_a[i] != gen_b[i]:
                    dist += 1
            return dist
        raise ValueError("Not correct input")
