class Account:
    def __init__(self, name, emails):
        self.name = name
        self.emails = emails
    
    def addEmail(email):
        self.emails.append(email)

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        accounts_m = {}
        for account in accounts:
            acc = None
            for email in account[1::]:
                if email in accounts_m:
                    acc = accounts_m[email]
            if acc is None:
                acc = Account(account[0], [])

            for email in account[1::]:
                if email not in acc.emails:
                    acc.emails.append(email)
                    accounts_m[email] = acc
        
        result = []
        for i in accounts_m.values():
            if [i.name]+ i.emails not in result:
                i.emails.sort()
                result.append([i.name]+ i.emails)

        if result == accounts:
            return result
        else:
            return self.accountsMerge(result)