# 433. Minimum Genetic Mutation
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1
        if startGene == endGene:
            return 0

        mutation = ['A', 'C', 'G', 'T']
        minimumMutation = sys.maxsize
        search = [[startGene, 0]]
        visited = {}
        while search:
            curr = search.pop(0)
            curr_gene = curr[0]
            curr_min = curr[1]
            visited[curr_gene] = True
            if curr_gene == endGene:
                minimumMutation = min(minimumMutation, curr_min)
            else:
                for i in range(len(curr_gene)):
                    for m in mutation:
                        copyGene = curr_gene[:i] + m + curr_gene[i+1:]
                        if copyGene in bank and (copyGene not in visited or not visited[copyGene]):
                            # can keep searching
                            search.append([copyGene, curr_min+1])
        if minimumMutation == sys.maxsize:
            return -1
        else:
            return minimumMutation