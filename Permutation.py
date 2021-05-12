from Letters import Letters


class Permutation:
    length = 26

    def __init__(self, permutation=[]):
        self.permutation = self._build_permutation(permutation)

    def permute(self, letter):
        code = Letters().code(letter)
        code = self.map(code)
        return Letters().char(code)

    def map(self, code):
        return self.permutation[code - 1]

    def shift(self, places=1):
        result = self.permutation[:]
        if places < 0:
            result.reverse()
        abs_places = places if places >= 0 else -places
        for k in range(0, abs_places):
            result.append(result.pop(0))
        if places < 0:
            result.reverse()
        return Permutation(result)

    def conjugate(self, permutation):
        return permutation + self - permutation

    def conjugate_shift(self, places=1):
        return self.conjugate(Permutation().shift(places))

    def _build_permutation(self, permutation):
        if type(permutation) is tuple:
            return self._build_from_cycle(permutation)
        if type(permutation) is str:
            permutation = self._string_to_list(permutation)
        return self._build_from_list(permutation)

    def _build_from_cycle(self, cycle):
        if len(cycle) < 2:
            return self._build_from_list([])
        result = list(range(1, Permutation.length + 1))
        last_k = cycle[-1]
        for k in cycle:
            result[last_k - 1] = k
            last_k = k
        return result

    def _build_from_list(self, permutation):
        result = permutation[:]
        for k in range(1, Permutation.length + 1):
            if k in result:
                continue
            result.append(k)
        return result

    def _string_to_list(self, permutation_string):
        return [Letters.code(letter) for letter in permutation_string]

    def __neg__(self):
        result = list(range(1, Permutation.length + 1))
        for fiber, image in enumerate(self.permutation):
            result[image - 1] = fiber + 1
        return Permutation(result)

    def __add__(self, permutation):
        new_permutation = [self.map(permutation.map(k)) for k in range(1, Permutation.length + 1)]
        return Permutation(new_permutation)

    def __sub__(self, other):
        return self + (-other)

    def __rmul__(self, other):
        other = int(other)
        result = Permutation()
        increment = self if other >= 0 else -self
        other = other if other >= 0 else -other
        for k in range(0, other):
            result += increment
        return result
